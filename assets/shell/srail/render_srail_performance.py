"""Render the S-rail cross-solver performance figure.

MinuteSim runtimes are the L40 measurements; OpenRadioss is the measured CPU
thread sweep. Both refinement levels (L2, L3) run the same deck and stroke.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

T = [2, 3, 4, 5, 6, 7, 8, 9, 10]
OR_L2 = [1528, 932, 874, 734, 722, 754, 678, 724, 710]
OR_L3 = [7276, 5376, 4469, 3431, 3159, 3007, 2869, 4794, 2980]
MS_L2, MS_L3 = 157.0, 705.0

C_L2, C_L3, C_MS2, C_MS3 = "#2b6cb0", "#b7791f", "#2b6cb0", "#b7791f"
GRID = dict(color="#d8dee6", lw=0.7, zorder=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.35))
fig.patch.set_facecolor("white")

# --- left: wall time -----------------------------------------------------------
ax1.set_yscale("log")
ax1.plot(T, OR_L3, "o-", color=C_L3, lw=2, ms=5, label="OpenRadioss — L3 deck (MAXLVL 4, ~40k el.)", zorder=3)
ax1.plot(T, OR_L2, "o-", color=C_L2, lw=2, ms=5, label="OpenRadioss — L2 deck (MAXLVL 3, ~11k el.)", zorder=3)
ax1.axhline(MS_L3, color=C_MS3, ls="--", lw=1.8, zorder=2)
ax1.axhline(MS_L2, color=C_MS2, ls="--", lw=1.8, zorder=2)
bb = dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.92)
ax1.annotate("MinuteSim GPU\nL3 deck  %.0f s" % MS_L3, (10.35, MS_L3), color=C_MS3,
             fontsize=8.6, va="center", ha="left", fontweight="bold", zorder=5)
ax1.annotate("MinuteSim GPU\nL2 deck  %.0f s" % MS_L2, (10.35, MS_L2), color=C_MS2,
             fontsize=8.6, va="center", ha="left", fontweight="bold", zorder=5)
for x, y in ((8, 2869), (8, 678)):
    ax1.plot([x], [y], "o", ms=10, mfc="none", mec="#c53030", mew=2, zorder=4)
ax1.annotate("best CPU", (8, 2869), textcoords="offset points", xytext=(4, 16),
             fontsize=8.5, color="#c53030")
ax1.set_xlabel("OpenRadioss CPU threads")
ax1.set_ylabel("Full-stroke wall time  [s]   (log)")
ax1.set_title("Wall time", fontsize=11, loc="left", fontweight="bold")
ax1.set_xticks(T)
ax1.set_xlim(1.7, 12.9)
ax1.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:,.0f}"))
ax1.grid(axis="y", which="both", **GRID)
ax1.set_axisbelow(True)
ax1.legend(fontsize=8.5, frameon=False, loc="upper right")

# --- right: speedup ------------------------------------------------------------
sp2 = [v / MS_L2 for v in OR_L2]
sp3 = [v / MS_L3 for v in OR_L3]
w = 0.38
xs = range(len(T))
ax2.bar([x - w / 2 for x in xs], sp2, w, color=C_L2, label="L2 deck  (~11k el.)", zorder=3)
ax2.bar([x + w / 2 for x in xs], sp3, w, color=C_L3, label="L3 deck  (~40k el.)", zorder=3)
for x, (a, b) in enumerate(zip(sp2, sp3)):
    ax2.text(x - w / 2, a + 0.12, f"{a:.1f}", ha="center", fontsize=7.4, color=C_L2)
    ax2.text(x + w / 2, b + 0.12, f"{b:.1f}", ha="center", fontsize=7.4, color=C_L3)
ax2.axhline(1, color="#4a5568", lw=1)
ax2.set_xticks(list(xs))
ax2.set_xticklabels(T)
ax2.set_xlabel("OpenRadioss CPU threads")
ax2.set_ylabel("MinuteSim wall-clock speedup  [x]")
ax2.set_title("Speedup over OpenRadioss", fontsize=11, loc="left", fontweight="bold")
ax2.set_ylim(0, 11.6)
ax2.grid(axis="y", **GRID)
ax2.set_axisbelow(True)
ax2.legend(fontsize=8.5, frameon=False)

fig.suptitle("S-rail full-stroke forming — MinuteSim (NVIDIA L40) vs OpenRadioss L2 (CPU)",
             fontsize=12.5, fontweight="bold", x=0.008, ha="left", y=0.985)
fig.text(0.008, 0.010,
         "Same deck and same stroke throughout.  MinuteSim: NVIDIA L40, FP32, GPU-resident.  "
         "OpenRadioss uses its L2 shell formulation in every run.\n"
         "“L2 deck” / “L3 deck” are the two adaptive refinement levels (MAXLVL 3 / 4).  "
         "Runtime comparison only — not an accuracy comparison.\n"
         "The 9-thread OpenRadioss points are measurement scatter, reported as measured.",
         fontsize=8, color="#5f6f7e", ha="left", linespacing=1.5)
fig.tight_layout(rect=(0, 0.105, 1, 0.955))
out = __import__("sys").argv[1]
fig.savefig(out, dpi=170, facecolor="white")
print("wrote", out)
