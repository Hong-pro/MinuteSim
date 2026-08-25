# S-rail forming — visual asset manifest

Presentation assets rendered from the MinuteSim S-rail full-stroke forming benchmark.
Everything here is produced by `render_srail_fullstroke.py`; no image was retouched.

**These are illustrations of a solver result, not a validation claim.** No reference solution,
error metric, or cross-code comparison is attached to this benchmark. Nothing on this page
should be cited as accuracy evidence. Measured accuracy lives in
[`docs/validation.md`](../../../docs/validation.md), measured timing in
[`docs/performance.md`](../../../docs/performance.md).

## Source

| Item | Value |
|---|---|
| Result file | `benchmarks/srail/srail_l3.xdmf` in the MinuteSim 0.9.0-beta.2 release package (L2 deck also ships) |
| Format | XDMF index over HDF5, read as an unstructured grid |
| States | 20, from `t = 0` to `t = 9.63224e-3` |
| Cells | blank 675 at `t = 0` → ~40,400 at the final state (L3 deck, `MAXLVL 4`) |
| Access | Read-only. The benchmark result was not modified, moved, or re-run. |

The result file is **not** part of this repository. The render script takes its location as
`--src` or through the `MINUTESIM_SRAIL_XDMF` environment variable.

### Arrays present in the file

Cell arrays: `damage`, `effective_stress`, `effective_stress_bot`, `effective_stress_top`,
`element_status`, `eqp`, `eqp_max`, `part_id`, `sigma_p1`, `sigma_p2`, `sigma_xx`, `sigma_xy`,
`sigma_xz`, `sigma_yy`, `sigma_yz`, `sigma_zz`, `thickness`, `warp`

Point arrays: `displacement`, `velocity`

Two are used here: `thickness` and `eqp`. `part_id` selects the scene — `6` is the deformable
blank, `1`/`2`/`3` are the rigid forming tools.

## Field ranges over the blank, final state

| Field | Rendered range | Measured range at the final state |
|---|---|---|
| `thickness` | 0.84 – 1.01 mm | 0.8304 – 1.0472 mm |
| `eqp` | 0.0 – 0.53 | 0.0 – 0.5288 |

Neither field is clipped in a way that hides its peak: the `eqp` bar covers the full measured
range. The `thickness` bar tops out at 1.01 mm against a measured 1.047 mm — a small number of
cells thicken slightly above nominal, and they render at the "near-nominal" end of the scale.

## Generated files

The element mesh is drawn on the blank in **every** asset. The media are published one level up,
in `assets/`, alongside the other README images; this directory keeps the script and this record.
Re-running the script rewrites the published files in place, under the same names.

| Published file (in `assets/`) | Dimensions | Size | Content |
|---|---|---|---|
| `srail-shell-eqp.png` | 2560 × 1440 | 1.28 MB | Whole part, isometric, plastic strain at full stroke — **README shell image** |
| `srail-shell-thickness.png` | 2560 × 1440 | 1.22 MB | Whole part, isometric, thickness at full stroke |
| `srail-shell-eqp-detail.png` | 2560 × 1440 | 2.39 MB | S-bend flank, plastic strain |
| `srail-shell-thickness-detail.png` | 2560 × 1440 | 2.27 MB | S-bend flank, thickness |
| `srail-shell-thickness-animation.gif` | 760 wide | 3.22 MB | 59 frames, looping — linked from the README |
| `srail-shell-eqp-animation.gif` | 760 wide | 2.69 MB | 59 frames, looping |
| `srail-shell-thickness-animation.mp4` | 1280 wide | 4.44 MB | H.264, 24 fps, 9.8 s |
| `srail-shell-eqp-animation.mp4` | 1280 wide | 3.35 MB | H.264, 24 fps, 9.8 s |
| `render_srail_fullstroke.py` | — | 12 KB | The script that produces all of the above |

`_frames_thickness/` and `_frames_eqp/` sit beside the script and hold the 20 rendered PNG frames
per field. They are regenerable intermediates kept only so the clips can be re-encoded without
re-rendering, and they are not committed.

