"""Builds latest.png for the Sisco Team daily XAUUSD analysis.
Usage: python3 make_chart.py input.json
input.json: {"title":"XAUUSD  Daily outlook  23 Nov","candles":[[ts_ms,o,h,l,c],...] (1H, last ~120),
 "support":[3503,3520], "resistance":[3595,3625], "buy_zone":[lo,hi], "sell_zone":[lo,hi],
 "buy_note":"Buy only on a Sisco BUY signal near here", "sell_note":"Sell only on a Sisco SELL signal near here",
 "footer":"Educational analysis, not financial advice."}"""
import json, sys, datetime as dt
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
j = json.load(open(sys.argv[1]))
C = j["candles"]
fig, ax = plt.subplots(figsize=(9, 11.2), dpi=110)
bg = "#0e1621"; fig.patch.set_facecolor(bg); ax.set_facecolor(bg)
n = len(C)
for i, (t, o, h, l, c) in enumerate(C):
    col = "#26a69a" if c >= o else "#ef5350"
    ax.plot([i, i], [l, h], color=col, lw=1)
    ax.add_patch(Rectangle((i - .35, min(o, c)), .7, max(abs(c - o), .05), color=col))
def band(rng, color, label):
    ax.axhspan(rng[0], rng[1], color=color, alpha=.18, lw=0)
    ax.axhline(rng[0], color=color, lw=.8, alpha=.7); ax.axhline(rng[1], color=color, lw=.8, alpha=.7)
    ax.text(n + 1, (rng[0] + rng[1]) / 2, label, color=color, va="center", fontsize=9, fontweight="bold")
if j.get("support"): band(j["support"], "#26a69a", f"SUPPORT {j['support'][0]:.0f}-{j['support'][1]:.0f}")
if j.get("resistance"): band(j["resistance"], "#ef5350", f"RESISTANCE {j['resistance'][0]:.0f}-{j['resistance'][1]:.0f}")
if j.get("buy_zone"): band(j["buy_zone"], "#42a5f5", "BUY ZONE")
if j.get("sell_zone"): band(j["sell_zone"], "#ffa726", "SELL ZONE")
last = C[-1][4]
ax.axhline(last, color="white", lw=.6, ls="--", alpha=.6)
ax.text(n + 1, last, f"{last:.1f}", color="white", fontsize=9, va="bottom")
idx = list(range(0, n, max(1, n // 6)))
ax.set_xticks(idx); ax.set_xticklabels([dt.datetime.fromtimestamp(C[i][0] / 1000, dt.timezone.utc).strftime("%d %b %H:%M") for i in idx], color="#9aa7b4", fontsize=8)
ax.tick_params(axis="y", colors="#9aa7b4"); ax.set_xlim(-1, n + 34)
lo = min(x[3] for x in C); hi = max(x[2] for x in C)
for k in ("support", "resistance", "buy_zone", "sell_zone"):
    if j.get(k): lo = min(lo, j[k][0]); hi = max(hi, j[k][1])
ax.set_ylim(lo - 8, hi + 8)
for s in ax.spines.values(): s.set_color("#243142")
ax.grid(color="#1c2a3a", lw=.5)
fig.text(.06, .955, j["title"], color="white", fontsize=17, fontweight="bold")
fig.text(.06, .928, "OANDA:XAUUSD  1H   |   Sisco Team", color="#d4af37", fontsize=11)
notes = [x for x in (j.get("buy_note"), j.get("sell_note")) if x]
fig.text(.06, .075, "\n".join(notes), color="#cfd8e3", fontsize=10, va="top")
fig.text(.06, .022, j.get("footer", "Educational analysis, not financial advice."), color="#7d8b99", fontsize=9)
fig.subplots_adjust(left=.07, right=.97, top=.9, bottom=.13)
fig.savefig("latest.png", facecolor=bg)
