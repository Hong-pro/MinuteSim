# Known Limitations

What MinuteSim's published evidence does and does not cover, and where the solver's current
constraints lie. This page is the scope control for the results reported in
[Validation](validation.md) and [Performance](performance.md) — read it alongside them, not instead
of them.

MinuteSim is at beta maturity (0.9.0 series).

## Evidence classes

Capability statements across this documentation carry a class:

| Class | Meaning |
|---|---|
| `VALIDATED` | Documented evidence against an independent reference |
| `SUPPORTED` | Implemented and reachable from documented user input — not an accuracy claim |
| `EXPERIMENTAL` | Implemented but not stabilized, not a default, or under active numerical closure |
| `PLANNED` | Intended. No implementation claim |
| `NOT SUPPORTED` | Explicitly absent |

Implementation existing is not validation.

---

## 1. Validation scope

**Shell validation covers the Nakajima hemispherical-dome family, and it is code-to-code.** One
forming operation, one material model, one thickness, at the documented mesh sizes, compared against
another solver rather than against experiment. The published work states it should be read as
computational verification and benchmarking, not as physical forming-limit validation. Deformable
self-contact is not implemented, anisotropic earing and asymmetric springback are not addressed, and
the material constants are a generic benchmark set rather than experimentally identified.

**The validated shell model restrains the flange with a kinematic clamp rather than a binder contact
pair.** In the published setup the outer clamped ring also acts as the binder region. Blank-holder
force, draw-in, and draw beads are untested, and the published contact-pressure comparison is an
active-contact-region diagnostic against a reconstructed pressure proxy, not a validated pressure
field. Treat binder contact as unvalidated when evaluating MinuteSim for a real draw operation.

**Solid validation covers normal contact and precision agreement.** A closed-form rounded-flat-punch
comparison and a GPU/CPU precision study on a hemisphere compression model. The punch case evaluates
the normal-contact response only — deformable-to-deformable contact, self-contact, and frictional
sliding are outside it. There is no published solid validation against another commercial solver.

**The published precision comparison should not be read as a universal guarantee.** It covers one
model class; the published work notes residual significant-digit risk in near-rigid regimes and
identifies a mixed-precision strategy as needed before the higher-order tetrahedral path is pushed to
production.

**Do not mix precision across studies.** The published shell work is double precision; the published
solid work is single precision, and the product default is single precision. A figure from one study
is not evidence about the other configuration.

**The published shell throughput figure predates the shipped build** and has not been reproduced on
it. The release package's own documentation says so.

**Accuracy is mesh- and problem-dependent, as expected for finite-element discretization.** The
published benchmark series documents convergence toward the reference solution; coarse discretizations
of doubly-curved, bending-dominated geometry need refinement, and the convergence trend is reported
in [Validation](validation.md).

## 2. Benchmark scope

One workstation and one model do not establish a universal speedup. Every published performance
figure is specific to its deck, mesh, GPU, CPU, precision, and time window. MinuteSim publishes no
product-wide multiplier, and a ratio quoted without its benchmark is not a MinuteSim claim.

Cross-solver timings are user-measured, and the reference solver's input decks and raw timing logs
are not part of the published supplementary archives, so a third party cannot re-derive them.
For the shell throughput comparison, whether I/O and initialization are included is not stated in the
published record.

Full context for every figure is in [Performance](performance.md).

## 3. Input coverage

MinuteSim reads a **selected subset** of LS-DYNA-style keyword input. It is an independently
developed solver — not compatible with, equivalent to, or a drop-in replacement for any commercial
code, and an arbitrary deck written for another solver should not be expected to run unchanged.

**A supported keyword may still ignore some of its fields.** The solver accepts certain cards and
reports at run time that specific parameters on them were parsed but not applied. This is announced
in the run log rather than failing the run, so a deck can execute successfully while a setting the
user intended has no effect. Read the run log.

The keyword reference is in preparation. Until it is published, treat keyword coverage as unverified
rather than assuming a card behaves as it does elsewhere.

## 4. Platform

| Constraint | Detail |
|---|---|
| Operating system | Windows x64 only. No Linux or macOS distribution. |
| GPU vendor | NVIDIA only. |
| GPU generation | Volta or newer. Older architectures have neither compiled code nor a just-in-time path. |
| Newer GPUs | Supported through just-in-time compilation, which adds start-up time on first run. |
| CPU backend | Selectable from the command line. It is the double-precision reference path the published solid speedups are measured against, but it is not tuned for production throughput and carries no independent accuracy validation of its own. |
| **Visual C++ Redistributable** | **Required and not bundled.** The executables will not start without it. |
| Multi-GPU | `NOT SUPPORTED`. |
| FP64 throughput | Substantially lower on GPUs with reduced double-precision rates — most consumer cards and several data-centre cards, including the one used for the published measurements. |

## 5. Features not validated or experimental

| Feature | Class | Note |
|---|---|---|
| Single-precision production runs | `SUPPORTED` | The default configuration. The published shell validation campaign is double precision. |
| Adaptive shell refinement | `EXPERIMENTAL` | Exercised in the shipped demonstration deck. |
| Adaptive coarsening | `NOT SUPPORTED` | The demonstration deck carries coarsening settings, and the solver reports at run time that those fields are parsed but not applied. |
| Mass scaling across adaptive topology changes | `EXPERIMENTAL` | Still under numerical closure. Treat results combining aggressive mass scaling with topology change as provisional. |
| Solid remeshing and state transfer | `NOT SUPPORTED` in the beta distribution | The code path and its command-line switch are in the shipped executable, but an external dependency it requires is not included in the beta distribution, so the path cannot run as shipped. No validation evidence is published. |
| Implicit analysis | `EXPERIMENTAL` | Implicit static modes are selectable from the command line and are outside all published validation. |
| Material and contact coverage | — | The validated forming deck uses one shell formulation, one hardening model, and one contact formulation. Other options exist in the solver without published validation evidence. |

## 6. Reproducibility notes

The published supplementary archive ships benchmark decks, processed results, and figures — but not
the solver source, and not every raw output file. Two consequences worth knowing before attempting to
reproduce a canonical number:

- Result files for the patch tests come from earlier single-element decks that the published results
  table marks as superseded; the shipped straight-cantilever file contains a single undeformed frame.
- For the curved cantilever and pinched cylinder, tabulated values and figures ship. Result files
  ship for two of those cases but come from earlier runs on a different loading and boundary basis,
  so they do not reproduce the tabulated values.

The canonical numbers are reproducible from the documented decks; they are not re-derivable from the
shipped raw output. For bit-level reproducibility, request the original run outputs.

## 7. Documentation in preparation

The capability matrix, input reference, and output reference are not yet published, and the
third-party software disclosure is prepared but not final. Until each is published, the claims
MinuteSim stands behind are those in [Validation](validation.md), [Performance](performance.md),
[Benchmarks](benchmarks.md), and the publications listed in [Publications](publications.md).

## Reporting a problem

If a limitation is missing, overstated, or superseded, please report it through the project's issue
channel with the section, the quoted text, and what you believe the correct statement to be. Missing
limitations are treated as defects.
