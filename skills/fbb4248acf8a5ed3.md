[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# manim

Create 3b1b-style mathematical animations with manimgl. Use when the user asks for animations, visualizations, 3D scenes, or manim code.

Project / 项目: [av-simi2/claude-manim-skill](../projects/av-simi2--claude-manim-skill.md)

## Sources / 来源

- [av-simi2/claude-manim-skill](https://github.com/av-simi2/claude-manim-skill/blob/f87274763f7416214899507fce6e55248fca2696/skill/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: manim
description: Create 3b1b-style mathematical animations with manimgl. Use when the user asks for animations, visualizations, 3D scenes, or manim code.
---

# Manim Animation Skill (manimgl / 3b1b)

You are an expert at creating animations using Grant Sanderson's **manimgl** (3b1b/manim, version 1.7.2).

> **IMPORTANT**: This project uses `manimlib` (3b1b's version), NOT `manim` (community edition). Always import with `from manimlib import *`.

## Source lookup

To find the installed manimlib source, run:
```bash
python3 -c "import manimlib; print(manimlib.__path__[0])"
```

When you need to verify a class signature, method, or parameter before writing code:
1. First check the reference file in the same directory as this SKILL.md: `reference.md`
2. If you need deeper detail, **read the actual source file** from the manimlib install path. Key files:
   - `mobject/geometry.py` — Line, Circle, Polygon, Arrow, Rectangle, etc.
   - `mobject/three_dimensions.py` — Sphere, Cylinder, Torus, Cube, Prism
   - `mobject/coordinate_systems.py` — Axes, ThreeDAxes, NumberPlane
   - `mobject/types/vectorized_mobject.py` — VMobject, VGroup, DashedVMobject
   - `mobject/types/surface.py` — Surface, SGroup
   - `mobject/types/image_mobject.py` — ImageMobject
   - `mobject/svg/tex_mobject.py` — Tex, TexText
   - `mobject/svg/text_mobject.py` — Text, MarkupText, Code
   - `animation/creation.py` — ShowCreation, Write, DrawBorderThenFill
   - `animation/fading.py` — FadeIn, FadeOut, FadeTransform
   - `animation/transform.py` — Transform, ReplacementTransform, MoveToTarget
   - `animation/composition.py` — AnimationGroup, Succession, LaggedStart
   - `animation/indication.py` — Indicate, Flash, FlashAround
   - `animation/rotation.py` — Rotate, Rotating
   - `scene/scene.py` — Scene, ThreeDScene
   - `camera/camera_frame.py` — CameraFrame (reorient, set_field_of_view, etc.)
   - `constants.py` — Colors, directions, math constants

**NEVER guess or hallucinate a method or parameter.** If unsure, read the source first.

## Example environments

Pre-built environment templates are in the `templates/` directory next to this file:
- `basic_3d_scene.py` — Minimal 3D scene with ground, objects, camera setup
- `drone_environment.py` — Drone with ground grid, altitude line, frustum visualization
- `math_2d_scene.py` — 2D scene with axes, graphs, and annotations
- `terrain_surface.py` — 3D terrain height field with contour coloring

Use these as starting points. Copy and modify rather than writing from scratch.

## Coordinate system (manimgl)

manimgl uses a **Y-up** coordinate system:
- X = Right, Y = Up, Z = Out (toward viewer)
- `RIGHT = [1,0,0]`, `UP = [0,1,0]`, `OUT = [0,0,1]`
- Diagonals: `UL`, `UR`, `DL`, `DR`
- Edges: `TOP`, `BOTTOM`, `LEFT_SIDE`, `RIGHT_SIDE`

If converting from ENU (East-North-Up): `manim_vec = [east, up, north]`

## Scene structure pattern

```python
from manimlib import *

class MyScene(ThreeDScene):  # or Scene for 2D
    def construct(self):
        # 1. Set up camera
        frame = self.camera.frame
        frame.reorient(-20, 72)           # azimuth, elevation (degrees)
        frame.set_field_of_view(55 * DEG)
        frame.set_height(10)
        frame.move_to(ORIGIN)

        # 2. Build mobjects
        obj = Sphere(radius=0.5, color=BLUE)
        obj.move_to([1, 2, 0])

        # 3. Animate
        self.play(FadeIn(obj), run_time=1.0)
        self.wait(0.5)

        # 4. Transform / morph
        new_obj = Sphere(radius=1.0, color=RED).move_to([1, 2, 0])
        self.play(Transform(obj, new_obj), run_time=1.5)
```

## Running animations

**IMPORTANT**: Always render to file with `-w` so the user can view the result. After rendering, open the video so the user can watch it.

```bash
# Render to file
manimgl scene_file.py ClassName -w --hd

# After rendering, open the video for the user to view:
code ./videos/ClassName.mp4
```

The output video lands in `./videos/ClassName.mp4`. After every successful render, **always run `code <path>` to open the video** so the user can view it directly in their editor.

## Key patterns and best practices

### Grouping objects
```python
group = VGroup(line1, line2, line3)      # for VMobjects (vectorized)
group = Group(sphere1, sphere2)           # for non-VMobjects (3D shapes)
```

### Fixed-in-frame overlays (HUD/labels on top of 3D)
```python
label = Text("Title", font_size=24, color=WHITE)
label.to_corner(UR, buff=0.3).fix_in_frame()
```

### Animating camera movement
```python
self.play(frame.animate.reorient(90, 5), run_time=2.0)
self.play(frame.animate.move_to([2, 1, 0]), run_time=1.5)
```

### Color palette (3b1b defaults)
```
BLUE_E, BLUE_D, BLUE_C (=BLUE), BLUE_B, BLUE_A  (dark to light)
Same pattern for RED, GREEN, YELLOW, PURPLE, GREY, TEAL, MAROON, GOLD, PINK
WHITE, BLACK, GREY_A through GREY_E
```

### Styling
```python
line.set_stroke(color=RED, width=3.0, opacity=0.8)
polygon.set_fill(color=BLUE, opacity=0.3)
mob.set_color(YELLOW)
```

### Common animation combos
```python
# Simultaneous animations
self.play(FadeIn(a), ShowCreation(b), Write(c), run_time=1.5)

# Sequential
self.play(FadeIn(a))
self.play(ShowCreation(b))

# Staggered
self.play(LaggedStart(*[FadeIn(m) for m in group], lag_ratio=0.15))

# Morphing between states
self.play(Transform(old_group, new_group), run_time=1.8)
```

### Value tracking for parameter animation
```python
tracker = ValueTracker(0)
obj = always_redraw(lambda: Circle(radius=tracker.get_value()))
self.play(tracker.animate.set_value(3), run_time=2)
```

## What to avoid

- Do NOT use `from manim import *` (community edition). Use `from manimlib import *`.
- Do NOT use `Create()` — use `ShowCreation()` instead (manimgl naming).
- Do NOT use `Scene.renderer` — manimgl uses `Scene.camera` directly.
- Do NOT use `config.frame_rate` — pass via CLI flags or `default_config.yml`.
- `Sphere`, `Cube`, `Prism` are NOT VMobjects — use `Group()` not `VGroup()` to contain them.
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/av-simi2--claude-manim-skill.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
