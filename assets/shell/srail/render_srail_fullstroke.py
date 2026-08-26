#!/usr/bin/env pvpython
"""Render presentation-quality MinuteSim S-rail forming assets from the benchmark XDMF.

Reproduces every image and animation frame in this directory. Nothing is hand-edited
afterwards, and the solver result is read read-only — no input is modified.

Usage
-----
    pvbatch --force-offscreen-rendering render_srail_fullstroke.py --src <PACKAGE>/benchmarks/srail/srail_fullstroke.xdmf
    pvbatch --force-offscreen-rendering render_srail_fullstroke.py --src ... --quick
    pvbatch --force-offscreen-rendering render_srail_fullstroke.py --src ... --only anim

where <PACKAGE> is an unpacked MinuteSim 0.9.0-beta.2 release directory. The path may
also be supplied through the MINUTESIM_SRAIL_XDMF environment variable. It is not baked
into this file: the benchmark result is not part of this repository, and a local absolute
path does not belong in a published one.

Use pvbatch, not pvpython. An on-screen OpenGL context silently clamps the saved image
to the desktop resolution, which caps the stills below the 2560x1440 they are meant to be.

Scene
-----
The deformable blank (part_id 6) carries the scalar field and visually dominates.
The forming tools (part_id 1, 2, 3) are drawn as a subordinate light-grey shell so the
reader can see what formed the part without the tools competing with the contour.
"""

import argparse
import os
import sys

from paraview.simple import *  # noqa: F403

# --- inputs --------------------------------------------------------------------
SRC_ENV = "MINUTESIM_SRAIL_XDMF"
SRC_HINT = "benchmarks/srail/srail_fullstroke.xdmf"

HERE = os.path.dirname(os.path.abspath(__file__))
# Published assets live at the top of assets/, alongside the other README images.
# Rendering writes them under their published names, so re-running this script
# regenerates exactly the committed files rather than a parallel set.
OUT = os.path.abspath(os.path.join(HERE, "..", ".."))

BLANK_PID = 6
TOOL_PIDS = (1, 2, 3)

