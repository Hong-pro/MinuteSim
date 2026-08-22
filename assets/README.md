# Figure Provenance

Every image in this directory is recorded here before it is committed. A figure with unknown origin
is not published.

Figures fall into three groups. **Replotted charts** are drawn by the MinuteSim documentation team
from numerical tables in the publications listed below — the numbers are transcribed exactly, never
fitted, smoothed, interpolated, or rescaled. **Reproduced figures** are author-created images taken
from the publications or their supplementary archives under CC BY 4.0, with attribution.
**Rendered results** are images generated here directly from a MinuteSim result file, with no
retouching. Nothing here contains third-party material.

Regenerate them with:

```bash
python tools/plot_public_benchmarks.py                      # replotted charts

pvbatch --force-offscreen-rendering \
        assets/shell/srail/render_srail_fullstroke.py \
        --src <PACKAGE>/benchmarks/srail/srail_fullstroke.xdmf    # rendered results
```

## Sources

| Key | Publication | DOI | Licence |
|---|---|---|---|
| **AS** | H. Kim, S. Hong, N. Kim, "A GPU-Resident MITC4 Shell Solver for a Nakajima Hemispherical-Dome Forming Benchmark: Verification, Abaqus Validation, and LS-DYNA Throughput Benchmarking," *Applied Sciences* **16**(12), 5826, 2026 | [10.3390/app16125826](https://doi.org/10.3390/app16125826) | CC BY 4.0 |
| **JMMP** | H. Kim, S. Hong, N. Kim, "Design and Computational Efficiency of a GPU-Resident Integrated Execution Pipeline for Explicit Large-Deformation Finite Element Analysis," *Journal of Manufacturing and Materials Processing* **10**(6), 197, 2026 | [10.3390/jmmp10060197](https://doi.org/10.3390/jmmp10060197) | CC BY 4.0 |

Both licences were confirmed on 2026-08-22 from the publisher-deposited Crossref licence field
(`https://creativecommons.org/licenses/by/4.0/`) and from the copyright statement on page 1 of each
article ("© 2026 by the authors").

## Figures

### `solid-scaling.png`

| Field | Value |
|---|---|
| Source | **JMMP**, Table 4 (mesh-scaling summary) |
| DOI | [10.3390/jmmp10060197](https://doi.org/10.3390/jmmp10060197) |
| Derivation | Replotted from the published table. Values used verbatim. |
| Content | CPU and GPU step time (µs/step) and per-step speedup versus element count, six mesh levels from 82,944 to 1,886,592 Tet4 elements |
| Axes | Left panel log–log; right panel log x, linear y with a zero baseline. Log scaling is stated in the figure caption. |
| Third-party material | None |
| Licence | CC BY 4.0, attributed in the figure footer |

### `shell-throughput.png`

| Field | Value |
|---|---|
| Source | **AS**, Table 11 (throughput comparison) |
| DOI | [10.3390/app16125826](https://doi.org/10.3390/app16125826) |
| Derivation | Replotted from the published table. Wall times and speedups used verbatim. |
| Content | Wall time for the ~505,000-element Nakajima deck over 15,808 explicit steps: MinuteSim on an NVIDIA L40 against LS-DYNA MPP R14.1 at 1, 8, and 32 CPU cores on the same workstation |
| Axes | Linear, zero baseline. No axis truncation. |
| Third-party material | None. LS-DYNA is named as the reference solver; no LS-DYNA material is reproduced. |
| Licence | CC BY 4.0, attributed in the figure footer |

### `shell-convergence.png`

| Field | Value |
|---|---|
| Source | **AS**, Table A1 / Figure A4 (pinched-cylinder mesh convergence) |
| DOI | [10.3390/app16125826](https://doi.org/10.3390/app16125826) |
| Derivation | Replotted from the published table. The reference line is the value reported in the publication; the normalization formula printed on the original figure is deliberately not reproduced. |
| Content | Normalized deflection at the loaded point for 4×4, 8×8, 16×16, and 32×32 octant meshes against the published reference |
| Axes | Linear, zero baseline |
| Third-party material | None reproduced. The reference value 5.0 is the normalized textbook value attributed in the source publication to MacNeal & Harder (doi:10.1016/0168-874X(85)90003-4) and Belytschko et al. (ISBN 978-1-118-63270-3). |
| Licence | CC BY 4.0, attributed in the figure footer |

### `solid-precision.png`

| Field | Value |
|---|---|
| Source | **JMMP**, Table 6 / §5.4 (GPU FP32 versus CPU FP64 field comparison) |
| DOI | [10.3390/jmmp10060197](https://doi.org/10.3390/jmmp10060197) |
| Derivation | Replotted from the published table. Relative L2 differences used verbatim. |
| Content | Relative L2 difference between the GPU single-precision and CPU double-precision runs of the same 162,000-element Tet4 model, for displacement magnitude, von Mises stress, effective plastic strain, and reaction-force history |
| Axes | Linear, zero baseline |
| Third-party material | None |
| Licence | CC BY 4.0, attributed in the figure footer |

### `shell-speedup.png`

| Field | Value |
|---|---|
| Type | Replotted chart |
| Source | Reference wall times from **AS**, Table 11. The latest MinuteSim wall time (125.1 s over 15,808 steps) is an **internal measurement, not published** |
| DOI | [10.3390/app16125826](https://doi.org/10.3390/app16125826) for the reference timings |
| Derivation | Published reference values used verbatim. Speedups derived by division: 28,127 / 125.1 = 224.8; 11,355 / 125.1 = 90.8; 8,674 / 125.1 = 69.3; 643 / 125.1 = 5.14 |
| Content | Wall time for the ~505,000-element Nakajima deck, and the latest result's per-step speedup against each reference |
| Axes | Left panel log scale (stated in the caption); right panel linear with a zero baseline |
| Third-party material | None. LS-DYNA is named as the reference solver; no LS-DYNA material is reproduced |
| Caveat carried in the figure | The latest run's hardware and precision are not reconfirmed; explicitly **not** a same-workstation comparison |

### `shell-result.png`

| Field | Value |
|---|---|
| Type | **Reproduced** author-created figure |
| Source | **AS** supplementary archive, `05_near50k_intermediate/figures/` |
| DOI | [10.3390/app16125826](https://doi.org/10.3390/app16125826) |
| Derivation | Used as published, unmodified |
| Content | Radial von Mises, shell thickness and equivalent plastic strain profiles at 40 mm and 80 mm punch stroke, intermediate Nakajima mesh |
| Third-party material | None. MinuteSim results only |
| Licence | CC BY 4.0. Authors: H. Kim, S. Hong, N. Kim; © 2026 the authors |

### `solid-result.png`

| Field | Value |
|---|---|
| Type | **Reproduced** author-created figure |
| Source | **JMMP**, Figure 2 (hemisphere compression benchmark) |
| DOI | [10.3390/jmmp10060197](https://doi.org/10.3390/jmmp10060197) |
| Derivation | Used as published, unmodified |
| Content | Initial and deformed configuration of the hemisphere compression model, with the effective plastic strain field |
| Third-party material | None. No third-party interface elements or vendor branding appear in the image |
| Licence | CC BY 4.0. Authors: H. Kim, S. Hong, N. Kim; © 2026 the authors |

### `srail-shell-*.png`, `srail-shell-*-animation.gif`, `srail-shell-*-animation.mp4`

Eight files sharing one provenance:
`srail-shell-eqp.png`, `srail-shell-thickness.png`, `srail-shell-eqp-detail.png`,
`srail-shell-thickness-detail.png`, and the `-animation.gif` / `-animation.mp4` pair for each field.

| Field | Value |
|---|---|
| Type | **Rendered result.** Not a publication figure and not a chart |
| Source | `benchmarks/srail/srail_fullstroke.xdmf` in the MinuteSim 0.9.0-beta.1 release package, read read-only |
| Derivation | Rendered by `assets/shell/srail/render_srail_fullstroke.py` under ParaView 6.1.0. No image was retouched; the result file was not modified or re-run |
| Content | S-rail draw-forming at full stroke — shell thickness and equivalent plastic strain on the blank, with the adaptively refined element mesh drawn. Forming tools shown as a subordinate translucent shell |
| Colour scales | Turbo. `eqp` covers the full measured range 0–0.53; `thickness` is scaled 0.84–1.01 mm against a measured 0.8304–1.0472 mm |
| Third-party material | None. MinuteSim output only; no vendor branding and no reference-solver result appears |
| Licence | MinuteSim's own output. No external licence applies and no CC BY attribution is required |
| Status | **Demonstration, not validation.** No reference solution or error metric is published for this case — see [Benchmarks](../docs/benchmarks.md) |

Full rendering decisions and limitations: [`shell/srail/assets_manifest.md`](shell/srail/assets_manifest.md).

### `benchmarks/*-model.png`

Five canonical shell load-case schematics:
`membrane-patch-model.png`, `bending-patch-model.png`, `straight-cantilever-model.png`,
`curved-cantilever-model.png`, `pinched-cylinder-model.png`.

| Field | Value |
|---|---|
| Type | **MinuteSim-authored schematic.** Not a publication figure and not a chart |
| Source | Drawn by MinuteSim's own benchmark-figure script from the documented benchmark geometry and boundary conditions of each case |
| Derivation | Downscaled to 900 px wide and re-encoded. No labels, numbers, or geometry were altered; nothing was added or removed |
| Content | Geometry, restraints and applied load for the membrane patch, bending patch, straight cantilever, curved cantilever, and pinched-cylinder benchmarks |
| Third-party material | **None.** These are original drawings of standard, publicly described benchmark problems. No figure, drawing, or panel from MacNeal & Harder, Belytschko et al., any textbook, or any commercial solver is reproduced |
| Licence | MinuteSim's own work. No external licence applies and no CC BY attribution is required |
| Note | The benchmark *problems* are classical and are attributed to their original sources in [Validation](../docs/validation.md); the *drawings* are MinuteSim's |

No model schematic is published for the Nakajima dome benchmark or for the solid benchmarks,
because no legitimate source figure exists for them. They are left without a thumbnail rather
than illustrated with an invented one.

## Rules for adding a figure

1. Record source, DOI, licence, derivation, content, axis treatment, and third-party status **before**
   committing.
2. Do not reuse a published figure that contains separately copyrighted third-party material.
3. When replotting, keep the published numbers exactly. Do not truncate an axis, drop a baseline, or
   change a scale in a way that makes a result look larger than it is; state log scaling explicitly.
4. Attribute in the figure itself, not only here — a figure gets separated from its directory.
