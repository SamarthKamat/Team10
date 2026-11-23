"""Builds all report and slide charts as PNG files in build/charts/."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

INK = "#1A1A1A"
ACCENT = "#E4572E"
GREY = "#8C8C8C"
LIGHT = "#D9D9D9"
BLUE = "#2F5D7C"
TEAL = "#3A8F85"
SAND = "#C9A227"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": GREY,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 11,
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def brand_revenue():
    data = [("Decathlon India (FY26)", 4478), ("adidas India (FY25)", 3259), ("Puma India (2026)", 3200),
            ("Skechers South Asia", 1971), ("Nike India (FY25)", 1380), ("ASICS India (est.)", 430)]
    data = data[::-1]
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    cols = [ACCENT if "Nike" in n else LIGHT for n, _ in data]
    bars = ax.barh([d[0] for d in data], [d[1] for d in data], color=cols, edgecolor="none", height=0.62)
    for b, (_, v) in zip(bars, data):
        ax.text(v + 60, b.get_y() + b.get_height() / 2, f"Rs {v:,} cr", va="center", fontsize=9, color=INK)
    ax.set_xlim(0, 5300)
    ax.set_xlabel("Revenue, Rs crore (all categories)")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    save(fig, "brand_revenue")


def tmm():
    yrs = ["2019", "2024", "2025", "2026"]
    vals = [47000, 59000, 65000, 69000]
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    bars = ax.bar(yrs, vals, color=[LIGHT, LIGHT, LIGHT, ACCENT], width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1200, f"{v/1000:.0f}k+", ha="center", fontsize=10, fontweight="bold")
    ax.set_ylim(0, 80000)
    ax.set_ylabel("Registered runners")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{int(x/1000)}k"))
    save(fig, "tmm")


def price_ladder():
    items = [
        ("Decathlon Jogflow 150", 1999, "Decathlon"), ("Nike Vegam Run", 3795, "Nike"),
        ("Kiprun Kipcore", 4999, "Decathlon"), ("Kiprun Kipride", 9999, "Decathlon"),
        ("ASICS Novablast 5 (Amazon)", 12000, "ASICS"), ("Nike Pegasus 42", 12995, "Nike"),
        ("ASICS Gel-Cumulus 28", 12999, "ASICS"), ("Nike Vomero 18", 13295, "Nike"),
        ("adidas Adizero EVO SL", 15999, "adidas"), ("ASICS Novablast 6", 15999, "ASICS"),
        ("Nike Pegasus Premium", 19295, "Nike"), ("Kiprun Kipstorm Elite", 19999, "Decathlon"),
    ]
    colmap = {"Nike": ACCENT, "ASICS": BLUE, "adidas": INK, "Decathlon": TEAL}
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    names = [i[0] for i in items]
    ax.barh(names, [i[1] for i in items], color=[colmap[i[2]] for i in items], height=0.6)
    for y, i in enumerate(items):
        ax.text(i[1] + 200, y, f"Rs {i[1]:,}", va="center", fontsize=8.5)
    ax.axvline(2500, color=GREY, ls="--", lw=1)
    ax.text(2600, len(items) - 0.4, "GST 5% below Rs 2,500 | 18% above", fontsize=8, color=GREY)
    ax.set_xlim(0, 23500)
    ax.set_xlabel("India MRP (Rs), November 2026 (indicative)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colmap.values()]
    ax.legend(handles, colmap.keys(), loc="lower right", frameon=False, fontsize=8.5)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    save(fig, "price_ladder")


PERCEPTUAL = {  # brand: (core trainer MRP Rs, provisional credibility 1-10)
    "Nike (Pegasus)": (12995, 8.4), "Nike Vegam Run": (3795, 6.0), "ASICS": (12999, 8.8),
    "adidas": (15999, 7.8), "Puma": (9000, 6.2), "Skechers": (7000, 4.8),
    "Decathlon Kiprun": (4999, 6.6), "Campus": (1500, 3.2),
}


def perceptual(data=PERCEPTUAL, name="perceptual"):
    fig, ax = plt.subplots(figsize=(6.6, 5.0))
    for b, (p, c) in data.items():
        col = ACCENT if "Nike" in b else BLUE
        ax.scatter(p, c, s=170, color=col, zorder=3, edgecolor="white", linewidth=1.5)
        ax.annotate(b, (p, c), xytext=(7, 6), textcoords="offset points", fontsize=8.8)
    ax.axhline(6, color=LIGHT, lw=1)
    ax.axvline(8000, color=LIGHT, lw=1)
    ax.add_patch(FancyBboxPatch((1200, 6.3), 5600, 3.3, boxstyle="round,pad=0.1", fc="#FBE3DA", ec="none", zorder=0))
    ax.text(1500, 9.3, "Open space:\naffordable + credible", fontsize=8.5, color=ACCENT, fontweight="bold", va="top")
    ax.set_xlim(0, 18500)
    ax.set_ylim(2, 10)
    ax.set_xlabel("Price level: India MRP of core running shoe (Rs)  ->  higher")
    ax.set_ylabel("Perceived running-performance credibility (1-10)")
    save(fig, name)


def plc():
    import numpy as np
    x = np.linspace(0, 10, 300)
    y = 1 / (1 + np.exp(-(x - 3.5) * 1.3)) * (1 - 0.35 / (1 + np.exp(-(x - 8.5) * 1.6)))
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.plot(x, y, color=INK, lw=2)
    for xs, lab in [(0, "Introduction"), (2.2, "Growth"), (5.3, "Maturity"), (8.3, "Decline")]:
        ax.text(xs + 0.9, -0.12, lab, ha="center", fontsize=9, color=GREY)
    for xv in [2.2, 5.3, 8.3]:
        ax.axvline(xv, color=LIGHT, lw=1, ls="--")
    pts = [(1.2, "Vegam Run"), (3.4, "Running category (India)"), (4.4, "Vomero"), (6.6, "Pegasus"), (5.6, "Super shoes")]
    for xv, lab in pts:
        yv = float(np.interp(xv, x, y))
        ax.scatter(xv, yv, s=80, color=ACCENT, zorder=3)
        ax.annotate(lab, (xv, yv), xytext=(-10, 12), textcoords="offset points", fontsize=8.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_ylim(-0.2, 1.15)
    ax.set_xlabel("Time"); ax.set_ylabel("Sales")
    save(fig, "plc")


def budget():
    items = [("First 5K with Vegam", 9.0), ("Ambassador + After Dark", 9.5), ("Marathon-season burst", 8.0),
             ("NRC City Crews", 6.0), ("Fit Lab", 5.5), ("Trade-Up credit", 4.0), ("Genuine Swoosh", 3.0)]
    items.sort(key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.barh([i[0] for i in items], [i[1] for i in items], color=[ACCENT if i[1] >= 8 else GREY for i in items], height=0.6)
    for y, i in enumerate(items):
        ax.text(i[1] + 0.15, y, f"Rs {i[1]:.1f} cr", va="center", fontsize=9)
    ax.set_xlim(0, 11.5)
    ax.set_xlabel("Assumed budget, Rs crore (total Rs 45 crore)")
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
    save(fig, "budget")


def gantt():
    months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
    rows = [("Genuine Swoosh", 1, 7), ("First 5K with Vegam", 1, 5), ("NRC City Crews", 2, 12),
            ("Fit Lab", 3, 9), ("Ambassador + After Dark", 4, 13), ("Trade-Up credit", 6, 12),
            ("Marathon-season burst", 11, 14)]
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    for i, (n, s, e) in enumerate(rows[::-1]):
        ax.barh(i, e - s, left=s, color=ACCENT if "Vegam" in n else BLUE, height=0.55)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows[::-1]])
    ax.set_xticks([i + 0.5 for i in range(14)]); ax.set_xticklabels(months, fontsize=8)
    ax.set_xlim(0, 14)
    ax.text(0.5, -1.4, "2026", fontsize=8, color=GREY); ax.text(1.5, -1.4, "2027 ->", fontsize=8, color=GREY)
    for xv in range(15):
        ax.axvline(xv, color=LIGHT, lw=0.6, zorder=0)
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
    save(fig, "gantt")


def timeline():
    ev = [("1995-96", "Licence with Sierra\n(SSIPL)"), ("1998", "First Nike store,\nNew Delhi"),
          ("2000s", "Wholly owned\nIndian subsidiary"), ("2017-19", "Partners cut\n~350 to ~150"),
          ("May 2025", "After Dark Tour\nMumbai 10K"), ("Feb 2026", "nike.com India\nrun by Nykaa"),
          ("Nov 2026", "Vegam Run\nlaunch")]
    fig, ax = plt.subplots(figsize=(7.6, 2.4))
    ax.axhline(0, color=INK, lw=1.5)
    for i, (d, t) in enumerate(ev):
        col = ACCENT if i >= 4 else INK
        ax.scatter(i, 0, s=90, color=col, zorder=3)
        up = i % 2 == 0
        ax.text(i, 0.35 if up else -0.35, d, ha="center", va="bottom" if up else "top", fontsize=9, fontweight="bold", color=col)
        ax.text(i, 0.85 if up else -0.85, t, ha="center", va="bottom" if up else "top", fontsize=8)
    ax.set_xlim(-0.6, len(ev) - 0.4); ax.set_ylim(-2.1, 2.1)
    ax.axis("off")
    save(fig, "timeline")


def channels():
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 6)

    def box(x, y, w, h, t, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", fc=fc, ec="none"))
        ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=8.5,
                color="white" if fc in (INK, ACCENT, BLUE) else INK)

    box(3.5, 4.7, 3, 0.9, "NIKE, Inc. / Nike India\n(product, brand, pricing)", INK)
    mids = [(0.0, "Retail partners\n(franchise EBOs)"), (2.55, "MBOs & sports\nstores"),
            (5.1, "Nykaa-run nike.com\n(from Feb 2026)"), (7.65, "Marketplaces:\nFlipkart, Myntra, Ajio")]
    for x, t in mids:
        box(x, 2.6, 2.3, 1.0, t, BLUE)
        ax.annotate("", xy=(x + 1.15, 3.6), xytext=(5, 4.7), arrowprops=dict(arrowstyle="->", color=GREY))
        ax.annotate("", xy=(5, 1.2), xytext=(x + 1.15, 2.6), arrowprops=dict(arrowstyle="->", color=GREY))
    box(3.0, 0.3, 4, 0.9, "Indian runner / buyer", ACCENT)
    ax.text(9.9, 0.1, "Quick commerce: not confirmed for Nike", ha="right", fontsize=7.5, color=GREY)
    save(fig, "channels")


def sources():
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from refs import REFS
    groups = {}
    for v in REFS.values():
        t = v[3]
        if t.startswith("Company official (other)"):
            t = "Company official"
        key = {"Company official": "Nike official", "Competitor official": "Competitor official",
               "Government": "Government / regulator"}.get(t)
        if key is None:
            if "report" in t.lower() or "vendor" in t.lower():
                key = "Industry reports / data"
            elif "blog" in t.lower() or "partner" in t.lower():
                key = "Specialist blogs / other"
            elif "organiser" in t.lower():
                key = "Event organisers"
            else:
                key = "News & trade press"
        groups[key] = groups.get(key, 0) + 1
    items = sorted(groups.items(), key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ax.barh([i[0] for i in items], [i[1] for i in items], color=[ACCENT if i[0] == "Nike official" else GREY for i in items], height=0.6)
    for y, i in enumerate(items):
        ax.text(i[1] + 0.3, y, str(i[1]), va="center", fontsize=9)
    ax.set_xlabel("Number of references")
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
    save(fig, "sources")


def build_all():
    for f in (brand_revenue, tmm, price_ladder, perceptual, plc, budget, gantt, timeline, channels, sources):
        f()


if __name__ == "__main__":
    build_all()
    print(sorted(os.listdir(OUT)))
