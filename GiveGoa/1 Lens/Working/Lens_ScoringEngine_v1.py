"""Lens scoring engine v1 (reference implementation of Lens_D2_ScoringRules_v1).

Owner: SRS (scoring rules). Exchange owner: AB (export to the shared record).
Synthetic data only. Learner codes only (for example P01, EX-01). Never real names.

Input: a responses CSV with these columns
    learner_code, stage, construct_code, item_id, source, score
    - stage: Foundational | Preparatory | Middle | Secondary | Post-school
    - source: observer | self | task
    - score: 0, 1, 2, 3, or NA (item not offered in an accessible format)

Output: one profile per learner (CSV + JSON), with these fields per construct
    <CODE>_score  (0-100 integer, or empty = "not enough evidence")
    <CODE>_band   (emerging | developing | strong | not enough evidence)
    <CODE>_n      (number of scored observer items)
plus domain scores, top_strengths (up to 3 construct codes), and notes.

Rules (see Lens_D2_ScoringRules_v1, section 3):
    R1  NA is never 0. NA items are left out of every sum.
    R2  The profile uses observer and task scores. Self-report is kept beside it.
    R3  Construct score = 100 * sum(w*x) / (3 * sum(w)) over scored items, rounded half up.
    R4  Report a construct only if 2 or more items were scored. Else "not enough evidence".
    R5  Bands: 0-33 emerging, 34-66 developing, 67-100 strong (on the rounded integer).
    R6  Domain score = mean of reported construct scores in the domain (needs >= 3 reported).
    R7  Self vs observer gap >= 2 points on the 0-3 scale: write a note, change nothing.
    R8  top_strengths = up to 3 constructs with the highest scores, band developing or strong,
        ties broken by more evidence (n), then by code. Never compare learners.

Usage:
    python3 Lens_ScoringEngine_v1.py responses.csv out_prefix [weights.csv]
    python3 Lens_ScoringEngine_v1.py --selftest
"""
import csv
import json
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

DOMAINS = {
    "MI": ["MI_LIN", "MI_LOG", "MI_SPA", "MI_BOD", "MI_MUS", "MI_INTER", "MI_INTRA", "MI_NAT"],
    "ER": ["ER_SA", "ER_SM", "ER_SOC", "ER_REL", "ER_RDM"],
    "PR": ["PR_PAT", "PR_CLS", "PR_SEQ", "PR_CAU", "PR_PRB"],
}
ALL_CODES = [c for codes in DOMAINS.values() for c in codes]
STAGES = {"Foundational", "Preparatory", "Middle", "Secondary", "Post-school"}
SOURCES = {"observer", "self", "task"}
MIN_ITEMS = 2          # R4
MIN_CONSTRUCTS = 3     # R6
GAP_NOTE = 2           # R7
NEE = "not enough evidence"


def round_half_up(x):
    return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def band(score):
    if score is None:
        return NEE
    if score <= 33:
        return "emerging"
    if score <= 66:
        return "developing"
    return "strong"


def parse_score(raw):
    raw = (raw or "").strip().upper()
    if raw in ("NA", "N/A", ""):
        return None
    v = int(raw)
    if v not in (0, 1, 2, 3):
        raise ValueError(f"score must be 0-3 or NA, got {raw}")
    return v


def load_weights(path):
    w = {}
    if path:
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                w[r["item_id"].strip()] = float(r["weight"])
    return w


