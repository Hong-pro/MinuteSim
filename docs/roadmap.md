# MinuteSim Development Roadmap

MinuteSim is being developed as a GPU-resident explicit finite-element platform for fast
engineering iteration. This roadmap summarizes released, current, and planned capabilities.

Target months for planned features may change as validation and release qualification progress.

## Timeline

<table>
<tr align="center">
<td>
<b>2026-02</b><br>✅<br>
<b>GPU Explicit Core</b><br>
<sub>Shell · solid · CUDA backend</sub>
</td>
<td>→</td>
<td>
<b>2026-03</b><br>✅<br>
<b>Contact &amp; Materials</b><br>
<sub>Penalty contact · anisotropy · output</sub>
</td>
<td>→</td>
<td>
<b>2026-06</b><br>✅<br>
<b>Peer-Reviewed</b><br>
<sub>Shell and solid publications</sub>
</td>
<td>→</td>
<td>
<b>2026-07</b><br>🟢<br>
<b>Adaptive Analysis</b><br>
<sub>Shell refinement · formulation dispatch</sub>
</td>
<td>→</td>
<td>
<b>2026-08</b><br>✅<br>
<b>0.9.0 Beta</b><br>
<sub>Release package · public documentation</sub>
</td>
<td>→</td>
<td>
<b>TBD</b><br>🔵<br>
<b>Qualification</b><br>
<sub>Target month not yet approved</sub>
</td>
</tr>
</table>

## How to read the status columns

A capability being **implemented** is not the same as its being **validated**, and neither is the
same as its being **released** for public use. This page tracks the three separately.

| Column | Meaning |
|---|---|
| **Implemented** | Month the capability first appears in the solver's own development history |
| **Evidence** | What independent evidence exists for it today |
| **Release** | How it is offered in the shipped product |

| Evidence | Meaning |
|---|---|
| ✅ Published validation | An independent or reference comparison for this capability is published |
| 📘 Published evidence | The capability was exercised, characterized or benchmarked in peer-reviewed work, but not independently validated as a standalone feature |
| 🟡 Qualification ongoing | Functional; validation or release qualification in progress |
| ⚪ No public evidence yet | No published evidence for this capability |

| Release | Meaning |
|---|---|
| **Supported** | Documented public capability |
| **Beta** | Ships, not fully qualified |
| **Internal** | Present but not offered publicly |
| **Not shipped** | Development tree only |

The two are independent. A capability can be **Supported** on 📘 evidence: it is reachable,
documented and exercised in published work, without a standalone independent validation of that
feature on its own.

Implementation months come from the solver's own version-control history. Where a capability was
already present in the first recorded commit, the month is written **2026-02 or earlier** rather
than estimated more precisely.

## Feature status

### Published and supported

<table>
<tr>
<th align="left">Area</th><th align="left">Capability</th><th align="left">Implemented</th>
<th align="left">Evidence</th><th align="left">Release</th><th align="left">Next milestone</th><th align="left">Target month</th>
</tr>
<tr>
<td rowspan="2"><b>Elements</b></td>
<td>MITC4 shell</td><td>2026-02 or earlier</td>
<td>✅ Published validation — Abaqus/Explicit comparison</td><td><b>Supported</b></td><td>Broader benchmark coverage</td><td>—</td>
</tr>
<tr>
<td>Tet4 solid</td><td>2026-02 or earlier</td>
<td>✅ Published validation — closed-form normal contact</td><td><b>Supported</b></td><td>Broader benchmark coverage</td><td>—</td>
</tr>
<tr>
<td rowspan="2"><b>Materials</b></td>
<td>Isotropic elasticity</td><td>2026-02 or earlier</td>
<td>✅ Published validation — canonical shell benchmarks</td><td><b>Supported</b></td><td>—</td><td>—</td>
</tr>
<tr>
<td>J2 plasticity, curve hardening</td><td>2026-02 or earlier</td>
<td>📘 Published evidence — exercised in the validated benchmarks; no standalone material validation</td><td><b>Supported</b></td><td>—</td><td>—</td>
</tr>
<tr>
<td rowspan="2"><b>Contact</b></td>
<td>Rigid-to-deformable contact</td><td>2026-03</td>
<td>✅ Published validation — closed-form normal contact</td><td><b>Supported</b></td><td>Definition-consistent contact-pressure validation</td><td>—</td>
</tr>
<tr>
<td>Coulomb friction</td><td>2026-03</td>
<td>📘 Published evidence — sensitivity study, not independent validation</td><td><b>Supported</b></td><td>—</td><td>—</td>
</tr>
<tr>
<td><b>Precision</b></td>
<td>FP32 and FP64 builds</td><td>2026-02 or earlier</td>
<td>📘 Published numerical comparison — self-consistency, not accuracy validation</td><td><b>Supported</b></td><td>—</td><td>—</td>
</tr>
<tr>
<td><b>Output</b></td>
<td>XDMF / HDF5 result output</td><td>2026-03</td>
<td>📘 Published evidence — the published results were produced through it</td><td><b>Supported</b></td><td>Post-processing coverage</td><td>—</td>
</tr>
<tr>
<td><b>GPU execution</b></td>
<td>GPU-resident explicit solve</td><td>2026-02 or earlier</td>
<td>📘 Published performance evidence — throughput and scaling</td><td><b>Supported</b></td><td>—</td><td>—</td>
</tr>
</table>

