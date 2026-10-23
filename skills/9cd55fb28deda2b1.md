[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# comfy-custom-nodes-troubleshooting

Packaged fallback for stage-specific custom-node troubleshooting.

Project / 项目: [Comfy-Org/comfy-cli](../projects/comfy-org--comfy-cli.md)

## Sources / 来源

- [Comfy-Org/comfy-cli](https://github.com/Comfy-Org/comfy-cli/blob/cdb505aeffa3df0272d94610fb76255f521da569/comfy_cli/skills/comfy-custom-nodes-troubleshooting/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: comfy-custom-nodes-troubleshooting
description: Packaged fallback for stage-specific custom-node troubleshooting.
---

# Troubleshooting fallback

- Parse/contract failure: repair source or identifiers.
- Import failure: use the startup traceback and ComfyUI's exact Python.
- Clean import but absent `/object_info`: repair registration or install path.
- Registered but execution fails: inspect traceback, shapes/types, and exact dependency versions.
- Search unavailable: continue only if local catalog and documented API settle the contract; otherwise stop instead of inventing an integration.

Restart and rediscover after every repair.
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/comfy-org--comfy-cli.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