def score_learners(rows, weights=None):
    weights = weights or {}
    by_learner = defaultdict(list)
    stage_of = {}
    errors = []
    for i, r in enumerate(rows, start=2):
        code = r["learner_code"].strip()
        stage = r["stage"].strip()
        cc = r["construct_code"].strip()
        src = r["source"].strip().lower()
        if stage not in STAGES:
            errors.append(f"row {i}: unknown stage '{stage}'")
            continue
        if cc not in ALL_CODES:
            errors.append(f"row {i}: unknown construct '{cc}'")
            continue
        if src not in SOURCES:
            errors.append(f"row {i}: unknown source '{src}'")
            continue
        if stage_of.setdefault(code, stage) != stage:
            errors.append(f"row {i}: learner {code} has two stages")
            continue
        by_learner[code].append((cc, r["item_id"].strip(), src, parse_score(r["score"])))
    if errors:
        raise ValueError("Input errors:\n" + "\n".join(errors))

    profiles = []
    for code in sorted(by_learner):
        items = by_learner[code]
        prof = {"learner_code": code, "stage": stage_of[code], "lens_version": "v1",
                "scoring_rule": "Option A (D2 v1)", "constructs": {}, "domains": {}, "notes": []}
        na_count = sum(1 for it in items if it[3] is None)
        prof["items_total"] = len(items)
        prof["items_na"] = na_count
        for cc in ALL_CODES:
            obs = [(iid, x) for c, iid, s, x in items if c == cc and s in ("observer", "task") and x is not None]
            slf = {iid: x for c, iid, s, x in items if c == cc and s == "self" and x is not None}
            n = len(obs)
            if n >= MIN_ITEMS:
                num = sum(weights.get(iid, 1.0) * x for iid, x in obs)
                den = 3 * sum(weights.get(iid, 1.0) for iid, _ in obs)
                sc = round_half_up(100 * num / den)
            else:
                sc = None
            self_sc = round_half_up(100 * sum(slf.values()) / (3 * len(slf))) if len(slf) >= MIN_ITEMS else None
            prof["constructs"][cc] = {"score": sc, "band": band(sc), "n": n, "self_score": self_sc}
            for iid, x in obs:
                if iid in slf and abs(slf[iid] - x) >= GAP_NOTE:
                    prof["notes"].append(
                        f"{cc} item {iid}: self-report {slf[iid]} and observer {x} differ by 2+; discuss with learner and educator.")
        for d, codes in DOMAINS.items():
            vals = [prof["constructs"][c]["score"] for c in codes if prof["constructs"][c]["score"] is not None]
            ds = round_half_up(sum(vals) / len(vals)) if len(vals) >= MIN_CONSTRUCTS else None
            prof["domains"][d] = {"score": ds, "band": band(ds), "constructs_reported": len(vals)}
        cands = [(c, v) for c, v in prof["constructs"].items()
                 if v["score"] is not None and v["band"] in ("developing", "strong")]
        cands.sort(key=lambda cv: (-cv[1]["score"], -cv[1]["n"], cv[0]))
        prof["top_strengths"] = [c for c, _ in cands[:3]]
        profiles.append(prof)
    return profiles


def flat_row(p):
    row = {"learner_code": p["learner_code"], "stage": p["stage"], "lens_version": p["lens_version"],
           "scoring_rule": p["scoring_rule"]}
    for cc in ALL_CODES:
        v = p["constructs"][cc]
        row[f"{cc}_score"] = "" if v["score"] is None else v["score"]
        row[f"{cc}_band"] = v["band"]
        row[f"{cc}_n"] = v["n"]
    for d in DOMAINS:
        v = p["domains"][d]
        row[f"{d}_domain_score"] = "" if v["score"] is None else v["score"]
        row[f"{d}_domain_band"] = v["band"]
    row["top_strengths"] = ";".join(p["top_strengths"])
    row["items_total"] = p["items_total"]
    row["items_na"] = p["items_na"]
    row["notes"] = " | ".join(p["notes"])
    return row


