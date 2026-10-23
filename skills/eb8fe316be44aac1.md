[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# character-rigging



Project / 项目: [calesthio/OpenMontage](../projects/calesthio--openmontage.md)

## Sources / 来源

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage/blob/c8066452325cb57c8fc1ba8c2a71b6e8842e6b65/.agents/skills/character-rigging/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: character-rigging
description: Build data-driven 2D character rigs for local animation: parts, pivots, layers, constraints, views, and reusable rig packages.
license: MIT
---

# Character Rigging

Use this skill when building OpenMontage `rig_plan` artifacts or renderer input
for local 2D character animation.

## Proven Patterns

- Keep runtime code generic; make each character a data package.
- Split characters into independently transformable parts.
- Define pivots in the same coordinate space as the artwork.
- Store constraints on moving parts to prevent impossible rotations.
- Keep layer order explicit; do not rely on SVG source order after generation.
- Start with one view and add views only when the shot list requires them.

## Rig Package

```json
{
  "character_id": "mouse",
  "rig_type": "svg_rig",
  "parts": [
    { "id": "body", "kind": "torso", "layer": 10 },
    { "id": "head", "kind": "head", "layer": 30, "parent": "body" },
    { "id": "arm_right", "kind": "limb", "layer": 40, "parent": "body" }
  ],
  "joints": {
    "head": { "pivot": [320, 180], "rotation": [-20, 20] },
    "arm_right": { "pivot": [390, 310], "rotation": [-70, 95] }
  }
}
```

## Quality Checklist

- Every moving part has a pivot.
- Every child part has a parent where hierarchy matters.
- Mouth shapes are separate assets or separate path groups.
- Eyes and pupils are separate when gaze needs to change.
- Props are separate if the character touches or carries them.

## Sources

- SVG transform-origin behavior is browser-defined and can be sensitive to
  coordinate space; prefer explicit SVG-coordinate pivots when using GSAP
  `svgOrigin`: https://gsap.com/docs/v3/GSAP/CorePlugins/CSS/
- Remotion animations must be frame-driven and deterministic via current frame:
  https://www.remotion.dev/docs/use-current-frame
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/calesthio--openmontage.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
