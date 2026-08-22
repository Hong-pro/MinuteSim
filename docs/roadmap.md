# MinuteSim Development Roadmap

MinuteSim is being developed as a GPU-resident explicit finite-element platform for fast
engineering iteration. This roadmap summarizes released, current, and planned capabilities.

Target months for planned features may change as validation and release qualification progress.

## Timeline

<table>
<tr align="center">
<td>
<b>2026-06</b><br>
✅<br>
<b>Published Core</b><br>
<sub>Shell · solid · GPU explicit</sub>
</td>
<td>→</td>
<td>
<b>2026-08</b><br>
🟢<br>
<b>0.9.0 Beta</b><br>
<sub>Adaptive shell · forming workflow</sub>
</td>
<td>→</td>
<td>
<b>2026-08</b><br>
✅<br>
<b>Public Documentation</b><br>
<sub>Validation · benchmarks · provenance</sub>
</td>
<td>→</td>
<td>
<b>TBD</b><br>
🔵<br>
<b>Capability Expansion</b><br>
<sub>Target month not yet approved</sub>
</td>
</tr>
</table>

## Status legend

| Status | Meaning |
|---|---|
| ✅ Released | Publicly supported and documented |
| 🟢 Implemented | Implemented and currently in beta qualification |
| 🟡 Validation | Functional, but validation/release qualification is ongoing |
| 🔵 Planned | Development target is defined |
| ⚪ Future | Longer-term development direction |
| TBD | Target month has not yet been approved |

## Feature status

<table>
<tr>
<th align="left">Area</th>
<th align="left">Feature</th>
<th align="left">Status</th>
<th align="left">Completed / Target</th>
<th align="left">Current state</th>
<th align="left">Next milestone</th>
</tr>

<tr>
<td rowspan="3"><b>Elements</b></td>
<td>MITC4 shell</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Published validation against Abaqus/Explicit</td>
<td>Broader benchmark coverage</td>
</tr>
<tr>
<td>Tet4 solid</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Published closed-form contact and scaling evidence</td>
<td>Broader benchmark coverage</td>
</tr>
<tr>
<td>Additional element formulations</td>
<td>⚪ Future</td>
<td>TBD</td>
<td>Outside the published capability set</td>
<td>Target month not yet approved</td>
</tr>

<tr>
<td rowspan="4"><b>Materials</b></td>
<td>Isotropic elasticity</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Canonical shell benchmark evidence</td>
<td>—</td>
</tr>
<tr>
<td>J2 plasticity, curve hardening</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Published shell and solid benchmark evidence</td>
<td>—</td>
</tr>
<tr>
<td><b>Barlat 89 planar anisotropy</b></td>
<td>🟡 Validation</td>
<td>TBD</td>
<td>Implemented and exercised in the shipped S-rail demonstration deck; no published validation study</td>
<td>Forming validation study</td>
</tr>
<tr>
<td>Expanded anisotropic material support</td>
<td>⚪ Future</td>
<td>TBD</td>
<td>Direction under consideration</td>
<td>Target month not yet approved</td>
</tr>

<tr>
<td rowspan="3"><b>Contact</b></td>
<td>Rigid-to-deformable contact</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Validated against a closed-form normal-contact solution</td>
<td>Definition-consistent contact-pressure validation</td>
</tr>
<tr>
<td>Coulomb friction</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Published friction sensitivity study</td>
<td>—</td>
</tr>
<tr>
<td>Broader contact workflows</td>
<td>⚪ Future</td>
<td>TBD</td>
<td>Direction under consideration</td>
<td>Target month not yet approved</td>
</tr>

<tr>
<td rowspan="2"><b>Adaptive analysis</b></td>
<td>Shell local refinement</td>
<td>🟢 Implemented</td>
<td>2026-08</td>
<td>Ships in the 0.9.0 beta; demonstrated on the S-rail full-stroke deck. No independent reference comparison is published</td>
<td>Independent validation</td>
</tr>
<tr>
<td>Adaptive analysis expansion</td>
<td>⚪ Future</td>
<td>TBD</td>
<td>Direction under consideration</td>
<td>Target month not yet approved</td>
</tr>

<tr>
<td><b>Precision</b></td>
<td>FP32 and FP64 builds</td>
<td>✅ Released</td>
<td>2026-06</td>
<td>Published FP32-versus-FP64 field comparison</td>
<td>—</td>
</tr>

<tr>
<td rowspan="2"><b>Output</b></td>
<td>XDMF / HDF5 result output</td>
<td>✅ Released</td>
<td>2026-08</td>
<td>Ships in the 0.9.0 beta package</td>
<td>Post-processing improvements</td>
</tr>
<tr>
<td>Pre- and post-processing improvements</td>
<td>⚪ Future</td>
<td>TBD</td>
<td>Direction under consideration</td>
<td>Target month not yet approved</td>
</tr>
</table>

## Current development

| Target month | Area | Development item | Status |
|---|---|---|---|
| TBD | Materials | Barlat 89 forming validation study | 🟡 Validation |
| TBD | Adaptive analysis | Independent validation of shell local refinement | 🟡 Validation |
| TBD | Contact | Definition-consistent contact-pressure validation | 🟡 Validation |

The three items above are open follow-ups identified by the published work and by the current
beta capability set. **No approved target month exists for any of them yet**, so each is listed
as TBD rather than given an estimated date.

## Planned development

| Target month | Area | Planned capability | Public objective |
|---|---|---|---|
| TBD | Elements | Additional element formulations | Broader structural application coverage |
| TBD | Materials | Expanded anisotropic material support | Broader sheet-metal material coverage |
| TBD | Contact | Broader contact workflows | Broader nonlinear application coverage |
| TBD | Adaptive analysis | Adaptive analysis expansion | Wider forming-process coverage |
| TBD | Tooling | Pre- and post-processing improvements | Faster engineering iteration |

These are development directions, not commitments. Target months are approved and published here
only once they are set.

## Completed milestones

| Completed | Milestone | Evidence |
|---|---|---|
| 2026-08 | Public documentation, validation and benchmark record | This repository |
| 2026-08 | MinuteSim 0.9.0 beta capability set — adaptive shell refinement, full-stroke forming workflow, FP32 and FP64 builds | Beta release package |
| 2026-06 | Shell validation and throughput benchmarking published | [Applied Sciences 16(12), 5826](https://doi.org/10.3390/app16125826), 2026-06-09 |
| 2026-06 | Solid GPU-resident pipeline and scaling published | [JMMP 10(6), 197](https://doi.org/10.3390/jmmp10060197), 2026-06-03 |

## How to read this page

A capability being **implemented** is not the same as its being **validated**, and neither is the
same as its being **publicly supported**. This roadmap separates the three, and
[Validation](validation.md) carries the measured evidence behind every ✅ entry. Where a target
month has not been approved, this page says TBD instead of estimating one.
