[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# init-agents-md

Create or refresh a minimal repository-level AGENTS.md for coding agents, keeping it short and repo-specific, and symlinking CLAUDE.md to it. Use when Codex needs to inspect a codebase, draft AGENTS.md, preserve useful details from an existing CLAUDE.md, stop before overwriting an existing AGENTS.md, or symlink CLAUDE.md to AGENTS.md.

Project / 项目: [zazencodes/skills](../projects/zazencodes--skills.md)

## Sources / 来源

- [zazencodes/skills](https://github.com/zazencodes/skills/blob/9f2d7c8f0e112e03d0e440676afd49fde3c9dff2/skills/init-agents-md/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: init-agents-md
description: Create or refresh a minimal repository-level AGENTS.md for coding agents, keeping it short and repo-specific, and symlinking CLAUDE.md to it. Use when Codex needs to inspect a codebase, draft AGENTS.md, preserve useful details from an existing CLAUDE.md, stop before overwriting an existing AGENTS.md, or symlink CLAUDE.md to AGENTS.md.
---

# Initialize AGENTS.md

Create a short, repo-specific `AGENTS.md`. Inspect the repository first, keep only the facts that help an agent work faster, treat `AGENTS.md` as the canonical context file, and ensure `CLAUDE.md` is a symlink to `AGENTS.md`.

Read [references/agents-md-best-practices.md](references/agents-md-best-practices.md) before drafting.

## Workflow

1. Check the current files.
- If `AGENTS.md` already exists, stop. Tell the user and ask whether to continue and overwrite it.
- If `CLAUDE.md` exists and is a regular file (not a symlink), read it and use it as seed material for the new `AGENTS.md`.
- If `CLAUDE.md` does not exist or is already a symlink, plan to symlink it after creating `AGENTS.md`.

2. Explore the repository.
- Inspect only enough to explain the real project shape and workflows.
- Start with root files and directories, using the `README` as an initial guide to understand the project.
- Look for the commands people actually run, where the important code lives, whether tests exist, and any sharp edges an agent could miss.
- Prefer `rg`, `rg --files`, `ls`, and targeted file reads over broad dumps.

3. Draft `AGENTS.md`.
- Keep it minimal. Cut anything generic, obvious, or duplicated from existing docs.
- Start the file with `# AGENTS.md`.
- Place `## Project Instructions` near the top. Leave it blank if there is nothing project-specific to add.
- Favor section names that match the real repo shape instead of generic placeholders.
- Focus on a few high-value facts:
  - what the repository is
  - where important code or content lives
  - the main workflows or commands
  - testing or validation expectations
  - any important gotchas
- Use short sections and terse bullets. If the file starts feeling long, compress it again.
- If the repository has useful topic-specific groupings, split them into small sections like `Reference Docs`, `Development Commands`, `Architecture`, `Important Notes`, or similarly precise names.

4. Symlink `CLAUDE.md`.
- If `CLAUDE.md` existed as a regular file, remove it after extracting any useful details into `AGENTS.md`.
- Create a relative symlink from `CLAUDE.md` pointing to `AGENTS.md`:
  ```bash
  ln -sf AGENTS.md CLAUDE.md
  ```

5. Sanity-check the result.
- Confirm `AGENTS.md` is the source of truth.
- Confirm `CLAUDE.md` is a relative symlink pointing to `AGENTS.md`.
- Confirm every command and path matches the repository.
- Confirm the file stays short and agent-specific.

## Suggested Shape

Use only the sections that earn their keep. A good default for a richer repo is:

- `## Project Overview`
- `## Project Instructions`
- `## Reference Docs`
- `## Development Commands`
- `## Architecture`
- `## Important Notes`
- `## Validation`

If the repository has clear domain-specific buckets, prefer those over the generic defaults. For example: `Styling System`, `Path Aliases`, `State Management`, or `Admin Scripts`.
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/zazencodes--skills.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
