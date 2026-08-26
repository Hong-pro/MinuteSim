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
| States | 236, from `t = 0` to `t = 9.8974e-3` |
| Cells | blank 675 at `t = 0` → 39,102 at the final state (L3 deck, `MAXLVL 4`).
  The three rigid tools add 1,265 shells that never change, so the total model is 40,367. |
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

The rendered range is a **display window**, not the measured extent. Both fields are strongly
one-sided — a fraction of a percent of the cells sits far outside the bulk — so a bar anchored to
the raw minimum and maximum pushes the whole part into a narrow band of the map.

| Field | Rendered range | Measured range | p1 – p99 | Middle 90% occupies |
|---|---|---|---|---|
| `thickness` | 0.94 – 1.05 mm | 0.9028 – 1.1467 | 0.947 – 1.038 | 44% of the bar |
| `eqp` | 0.00 – 0.30 | 0.0000 – 1.9254 | 0.000 – 0.520 | 86% of the bar |

**These windows clip, deliberately.** Values outside clamp to the end colour, so thinning and
high-strain hot spots saturate rather than being averaged away. The previous windows
(0.90–1.15 and 0.0–0.53) were anchored near the measured extremes, and under them the middle 90%
of the cells occupied only 20% and 49% of the bar respectively — the part rendered as one flat
colour with no readable contour. The true extremes are stated above and in
[`docs/benchmarks.md`](../../../docs/benchmarks.md#s-rail-full-stroke-forming); no peak is hidden,
only rescaled.

Distributions were measured over the L3 stroke at four states (25%, 50%, 75%, 100%) before the
windows were chosen.

## Generated files

The element mesh is drawn **only on the detail views** — see *Element mesh* below. The media are
published one level up, in `assets/`, alongside the other README images; this directory keeps the
script and this record. Re-running the script rewrites the published files in place, under the
same names.

| Published file (in `assets/`) | Dimensions | Size | Mesh | Content |
|---|---|---|---|---|
| `srail-shell-eqp.png` | 2560 × 1440 | 0.93 MB | no | Whole part, isometric, plastic strain at full stroke — **README shell image** |
| `srail-shell-thickness.png` | 2560 × 1440 | 0.92 MB | no | Whole part, isometric, thickness at full stroke |
| `srail-shell-eqp-detail.png` | 2560 × 1440 | 2.89 MB | yes | S-bend flank, plastic strain |
| `srail-shell-thickness-detail.png` | 2560 × 1440 | 2.83 MB | yes | S-bend flank, thickness |
| `srail-shell-thickness-animation.gif` | 800 wide | 2.04 MB | no | 79 frames, looping — **README hero** |
| `srail-shell-eqp-animation.gif` | 800 wide | 2.21 MB | no | 79 frames, looping |
| `srail-shell-thickness-animation.mp4` | 1600 × 900 | 0.97 MB | no | H.264, 24 fps, 9.8 s, 236 frames |
| `srail-shell-eqp-animation.mp4` | 1600 × 900 | 1.10 MB | no | H.264, 24 fps, 9.8 s, 236 frames |
| `render_srail_fullstroke.py` | — | 14 KB | — | The script that produces all of the above |

`_frames_thickness/` and `_frames_eqp/` sit beside the script and hold the 236 rendered PNG frames
per field, at 1600 × 900. They are regenerable intermediates kept only so the clips can be
re-encoded without re-rendering, and they are not committed.

## Presentation choices

**Scene.** The blank carries the scalar field at full opacity. The forming tools are drawn as a
neutral grey shell at 0.13 opacity — enough to show what formed the part, not enough to compete
with the contour. Background is pure white; no orientation axes, no ParaView interface.

**Element mesh — detail views only.** The blank starts as a uniform coarse grid of 675 cells and
ends at 39,102, with the added elements concentrated in the S-bend and the sidewalls while the
flange stays coarse. That contrast is worth showing, but only where an element is large enough on
screen to carry both the mesh and the contour.

It is not, in the wide framing. At 39,102 elements a refined cell spans a few pixels in a
2560-wide still and fewer in a 1600-wide animation frame, so a one-pixel edge covers most of it
and the refined region renders as a solid dark mass — precisely over the S-bend, where the field
matters most. Earlier revisions drew the mesh everywhere and the animations lost their contour to
it entirely. The closeups are zoomed far enough in for the mesh to read as countable elements, and
that is where it is now drawn.

Edge colour is **per field**, because the two fields put their dark end in different places:

| Field | Edge grey | Why |
|---|---|---|
| `thickness` | 0.12 (near-black) | The formed region spans the bright middle of the map, so dark edges stay legible and keep the contour fully saturated. |
| `eqp` | 0.55 (mid grey) | Unstrained material is the dark end of the map, and early in the stroke that is nearly the whole part. Near-black edges vanish there, exactly where the refinement is most worth seeing. |

Four greys (0.12 / 0.50 / 0.72 / 0.94) were rendered for `eqp` at an early state and at full
stroke before choosing. 0.72 and above read the mesh better early but visibly desaturate the
high-strain band at full stroke; 0.12 is invisible early. 0.55 is the value that survives both.

**Camera.** Parallel projection, so the framing is a pure function of the blank's bounding box
and does not drift between the stills and the animations. The animation camera is fixed from the
*final* geometry, so the part grows into a stationary frame instead of the view chasing it.

**Colour maps.** Turbo for both fields — inverted for thickness, so warm reads as thinned and
blue as thickened; upright for `eqp`, so warm reads as high strain. Viridis and Inferno were
both tried for `eqp` and rejected: each compresses the 0.1–0.3 band where this part actually
lives, and Inferno's black low end swallows the large unstrained flange against a white page.

**Scalar bars.** Horizontal, bottom-left, explicit tick values. ParaView's automatic labelling
prints a range label on top of a generated tick at the same value, which made the thickness bar
read `1 1.0e+00`.

## Known limitations of these renders

- **Faceted contour bands.** `thickness` and `eqp` are cell data, drawn without interpolation, on
  an adaptively refined mesh. The blocky stair-stepping across refinement boundaries is the
  discretization, not a rendering artifact, and it is left visible rather than smoothed away. In
  the detail views it is directly checkable against the drawn element boundaries.
- **Coarse-flange blockiness.** The flange keeps its original coarse cells, so isolated elements
  there can carry a value very different from their neighbours and read as bright squares. That is
  one cell's value at cell resolution, not a localized physical feature.
- **Clipped colour bars.** Both windows clip — see *Field ranges* above. Do not read an end-colour
  region as being exactly at the bar's end value; read it as "at or beyond".
- **Do not count elements from a wide view.** The mesh is not drawn there at all. Use the detail
  views.
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

`--only statics` and `--only anim` re-render one product without redoing the other.

Video encoding is a separate step and needs `ffmpeg` (H.264 support is not compiled into this
ParaView build). Both clips are written straight to their published names in `assets/`:

```
# MP4 — every frame
ffmpeg -framerate 24 -i _frames_<field>/f%04d.png \
       -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -movflags +faststart \
       ../../srail-shell-<field>-animation.mp4

# GIF — every 3rd frame, 800 px wide, 128-colour diff palette
ffmpeg -i _frames_<field>/f%04d.png -vf \
  "select='not(mod(n\,3))',setpts=N/12/TB,scale=800:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
  -loop 0 ../../srail-shell-<field>-animation.gif
```

Encoded with ffmpeg 9.0.1. Dropping the element mesh cut both clips to well under half their
previous size *at higher resolution*: the dense edges were high-frequency detail that neither
H.264 nor a 128-colour palette could carry cheaply.
