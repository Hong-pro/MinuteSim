# Performance

MinuteSim keeps the whole explicit time step on the GPU. This page reports what that produces on
benchmark workloads, with the hardware, precision, model, and comparison basis attached to every
number.

Most figures here come from the two peer-reviewed publications listed in
[Publications](publications.md) — [Applied Sciences 16(12), 5826](https://doi.org/10.3390/app16125826)
for shell and [JMMP 10(6), 197](https://doi.org/10.3390/jmmp10060197) for solid.

**One exception:** the "Shell — latest internal result" section below reports an **internal
measurement that has not been published**. Its hardware and precision have not been reconfirmed, and
it is compared against the *published* LS-DYNA reference timing rather than a fresh reference run.
It is marked as such where it appears.

## Summary

| Domain | Benchmark | MinuteSim | Comparison | Result |
|---|---|---|---|---|
| Solid | Hemisphere compression, 1.89 M Tet4 | 3,378 µs/step (L40, FP32) | MinuteSim's single-thread CPU path (EPYC 75F3, FP64) | **137.2×** per step |
| Solid | Same, six mesh levels, 83 K → 1.89 M elements | — | MinuteSim's single-thread CPU path | **98.7×** at 83 K, peak **137.6×** near 1 M, **137.2×** at 1.89 M |
| Solid | Same problem | single GPU | LS-DYNA SMP, best 8-core configuration | **≈ 94×** faster |
| Shell | Nakajima dome, ~505 K elements | 643 s / 15,808 steps (L40, FP64) | LS-DYNA MPP R14.1, 1 / 8 / 32 cores | **43.7× / 17.7× / 13.5×** per step |

---

## Solid — hemisphere compression

<table>
<tr>
<td width="44%"><img src="../assets/solid-result.png" width="100%"><br>
<sub>Published benchmark model — JMMP 2026, Figure 2 (CC BY 4.0)</sub></td>
<td width="56%" valign="top">

**Hemisphere compression scaling study**

- Rigid punch against a deformable block, Tet4
- Six mesh levels, 82,944 → 1,886,592 elements
- NVIDIA L40, GPU FP32 against CPU FP64
- Peak **137.6×** vs MinuteSim's single-thread CPU path

</td>
</tr>
</table>

![Solid scaling](../assets/solid-scaling.png)

### Configuration

| Item | Value |
|---|---|
| Benchmark | Hemisphere compression, rigid punch against a deformable block |
| Element | Tet4, single-point integration |
| Model sizes | Six levels: 82,944 · 162,000 · 384,000 · 750,000 · 998,250 · 1,886,592 elements |
| GPU | NVIDIA L40, 48 GB GDDR6, Ada Lovelace, 300 W |
| CPU | AMD EPYC 75F3, 32-core |
| Precision | GPU single precision; CPU reference double precision |
| Statistic | Median of three runs; output disabled during timing, first 200 steps excluded as warm-up |
| Execution mode | GPU graph capture disabled — not the shipped default |
| CPU baseline | MinuteSim's own CPU path, single thread. This is a GPU-versus-CPU comparison of the same solver, not a comparison against a third-party code. |

### Measured step times

| Level | Elements | MinuteSim CPU, 1 thread (µs/step) | MinuteSim GPU (µs/step) | Per-step speedup |
|---|---|---|---|---|
| L1 | 82,944 | 24,053 | 243.6 | **98.7×** |
| L2 | 162,000 | 44,966 | 386.0 | **116.5×** |
| L3 | 384,000 | 104,012 | 822.5 | **126.5×** |
| L4 | 750,000 | 187,375 | 1,391.0 | **134.7×** |
| L5 | 998,250 | 251,752 | 1,829.0 | **137.6×** |
| L6 | 1,886,592 | 463,434 | 3,378.0 | **137.2×** |

### Scaling behaviour

Speedup rises with model size and flattens: from about 99× at 83 K elements to a peak near 138× at
about 1 M elements, holding near 137× at 1.89 M. Larger models amortize fixed per-step overhead over
more work, and the curve plateaus once that overhead is no longer the limiter.

This is a useful property in practice — the advantage does not erode as models grow into the range
where explicit analysis is expensive.

### Contact cost

Enabling contact adds a net **+13 % to +21 %** to step time, measured at three mesh levels —
162,000, 384,000 and 998,250 elements (+20.9 %, +16.6 %, +13.0 % respectively). The overhead falls
as the model grows. This is a net contact-ON minus contact-OFF difference under the published
instrumentation, not an isolated contact-kernel time.

### Against LS-DYNA in shared-memory mode

On the same problem, MinuteSim on a single GPU is **roughly 94× faster than the best 8-core LS-DYNA
SMP configuration**. LS-DYNA SMP scalability was measured at 1, 2, 4, 8, 16, and 32 cores; the margin
reflects the multicore saturation observed in those measurements.

This is a **shared-memory** comparison. The published solid study states that the distributed-memory
picture is substantively different and identifies a balanced distributed-memory comparison as work
not yet done. The shell throughput benchmark below does use a distributed-memory reference, but on a
different solver path, a different element type, and a different problem — it is not evidence about
solid distributed-memory scaling.

---

## Shell — latest internal result

<table>
<tr>
<td width="44%"><img src="../assets/benchmarks/nakajima-model.png" width="100%"><br>
<sub>Nakajima dome model. The throughput deck uses the same geometry at ~505,000 elements.</sub></td>
<td width="56%" valign="top">

**Large-model Nakajima throughput**

- ~505,000 shell elements
- 15,808 explicit steps
- **125.1 s** wall time
- ≈ 224.8× per step vs the published LS-DYNA MPP 1-core timing

This is a **throughput** measurement over a fixed step window, not a
full-stroke forming run.

</td>
</tr>
</table>

![Latest shell benchmark](../assets/shell-speedup.png)

A more recent internal run of the same ~505,000-element Nakajima deck over the same
15,808-step window completed in **125.1 s**, i.e. **0.007914 s/step**.

| Comparison basis | Latest per-step speedup |
|---|---|
| LS-DYNA MPP R14.1, 1 core (published reference timing) | **224.8×** |
| LS-DYNA MPP R14.1, 8 cores (published reference timing) | **90.8×** |
| LS-DYNA MPP R14.1, 32 cores (published reference timing) | **69.3×** |
| MinuteSim's own published build (643 s) | **5.14×** improvement |

**This result is internal and not yet published.** It is compared against the *published*
LS-DYNA reference timing rather than a fresh reference run. The latest run's hardware and
precision have not been reconfirmed, so — unlike the published comparison below — **it is
not a same-workstation comparison**, and it should not be read as one. Treat it as
`EXPERIMENTAL` evidence pending publication of its configuration.

## Shell — published Nakajima dome throughput

![Shell throughput](../assets/shell-throughput.png)

The peer-reviewed throughput comparison, retained here as the historical reference basis.
These are the figures the latest result above is measured against.

### Configuration

| Item | Value |
|---|---|
| Benchmark | Nakajima hemispherical-dome forming, throughput deck |
| Model size | ~505,000 shell elements |
| Window | 1.0 × 10⁻³ s, 15,808 explicit steps |
| GPU | NVIDIA L40 |
| CPU | AMD EPYC 75F3, 32-core, same workstation |
| Precision | Double precision |
| Reference solver | LS-DYNA MPP R14.1, ELFORM 16 shells |

### Results

| Configuration | Wall time | Per-step time | Per-step speedup |
|---|---|---|---|
| **MinuteSim, GPU** | **643 s** | 0.0407 s | — |
| LS-DYNA MPP, 1 core | 28,127 s | 1.779 s | **43.7×** |
| LS-DYNA MPP, 8 cores | 11,355 s | 0.718 s | **17.7×** |
| LS-DYNA MPP, 32 cores | 8,674 s | 0.549 s | **13.5×** |

Both solvers ran on the same workstation, so the comparison is like-for-like in hardware.

### Interpretation

The speedup shrinks as CPU cores are added, as it should — 32 cores of LS-DYNA MPP close most of the
gap to 8 cores, but the distributed-memory scaling is sublinear, so the GPU advantage persists at
every core count measured.

This is a **throughput** measurement. Accuracy for the shell path is established on the
10,000-element deck, documented in [Validation](validation.md), not on this one. The late-time state
of a throughput deck is not offered as physically meaningful.

---

## Scope of these numbers

Read every figure on this page with its configuration attached. Specifically:

**No product-wide multiplier exists.** "MinuteSim is N× faster" is not a claim MinuteSim makes. The
supported form names the benchmark, the hardware, the precision, and the comparison basis — as the
tables above do.

**Precision differs between the two studies.** The solid results are GPU single precision against a
double-precision CPU reference; the shell throughput result is double precision throughout. Do not
combine a figure from one with a figure from the other.

**Cross-solver timings are user-measured** on a single workstation with vendor-default reference-solver
settings, and could shift on a tuned cluster. The LS-DYNA input decks and raw timing logs are not part
of the published supplementary archives, so a third party cannot re-derive those rows from the
published material. These are runtime benchmarks, not a total-cost-of-ownership analysis.

**I/O and initialization inclusion is not stated** in the published record for the shell throughput
comparison. That matters for a CPU-versus-GPU ratio and is an open question rather than an assumption.

**The shell throughput figure predates the shipped build.** It was measured on an earlier build and
has not been reproduced on the current beta; the release package's own documentation says so.

**The solid benchmark configuration is not the shipped configuration.** The published solid runs used
a contact configuration and an execution mode that differ from the shipped defaults.

**One benchmark is not a performance model.** Each row is one deck, one mesh, one GPU, one precision,
one window. Extrapolating to a different model, element mix, or machine is not supported by this
evidence.

---

## Reproducing these results

The benchmark input decks and processed result data for the shell work are published in the
supplementary archive accompanying the Applied Sciences paper. The solid benchmark configuration is
documented in the JMMP paper. See [Benchmarks](benchmarks.md) for the full matrix.

---

## S-rail Full-Stroke Forming

**Up to 10.3× faster than OpenRadioss on the full-stroke S-rail benchmark, measured across both
refinement levels and the full CPU thread sweep.**

![S-rail cross-solver performance](../assets/srail-performance.png)

The same deck and the same 9.9 ms stroke throughout. Two adaptive refinement levels ship with the
benchmark, so the comparison is measured at two problem sizes rather than one — see
[Benchmark Cases](benchmarks.md#s-rail-full-stroke-forming) for the model.

### Configuration

| Item | MinuteSim | OpenRadioss |
|---|---|---|
| Version | 0.9.0-beta.2 | Built from source at commit `bd4557b`, 2026-08-21 |
| Build | Windows, CUDA | Linux 64-bit, GNU compiler |
| Hardware | NVIDIA L40 | Intel Core i5-13400F — 10 cores / 16 threads |
| **Precision** | **FP32** | **FP64 (double-precision build)** |
| Shell formulation | MITC4 (ELFORM 16) | Fully integrated 4-node shell, `Ishell = 12` |
| Timing | Full-stroke wall clock, output enabled | Full-stroke wall clock |

**Two asymmetries matter and are not corrected for.**

**Precision is not matched.** MinuteSim runs single precision; the OpenRadioss build is
double precision. That difference favours MinuteSim, and no single-precision OpenRadioss build was
measured, so the size of the effect is unknown rather than estimated.

**This is not a same-workstation comparison.** The OpenRadioss sweep ran on the i5-13400F above;
the MinuteSim timings are L40 measurements taken on different hardware. The two solvers were not
run side by side, unlike the published Nakajima comparison earlier on this page.

Both solvers use a **fully integrated** 4-node shell, so the element formulation is matched in kind.

| | L2 deck (`MAXLVL 3`) | L3 deck (`MAXLVL 4`) |
|---|---:|---:|
| Blank at start | 675 elements | 675 elements |
| Model at full stroke | ~11,300 | ~40,400 |
| Explicit steps | 40,494 | 79,926 |
| **MinuteSim** — NVIDIA L40, FP32 | **157 s** | **705 s** |
| OpenRadioss best — 8 CPU threads | 678 s | 2,869 s |
| Speedup vs best CPU configuration | **4.3×** | **4.1×** |
| Speedup vs 2-thread CPU | **9.7×** | **10.3×** |

### OpenRadioss CPU scaling

| CPU threads | L2 deck [s] | MinuteSim speedup | L3 deck [s] | MinuteSim speedup |
|---:|---:|---:|---:|---:|
| 2 | 1,528 | 9.7× | 7,276 | 10.3× |
| 3 | 932 | 5.9× | 5,376 | 7.6× |
| 4 | 874 | 5.6× | 4,469 | 6.3× |
| 5 | 734 | 4.7× | 3,431 | 4.9× |
| 6 | 722 | 4.6× | 3,159 | 4.5× |
| 7 | 754 | 4.8× | 3,007 | 4.3× |
| **8** | **678** | **4.3×** | **2,869** | **4.1×** |
| 9 | 724 | 4.6× | 4,794 | 6.8× |
| 10 | 710 | 4.5× | 2,980 | 4.2× |

OpenRadioss reaches its best runtime at **8 threads on both decks** and does not improve beyond
that; from 2 to 8 threads it gains 2.3× on L2 and 2.5× on L3, well short of the 4× the thread
count would suggest. The headline comparison uses that best CPU result.

The 9-thread points sit off the trend on both decks. They are reported as measured rather than
dropped or re-run.

### Interpretation

**This benchmark is too small to show what GPU-resident execution is for.** At ~11,000 and
~40,400 elements, the S-rail decks sit far below the size where a GPU is worth reaching for. A
device of this class is nowhere near saturated by tens of thousands of shell elements, so most of
its throughput goes unused and a large part of each step is fixed overhead rather than element
work. Four to ten times is what that regime produces — it is not the ceiling, and it should not be
read as one.

The flatness across the two levels says the same thing from another angle: quadrupling the element
count barely moves the ratio, because neither solver is yet limited by the thing that separates
them. The GPU advantage widens with problem size, and this case is not large enough to show it.

The ~505,000-element Nakajima throughput deck on this page is where that regime begins. It is a
different measurement with a different reference and metric, so the two are not points on one
curve — but the size difference is the reason the margins differ so much.

### Scope of this comparison

The S-rail and Nakajima results are **not** a single scaling curve. Three things differ:

| | S-rail | Nakajima throughput |
|---|---|---|
| Reference solver | OpenRadioss, CPU thread sweep | LS-DYNA MPP R14.1, published timing |
| Metric | Wall clock, full stroke | Per step, fixed step window |
| Basis | Both measured here | MinuteSim measured, reference published |

Quoting the S-rail speedup beside the Nakajima per-step figure as if they were points on one curve
would overstate both. They are separate benchmarks with separate reference configurations.

Every number here is a runtime comparison only. **Neither is an accuracy result** — no reference
solution is compared against the S-rail case. Measured shell accuracy is reported in
[Validation](validation.md).

Read the S-rail figures with the two asymmetries in the configuration table attached: MinuteSim is
single precision against a double-precision OpenRadioss build, and the two solvers ran on different
machines. A precision-matched, same-workstation S-rail comparison has not been measured.
