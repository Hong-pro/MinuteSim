<div align="center">

# MinuteSim

### GPU-Resident Explicit Finite Element Solver

## **From model to result — in minutes.**

**High-throughput explicit FEA for shell forming, large deformation,
and contact-intensive structural analysis on NVIDIA GPUs.**

[Performance](docs/performance.md) ·
[Validation](docs/validation.md) ·
[Benchmarks](docs/benchmarks.md) ·
[Publications](docs/publications.md) ·
[Roadmap](docs/roadmap.md)

</div>

---

## See MinuteSim in Action

<div align="center">

<img src="assets/srail-shell-thickness-animation.gif" alt="S-rail full-stroke shell forming: shell thickness developing through the draw on an adaptively refining mesh" width="88%">

**Full-stroke S-rail forming — 66.5 s (1.1 min)**<br>
GPU explicit shell simulation with adaptive local refinement

32,222 explicit steps

**Deformable blank:** 675 → 6,963 shell elements<br>
**Total model:** 1,940 → 8,228 shell elements

</div>

This is a MinuteSim shell simulation result for this specific benchmark configuration, and a
capability demonstration rather than an accuracy claim. Independent accuracy evidence is
reported separately in [Validation](docs/validation.md).

---

## Performance

<table>
<tr>
<td align="center" width="50%">
<h1>≈220×</h1>
<b>Shell GPU Speedup</b><br>
<sub>Latest internal Nakajima throughput benchmark</sub><br>
<sub>vs published LS-DYNA MPP R14.1 1-core timing</sub>
</td>
<td align="center" width="50%">
<h1>137.6×</h1>
<b>Solid GPU/CPU Speedup</b><br>
<sub>Peer-reviewed benchmark</sub><br>
<sub>vs MinuteSim single-thread CPU path</sub>
</td>
</tr>
</table>

<div align="center">

**Large-model Nakajima throughput benchmark**<br>
~505,000 shell elements · 15,808 explicit steps · 125.1 s<br>
<sub>Latest internal MinuteSim result — see benchmark scope below</sub>

</div>

<table>
<tr>
<td align="center" width="50%">
<img src="assets/shell-speedup.png" alt="Latest shell benchmark: wall time and per-step speedup against published LS-DYNA reference timing" width="100%">
<br>
<b>Nakajima throughput</b><br>
<sub>125.1 s wall time · per-step speedup vs published LS-DYNA reference</sub>
</td>
<td align="center" width="50%">
<img src="assets/solid-scaling.png" alt="Published solid benchmark: CPU and GPU step time and speedup versus element count" width="100%">
<br>
<b>Solid scaling</b><br>
<sub>up to 137.6× · published scaling study · 83 K to 1.89 M elements</sub>
</td>
</tr>
</table>

<details>
<summary><b>Benchmark scope and comparison basis</b></summary>

**Shell.** The latest MinuteSim internal runtime on the ~505,000-element Nakajima deck is
**125.1 s** over 15,808 explicit steps. Against the *published* LS-DYNA MPP R14.1 reference
timing that is approximately **224.8×** per step at 1 core and **69.3×** at 32 cores. This is
an internal measurement compared against published reference timing rather than a fresh
reference run; its hardware and precision have not been reconfirmed, so it is **not** claimed
as a same-workstation comparison.

**Solid.** The **137.6×** figure is MinuteSim GPU single precision against **MinuteSim's own**
single-thread CPU double-precision path on the published benchmark. It is **not** a
cross-solver comparison.

Every speedup is specific to its benchmark, hardware, precision and configuration. MinuteSim
makes no product-wide multiplier claim.

[Full benchmark methodology →](docs/performance.md)

</details>

---

## What MinuteSim Supports

<table>
<tr>
<th align="left">Area</th>
<th align="left">Capability</th>
<th align="left">Current support</th>
</tr>

<tr>
<td rowspan="2"><b>Elements</b></td>
<td>Shell</td>
<td>MITC4 fully integrated quadrilateral — <b>Validated</b></td>
</tr>
<tr>
<td>Solid</td>
<td>Tet4 — <b>Validated</b></td>
</tr>

<tr>
<td rowspan="4"><b>Materials</b></td>
<td>Elastic</td>
<td>Isotropic elasticity — <b>Validated</b></td>
</tr>
<tr>
<td>Isotropic plasticity</td>
<td>J2 with piecewise-linear / curve hardening — <b>Validated</b></td>
</tr>
<tr>
<td>Planar anisotropy</td>
<td><b>Barlat 89 planar anisotropy</b> — Supported</td>
</tr>
<tr>
<td>Rigid</td>
<td>Rigid tooling bodies — Supported</td>
</tr>

<tr>
<td><b>Large deformation</b></td>
<td>Explicit large-strain kinematics</td>
<td>Shell and solid — <b>Validated</b></td>
</tr>

<tr>
<td rowspan="2"><b>Contact</b></td>
<td>Rigid-to-deformable</td>
<td><b>Validated</b> against a closed-form contact solution</td>
</tr>
<tr>
<td>Friction</td>
<td>Coulomb friction — Supported</td>
</tr>

<tr>
<td><b>Adaptive analysis</b></td>
<td>Shell mesh refinement</td>
<td>Adaptive local refinement during forming — Supported</td>
</tr>

<tr>
<td><b>Precision</b></td>
<td>GPU precision</td>
<td>FP32 and FP64 builds — <b>Validated</b> (FP32 vs FP64 comparison)</td>
</tr>

