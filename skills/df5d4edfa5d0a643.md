[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# svg-add-primitive

Add a new reusable motion / shape / filter primitive to lib/primitives/
with safety: JSDoc + sensible defaults + at least one consuming preset +
passing snapshot tests + updated docs/lib-api.md + CLAUDE.md index.
Use this only when /svg-animate has flagged a missing capability or when
the user explicitly asks to "add a primitive", "extend the lib", "teach
the system to <verb>", or "I need a new <motion / filter / shape> for ...".
This is the only sanctioned path for growing lib/primitives/; do not edit
those files directly.


Project / 项目: [ChanMeng666/svg-animation-studio](../projects/chanmeng666--svg-animation-studio.md)

## Sources / 来源

- [ChanMeng666/svg-animation-studio](https://github.com/ChanMeng666/svg-animation-studio/blob/6ff6fa216da17192ef4449c651e74dac8a84856a/.claude/skills/svg-add-primitive/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: svg-add-primitive
description: |
  Add a new reusable motion / shape / filter primitive to lib/primitives/
  with safety: JSDoc + sensible defaults + at least one consuming preset +
  passing snapshot tests + updated docs/lib-api.md + CLAUDE.md index.
  Use this only when /svg-animate has flagged a missing capability or when
  the user explicitly asks to "add a primitive", "extend the lib", "teach
  the system to <verb>", or "I need a new <motion / filter / shape> for ...".
  This is the only sanctioned path for growing lib/primitives/; do not edit
  those files directly.
context: fork
agent: lib-extender
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(npm test*), Bash(npm run snapshot:update*)
argument-hint: <category>.<name>  (e.g., motion.createOrbit)
---

You are extending the system's vocabulary. A new primitive is a long-term
commitment — once shipped, presets will depend on it. Your job is to ship
it correctly the first time, not to ship it fast.

## What was passed in

`$ARGUMENTS` is the primitive's category-qualified name (e.g.,
`motion.createOrbit`, `shapes.createStar`, `filters.createTurbulence`).
If the argument is missing or unparseable, stop and ask the calling thread
to clarify with format `<category>.<name>`.

## Why this skill exists

Without a gatekept extension path, `lib/primitives/` quickly accumulates
inconsistent signatures, undocumented functions, and primitives used by no
one. The discipline below is what makes the library compound rather than
sprawl. See `D:\github_repository\svg-animation-studio\docs\extension-protocol.md`
for the rationale.

## Step 1 — Read the existing category

Before adding to `lib/primitives/<category>.js`, read the whole file. Match:

- **Naming**: `create<Verb>` for actions (createJump), `create<Noun>` for
  static elements (createMusicalNote).
- **Return shape**:
  - `motion.*` → `{ css: string, className: string }`
  - `shapes.*` → raw SVG element `string`
  - `filters.*` → `<filter>` element `string`
- **Opts pattern**: single `opts = {}` object; destructure with defaults at
  the top; never positional args.
- **ID generation**: `motion.*` uses `uniqueId(prefix)` and includes the
  className in the keyframe name to avoid collisions. `shapes.*` and
  `filters.*` accept `id` from the caller.
- **Counter reset**: not your concern — the preset's `compose()` calls
  `motion.resetIdCounter()` at start.

## Step 2 — Write the function

Add the new function to `lib/primitives/<category>.js` and to its
`module.exports`. Include a 1-line JSDoc above the function explaining what
motion / shape / filter it produces and what the key params control. Do
not pad the JSDoc with `@param` lines for every option — the lib-api.md
table is the contract for that.

Example skeleton (motion):

```js
/** Orbital sweep: an element traces a circle around a center point. */
function createOrbit(opts = {}) {
  const {
    duration = '4s', easing = 'linear',
    radius = 20, centerX = 0, centerY = 0,
    direction = 'cw'
  } = opts;
  const cls = uniqueId('cv-orbit');
  const kf = `kf-${cls}`;
  const sign = direction === 'cw' ? 1 : -1;
  const css = `.${cls} {
  animation: ${kf} ${duration} ${cssEasing[easing]} infinite;
  transform-origin: ${centerX}px ${centerY}px;
}
@keyframes ${kf} {
  0%   { transform: rotate(0deg) translateX(${radius}px) rotate(0deg); }
  100% { transform: rotate(${sign * 360}deg) translateX(${radius}px) rotate(${-sign * 360}deg); }
}`;
  return { css, className: cls };
}
```

## Step 3 — Use it from at least one preset

A primitive that no preset uses is unverified vocabulary. Pick an existing
preset that legitimately needs the new primitive, OR — if the user is
adding the primitive for a brand-new animation — make sure they're about
to write that preset.

If no preset will use it within this session, stop and report:

> Need primitive `<name>` but no consuming preset is being built. Either
> wait until building one needs it, or write a placeholder preset that
> demonstrates the primitive (recommended: name it `<name>-demo`).

## Step 4 — Run snapshots

```bash
npm test
```

Three outcomes:

- All pass → great. Move to step 5.
- A previously-passing snapshot now differs → you changed a primitive
  signature used elsewhere, or the export order in `module.exports` shifted
  something. Re-examine your diff. If the change is intentional, run
  `npm run snapshot:update` AND in your final report flag every affected
  preset so the caller does a visual recheck.
- A test errors out (not just snapshot mismatch) → you broke an import.
  Fix before proceeding.

## Step 5 — Document

Two files MUST be updated:

1. `docs/lib-api.md` — add an H3 section under the right category with:
   - one-paragraph description
   - opts table (option / type / default)
   - the consuming preset(s)
   - source line range if reverse-engineered from a seed SVG

2. `CLAUDE.md` — add a one-line entry under `lib/primitives/<category>.js`
   in the "lib API index" section. Format:
   `- \`createOrbit\` — orbital sweep around a center point`

Increment the count in CLAUDE.md (e.g., "(10)" → "(11)").

## Step 6 — Report

Return a one-block report. Keep it short.

```
EXTENDED: motion.createOrbit
Signature: createOrbit({ duration, easing, radius, centerX, centerY, direction })
Used by: <preset slug>
Tests: <pass | updated snapshots: list>
Docs: docs/lib-api.md, CLAUDE.md
```

## What you must NOT do

- ❌ Edit `lib/primitives/*.js` for any reason other than this skill.
- ❌ Add a primitive with no consuming preset.
- ❌ Skip the docs update — undocumented primitives become invisible to
  future sessions and rot quickly.
- ❌ Use positional args. The convention is one `opts` object.
- ❌ Forget `module.exports` — the function exists in memory but no one can
  use it.
- ❌ Run `npm run snapshot:update` without explicit reason. Snapshots that
  silently change are bug seeds.

## When the primitive doesn't fit any category

If `motion`, `shapes`, `filters` doesn't seem right — stop and propose a
new category. This is rare (we've seen `easing` cover one edge case).
Adding a fourth category is a design decision, not a routine extension.
Ask the calling thread before proceeding.
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/chanmeng666--svg-animation-studio.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
