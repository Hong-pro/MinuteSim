#!/usr/bin/env python3
"""Regenerate the MinuteSim README benchmark figures from published data.

Almost every number below is transcribed from a peer-reviewed, open-access
publication by the MinuteSim authors; nothing is fitted, smoothed, or interpolated.

The one exception is the latest shell wall time in `fig_shell_speedup` (125.1 s),
which is an INTERNAL measurement not yet published. It is labelled as such in the
figure caption and in the section comment above that function. Everything it is
compared against is published.

Sources
-------
[AS]   H. Kim, S. Hong, N. Kim, "A GPU-Resident MITC4 Shell Solver for a Nakajima
       Hemispherical-Dome Forming Benchmark: Verification, Abaqus Validation, and
       LS-DYNA Throughput Benchmarking", Applied Sciences 16(12), 5826, 2026.
       doi:10.3390/app16125826  (CC BY 4.0)

[JMMP] H. Kim, S. Hong, N. Kim, "Design and Computational Efficiency of a
       GPU-Resident Integrated Execution Pipeline for Explicit Large-Deformation
       Finite Element Analysis", Journal of Manufacturing and Materials Processing
       10(6), 197, 2026.  doi:10.3390/jmmp10060197  (CC BY 4.0)

Usage
-----
    python tools/plot_public_benchmarks.py

Writes PNG files into assets/.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#1a1a1a"
GPU = "#0b6e4f"
CPU = "#8c8c8c"
ACCENT = "#b3541e"

plt.rcParams.update({
    "font.size": 11,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 160,
})


def _credit(fig, text, width=118):
    """Bottom-left provenance line, wrapped so it never runs off the canvas."""
    import textwrap
    fig.text(0.01, 0.01, "\n".join(textwrap.wrap(text, width)),
             fontsize=7.5, color="#5a5a5a", ha="left", va="bottom")


# ---------------------------------------------------------------------------
# Figure 1 — SOLID: CPU vs GPU step time and speedup vs model size
# [JMMP] Table 4. Hemisphere compression, Tet4, NVIDIA L40, AMD EPYC 75F3
# 32-core, GPU FP32, three-run median, microseconds per step.
# ---------------------------------------------------------------------------
solid_elements = [82_944, 162_000, 384_000, 750_000, 998_250, 1_886_592]
solid_cpu_us = [24_053, 44_966, 104_012, 187_375, 251_752, 463_434]
solid_gpu_us = [243.6, 386.0, 822.5, 1391.0, 1829.0, 3378.0]
solid_speedup = [98.7, 116.5, 126.5, 134.7, 137.6, 137.2]


def fig_solid_scaling():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.2))

    ax1.loglog(solid_elements, solid_cpu_us, "o-", color=CPU, lw=2, ms=6,
               label="CPU, 1 core (FP64)")
    ax1.loglog(solid_elements, solid_gpu_us, "o-", color=GPU, lw=2, ms=6,
               label="MinuteSim GPU (FP32)")
    ax1.set_xlabel("Elements (Tet4)")
    ax1.set_ylabel("Step time  (µs/step)")
    ax1.set_title("Solid — step time vs model size", fontsize=12, loc="left")
    ax1.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)
    ax1.legend(frameon=False, fontsize=10)

    ax2.semilogx(solid_elements, solid_speedup, "o-", color=ACCENT, lw=2, ms=6)
    # L4/L5 sit close together on a log axis; stagger their labels so they stay legible.
    offsets = [(0, 10), (0, 10), (0, 10), (0, -20), (0, 10), (0, 10)]
    for (x, y), off in zip(zip(solid_elements, solid_speedup), offsets):
        ax2.annotate(f"{y:.1f}×", (x, y), textcoords="offset points",
                     xytext=off, ha="center", fontsize=9)
    ax2.set_xlabel("Elements (Tet4)")
    ax2.set_ylabel("Per-step speedup vs 1 CPU thread")
    ax2.set_ylim(0, 160)
    ax2.set_title("Solid — speedup approaches a plateau", fontsize=12, loc="left")
    ax2.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)

    fig.suptitle("MinuteSim solid benchmark — hemisphere compression, NVIDIA L40 vs AMD EPYC 75F3",
                 fontsize=12.5, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.07, 1, 0.94))
    _credit(fig, "Replotted from published data — Kim et al., JMMP 10(6), 197, 2026, "
                 "doi:10.3390/jmmp10060197 . © 2026 the authors, CC BY 4.0 "
                 "(https://creativecommons.org/licenses/by/4.0/). Left panel log–log; right panel log x.")
    fig.savefig(OUT / "solid-scaling.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2 — SHELL: throughput vs LS-DYNA MPP
# [AS] Table 11. ~505k-element Nakajima deck, 15,808 explicit steps,
# 1.0e-3 s window, NVIDIA L40, GPU FP64, same workstation.
# ---------------------------------------------------------------------------
shell_labels = ["MinuteSim\nGPU (L40)", "LS-DYNA MPP\n1 core", "LS-DYNA MPP\n8 cores",
                "LS-DYNA MPP\n32 cores"]
shell_wall_s = [643, 28_127, 11_355, 8_674]
shell_speedup = [None, 43.7, 17.7, 13.5]


def fig_shell_throughput():
    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    colors = [GPU, CPU, CPU, CPU]
    bars = ax.bar(shell_labels, shell_wall_s, color=colors, width=0.6)

    for bar, wall, sp in zip(bars, shell_wall_s, shell_speedup):
        ax.annotate(f"{wall:,} s", (bar.get_x() + bar.get_width() / 2, wall),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=10)
        if sp is not None:
            ax.annotate(f"{sp}× slower\nper step", (bar.get_x() + bar.get_width() / 2, wall / 2),
                        ha="center", va="center", fontsize=9.5, color="white", weight="bold")

    ax.set_ylabel("Wall time  (s)")
    ax.set_title("Shell throughput — ~505,000-element Nakajima deck, 15,808 explicit steps",
                 fontsize=12, loc="left")
    ax.grid(True, axis="y", ls=":", lw=0.6, alpha=0.6)
    ax.set_axisbelow(True)

    fig.tight_layout(rect=(0, 0.10, 1, 1))
    _credit(fig, "Replotted from published data — Kim et al., Applied Sciences 16(12), 5826, 2026, "
                 "doi:10.3390/app16125826 . © 2026 the authors, CC BY 4.0 "
                 "(https://creativecommons.org/licenses/by/4.0/). Same workstation; GPU FP64. Linear axis, zero baseline.")
    fig.savefig(OUT / "shell-throughput.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3 — SHELL: canonical convergence (pinched cylinder, octant meshes)
# [AS] Table A1 / Figure A4. Reference value 5.0 as reported in the publication.
# ---------------------------------------------------------------------------
pinched_labels = ["4×4", "8×8", "16×16", "32×32"]
pinched_values = [3.60, 4.40, 4.80, 4.97]
pinched_err = [28.0, 12.0, 4.0, 0.6]
PINCHED_REF = 5.0


def fig_shell_convergence():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    x = range(len(pinched_labels))

    ax.axhline(PINCHED_REF, ls="--", color=INK, lw=1.5,
               label=f"Published reference  {PINCHED_REF}")
    ax.plot(x, pinched_values, "o-", color=GPU, lw=2, ms=9, mfc="white", mew=2,
            label="MinuteSim")
    for xi, yi, e in zip(x, pinched_values, pinched_err):
        ax.annotate(f"{e:.1f}%", (xi, yi), textcoords="offset points",
                    xytext=(0, -18), ha="center", fontsize=9.5, color=ACCENT)

    ax.set_xticks(list(x))
    ax.set_xticklabels(pinched_labels)
    ax.set_xlabel("Octant mesh subdivision")
    ax.set_ylabel("Normalized deflection at the loaded point")
    ax.set_ylim(0, 6)
    ax.set_title("Shell convergence — pinched cylinder with end diaphragms",
                 fontsize=12, loc="left")
    ax.grid(True, axis="y", ls=":", lw=0.6, alpha=0.6)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=10, loc="lower right")

    fig.tight_layout(rect=(0, 0.10, 1, 1))
    _credit(fig, "Replotted from published data — Kim et al., Applied Sciences 16(12), 5826, 2026, "
                 "doi:10.3390/app16125826 . © 2026 the authors, CC BY 4.0 "
                 "(https://creativecommons.org/licenses/by/4.0/). Annotations are the relative difference "
                 "from the published reference. Linear axis, zero baseline.")
    fig.savefig(OUT / "shell-convergence.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4 — SOLID: GPU FP32 vs CPU FP64 field agreement
# [JMMP] Table 6 / Section 5.4. L2 mesh, 162,000 Tet4, J2 elastoplastic,
# node-to-surface penalty contact. Relative L2 errors, in percent.
# ---------------------------------------------------------------------------
fp_labels = ["Displacement\nmagnitude", "von Mises\nstress", "Effective\nplastic strain",
             "Reaction-force\nhistory"]
fp_values = [0.99, 0.27, 0.81, 0.31]


def fig_solid_precision():
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    bars = ax.bar(fp_labels, fp_values, color=GPU, width=0.55)
    for bar, v in zip(bars, fp_values):
        ax.annotate(f"{v:.2f}%", (bar.get_x() + bar.get_width() / 2, v),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=10)

    ax.set_ylabel("Relative L2 difference  (%)")
    ax.set_ylim(0, 1.4)
    ax.set_title("Solid — GPU single precision vs CPU double precision, same model",
                 fontsize=12, loc="left")
    ax.grid(True, axis="y", ls=":", lw=0.6, alpha=0.6)
    ax.set_axisbelow(True)

    fig.tight_layout(rect=(0, 0.10, 1, 1))
    _credit(fig, "Replotted from published data — Kim et al., JMMP 10(6), 197, 2026, "
                 "doi:10.3390/jmmp10060197 . © 2026 the authors, CC BY 4.0 "
                 "(https://creativecommons.org/licenses/by/4.0/). 162,000-element Tet4 hemisphere "
                 "compression benchmark. Linear axis, zero baseline.")
    fig.savefig(OUT / "solid-precision.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 5 — SHELL: latest internal Nakajima result against the published
# LS-DYNA reference timing.
#
# The latest MinuteSim wall time is an INTERNAL measurement, not yet published:
# 125.1 s over the same 15,808-step window, i.e. 0.007914 s/step. The LS-DYNA
# reference wall times and the published MinuteSim 643 s are [AS] Table 11.
#
# The latest run's hardware and precision are not yet reconfirmed, so this is
# deliberately NOT presented as a same-workstation comparison.
# ---------------------------------------------------------------------------
shell_latest_labels = ["LS-DYNA\n1 core", "LS-DYNA\n8 cores", "LS-DYNA\n32 cores",
                       "MinuteSim\npublished", "MinuteSim\nlatest"]
shell_latest_wall = [28_127, 11_355, 8_674, 643, 125.1]
speedup_labels = ["vs LS-DYNA\n1 core", "vs LS-DYNA\n8 cores", "vs LS-DYNA\n32 cores",
                  "vs MinuteSim\npublished"]
speedup_values = [224.8, 90.8, 69.3, 5.14]
PUBLISHED_GREEN = "#6aa88f"


def fig_shell_speedup():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.4))

    bars = ax1.bar(shell_latest_labels, shell_latest_wall,
                   color=[CPU, CPU, CPU, PUBLISHED_GREEN, GPU], width=0.62)
    ax1.set_yscale("log")
    ax1.set_ylabel("Wall time  (s, log scale)")
    ax1.set_title("Wall time — ~505,000-element Nakajima deck, 15,808 steps",
                  fontsize=11, loc="left")
    for bar, w in zip(bars, shell_latest_wall):
        ax1.annotate(f"{w:,.1f} s" if w < 1000 else f"{w:,.0f} s",
                     (bar.get_x() + bar.get_width() / 2, w), textcoords="offset points",
                     xytext=(0, 4), ha="center", fontsize=9.5)
    ax1.grid(True, axis="y", ls=":", lw=0.6, alpha=0.6)
    ax1.set_axisbelow(True)

    b2 = ax2.bar(speedup_labels, speedup_values,
                 color=[GPU, GPU, GPU, PUBLISHED_GREEN], width=0.6)
    for bar, v in zip(b2, speedup_values):
        ax2.annotate(f"{v:g}×", (bar.get_x() + bar.get_width() / 2, v),
                     textcoords="offset points", xytext=(0, 4), ha="center",
                     fontsize=10.5, weight="bold")
    ax2.set_ylabel("Per-step speedup of the latest result")
    ax2.set_ylim(0, 260)
    ax2.set_title("Latest MinuteSim result — per-step speedup", fontsize=11.5, loc="left")
    ax2.grid(True, axis="y", ls=":", lw=0.6, alpha=0.6)
    ax2.set_axisbelow(True)

    fig.tight_layout(rect=(0, 0.13, 1, 1))
    _credit(fig, "Latest internal MinuteSim result (125.1 s, 0.007914 s/step) compared with published "
                 "LS-DYNA reference timing. Reference and published MinuteSim wall times from Kim et al., "
                 "Applied Sciences 16(12), 5826, 2026, doi:10.3390/app16125826 . © 2026 the authors, "
                 "CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The latest run's hardware and "
                 "precision are not yet reconfirmed; this is not a same-workstation comparison. "
                 "Left panel log scale; right panel linear with a zero baseline.")
    fig.savefig(OUT / "shell-speedup.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_solid_scaling()
    fig_shell_throughput()
    fig_shell_convergence()
    fig_solid_precision()
    fig_shell_speedup()
    for p in sorted(OUT.glob("*.png")):
        print(f"wrote {p.relative_to(OUT.parent)}  ({p.stat().st_size:,} bytes)")