`srail-shell-eqp.png` was chosen over the thickness image for the README after comparing both at
the width GitHub actually renders a two-column table cell. Most of the blank sits near nominal
thickness, so at that size the thickness image reads as a dark shape with a narrow bright band,
while the strain field spans the whole formed wall and stays legible.

## Presentation choices

**Scene.** The blank carries the scalar field at full opacity. The forming tools are drawn as a
neutral grey shell at 0.13 opacity — enough to show what formed the part, not enough to compete
with the contour. Background is pure white; no orientation axes, no ParaView interface.

**Element mesh.** Drawn on the blank in every asset, at one pixel. Showing it is the point
rather than a decoration: the blank starts as a uniform coarse grid of 675 cells and ends at
~40,400, with the added elements concentrated in the S-bend and the sidewalls while the flange
stays coarse. That contrast is legible in the stills and develops over the animations.

Edge colour is **per field**, because the two fields put their dark end in different places:

| Field | Edge grey | Why |
|---|---|---|
| `thickness` | 0.12 (near-black) | Most of the part is at or near nominal, which is the *dark* end of the inverted map — but the formed region spans the bright middle, so dark edges stay legible and keep the contour fully saturated. |
| `eqp` | 0.55 (mid grey) | Unstrained material is the dark end of the map, and early in the stroke that is nearly the whole part. Near-black edges vanish there, exactly where the refinement is most worth seeing. |

Four greys (0.12 / 0.50 / 0.72 / 0.94) were rendered for `eqp` at an early state and at full
stroke before choosing. 0.72 and above read the mesh better early but visibly desaturate the
high-strain band at full stroke; 0.12 is invisible early. 0.55 is the value that survives both.

**Camera.** Parallel projection, so the framing is a pure function of the blank's bounding box
and does not drift between the stills and the animations. The animation camera is fixed from the
*final* geometry, so the part grows into a stationary frame instead of the view chasing it.

**Colour maps.** Turbo for both fields — inverted for thickness, so warm reads as thinned and
blue as near-nominal; upright for `eqp`, so warm reads as high strain. Viridis and Inferno were
both tried for `eqp` and rejected: each compresses the 0.1–0.3 band where this part actually
lives, and Inferno's black low end swallows the large unstrained flange against a white page.

**Scalar bars.** Horizontal, bottom-left, explicit tick values. ParaView's automatic labelling
prints a range label on top of a generated tick at the same value, which made the thickness bar
read `1 1.0e+00`.

## Known limitations of these renders

- **Faceted contour bands.** `thickness` and `eqp` are cell data, drawn without interpolation, on
  an adaptively refined mesh. The blocky stair-stepping across refinement boundaries is the
  discretization, not a rendering artifact, and it is left visible rather than smoothed away —
  with the mesh drawn, it is also directly checkable against the element boundaries.
- **Dense-mesh regions at hero zoom.** Where refinement is finest, cell edges approach the line
  width and the mesh reads as texture rather than as individually countable elements. The
  closeups exist for that; do not use a hero still to count elements.
- **236 states.** The clips play the 236 states written by the benchmark run, at 24 fps with the final
  state held. Motion is therefore stepped, not continuous; there is no interpolated geometry.
- **No time or stroke annotation.** The frames carry no timestamp or stroke overlay.
- **Final state only, for the stills.** All four PNGs are the last written state.

## Reproducing

```
pvbatch --force-offscreen-rendering render_srail_fullstroke.py \
        --src <PACKAGE>/benchmarks/srail/srail_fullstroke.xdmf
```

Rendered with ParaView 6.1.0. Use `pvbatch`, not `pvpython`: an on-screen OpenGL context clamps
the saved image to the desktop resolution, which silently caps the stills below 2560 × 1440.

Video encoding is a separate step and needs `ffmpeg` (H.264 support is not compiled into this
ParaView build):

```
ffmpeg -framerate 10 -i _frames_<field>/f%04d.png \
       -vf "tpad=stop_mode=clone:stop_duration=1.2,format=yuv420p" \
       -c:v libx264 -crf 18 -preset slow -movflags +faststart srail-shell-<field>-animation.mp4
```
