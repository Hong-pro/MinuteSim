# MinuteSim Documentation Governance

This document explains how MinuteSim's public documentation is written, reviewed, and maintained,
and what a reader is entitled to expect from it.

MinuteSim is a proprietary GPU-resident explicit finite element solver. Its documentation is
public; its implementation is not. This document describes how that line is drawn, so that readers
can judge the documentation on its own terms.

---

## 1. What this documentation is for

Public MinuteSim documentation exists to answer, for users, evaluators, customers, and researchers:

- **What is MinuteSim, and what problems does it solve?**
- **What does it support today** — and what does it not?
- **How is a model prepared, run, and post-processed?**
- **What evidence backs each capability claim?**
- **What are the known limitations?**
- **What theoretical and third-party foundations does it rest on?**

It is technical documentation, not marketing copy.

---

## 2. What is published and what is not

**Published.** What MinuteSim does, how it is used, how it has been validated, what it measured, what
it cannot do, and what public sources support it.

**Not published.** How the proprietary implementation achieves those results — solver source,
internal algorithm implementation, and implementation micro-architecture.

This is a deliberate boundary, not an oversight. Technical credibility here comes from reproducible
validation, transparent limitations, accurate references, clear capability boundaries, measured
performance, and traceable provenance — not from published source.

Where a description would cross that line, the documentation states the capability and stops. If a
reader needs more detail than the documentation provides in order to evaluate MinuteSim, that is a
reasonable request to raise with the project rather than a gap to be inferred around.

---

## 3. Capability claims carry an evidence class

Every substantial capability statement is labelled:

| Class | Meaning |
|---|---|
| `SUPPORTED` | Implemented and reachable through documented user input |
| `VALIDATED` | `SUPPORTED`, plus documented evidence against a reference solution |
| `EXPERIMENTAL` | Implemented but not stabilized, not a default, or under active numerical closure |
| `PLANNED` | Intended. **No implementation claim whatsoever.** |
| `NOT SUPPORTED` | Explicitly absent |

Two consequences worth stating plainly:

- **A feature is not `VALIDATED` because the code exists.** Validation requires evidence.
- **`PLANNED` never implies partial availability.** If it is planned, it does not work yet.

Where evidence has not yet been assembled, the documentation says so explicitly rather than
producing plausible text. A reader encountering an explicit "requires verified source" marker is
looking at an acknowledged gap, not an accidental omission.

---

## 3b. Evidence discipline and narrative priority are different things

Evidence discipline governs whether a statement may be made. Narrative priority governs where it
appears. The two are often confused, and confusing them produces documentation that is accurate and
still misleading.

**Public documentation may foreground strong verified results.** A validated headline result and a
scope limitation do not need equal visual prominence merely because both exist. Leading with
caveats would misrepresent the evidence just as surely as omitting them.

What does not bend:

- A limitation that materially affects how a result should be interpreted stays easy to find, and is
  stated in the same document as the result it qualifies.
- Every number keeps its benchmark, hardware, precision, and comparison basis attached.
- No result is generalized beyond the configuration that produced it.
- A self-consistency check is never presented as independent validation.

So a benchmark's coarse-mesh error belongs in a convergence series, not in a headline; a
region-dependent disagreement belongs beside the regional agreement figures, not buried; and a
measured speedup belongs where a reader will actually see it, with its configuration in the same
table.

Documentation here is both engineering evidence and technical communication. Those goals are
compatible, and where they appear to conflict the resolution is more precision, not less
information.

---

## 4. Validation reporting

Each validation case aims to document: purpose, physical problem, geometry, element formulation,
mesh, material, boundary conditions, contact and friction conditions, reference solution, reference
solver or experiment, MinuteSim configuration, measured quantities, error metric, result plots,
runtime where relevant, hardware, precision, known limitations, and conclusion.

Two standing commitments:

- **Limitations that materially affect interpretation are published in the same document as the
  result** — not relegated elsewhere.
- **Internal debugging history is not published.** The configuration and the outcome are; the path
  taken to get there is not.

---

## 5. Performance reporting

A performance figure is reported together with the context that makes it meaningful: solver version,
hardware, precision, model size, number of steps, measured wall time, comparison basis, and whether
I/O and initialization are included.

- No speedup is published without stating what it is measured against.
- No single benchmark is generalized into a product-wide speed claim.
- Throughput benchmarks are labelled as such, and their late-time state is not offered as accuracy
  evidence.

Superlatives such as "industry-leading", "world's fastest", "fully compatible", "drop-in
replacement", "production proven", or "certified" are not used.

---

## 6. Relationship to other solvers

MinuteSim is an **independently developed** solver.

It is not described as compatible with, equivalent to, or an implementation of any commercial
solver. Where a relationship exists, it is stated precisely:

> MinuteSim supports a selected subset of LS-DYNA-style keyword input syntax.

> Selected formulations have been cross-checked against published technical references
> including the LS-DYNA Theory Manual.

Comparisons against other solvers, where published, are black-box comparisons of documented inputs
and outputs. Agreement in such a comparison is reported as agreement — it is never presented as
equivalence.

---

## 7. References and third-party material

**Theory sources are cited, never redistributed.** Commercial technical manuals are referenced by
title, revision, chapter, section, and equation number, with a link to the official source. Manual
PDFs, pages, screenshots, figures, tables, and substantial verbatim excerpts are not hosted here —
public availability of a document does not grant redistribution rights.

**Academic papers are cited in full** (authors, title, venue, year, DOI, official URL). Where a
commercial manual cites an original paper, the original paper is cited directly. The preferred
provenance chain is:

```text
original academic publication
    -> independent theoretical derivation
    -> MinuteSim implementation
    -> comparison with published technical references
```

**Third-party software is disclosed.** A dedicated record — in preparation, not yet published —
will list the components incorporated into, linked by, or redistributed with MinuteSim, with
license, version, purpose, linkage type, and attribution obligations. Licenses are verified against
authoritative upstream sources; a component whose license cannot be verified is marked as requiring
review rather than being guessed at or omitted. That record will be an engineering disclosure, not
legal advice.

Developer tooling that is not shipped as part of the product is not listed as a product dependency.

---

## 8. Intellectual property posture

The public statement MinuteSim makes about its own origins is deliberately limited to what it can
defend:

> MinuteSim is independently developed. Published academic literature and publicly accessible
> technical documentation are used as theoretical and validation references. MinuteSim does not
> incorporate source code from proprietary commercial finite-element solvers.

Stronger legal assertions are not made. Detailed provenance records are maintained internally and
are not published; the IP provenance page, once published, will carry only the high-level position.

---

## 9. Review before publication

Documentation changes that introduce or alter technical claims pass through staged review before
publication:

1. **Structure and terminology** — where the content belongs, and consistent language.
2. **Technical evidence** — every claim checked against actual evidence and assigned its class.
3. **Domain specialist review** — references, validation, or third-party licensing, as applicable.
4. **Disclosure review** — public/private boundary, with authority to block.
5. **Release gate** — a final pass returning pass, pass-with-notes, or blocked.

Disclosure review can block a document; no other stage can overrule it. Trivial edits that introduce
no new claim do not require the full sequence.

---

## 10. Reporting a documentation problem

Documentation defects are treated as defects. If you find a claim that is unsupported, a limitation
that is missing, a citation that does not resolve, a license that is misstated, or a number without
its comparison basis, please report it through the project's issue channel with the document, the
quoted text, and what you believe the correct statement to be.

Corrections to published claims are made in place, and material corrections are noted in the release
notes.