### Implemented, qualification ongoing

<table>
<tr>
<th align="left">Area</th><th align="left">Capability</th><th align="left">Implemented</th>
<th align="left">Evidence</th><th align="left">Release</th><th align="left">Next milestone</th><th align="left">Target month</th>
</tr>
<tr>
<td rowspan="2"><b>Elements</b></td>
<td>Tet10 solid</td><td>2026-02 or earlier</td>
<td>⚪ No public evidence yet — stable-timestep validation deferred</td><td><b>Beta</b> — not the default</td>
<td>Timestep validation, then default qualification</td><td>TBD</td>
</tr>
<tr>
<td>Additional shell formulations</td><td>2026-07</td>
<td>⚪ No public evidence yet</td><td><b>Internal</b></td>
<td>Qualification not yet scheduled</td><td>TBD</td>
</tr>
<tr>
<td rowspan="2"><b>Materials</b></td>
<td>Barlat 89 planar anisotropy</td><td>2026-03</td>
<td>🟡 Qualification ongoing — exercised in the shipped demonstration deck; formulation work continues</td><td><b>Beta</b></td>
<td>Forming validation study</td><td>TBD</td>
</tr>
<tr>
<td>Ductile damage / element erosion</td><td>2026-03</td>
<td>⚪ No public evidence yet</td><td><b>Internal</b></td>
<td>Qualification not yet scheduled</td><td>TBD</td>
</tr>
<tr>
<td><b>Adaptive analysis</b></td>
<td>Shell local refinement</td><td>2026-07</td>
<td>🟡 Qualification ongoing — demonstrated on the shipped S-rail deck; no independent comparison</td><td><b>Beta</b></td>
<td>Independent validation</td><td>TBD</td>
</tr>
<tr>
<td><b>Output</b></td>
<td>Offline solid HDF5 → d3plot conversion</td><td>2026-03</td>
<td>⚪ Development utility; solid element data only</td><td><b>Not shipped</b></td>
<td>Post-processing interoperability review</td><td>TBD</td>
</tr>
</table>

#### Output-format note

MinuteSim writes **XDMF over HDF5**. It does not write d3plot files. `*DATABASE_BINARY_D3PLOT` is
accepted from the keyword deck, but only as an **output-cadence** setting — it schedules writes, it
does not select a d3plot writer. An offline HDF5-to-d3plot converter exists in the development tree;
it covers **solid element data only**, has no shell coverage, and is **not part of the release
package**.

| Capability | Shell | Solid | Current state | Shipped |
|---|---|---|---|---|
| `*DATABASE_BINARY_D3PLOT` keyword parsing | ✅ | ✅ | Output cadence only | ✅ |
| Native d3plot writer | ✕ | ✕ | Does not exist | ✕ |
| Offline HDF5 → d3plot conversion | ✕ | ✅ | Development tool, dormant since 2026-03 | ✕ |
| XDMF / HDF5 output | ✅ | ✅ | Product output format | ✅ |

### Planned

| Target month | Area | Planned capability | Public objective |
|---|---|---|---|
| TBD | Elements | Qualification of additional element formulations | Broader structural application coverage |
| TBD | Materials | Barlat 89 forming validation study | Published anisotropic forming accuracy |
| TBD | Adaptive analysis | Independent validation of shell refinement | Accuracy evidence for adaptive forming |
| TBD | Contact | Definition-consistent contact-pressure validation | Closes an open item from the published work |
| TBD | Output | Broader post-processing interoperability | Easier downstream workflow integration |

No approved target month exists for any planned item, so each is listed as TBD rather than given an
estimated date. These are development directions, not commitments.

## Related pages

Format-level direction for model import, result export and checkpointing is in the
[I/O Roadmap](io-roadmap.md). Components MinuteSim distributes or expects you to install are listed
in [Third-Party Software](third-party-software.md).

## Completed milestones

| Completed | Milestone | Evidence |
|---|---|---|
| 2026-08 | Public documentation, validation and benchmark record | This repository |
| 2026-08 | MinuteSim 0.9.0 beta release package — FP32 and FP64 builds, adaptive shell refinement, full-stroke forming demonstration deck | Beta release package |
| 2026-07 | Adaptive shell refinement; shell formulation dispatch | Solver development history |
| 2026-06 | Solid GPU-resident pipeline and scaling published | [JMMP 10(6), 197](https://doi.org/10.3390/jmmp10060197), 2026-06-03 |
| 2026-06 | Shell validation and throughput benchmarking published | [Applied Sciences 16(12), 5826](https://doi.org/10.3390/app16125826), 2026-06-09 |
| 2026-03 | Penalty contact; XDMF output; anisotropic and damage material work | Solver development history |
| 2026-02 | GPU-resident explicit core with shell and solid elements | Solver development history |
