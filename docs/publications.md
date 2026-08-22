# Publications

Peer-reviewed publications by the MinuteSim developers. Together they form the public technical
evidence base for the solver: what it does, how its execution is organized, and how far it has been
verified and benchmarked.

MinuteSim's source code is not public. These papers, and the supplementary data published with them,
are therefore the primary way an outside reader can examine the solver's numerical behaviour
independently.

> **This page is not a validation claim.** A publication documents the configurations it studied.
> It does not certify the product, and it does not extend to capabilities the paper did not test.
> For what is and is not covered, read [Limitations](limitations.md).

**Distinction from the references page** (in preparation): this page lists work *authored by* the
MinuteSim developers. The references page will list the external literature, standards, and technical
documentation that MinuteSim's formulations are *derived from or checked against*. The two are kept
separate on purpose — publishing about a solver and citing the theory it rests on are different
kinds of evidence.

---

## 1. GPU-Resident MITC4 Shell Solver — verification, validation, and throughput

H. Kim, S. Hong, and N. Kim, "A GPU-Resident MITC4 Shell Solver for a Nakajima Hemispherical-Dome
Forming Benchmark: Verification, Abaqus Validation, and LS-DYNA Throughput Benchmarking,"
*Applied Sciences*, **16**(12), 5826, 2026.

