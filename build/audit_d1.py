"""Automated pre-review audit of Lens_ConstructMap_v1 (helps ANA's 15-min review; does not replace it)."""
import csv, re, sys, collections
path = sys.argv[1]
rows = list(csv.DictReader(open(path, encoding="utf-8")))
HDR = ["Domain", "Construct", "Indicator", "NEP stage", "EBA tag", "Source"]
BUZZ = ["leverage", "robust", "seamless", "delve", "synergy", "holistic", "utilize", "cutting-edge"]
LABELS = ["weak", "low iq", "iq", "retard", "disabled child", "suffer", "victim", "normal child", "deficit",
          "lazy", "poor at", "cannot", "can't", "unable", "fails", "handicap", "abnormal", "dyslexic", "autistic"]
STAGES = ["Foundational (3–8)", "Preparatory (8–11)", "Middle (11–14)", "Secondary (14–18)", "Post-school (18–35)"]
EBA = {"None", "Environment", "Biodiversity", "Agriculture"}
res = []
def chk(name, ok, detail="", warn=False):
    res.append((name, "PASS" if ok else ("REVIEW" if warn else "FAIL"), detail))
chk("Exact columns", list(rows[0].keys()) == HDR, ",".join(rows[0].keys()))
chk("90 indicators", len(rows) == 90, str(len(rows)))
cov = collections.Counter((r["Construct"], r["NEP stage"]) for r in rows)
cons = sorted({r["Construct"] for r in rows})
chk("18 constructs x 5 stages, one each", len(cons) == 18 and all(cov[(c, s)] == 1 for c in cons for s in STAGES),
    f"{len(cons)} constructs")
chk("3 domains", len({r['Domain'] for r in rows}) == 3)
chk("Every row has a source", all(r["Source"].strip() for r in rows))
chk("Stage values valid", all(r["NEP stage"] in STAGES for r in rows))
bad_eba = [r["EBA tag"] for r in rows if not set(t.strip() for t in r["EBA tag"].replace(";", "/").split("/")) <= EBA]
chk("EBA tags valid (Environment/Biodiversity/Agriculture/None)", not bad_eba, ";".join(bad_eba[:5]))
txt = lambda r: " ".join(r.values()).lower()
hits = [(b, r["Construct"], r["NEP stage"]) for r in rows for b in BUZZ if re.search(r"\b" + b + r"\b", txt(r))]
chk("No banned buzzwords", not hits, str(hits[:5]))
SLOWW = re.compile(r"\\bslow(ly|er)?\\b(?!.{0,15}\\b(loud|soft|happy|sad|music|beat))")
lh = [("slow", r["Construct"], r["NEP stage"]) for r in rows if SLOWW.search(r["Indicator"].lower()) and "fast or slow" not in r["Indicator"].lower()]
lh += [(b, r["Construct"], r["NEP stage"]) for r in rows for b in LABELS if re.search(r"\b" + re.escape(b) + r"\b", r["Indicator"].lower())]
chk("No label / deficit words in indicators", not lh, str(lh[:5]))
neg = [r["Indicator"] for r in rows if re.search(r"\b(not|never|no|doesn't|does not)\b", r["Indicator"].lower())]
chk("Negation words (human check: content, not deficit?)", not neg, " | ".join(neg[:3]), warn=True)
long_ = [r["Indicator"] for r in rows if len(r["Indicator"].split()) > 25]
chk("Indicators <= 25 words (plain English)", not long_, " | ".join(long_[:3]))
dup = [k for k, v in collections.Counter(r["Indicator"] for r in rows).items() if v > 1]
chk("No duplicate indicators", not dup, " | ".join(dup))
timed = [r["Indicator"] for r in rows if re.search(r"\b(seconds|minutes|quickly|fast|timed)\b", r["Indicator"].lower())]
chk("Speed / time words (human check: no time limit?)", not timed, " | ".join(timed[:3]), warn=True)
print("| Check | Result | Detail |\n|---|---|---|")
for n, s, d in res:
    print(f"| {n} | {s} | {d.replace('|','/')} |")
print(f"\nEBA tag counts: {dict(collections.Counter(r['EBA tag'] for r in rows))}")
sys.exit(0 if all(s != "FAIL" for _, s, _ in res) else 1)