def write_outputs(profiles, prefix):
    rows = [flat_row(p) for p in profiles]
    with open(prefix + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(prefix + ".json", "w", encoding="utf-8") as f:
        json.dump(profiles, f, indent=2, ensure_ascii=False)


def selftest():
    """Checks every rule on illustrative numbers (EX-01, EX-02 are invented, not data)."""
    def r(code, stage, cc, iid, src, s):
        return {"learner_code": code, "stage": stage, "construct_code": cc, "item_id": iid, "source": src, "score": s}
    rows = [
        # EX-01: MI_NAT 3,3,2 -> 8/9 = 88.9 -> 89 strong
        r("EX-01", "Preparatory", "MI_NAT", "NAT-P-1", "observer", "3"),
        r("EX-01", "Preparatory", "MI_NAT", "NAT-P-2", "task", "3"),
        r("EX-01", "Preparatory", "MI_NAT", "NAT-P-3", "observer", "2"),
        # MI_LIN: 1,1 and one NA -> 2/6 = 33.3 -> 33 emerging; NA ignored (R1)
        r("EX-01", "Preparatory", "MI_LIN", "LIN-P-1", "observer", "1"),
        r("EX-01", "Preparatory", "MI_LIN", "LIN-P-2", "observer", "1"),
        r("EX-01", "Preparatory", "MI_LIN", "LIN-P-3", "observer", "NA"),
        # MI_SPA: 2,1 -> 3/6 = 50 developing ; self-report 3 on SPA-P-2 vs observer 1 -> note (R7)
        r("EX-01", "Preparatory", "MI_SPA", "SPA-P-1", "observer", "2"),
        r("EX-01", "Preparatory", "MI_SPA", "SPA-P-2", "observer", "1"),
        r("EX-01", "Preparatory", "MI_SPA", "SPA-P-2", "self", "3"),
        # MI_MUS: only one scored item -> not enough evidence (R4)
        r("EX-01", "Preparatory", "MI_MUS", "MUS-P-1", "observer", "3"),
        r("EX-01", "Preparatory", "MI_MUS", "MUS-P-2", "observer", "NA"),
        # EX-02: all NA on PR_PAT -> not enough evidence, never 0
        r("EX-02", "Secondary", "PR_PAT", "PAT-S-1", "observer", "NA"),
        r("EX-02", "Secondary", "PR_PAT", "PAT-S-2", "observer", "NA"),
        # rounding: 2,2,2,1,1,2 -> 10/18 = 55.56 -> 56 ; and 1,1,1,2 -> 5/12 = 41.67 -> 42
        *[r("EX-02", "Secondary", "ER_SA", f"SA-S-{k}", "observer", s) for k, s in enumerate("222112", 1)],
        *[r("EX-02", "Secondary", "ER_SM", f"SM-S-{k}", "observer", s) for k, s in enumerate("1112", 1)],
        # boundary: exactly 2/6 = 33.33 -> 33 emerging ; 4/6 = 66.67 -> 67 strong
        r("EX-02", "Secondary", "ER_SOC", "SOC-S-1", "observer", "1"),
        r("EX-02", "Secondary", "ER_SOC", "SOC-S-2", "observer", "1"),
        r("EX-02", "Secondary", "ER_REL", "REL-S-1", "observer", "2"),
        r("EX-02", "Secondary", "ER_REL", "REL-S-2", "observer", "2"),
    ]
    p = {x["learner_code"]: x for x in score_learners(rows)}
    c1, c2 = p["EX-01"]["constructs"], p["EX-02"]["constructs"]
    assert c1["MI_NAT"] == {"score": 89, "band": "strong", "n": 3, "self_score": None}, c1["MI_NAT"]
    assert c1["MI_LIN"]["score"] == 33 and c1["MI_LIN"]["band"] == "emerging" and c1["MI_LIN"]["n"] == 2
    assert c1["MI_SPA"]["score"] == 50 and c1["MI_SPA"]["band"] == "developing"
    assert c1["MI_MUS"]["score"] is None and c1["MI_MUS"]["band"] == NEE
    assert any("MI_SPA item SPA-P-2" in n for n in p["EX-01"]["notes"])
    assert p["EX-01"]["top_strengths"] == ["MI_NAT", "MI_SPA"]   # MI_LIN is emerging, so not listed
    assert p["EX-01"]["domains"]["MI"]["score"] == round_half_up((89 + 33 + 50) / 3) == 57
    assert p["EX-01"]["domains"]["ER"]["score"] is None            # fewer than 3 constructs (R6)
    assert c2["PR_PAT"]["score"] is None and c2["PR_PAT"]["band"] == NEE
    assert c2["ER_SA"]["score"] == 56 and c2["ER_SM"]["score"] == 42
    assert c2["ER_SOC"]["score"] == 33 and c2["ER_SOC"]["band"] == "emerging"
    assert c2["ER_REL"]["score"] == 67 and c2["ER_REL"]["band"] == "strong"
    assert p["EX-02"]["items_na"] == 2
    # weights (R3): NAT-P-3 weight 2 -> (3+3+4)/(3*4) = 83.3 -> 83
    pw = score_learners(rows, {"NAT-P-3": 2.0})
    assert pw[0]["constructs"]["MI_NAT"]["score"] == 83
    # bad input is refused
    try:
        score_learners([r("EX-03", "Grade 5", "MI_LIN", "x", "observer", "2")])
        raise AssertionError("bad stage accepted")
    except ValueError:
        pass
    print("selftest: all 15 checks passed")
    return rows


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        selftest()
        sys.exit(0)
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
    profs = score_learners(data, load_weights(sys.argv[3] if len(sys.argv) > 3 else None))
    write_outputs(profs, sys.argv[2])
    print(f"Wrote {len(profs)} profiles to {sys.argv[2]}.csv and {sys.argv[2]}.json")