**DOI: [10.3390/app16125826](https://doi.org/10.3390/app16125826)**

### Key published results

| Result | Value | Configuration |
|---|---|---|
| Nakajima agreement with Abaqus/Explicit 2024 HF3 (S4) | Mean von Mises difference **2.95 %** over **94 %** of specimen elements | 10,000 elements, 80 mm stroke, FP64 |
| Maximum shell-thickness difference | **2.08 %** | same |
| Intermediate-mesh check | Section-mean von Mises **+0.6 %** globally, **+0.4 %** in the transition band; section-maximum transition-band gap **−4.3 %** | 50,176 elements, 80 mm stroke |
| Canonical cantilevers | Straight **1.65 %**; curved about **±5 %** vs MacNeal & Harder | 1 × 6 and 5-element meshes |
| Pinched-cylinder convergence | **−0.6 %** at the finest mesh | 32×32 octant |
| Throughput | **643 s** over **15,808** steps | ~505,000 elements, NVIDIA L40, FP64 |
| Per-step speedup vs LS-DYNA MPP R14.1 | **43.7× / 17.7× / 13.5×** | 1 / 8 / 32 CPU cores, same workstation |

### Evidence provided

- Canonical MITC4 shell verification against classical benchmark problems
- Nakajima hemispherical-dome forming benchmark
- Validation against Abaqus/Explicit 2024 HF3 using S4 shells
- Mesh, friction, and contact-penalty sensitivity studies
- Contact-pressure comparison
- Throughput benchmark on a ~505,000-element model
- Throughput comparison against LS-DYNA MPP R14.1

A supplementary archive published with the paper contains the benchmark input decks, processed
result data, timing summaries, and the figures and tables the manuscript is computed from. It
deliberately excludes the solver source and the largest raw result files.

### Scope and caveats

The results correspond to the configurations documented in the paper and must not be generalized
beyond them. Specifically:

- The published runs are **double precision**. MinuteSim's default configuration is single precision.
- The throughput comparison is a **user-measured** result for one benchmark deck at specific core
  counts on one workstation. The supplementary archive does not contain the reference solver's input
  deck or raw timing logs, so a third party cannot re-derive it from the published material. It is a
  throughput measurement, not accuracy evidence, and does not support a product-wide speed claim.
- Agreement with the reference code is **zone-dependent**, and the validated model does not include
  binder or blank-holder contact.

All three caveats, with numbers, are set out in [Limitations](limitations.md).

---

## 2. GPU-Resident Integrated Execution Pipeline — architecture and computational efficiency

H. Kim, S. Hong, and N. Kim, "Design and Computational Efficiency of a GPU-Resident Integrated
Execution Pipeline for Explicit Large-Deformation Finite Element Analysis," *Journal of
Manufacturing and Materials Processing*, **10**(6), 197, 2026.

**DOI: [10.3390/jmmp10060197](https://doi.org/10.3390/jmmp10060197)**

### Key published results

| Result | Value | Configuration |
|---|---|---|
| Per-step speedup vs MinuteSim's single-thread CPU path | **98.7×** at 82,944 elements, rising to a peak of **137.6×** at 998,250 | Hemisphere compression, Tet4, six mesh levels |
| Largest model | **137.2×**, 3,378 µs/step | 1,886,592 Tet4 elements |
| Scaling behaviour | Plateau near 137× above roughly 1 M elements | six mesh levels |
| Speedup vs LS-DYNA in shared-memory mode | **≈ 94×** faster than the best 8-core configuration | SMP measured at 1/2/4/8/16/32 cores |
| Contact cost | **+13 % to +21 %** added to step time | contact enabled vs disabled |
| Closed-form contact validation | Normal force **+1.69 %**, contact radius **+1.0 %** | rounded flat punch, coarse Tet4 |
| GPU FP32 vs CPU FP64, same model | von Mises **0.27 %**, displacement **0.99 %**, force history **0.31 %** relative L2 | 162,000 Tet4, J2 elastoplastic, penalty contact |

Hardware for all rows: NVIDIA L40 (48 GB, Ada Lovelace) and AMD EPYC 75F3 32-core. The three-run
median statistic applies to the GPU mesh-scaling and contact-overhead timings; the closed-form
contact and precision rows are single documented comparisons. The CPU side of the speedup rows is
MinuteSim's own single-thread CPU path, not a third-party code.

### Evidence provided

- Design of a GPU-resident execution pipeline for explicit large-deformation analysis
- GPU-resident explicit integration, device-side force evaluation, and device-side contact processing
- Scalability across model size on a hemisphere compression benchmark, six mesh resolutions
- Throughput comparison against single-core CPU execution and against a commercial solver in
  shared-memory mode
- Contact validation against a closed-form analytical solution
- Field-level agreement between the GPU single-precision and CPU double-precision paths

The paper describes how that pipeline is organized internally. This documentation deliberately does
not restate those details; read the paper for them.

### Scope and caveats

This paper documents an execution-pipeline design and the benchmark configuration used to study it.
It is an architecture and performance study, **not** a validation of MinuteSim's physics, and it does
not imply that every current MinuteSim capability shares the validation status of the shell work in
publication 1.

The paper states its own configuration limits, and they differ from publication 1 and from the
shipped defaults in ways worth knowing before comparing numbers across the two papers:

- **Single precision (FP32)** — the opposite of publication 1, whose runs are double precision.
- **Single-GPU execution.**
- A contact configuration that differs from the shipped default. The paper's performance figures
  therefore do not describe the shipped configuration.

Reported speedups are relative to the specific comparison basis and hardware stated in the paper.

---

## How the two papers relate

```text
                        MinuteSim
                            │
              ┌─────────────┴──────────────┐
              │                            │
     Execution architecture        Shell / forming behaviour
              │                            │
        JMMP 2026 (2)              Applied Sciences 2026 (1)
              │                            │
   GPU-resident pipeline          MITC4 verification
   large-deformation flow         Abaqus/Explicit validation
   device-side execution          LS-DYNA MPP throughput comparison
   CPU + LS-DYNA SMP comparison
              │                            │
              └─────────────┬──────────────┘
                            ▼
                   Public evidence base
```

Publication 2 addresses *why the computation is organized the way it is*. Publication 1 addresses
*how far the resulting solver has been verified and validated for shell forming*. Neither substitutes
for the other, and neither covers capabilities outside its own scope.

---

## Reuse of published material

Both papers are open access under the **Creative Commons Attribution 4.0 International licence
(CC BY 4.0)**. Figures, tables, and data from them may be reused, including commercially, provided
the original work is attributed — for example:

```text
Figure replotted from data in H. Kim, S. Hong and N. Kim, Applied Sciences 16(12), 5826, 2026,
https://doi.org/10.3390/app16125826 . © 2026 the authors. Licensed under CC BY 4.0,
https://creativecommons.org/licenses/by/4.0/ . Modified: values re-plotted from the published
table; no published figure reproduced. Provided as-is, without warranties.
```

**Exception:** where a paper itself reproduces material owned by a third party, that material is not
covered by the paper's CC BY licence. It carries its own rights and must be cleared separately. Check
the figure credit line before reusing anything.

This repository links to the publisher-hosted articles rather than committing copies of them. The DOI
is the canonical identifier and will keep resolving if publisher URLs change.

---

## Reporting a problem with this page

If a citation is incorrect, incomplete, or has been superseded, please report it through the
project's issue channel with the entry and the corrected details.
