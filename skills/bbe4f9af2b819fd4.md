[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# hand-drawn

Use when users ask for a hand-drawn or illustrated image prompt, name one of the repository's 20 numbered styles or the 3.1 stable variant, or mention triggers such as 亲子手绘、家庭蜡笔画、蜡笔、吉卜力、水墨、像素、淡彩速写、动画概念、水粉、北欧绘本、纸雕、软胶潮玩、墨线绘本、暖色扁平绘本、圆头红线、暖黄墨线、family-crayon-card、warm-flat-storybook、roundhead-redline、warm-yellow-ink-story. Produces prompt text or a formal reference-bearing call bundle and does not generate images.

Project / 项目: [threerocks/hand-drawn-styles](../projects/threerocks--hand-drawn-styles.md)

## Sources / 来源

- [threerocks/hand-drawn-styles](https://github.com/threerocks/hand-drawn-styles/blob/3306ef522a0c305b46efdbe7422550d7dcc9deea/SKILL.md)

## Skill text / Skill 原文

> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。

<details>
<summary>Expand complete SKILL.md / 展开完整 Skill</summary>

````text
---
name: hand-drawn
description: Use when users ask for a hand-drawn or illustrated image prompt, name one of the repository's 20 numbered styles or the 3.1 stable variant, or mention triggers such as 亲子手绘、家庭蜡笔画、蜡笔、吉卜力、水墨、像素、淡彩速写、动画概念、水粉、北欧绘本、纸雕、软胶潮玩、墨线绘本、暖色扁平绘本、圆头红线、暖黄墨线、family-crayon-card、warm-flat-storybook、roundhead-redline、warm-yellow-ink-story. Produces prompt text or a formal reference-bearing call bundle and does not generate images.
---

# 手绘风格 prompt 生成器

完整指令与画风配方是工具无关的,放在同目录:

1. 按 [PROTOCOL.md](PROTOCOL.md) 的 5 步流程执行:确定画风 → 取配方 → 自动填占位符 → 处理比例 → 输出 prompt。
2. 从 [STYLES.md](STYLES.md) 取对应编号的完整模板。
3. 能执行脚本时优先调用 `scripts/render_prompt.py`,不得手工缩写、同义改写或与业务项目的画风段落混配。
4. 风格 3.1 用于正式生产、连续故事或多页作品时，必须完整执行 `family-crayon-card-v4`：基础生成 → `scribble-correction` → `scribble-chaos-correction` → `style-contract-check`。三次图像操作只得到 `final-candidate`，独立验收报告为 pass 才能成为 final。锚点、阶段或审核证据缺失不可放行，见 [docs/style-3.1-review.md](docs/style-3.1-review.md)。
5. 风格 19 正式生产必须使用正式 JSON 调用包:每张携带原创锚点,锁定模型快照和高保真参考图输入,基础图只标为 `candidate-only`,通过 `acceptance_contract` 后才能标为 final;任一条件不可用时停止正式生产。
6. 风格 20 正式生产必须使用正式 JSON 调用包:使用固定原创锚点生成 `final-candidate`,再运行机读验收器;失败候选整张拒收并重新生成,禁止用通用画风迁移编辑修补。
7. 其他画风默认只输出最终 prompt;风格 3.1/19/20 的纯文本只允许显式 `--text-only-preview`。不生图;仓库维护者新增或验收画风时,按 `AGENTS.md` 的维护者验证例外执行。

安装方法见 [INSTALL.md](INSTALL.md)。安装后先运行 `python3 -B scripts/check_skill.py` 汇总检查文件、参考图、别名和全部画风调用；检查不生图。使用 `python3 -B scripts/render_prompt.py --list` 取得原菜单与参数；用独立的 `--catalog` 查询有来源的选型说明，无需图片缓存。未指定画风时按协议提供有依据的 2–3 项候选或完整菜单，等待用户选择；显式指定优先。详见 [选型与证据范围](docs/style-selection.md)，保持整个安装包的目录结构。

图片使用 `assets/image-manifest.json` 中的公开链接。渲染器按需下载并校验参考图，JSON 同时返回公开地址、SHA-256 和缓存绝对路径；正式调用仍须传入参考图文件。首次调用需要网络，可先运行 `python3 -B scripts/hosted_images.py fetch`。缓存和离线规则、新图片上传步骤见 [docs/image-hosting.md](docs/image-hosting.md)。不要向 Git 或安装包添加图片二进制。
````

</details>

## Effects / 效果展示

[Project demo & dependency notes / 项目示例与依赖](../projects/threerocks--hand-drawn-styles.md#effects--效果展示)

Project-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。
