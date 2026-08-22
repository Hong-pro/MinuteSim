# Benchmark Cases

The models MinuteSim is measured on. This page describes **what problems are used**;
[Validation](validation.md) reports **how accurate** the results are, and
[Performance](performance.md) reports **how fast** they run. Numbers are not repeated here.

Publications: **[AS]** = [Applied Sciences 16(12), 5826](https://doi.org/10.3390/app16125826) ·
**[JMMP]** = [JMMP 10(6), 197](https://doi.org/10.3390/jmmp10060197)

## Case catalog

<table>
<tr>
<th align="left" width="24%">Model</th>
<th align="left">Case</th>
<th align="left">Element</th>
<th align="left">Model size</th>
<th align="left">Used for</th>
</tr>

<tr>
<td rowspan="7" align="center"><img src="../assets/benchmarks/nakajima-model.png" width="100%"><br><sub>Nakajima dome</sub></td>
<td>Forming validation vs Abaqus/Explicit</td><td>MITC4</td><td>10,000</td>
<td><a href="validation.md">Validation →</a></td>
</tr>
<tr><td>Contact-pressure diagnostic</td><td>MITC4</td><td>10,000</td><td><a href="validation.md">Validation →</a></td></tr>
<tr><td>Mesh sensitivity</td><td>MITC4</td><td>~4,900 / 10,000 / ~19,900</td><td><a href="validation.md">Validation →</a></td></tr>
<tr><td>Friction sensitivity</td><td>MITC4</td><td>10,000</td><td><a href="validation.md">Validation →</a></td></tr>
<tr><td>Penalty-scale sensitivity</td><td>MITC4</td><td>10,000</td><td><a href="validation.md">Validation →</a></td></tr>
<tr><td>Intermediate-mesh cross-code check</td><td>MITC4</td><td>50,176</td><td><a href="validation.md">Validation →</a></td></tr>
<tr><td>Large-model throughput deck</td><td>MITC4</td><td>~505,000</td><td><a href="performance.md">Performance →</a></td></tr>

<tr>
<td rowspan="3" align="center"><img src="../assets/solid-result.png" width="100%"><br><sub>Hemisphere compression</sub></td>
<td>Mesh-scaling study</td><td>Tet4</td><td>82,944 → 1,886,592</td><td><a href="performance.md">Performance →</a></td>
</tr>
<tr><td>Contact-overhead study</td><td>Tet4</td><td>162,000 / 384,000 / 998,250</td><td><a href="performance.md">Performance →</a></td></tr>
<tr><td>GPU FP32 vs CPU FP64 self-consistency</td><td>Tet4</td><td>162,000</td><td><a href="validation.md">Validation →</a></td></tr>

<tr>
<td align="center"><img src="../assets/benchmarks/flat-punch-contact-model.png" width="100%"><br><sub>Rounded flat punch<br>geometry schematic</sub></td>
<td>Closed-form contact validation</td><td>Tet4</td><td>Coarse quarter domain</td>
<td><a href="validation.md">Validation →</a></td>
</tr>

<tr>
<td align="center"><img src="../assets/srail-shell-eqp.png" width="100%"><br><sub>S-rail</sub></td>
<td>Full-stroke forming demonstration</td><td>MITC4</td><td>675 → 6,963 (adaptive)</td>
<td><a href="../README.md">Demonstration →</a></td>
</tr>
</table>

The S-rail case is a **capability demonstration**. No reference solution is compared against it, so
it produces no accuracy or speedup claim.

---

## Canonical shell benchmark models

The five element-level verification cases, as load-case schematics. Their measured results are in
[Validation](validation.md).

<table>
<tr align="center">
<td width="20%"><img src="../assets/benchmarks/membrane-patch-model.png" width="100%"></td>
<td width="20%"><img src="../assets/benchmarks/bending-patch-model.png" width="100%"></td>
<td width="20%"><img src="../assets/benchmarks/straight-cantilever-model.png" width="100%"></td>
<td width="20%"><img src="../assets/benchmarks/curved-cantilever-model.png" width="100%"></td>
<td width="20%"><img src="../assets/benchmarks/pinched-cylinder-model.png" width="100%"></td>
</tr>
<tr align="center">
<td><sub>Membrane patch</sub></td>
<td><sub>Bending patch</sub></td>
<td><sub>Straight cantilever</sub></td>
<td><sub>Curved cantilever</sub></td>
<td><sub>Pinched cylinder</sub></td>
</tr>
</table>

## Detailed case index

Each case with its evidence class. Measured numbers are **not** repeated here — see
[Validation](validation.md) for accuracy and [Performance](performance.md) for speed.

**Purpose** is one of:

| Purpose | Meaning |
|---|---|
| `VALIDATION` | Compared against an independent reference — another solver, or a closed-form solution |
| `CONVERGENCE` | Mesh refinement series showing the discretization error trend |
| `THROUGHPUT` | Wall-time measurement; not an accuracy claim |
| `SCALING` | Performance across model size |
| `SELF-CONSISTENCY` | Internal check against MinuteSim's own reference, or one MinuteSim path against another |
| `DIAGNOSTIC` | Run to locate or characterize a behaviour, not to certify agreement |
| `INSUFFICIENT EVIDENCE` | The case exists and its inputs are published, but no result metric is |

### Shell benchmarks

| Benchmark | Element | Model size | Purpose | Precision | Publication |
|---|---|---|---|---|---|
| Membrane patch test | MITC4 | 1 element | `VALIDATION` | FP64 | [AS] |
| Bending patch test | MITC4 | 1 element | `SELF-CONSISTENCY` | FP64 | [AS] |
| Straight cantilever, force-driven | MITC4 | 1 × 6 | `VALIDATION` | FP64 | [AS] |
| Curved cantilever, in/out-of-plane shear | MITC4 | 5 elements along the arc | `VALIDATION` | FP64 | [AS] |
| Pinched cylinder with end diaphragms | MITC4 | 4×4 → 32×32 octant | `CONVERGENCE` | FP64 | [AS] |
| Nakajima hemispherical dome | MITC4 | 10,000 | `VALIDATION` | FP64 | [AS] |
| Nakajima contact pressure | MITC4 | 10,000 | `DIAGNOSTIC` | FP64 | [AS] |
| Nakajima mesh sensitivity | MITC4 | ~4,900 / 10,000 / ~19,900 | `CONVERGENCE` | FP64 | [AS] |
| Nakajima friction sensitivity | MITC4 | 10,000 | `SELF-CONSISTENCY` | FP64 | [AS] |
| Nakajima penalty-scale sensitivity | MITC4 | 10,000 | `SELF-CONSISTENCY` | FP64 | [AS] |
| Nakajima intermediate mesh, 40 mm stroke | MITC4 | ~50,000 | `INSUFFICIENT EVIDENCE` | FP64 | [AS] |
| Nakajima intermediate mesh, 80 mm stroke | MITC4 | 50,176 | `VALIDATION` | FP64 | [AS] |
| Nakajima throughput deck | MITC4 | ~505,000 | `THROUGHPUT` | FP64 | [AS] |

The intermediate-mesh cross-code result is published at the 80 mm production stroke only.

### S-rail full-stroke forming — demonstration case

An S-rail draw-forming case ships with the 0.9.0-beta.1 release package
(`benchmarks/srail/`). It runs the full stroke on an adaptively refined blank that grows from 675
to 6,963 elements, concentrating refinement in the S-bend and sidewalls while the flange stays
coarse.

It is **not** in the matrix above and carries no evidence class, because no reference solution,
error metric, or cross-code comparison is published for it. Its role is to show what a MinuteSim
shell run produces, which is why it supplies the shell image on the
[README](../README.md) — a full 3D formed part reads more directly there than a profile plot does.
Nakajima remains the shell **validation** benchmark and the basis of every accuracy figure in
[Validation](validation.md); the two are doing different jobs.

### Solid benchmarks

| Benchmark | Element | Model size | Purpose | Precision | Publication |
|---|---|---|---|---|---|
| Rounded flat-punch contact | Tet4 | Coarse quarter domain | `VALIDATION` | FP32 | [JMMP] |
| Hemisphere compression, L1 | Tet4 | 82,944 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression, L2 | Tet4 | 162,000 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression, L3 | Tet4 | 384,000 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression, L4 | Tet4 | 750,000 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression, L5 | Tet4 | 998,250 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression, L6 | Tet4 | 1,886,592 | `SCALING` | FP32 | [JMMP] |
| Hemisphere compression vs LS-DYNA SMP | Tet4 | 1,886,592 | `THROUGHPUT` | FP32 | [JMMP] |
| Precision comparison | Tet4 | 162,000 | `SELF-CONSISTENCY` | FP32 vs FP64 | [JMMP] |
| Contact overhead | Tet4 | 162,000 / 384,000 / 998,250 | `SCALING` | FP32 | [JMMP] |

## Hardware

Both benchmark programs ran on the same class of machine:

| Component | Specification |
|---|---|
| GPU | NVIDIA L40, 48 GB GDDR6, Ada Lovelace, 300 W |
| CPU | AMD EPYC 75F3, 32-core |
| OS | Windows 10 |

## Reading this matrix

- A `THROUGHPUT` row is a wall-time result. It says nothing about accuracy, and the late-time state
  of a throughput deck is not offered as physically meaningful.
- A `SELF-CONSISTENCY` row compares MinuteSim against itself or against its own reference value. It
  is genuine evidence of internal stability, and it is **not** independent accuracy validation.
- `CONVERGENCE` rows report a trend, not a single number. A coarse-mesh deviation in a convergence
  series is expected behaviour; what matters is that the series converges.
- Precision is listed per row because the two publications used different precision, and figures from
  one should not be combined with figures from the other.

Detail lives in [Validation](validation.md) and [Performance](performance.md). Scope boundaries are
in [Limitations](limitations.md).