# Field presentation.
#
# Ranges are display windows chosen from the measured distribution, not the raw
# min/max. Both fields are strongly one-sided: a fraction of a percent of the cells
# sits far outside the bulk, and anchoring the colour bar to those outliers pushes
# the entire part into a narrow band of the map. Measured over the L3 stroke:
#
#   thickness  full range 0.903-1.147   p1-p99 0.947-1.038   p99.5 = 1.0495
#   eqp        full range 0.000-1.925   p1-p99 0.000-0.520   p95   = 0.262
#
# Under the previous windows (0.90-1.15 and 0.0-0.53) the middle 90% of the cells
# occupied 20% and 49% of the colour bar respectively, so the part rendered as one
# flat colour. The windows below spread that bulk across the map instead. Values
# outside a window clamp to its end colour, which is the wanted behaviour here:
# the thinning and high-strain hot spots saturate rather than being averaged away.
# The true extremes stay documented above and in docs/benchmarks.md.
FIELDS = {
    "thickness": dict(
        title="Shell thickness  (mm)",
        preset="Turbo",
        invert=True,          # red/warm = thinned, blue = thickened
        rng=(0.94, 1.05),
        nominal=1.0,
        labels=[0.94, 0.96, 0.98, 1.00, 1.02, 1.04],
        fmt="{:.2f}",
        edge=[0.12, 0.12, 0.15],
    ),
    "eqp": dict(
        title="Equivalent plastic strain  (\u2013)",
        # Turbo: Viridis and Inferno both compress the band this part actually lives in.
        preset="Turbo",
        invert=False,
        rng=(0.0, 0.30),
        nominal=None,
        labels=[0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        fmt="{:.2f}",
        # Lighter than the thickness edges on purpose. Unstrained material sits at the
        # dark end of Turbo, and that is most of the part early in the stroke, so dark
        # edges disappear exactly where the refinement is most worth seeing.
        edge=[0.55, 0.55, 0.60],
    ),
}

BACKGROUND = [1.0, 1.0, 1.0]
TOOL_COLOR = [0.58, 0.62, 0.69]      # cool neutral grey-blue

# The mesh is drawn only on the closeups.
#
# At full stroke the blank carries ~40,000 elements. In the wide hero framing — and
# especially in the 1600x900 animation — a refined element is a few pixels across, so a
# one-pixel edge covers most of it and the refined region renders as a solid dark mass
# with no contour left to read. Drawing the mesh there hides the very field the asset
# exists to show. The closeup is zoomed far enough in for an element to carry both.
#
# Edge colour is per field (see FIELDS above) because the two fields put their dominant
# colour in different places, and an edge that reads well on one disappears on the other.
EDGES = {"hero": False, "closeup": True, "anim": False}
EDGE_WIDTH = {"hero": 1.0, "closeup": 1.2, "anim": 1.0}


def resolve_src(cli_path):
    path = cli_path or os.environ.get(SRC_ENV)
    if not path:
        sys.exit(f"error: pass --src <...>/{SRC_HINT}, or set {SRC_ENV}.")
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        sys.exit(f"error: source not found: {path}")
    return path.replace("\\", "/")


def build_scene(SRC):
    src = XDMFReader(registrationName="srail", FileNames=[SRC])
    src.UpdatePipeline()

    blank = Threshold(registrationName="blank", Input=src)
    blank.Scalars = ["CELLS", "part_id"]
    blank.LowerThreshold = BLANK_PID - 0.5
    blank.UpperThreshold = BLANK_PID + 0.5
    blank.ThresholdMethod = "Between"

    tools = Threshold(registrationName="tools", Input=src)
    tools.Scalars = ["CELLS", "part_id"]
    tools.LowerThreshold = min(TOOL_PIDS) - 0.5
    tools.UpperThreshold = max(TOOL_PIDS) + 0.5
    tools.ThresholdMethod = "Between"

    return src, blank, tools


def style_view(view, size):
    view.ViewSize = size
    view.Background = BACKGROUND
    view.UseColorPaletteForBackground = 0
    view.BackgroundColorMode = "Single Color"
    view.OrientationAxesVisibility = 0
    view.CameraParallelProjection = 1   # deterministic, and the right look for CAE
    try:
        view.UseAmbientOcclusion = 1
    except Exception:
        pass
    return view


def style_blank(disp, field, cfg, mode="hero"):
    ColorBy(disp, ("CELLS", field))
    if EDGES.get(mode, False):
        disp.SetRepresentationType("Surface With Edges")
        disp.EdgeColor = cfg["edge"]
        disp.LineWidth = EDGE_WIDTH.get(mode, 1.0)
    else:
        disp.SetRepresentationType("Surface")
    disp.RenderLinesAsTubes = 0
    disp.Opacity = 1.0
    disp.Specular = 0.18
    disp.SpecularPower = 30

    lut = GetColorTransferFunction(field)
    lut.ApplyPreset(cfg["preset"], True)
    if cfg["invert"]:
        lut.InvertTransferFunction()
    lut.RescaleTransferFunction(*cfg["rng"])
    lut.NanColor = [0.8, 0.8, 0.8]

    pwf = GetOpacityTransferFunction(field)
    pwf.RescaleTransferFunction(*cfg["rng"])
    return lut


def style_tools(disp):
    disp.SetRepresentationType("Surface")
    disp.AmbientColor = TOOL_COLOR
    disp.DiffuseColor = TOOL_COLOR
    disp.Opacity = 0.13
    disp.Specular = 0.02


def style_bar(view, lut, cfg):
    bar = GetScalarBar(lut, view)
    bar.Title = cfg["title"]
    bar.ComponentTitle = ""
    bar.TitleColor = [0.12, 0.12, 0.12]
    bar.LabelColor = [0.12, 0.12, 0.12]
    bar.TitleFontSize = 20
    bar.LabelFontSize = 17
    bar.TitleBold = 1
    bar.Orientation = "Horizontal"
    bar.ScalarBarLength = 0.30
    bar.ScalarBarThickness = 13
    bar.WindowLocation = "Any Location"
    bar.Position = [0.035, 0.045]
    # Explicit ticks. ParaView's automatic labelling prints a range label on top of a
    # generated tick at the same value, so the thickness bar ends up reading "1 1.0e+00".
    bar.AutomaticLabelFormat = 0
    bar.LabelFormat = cfg["fmt"]
    bar.RangeLabelFormat = cfg["fmt"]
    bar.AddRangeLabels = 0
    bar.UseCustomLabels = 1
    bar.CustomLabels = cfg["labels"]
    bar.DrawTickMarks = 0
    bar.DrawTickLabels = 1
    try:
        bar.TextPosition = "Ticks right/up, annotations left/down"
    except ValueError:
        pass
    return bar


def set_camera(view, bounds, mode):
    """Fixed, reproducible camera derived from the blank's bounding box.

    Parallel projection keeps the framing exactly repeatable: the composition is a
    pure function of the bounds and the mode, with no perspective fitting in the
    loop. That matters because the same camera has to serve four stills and two
    animations without drifting between them.

    Call this only *after* a view has rendered once. A render view resets its own
    camera on its first render, which silently discards anything set beforehand.
    """
    cx = 0.5 * (bounds[0] + bounds[1])
    cy = 0.5 * (bounds[2] + bounds[3])
    cz = 0.5 * (bounds[4] + bounds[5])
    dx, dy = bounds[1] - bounds[0], bounds[3] - bounds[2]
    span = max(dx, dy)

    # 3/4 view: down the -y axis, swung left and lifted.
    if mode == "hero":
        focal = [cx, cy, cz - 0.05 * span]   # lift the part clear of the scalar bar
        scale = 0.390 * span
        off = (-0.80, -1.05, 0.72)
    else:  # closeup on the S-bend flank, where thinning and strain localize
        focal = [cx - 0.04 * dx, cy - 0.16 * dy, cz - 0.03 * span]
        scale = 0.235 * span
        off = (-0.55, -0.95, 0.55)

    view.CameraFocalPoint = focal
    view.CameraPosition = [focal[0] + off[0] * span,
                           focal[1] + off[1] * span,
                           focal[2] + off[2] * span]
    view.CameraViewUp = [0.0, 0.0, 1.0]
    view.CameraParallelScale = scale
    return view


def render_statics(src, blank, tools, tlast, size):
    written = []
    for field, cfg in FIELDS.items():
        for mode in ("hero", "closeup"):
            view = CreateView("RenderView")
            style_view(view, size)

            bd = Show(blank, view)
            lut = style_blank(bd, field, cfg, mode)
            td = Show(tools, view)
            style_tools(td)

            bar = style_bar(view, lut, cfg)
            bar.Visibility = 1
            bd.SetScalarBarVisibility(view, True)

            view.ViewTime = tlast
            UpdatePipeline(time=tlast, proxy=blank)
            UpdatePipeline(time=tlast, proxy=tools)
            b = blank.GetDataInformation().GetBounds()
            Render(view)               # absorb the view's one-time camera reset
            set_camera(view, b, mode)
            Render(view)

            name = f"srail-shell-{field}.png" if mode == "hero" \
                else f"srail-shell-{field}-detail.png"
            path = os.path.join(OUT, name)
            SaveScreenshot(path, view, ImageResolution=size,
                           TransparentBackground=0, CompressionLevel=2)
            written.append(name)
            print(f"  wrote {name}")
            Delete(view)
            del view
    return written


def render_animations(src, blank, tools, times, size, stride):
    written = []
    frames = times[::stride]
    if frames[-1] != times[-1]:
        frames.append(times[-1])

    for field, cfg in FIELDS.items():
        view = CreateView("RenderView")
        style_view(view, size)
        bd = Show(blank, view)
        lut = style_blank(bd, field, cfg, "anim")
        td = Show(tools, view)
        style_tools(td)
        bar = style_bar(view, lut, cfg)
        bar.Visibility = 1
        bd.SetScalarBarVisibility(view, True)

        # Camera is set once from the FINAL geometry and then frozen, so the
        # part grows into a fixed frame instead of the view chasing it.
        UpdatePipeline(time=times[-1], proxy=blank)
        view.ViewTime = times[-1]
        Render(view)                   # absorb the view's one-time camera reset
        set_camera(view, blank.GetDataInformation().GetBounds(), "hero")

        # Frames stay beside this script, not in the published asset folder: they are
        # regenerable scratch that only exists so the clips can be re-encoded.
        fdir = os.path.join(HERE, f"_frames_{field}")
        os.makedirs(fdir, exist_ok=True)
        for i, t in enumerate(frames):
            view.ViewTime = t
            UpdatePipeline(time=t, proxy=blank)
            UpdatePipeline(time=t, proxy=tools)
            Render(view)
            SaveScreenshot(os.path.join(fdir, f"f{i:04d}.png"), view,
                           ImageResolution=size, TransparentBackground=0)
        print(f"  wrote {len(frames)} frames -> {os.path.basename(fdir)}")
        written.append(fdir)
        Delete(view)
        del view
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", help=f"path to {SRC_HINT} in an unpacked release package")
    ap.add_argument("--out", help="directory for the rendered images (default: assets/)")
    ap.add_argument("--quick", action="store_true", help="smaller/faster preview run")
    ap.add_argument("--only", choices=("statics", "anim"),
                    help="render only one product (default: both)")
    args = ap.parse_args()
    SRC = resolve_src(args.src)

    global OUT
    if args.out:
        OUT = os.path.abspath(args.out)
    os.makedirs(OUT, exist_ok=True)

    size = [1600, 900] if args.quick else [2560, 1440]
    # Animations are deliberately smaller than the stills: they are viewed inline in a
    # README, and a 2560-wide clip buys nothing there while costing a great deal of file.
    anim_size = [960, 540] if args.quick else [1600, 900]
    stride = 2 if args.quick else 1

    src, blank, tools = build_scene(SRC)
    times = list(src.TimestepValues)
    print(f"source   : {SRC}")
    print(f"timesteps: {len(times)}  (t_last={times[-1]:.6g})")
    print(f"output   : {OUT}")
    print(f"stills   : {size[0]}x{size[1]}    animation: {anim_size[0]}x{anim_size[1]}")

    if args.only in (None, "statics"):
        print("statics:")
        render_statics(src, blank, tools, times[-1], size)
    if args.only in (None, "anim"):
        print("animation frames:")
        render_animations(src, blank, tools, times, anim_size, stride)
    print("done.")


if __name__ == "__main__":
    main()