<tr>
<td rowspan="3"><b>Results</b></td>
<td>Result fields</td>
<td>Stress · equivalent plastic strain · shell thickness · displacement · velocity · contact force</td>
</tr>
<tr>
<td>Output format</td>
<td>XDMF index over HDF5 — Supported</td>
</tr>
<tr>
<td>d3plot</td>
<td>Not written by the solver. <code>*DATABASE_BINARY_D3PLOT</code> is read as an output-cadence setting only — see the <a href="docs/roadmap.md">Roadmap</a></td>
</tr>

<tr>
<td><b>GPU execution</b></td>
<td>GPU-resident explicit solve</td>
<td>NVIDIA GPUs, Volta or newer — <b>Validated</b></td>
</tr>
</table>

<sub><b>Validated</b> means published evidence against an independent reference exists — see
<a href="docs/validation.md">Validation</a>. <b>Supported</b> means the capability is implemented
and reachable through documented keyword input, without an independent reference comparison.</sub>

**Also implemented, qualification ongoing.** Tet10 solid elements, Barlat 89 planar anisotropy,
adaptive shell refinement, additional shell formulations, and ductile damage exist in the product
at various stages of qualification. The [Roadmap](docs/roadmap.md) lists each one with its
implementation month, the evidence behind it, and its release status — implemented, validated and
released are tracked as three separate things.

---

## Simulation Results

<table>
<tr>
<td align="center" width="50%">
<img src="assets/srail-shell-eqp.png" alt="S-rail shell forming result: equivalent plastic strain on the fully formed part, with the adaptively refined element mesh visible" width="100%">
<br>
<b>S-rail Shell Forming</b><br>
<sub>Equivalent plastic strain at full stroke</sub>
</td>
<td align="center" width="50%">
<img src="assets/solid-result.png" alt="Solid result: hemisphere compression, initial and deformed configuration with plastic strain contour" width="100%">
<br>
<b>Solid Hemisphere Compression</b><br>
<sub>Effective plastic strain</sub>
</td>
</tr>
</table>

[Thickness result](assets/srail-shell-thickness.png) ·
[GIF animation](assets/srail-shell-thickness-animation.gif) ·
[MP4 animation](assets/srail-shell-thickness-animation.mp4)

The S-rail case is a **capability demonstration, not a validation result** — no reference
solution is compared against it. Measured shell accuracy comes from the Nakajima benchmark,
in [Validation](docs/validation.md).

---

## Validated Accuracy

<table>
<tr>
<td align="center" width="25%">
<h2>2.95%</h2>
<b>Shell stress</b><br>
<sub>Mean von Mises difference vs Abaqus/Explicit, over 94% of specimen elements</sub>
</td>
<td align="center" width="25%">
<h2>2.08%</h2>
<b>Shell thickness</b><br>
<sub>Maximum difference vs Abaqus/Explicit</sub>
</td>
<td align="center" width="25%">
<h2>1.69%</h2>
<b>Solid force</b><br>
<sub>Difference from closed-form reference</sub>
</td>
<td align="center" width="25%">
<h2>1.0%</h2>
<b>Contact radius</b><br>
<sub>Difference from closed-form reference</sub>
</td>
</tr>
</table>

**Shell validation** — 10,000-element Nakajima benchmark against Abaqus/Explicit 2024 HF3,
S4 shells.

**Solid validation** — independent closed-form normal-contact solution.

[Explore validation evidence →](docs/validation.md)

---

## Why MinuteSim

<table>
<tr>
<td align="center" width="25%" valign="top">
<b>Results in minutes</b><br>
<sub>MinuteSim was built around a simple goal: make practical explicit finite-element analysis fast enough that engineers can get results in minutes rather than waiting hours.</sub>
</td>
<td align="center" width="25%" valign="top">
<b>GPU-first computation</b><br>
<sub>Designed for high-throughput explicit finite-element analysis on NVIDIA GPUs.</sub>
</td>
<td align="center" width="25%" valign="top">
<b>Validated against independent references</b><br>
<sub>Shell forming is compared with Abaqus/Explicit. Solid contact is compared with a closed-form analytical reference.</sub>
</td>
<td align="center" width="25%" valign="top">
<b>Peer-reviewed development</b><br>
<sub>The solver, its validation studies, and its benchmark results are documented in two peer-reviewed 2026 publications.</sub>
</td>
</tr>
</table>

---

## Peer-Reviewed Evidence

**A GPU-Resident MITC4 Shell Solver for a Nakajima Hemispherical-Dome Forming Benchmark:
Verification, Abaqus Validation, and LS-DYNA Throughput Benchmarking**<br>
*Applied Sciences* 16(12), 5826, 2026 ·
[Read the paper →](https://doi.org/10.3390/app16125826)

**Design and Computational Efficiency of a GPU-Resident Integrated Execution Pipeline for
Explicit Large-Deformation Finite Element Analysis**<br>
*Journal of Manufacturing and Materials Processing* 10(6), 197, 2026 ·
[Read the paper →](https://doi.org/10.3390/jmmp10060197)

---

## Availability

**MinuteSim 0.9.0 Beta**

Windows x64 · NVIDIA GPU (Volta or newer) · Single / Double Precision

The Microsoft Visual C++ Redistributable is required and is not bundled.

MinuteSim is proprietary and is not distributed from this repository, which holds its public
documentation and published evidence. For beta access or technical evaluation, please
[open an issue](https://github.com/Hong-pro/MinuteSim/issues).

---

## Technical Resources

[Performance](docs/performance.md) ·
[Validation](docs/validation.md) ·
[Benchmarks](docs/benchmarks.md) ·
[Publications](docs/publications.md) ·
[Roadmap](docs/roadmap.md)

<sub>[Limitations](docs/limitations.md) ·
[Documentation Governance](docs/DOCUMENTATION_GOVERNANCE.md)</sub>
