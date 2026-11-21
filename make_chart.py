"""Builds latest.png (same look as the first Sisco Team weekly review) for the daily XAUUSD analysis.
Usage: python3 make_chart.py input.json
input.json:
 {"subtitle": "Daily outlook 23 Nov  |  last price 3538",
  "candles": [[ts_ms,o,h,l,c], ...],          # OANDA:XAUUSD 1H, last ~120, oldest first
  "levels": [ {"price":3690,"label":"Resistance 3690","kind":"res"},                       # dashed red line
              {"price":3503,"label":"Support 3503-3520","kind":"sup","zone":[3503,3520]},  # green, shaded zone
              {"price":3595,"label":"Friday high 3595","kind":"info"},                     # white dashed line
              {"price":3600,"label":"SELL zone 3595-3610 (with Sisco signal)","kind":"sell","zone":[3595,3610]},  # orange
              {"price":3515,"label":"BUY zone 3503-3515 (with Sisco signal)","kind":"buy","zone":[3503,3515]} ], # blue
  "footer": "Educational analysis, not financial advice."}
For zones, "price" is the line drawn (edge); labels sit at the right of the chart. Keep labels under ~45 chars."""
import json, sys, datetime as dt
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
j = json.load(open(sys.argv[1])); C = j["candles"]; n = len(C)
BG = "#0a0d14"; GRID = "#161b26"; TXT = "#e6e9f2"; MUT = "#8b93a7"
UP, DN = "#2ecc9a", "#ff6b6b"
KIND = {"res": "#ff6b6b", "sup": "#2ecc9a", "info": "#e6e9f2", "buy": "#5aa9ff", "sell": "#ffa94d"}
def ema(vals, p):
    k = 2 / (p + 1); out = [vals[0]]
    for v in vals[1:]: out.append(v * k + out[-1] * (1 - k))
    return out
cl = [x[4] for x in C]
fig, ax = plt.subplots(figsize=(9, 9), dpi=180)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
for i, (t, o, h, l, c) in enumerate(C):
    col = UP if c >= o else DN
    ax.plot([i, i], [l, h], color=col, lw=.8, zorder=3)
    ax.add_patch(Rectangle((i - .38, min(o, c)), .76, max(abs(c - o), .04 * (h - l + 1)), color=col, zorder=3))
ax.plot(range(n), ema(cl, 20), color="#ffc94d", lw=1.2, label="EMA 20", zorder=4)
ax.plot(range(n), ema(cl, 50), color="#6ea8ff", lw=1.2, label="EMA 50", zorder=4)
lo = min(x[3] for x in C); hi = max(x[2] for x in C)
for L in j.get("levels", []):
    col = KIND.get(L.get("kind", "info"), TXT)
    if L.get("zone"):
        ax.axhspan(L["zone"][0], L["zone"][1], color=col, alpha=.12, lw=0, zorder=1)
        lo = min(lo, L["zone"][0]); hi = max(hi, L["zone"][1])
    ax.axhline(L["price"], color=col, lw=.8, ls=(0, (4, 3)), zorder=2)
    ax.text(n * 1.015, L["price"], L["label"], color=col, fontsize=7.5, va="bottom")
    lo = min(lo, L["price"]); hi = max(hi, L["price"])
ax.set_xlim(-2, n * 1.5 if n else 10)
pad = (hi - lo) * .04; ax.set_ylim(lo - pad * 2, hi + pad)
st = max(1, n // 7); idx = list(range(0, n, st)); idx = [i for i in idx if n - 1 - i > st // 2] + [n - 1]
ax.set_xticks(idx); ax.set_xticklabels([dt.datetime.fromtimestamp(C[i][0] / 1000, dt.timezone.utc).strftime("%b %d\n%H:%M") for i in idx], color=TXT, fontsize=6.5)
ax.tick_params(axis="y", colors=TXT, labelsize=7); ax.tick_params(length=2, color=MUT)
ax.grid(color=GRID, lw=.6)
for s in ax.spines.values(): s.set_color("#1f2533")
leg = ax.legend(loc="upper left", fontsize=7, facecolor=BG, edgecolor="#1f2533", labelcolor=TXT)
fig.text(.076, .945, "XAUUSD  ·  OANDA  ·  1H", color=TXT, fontsize=16, fontweight="bold")
fig.text(.076, .905, j.get("subtitle", ""), color=MUT, fontsize=9.5)
fig.text(.975, .945, "Sisco Team", color=UP, fontsize=14, fontweight="bold", ha="right")
fig.text(.076, .018, j.get("footer", "Educational analysis, not financial advice."), color="#5f677a", fontsize=7.5)
fig.subplots_adjust(left=.076, right=.975, top=.885, bottom=.09)
fig.savefig("latest.png", facecolor=BG)
