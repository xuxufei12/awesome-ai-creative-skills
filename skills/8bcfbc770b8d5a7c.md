[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# canvas-procedural-animation



Project / 项目: [calesthio/OpenMontage](../projects/calesthio--openmontage.md)

## Sources / 来源

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage/blob/c8066452325cb57c8fc1ba8c2a71b6e8842e6b65/.agents/skills/canvas-procedural-animation/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: canvas-procedural-animation
description: Use p5.js/canvas for local procedural character effects: particles, weather, squash/stretch, walk cycles, and environmental motion.
license: MIT
---

# Canvas Procedural Animation

Use this skill when p5.js or Canvas is used for character-supporting motion:
rain, snow, leaves, feathers, ambient particles, squash/stretch, or procedural
walk cycles.

## Proven Pattern

p5.js runs setup once and redraws continuously through `draw()`. Keep animation
state deterministic from time/frame values when rendering previews.

```js
function setup() {
  createCanvas(1920, 1080);
}

function draw() {
  const t = millis() / 1000;
  clear();
  drawCharacter(width / 2, height / 2 + sin(t * 8) * 8);
}
```

## Use For

- Particle/weather overlays.
- Environmental motion.
- Simple procedural bodies.
- Effects that do not need individually authored SVG parts.

## Avoid For

- Complex facial acting where SVG/layered rig parts are easier to inspect.
- Final renders that need exact frame determinism unless the runtime exposes
  frame-index control.

## Sources

- p5.js `setup()` reference: https://p5js.org/reference/p5/setup/
- p5.js `draw()` reference: https://p5js.org/reference/p5/draw/
- p5.js animation examples: https://p5js.org/examples/
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/calesthio--openmontage.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
