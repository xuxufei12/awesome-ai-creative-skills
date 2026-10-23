[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# eternityspring/shuohao-skills

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | 广告与产品演示 |
| Type / 类型 | Skill / prompt / creative tool |
| Hosts mentioned / 提及宿主 | Claude / Opus, Codex |
| Source status / 来源状态 | GitHub source collected |
| Stars at snapshot / 采集时 Stars | 4988 |
| Snapshot / 来源快照 | 2026-10-23T06:16:28.516023+00:00 |
| Pinned commit / 固定提交 | d28a9c539b40523d081794b25ff9113016bd98e0 |
| Upstream license / 上游许可证 | Apache-2.0 |
| Archived upstream / 上游归档 | No |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot via PDF reference](https://github.com/eternityspring/shuohao-skills/blob/d28a9c539b40523d081794b25ff9113016bd98e0/README.md)
  - PDF: `opus-deepseek-video-prompts.pdf`, pp. 45; original post not independently verified / 未独立核验原帖。

## Setup & limits / 依赖与限制

See the pinned upstream README for setup and dependencies.

Source inspection only; not installed or rendered in this collection.

## Effects / 效果展示

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/assets/reelbench-first-screen-en.png" alt="ReelBench AI Video Workspace" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/assets/reelbench-first-screen-en.png)

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-outline/assets/report.webp" alt="Adaptation outline report" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-outline/assets/report.webp)

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-characters/assets/report.webp" alt="Character bible report" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-characters/assets/report.webp)

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-art/assets/report.webp" alt="Art bible report" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-art/assets/report.webp)

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-script/assets/report.webp" alt="Screenplay report" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-script/assets/report.webp)

<img src="https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-staging/assets/report-en.jpg" alt="Staging report with English UI" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/eternityspring/shuohao-skills/d28a9c539b40523d081794b25ff9113016bd98e0/skills/novel-staging/assets/report-en.jpg)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*

## Skills (7)

- [novel-art](../skills/688116bcb868ad68.md) — 给 AI 短剧出美术设定集（场景 + 叙事道具）：场景的设计意图、一致性锚点、光照时段变体、 空景提示词；道具的戏剧功能、状态变体、尺度参照、白底无手提示词。 产出 art.json + Markdown + 单页评审报告（含导出 JSON）。 为 AI 生成而设计，不是实拍——环境和道具都是生成资产，交付的是让它们跨
- [novel-staging](../skills/0afc3ade75ee6b01.md) — 给 AI 短剧的每一场排开场站位：先从场景图里认出能站能坐的东西（推算到俯视平面上）， 再按剧本给每一场排谁在哪件东西的哪一侧、坐还是站、面朝哪、有没有群演， 程序写出每一场的开场走位句，分镜这一场第一段照抄它。 默认交付能拖动调整站位的 HTML 工具报告，页面内可导出 staging.json；JSON 同时作为工
- [novel-outline](../skills/055e2fb2ad764626.md) — 把一本小说改编成短剧大纲五件套：改编说明、人物表、爽点表、分集梗概、资产清单， 产出 outline.json + Markdown + 单页评审报告（KPI 带、关键决策、爽点时间轴、调度矩阵、场景概览、质量门）。 14 道质量门全部由脚本确定性检查（角色分档上限、主场景上限随集数动态、爽点间隔≤3集、每集钩子悬念必
- [novel-script](../skills/689e28a0824dafad.md) — 给 AI 短剧写剧本：把 novel-outline 的分集梗概落成结构化的场次 + 节拍流（动作节拍与台词行交替）， 台词逐句带说话人与语气，时长逐集按语速确定性折算。产出 script.json + Markdown + 单页评审报告 （时长仪表 / 分集剧本 / 场次总表 / 按角色聚合的台词本，含导出 JSON
- [character-refs](../skills/16f39d589dbf727b.md) — 给任何故事里的角色真出参考图（小说改编、自己原创的故事、单独设计一个角色都行，不需要小说原文）： 一段话描述角色，拆成分层字段、补全后确认， 先出一张正面全身锚点，其余视图（大头照、90° 侧面、背面、细节、45° 大头照）都只参考这张锚点， 按需分档出图。每张图带标识、可单独重出，重出后自动标出哪些图过期。 支持 Q
- [novel-characters](../skills/cda2bc652a24548a.md) — 从小说或短故事里拆出角色表、人物画像、形象提示词、音色提示词， 其中形象提示词含一张角色设定图的完整版面指令（左半身像 + 右全身三视图 + 细节条）， 产出 JSON + Markdown + 可交互的 report.html。 报告语言可指定（--lang），默认中文，任意语言都支持；零依赖、零 API key、不
- [novel-storyboard](../skills/2af3bb17fa971997.md) — 给 AI 短剧出分镜：三层结构——段（一次视频生成，≤15 秒）→ 分镜（段内 2–5 秒的剪切，认领剧本节拍） → 分镜图（每切一张关键帧：主分镜图钉 0.00 秒，子分镜图钉各自切点）。 每段自带一条 MiniMax H3 视频提示词（官方口径默认英文、逐镜换行，promptLang 可切中文）：对齐指令和 &#91;Sh

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#eternityspring/shuohao-skills&Date)
