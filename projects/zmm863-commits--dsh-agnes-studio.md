[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# zmm863-commits/dsh-agnes-studio

🎬 泡泡猫的影视工具 — AI 影视创作工作站：文生图、图生图、文生视频、图生视频、短剧剧本拆解与提示词专家。支持 Agnes / DeepSeek / Qwen / 豆包 / MiniMax / Ollama 六大厂商，全局浮层不堵对话框。

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | 图像生成与商业视觉 |
| Type / 类型 | Skill／技能包 |
| Hosts mentioned / 提及宿主 | DeepSeek / DSH |
| Source status / 来源状态 | 已存 README 与 Skill |
| Stars at snapshot / 采集时 Stars | 22 |
| Snapshot / 来源快照 | 2026-10-22T05:55:34.247785+00:00 |
| Pinned commit / 固定提交 | e1947f749d216770b3eb5f886363518d730fc883 |
| Upstream license / 上游许可证 | MIT 类许可（见原文） |
| Archived upstream / 上游归档 | No |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot](https://github.com/zmm863-commits/dsh-agnes-studio/blob/e1947f749d216770b3eb5f886363518d730fc883/README.md)

## Setup & limits / 依赖与限制

依赖与安装方式见固定提交的 README；本次未部署。

扩展条目已收集来源说明；功能和效果未逐项运行复验。

## Effects / 效果展示

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/01-image.png" alt="🎨 生图" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/01-image.png)

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/02-video.png" alt="🎬 生视频" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/02-video.png)

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/03-ohstory.png" alt="✍️ 创作台" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/03-ohstory.png)

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/04-drama.png" alt="📖 短剧" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/04-drama.png)

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/05-bgvideo.png" alt="🎬 背景视频（新）" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/05-bgvideo.png)

<img src="https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/06-mtv.png" alt="🎵 MTV（新）" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/zmm863-commits/dsh-agnes-studio/e1947f749d216770b3eb5f886363518d730fc883/screenshots/06-mtv.png)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*

## Skills (37)

- [short-drama-assets](../skills/a8d3a4568b98ce25.md) — 从短剧剧本拆出人物/造型、地点/视图、道具/状态和跨场连续性，写成创作者可读的视觉设定。用户说“拆角色/场景/道具”“做资产设定”“判断复用还是新变体”“更新造型/道具状态”，或拿现成剧本直接做视觉资产准备时使用；不写图片提示词，不生成媒体。
- [short-drama-develop](../skills/98e537c3114fe1c2.md) — 将中文小说、短剧或漫剧想法、梗概、改编材料、已有系列笔记或多集完整剧本发展成可追溯的改编方案、戏剧方向、创作简报、导演阐述、故事引擎与分集地图，并按题材与制作形态（画风）选择写法。用户提出“导入小说做短剧”“从多集整稿生成/补分集地图”“开发短剧/漫剧”“做故事设定/系列大纲/分集规划”“写导演阐述”“这个题材怎么写”
- [short-drama-edit](../skills/2e53700bceae46e7.md) — 将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。用于套剪、加字幕、统一响度、调整节奏或导出精修素材；需要补素材或修改故事时转回对应创作阶段。
- [short-drama-image-prompts](../skills/95f0bd1da8a53d88.md) — 为短剧人物、造型、地点、道具和状态编写或修改可直接复制的图片提示词 Markdown。用户提到角色设定图、三视图、参考图、场景板、道具图、风格帧、Look Development、状态变体或局部编辑提示词时使用；不生成图片，也不调用供应商。
- [short-drama-novel-analyze](../skills/4124c97f70f91b6f.md) — 把长篇小说、连载网文或多集散稿拆成可追溯的原著分析：章节索引、改编价值快评、逐章功能提取、剧情单元与节奏聚合、人物与设定归并，最后给出改编价值判定与分集候选，交给 $short-drama-develop 立契约。用户说“导入这本小说”“拆这本书”“分析原著”“这本书能不能改短剧”“先看看值不值得拆”“把长篇拆成分集候
- [short-drama-produce](../skills/90716253be3e28ea.md) — 在创作者明确确认后，执行短剧项目的图片、视频、TTS/配音或时间线音乐生产任务，并把结果与精简运行记录落回项目。用户说“生成这张图/这段视频/这句配音/这段配乐”“开始跑图/跑视频/合成语音/生成音乐”“把已确认提示词送去生产”，或要求批量执行已确认媒体任务时使用；不负责创作提示词、镜头、台词、歌词或声音身份，也绝不把
- [short-drama-review](../skills/251364f35886455b.md) — 审查短剧项目中的原著分析、故事、剧本、视觉设定、图片提示词、分镜、冻结关键帧、视频提示词和已有媒体。用户提出“审稿/检查剧本”“检查资产或连续性”“检查图片/视频提示词”“检查原著分析”“审查模板感”“根据生产观察做项目校准”时使用；只写审查问题、结论和修订要求，不代替 owner 修改来源文件。
- [short-drama-storyboard](../skills/f893fb81cb45f02a.md) — 把中文短剧剧本和视觉设定写成有戏剧职责、连续性边界与冻结关键帧提示词的分镜 Markdown。用户提出“拆分镜/设计镜头/做镜头表”“场次视觉计划/调度故事板”“比较导演方案”“写首帧/关键帧提示词”或检查轴线、站位、视线、持物连续性时使用；不生成媒体。
- [short-drama-video-prompts](../skills/e9ab120687deabf1.md) — 把短剧分镜和冻结关键帧写成可直接复制的视频提示词 Markdown，也可按用户要求写时间线配乐/主题曲意图。用户提到文生/图生视频动作、人物表演、运镜、口型、环境运动、镜头时长、起止状态、把分镜转成视频提示词或写配乐提示词时使用；不生成媒体、不创作歌词、不改分镜边界。
- [short-drama-write](../skills/f0a74465dbdd12c0.md) — 编写或修订可拍摄的中文短剧、漫剧单集 Markdown 剧本，也负责保留作者原文地规范化现成剧本。用户提出“写/改一集短剧”“把大纲写成剧本”“优化场景/对白”“去模板感”“去 AI 味润色”“续写下一集”或提供剧本要求进入后续制作时使用；不负责资产、分镜、媒体提示词或终审。
- [short-drama](../skills/a8efa0cc1f73a4cb.md) — 基于文件系统初始化和继续短剧或漫剧项目，提供 creator-first 五文档路由、本地 Dashboard、制作形态与 Look Development 决策。用户提出“创建/继续短剧项目”“看进度/下一步”“做 Look Development”“打开 dashboard/短剧创作台”“导出制作资料”，或任务跨多
- [game-art-direction](../skills/79aada543bbc876e.md) — Direct game art and creative vision. Turn GAME_DESIGN into ART_DIRECTION defining a recognizable visual identity, functional visual and audio feedback, and key 
- [game-build](../skills/a3b01dfc8dff5cb0.md) — Build a risk-matched whitebox or the approved production game for its target runtime. Turn GAME_DESIGN, and ART_DIRECTION when production begins, into a minimal
- [game-concept](../skills/fd07b5f61f440888.md) — Design game concepts from a novel. From SOURCE_BIBLE and PRODUCT_BRIEF, compare meaningful alternatives on the dimensions still unlocked, then select a playable
- [game-qa](../skills/03bebbe8f6179a40.md) — Verify a game with evidence on its selected target runtime. Launch the actual build and prove real rendering, input, the core loop, at least one designed outcom
- [game-world-design](../skills/3d83f142305906af.md) — Design game experience, systems, and levels. Converge the chosen concept into one GAME_DESIGN defining the player promise, core loop, how the world responds, th
- [novel-game-analyze](../skills/193253249ebcf75e.md) — Deconstruct a novel for game adaptation. Compress a raw novel, deconstruction library, or writing project into a SOURCE_BIBLE with cited textual evidence, extra
- [novel-to-game](../skills/12c82429d8bfeff5.md) — Turn a novel into a fully playable game on the selected target platform. Orchestrates the whole adaptation pipeline — requirements intake, gameable deconstructi
- [browser-cdp](../skills/aa594fbec8ba42f0.md) — Use this skill when you need to control a Chrome browser via CDP (Chrome DevTools Protocol) to reuse existing login sessions. Covers: launching Chrome in debug 
- [story-cover](../skills/9b1feb85506a32b2.md) — 小说封面生成。根据书名、作者名自动分析题材风格，调用 GPT-Image-2 生成含标题和署名的专业级网文封面；Codex CLI 优先使用内置 ImageGen，无需单独 API Key。触发方式：/story-cover、/封面、「帮我做个封面」「生成封面图」「做个小说封面」「封面设计」。
- [story-deslop](../skills/a7b1c01496938a53.md) — 网文去AI味。检测并清除文本中的AI写作痕迹，让文字回归自然、非模板化。触发方式：/story-deslop、/去AI味、「去AI味」「这篇太AI了」「网文去AI味」。
- [story-import](../skills/b3b3f8db7e83666d.md) — 逆向导入已有小说。将已写好的小说（半成品或完本）反向解析为标准项目目录结构，兼容 story-long-write / story-short-write 后续写作流程；内部复用 story-long-analyze / story-short-analyze 的拆解管道，按篇幅自动分流。触发方式：/story-imp
- [story-long-analyze](../skills/f84fbae845160938.md) — 长篇网文拆文。保留黄金三章、逐章摘要、剧情、情绪、节奏、角色、设定和文风接口，以连续章节块完成因果、双时间线、关系与三维节奏分析；兼容旧成果直接使用、按需增强和断点续跑。含可选三层灵感库管道（灵感库、跨书灵感聚合、更新灵感库）。触发方式：/story-long-analyze、/长篇拆文、「帮我拆这本书」「拆这本书」「
- [story-long-scan](../skills/5b56a6c0b3307614.md) — 长篇网文扫榜。分析起点、番茄、晋江等平台排行榜数据，提炼市场趋势与热门题材。触发方式：/story-long-scan、/长篇扫榜、「长篇什么火」「起点排行」。
- [story-long-write](../skills/7fef8dc0e33b625b.md) — 长篇网文规划与写作。支持只讨论结构、只写大纲或指定细纲，明确要求正文后再写章节。触发方式：/story-long-write、/写长篇、「帮我开书」「规划剧情」「写大纲」「补细纲」「日更」「续写」「继续写」「修改第X章」「回炉」「重写第X章」。
- [story-review](../skills/eed14be28c865520.md) — 多视角对抗式审查。full/lean 模式在已部署 reviewer agents 时并行 spawn；缺失/异常 agents 或 spawn 失败时自动降级 solo，参考文件不可读时使用内置 rubric fallback。触发方式：/story-review、/审查、「审查一下」「帮我审一下」。
- [story-setup](../skills/2504129415f695bf.md) — 网文写作工具集基础设施部署与检查。为 Claude Code / OpenCode / Codex / Google Antigravity / ZCode / OpenClaw / Reasonix 提供内置适配；Web AI / 通用 Agent 可走 skills + AGENTS.md 文件模式。触发方式：/s
- [story-short-analyze](../skills/3c9ccd95a5a8b4ff.md) — 短篇网文拆文。拆解爆款短篇小说（番茄短篇 / 故事会 / 知乎盐选 / 追妻 / 世情 / 重生 / 虐渣等通俗题材）的故事核、结构、情感线、反转设计、写作手法、共鸣层次。单一全量拆解管道：跑完 Stage 2-6 产出完整拆文报告，落盘到 拆文库/{书名}/，下游 story-short-write 同时读拆文报告 
- [story-short-scan](../skills/10a656d50c02278f.md) — 短篇网文扫榜。分析知乎盐言、七猫、黑岩、点众等平台热门短篇数据，捕捉风口题材。触发方式：/story-short-scan、/短篇扫榜、「短篇什么火」「知乎故事排行」。
- [story-short-write](../skills/d41caefb4e33788e.md) — 短篇网文写作。辅助短篇小说创作，从构思到成稿，聚焦情绪拉扯与节奏把控。触发方式：/story-short-write、/写短篇、「帮我写一篇短篇」「写个盐言故事」。
- [story](../skills/aca12db9e3872b15.md) — 网络小说工具箱主入口。根据用户需求自动路由到对应 skill，并可管理作者习惯、启动本地 Dashboard。触发方式：/story、$story、/story dashboard、/网文、「我想写小说」「记住我的写作习惯」「打开工作台」「检查更新」。
- [video-assemble](../skills/e0771facf681f6a5.md) — 合成视频解说最终成片：把旁白音频铺到源视频上，按旁白窗口压低原声，生成 SRT / ASS 字幕并可烧录， 最后做响度标准化。作为最终合成阶段使用。输入源视频、tts_meta.json 与旁白位置； 输出 recap 成片和字幕。触发词：视频合成、混音、字幕、压字幕、assemble video、mux、duckin
- [video-cut](../skills/6ac561990a6eb89d.md) — 把长视频按 Agent 选择的原片区间剪成短片。作为两阶段创作流程中的剪辑环节，读取 clip_plan.json 与源视频， 输出 edited_source.mp4；随后 Agent 按输出时间线写 narration.json。单独调用且未传 --no-narration-map 时， 仍支持旧版单阶段路径，把原
- [video-recap](../skills/217913bc6f9e47e0.md) — 从输入视频端到端生成中文解说成片。用户提供 .mp4 / .mov / .mkv / .webm，并要求添加旁白、 配音、总结、短剧/电视剧/电影/纪录片/科普解说时使用。负责编排 video-* 技能链：视频理解 → Agent 制定故事与视听方案 → 剪辑 → 配音 → 合成。触发词：视频解说、视频旁白、生成解说、
- [video-script](../skills/58d03a784e81589a.md) — 对已完成分析的视频进行导演与剪辑策划，再写带时间戳的中文解说并校验。work_dir 已包含 agent_narration_brief.md 与 vlm_analysis.json 时使用。适用于故事方向、片段选择、画面/原声/旁白分工、 解说写作与复核。输入 work_dir 中的理解索引；输出 recap_sto
- [video-understanding](../skills/86c395f032d934f6.md) — 把视频分析为结构化理解索引：场景检测、ASR 转写、逐场景 VLM 观察、静音窗口、融合时间线和写作 brief。 用于理解、索引或总结视频，也作为后续创作前的分析阶段。输入视频文件；输出 scenes.json、 asr_result.json、vlm_analysis.json、silence_periods.js
- [video-voiceover](../skills/e726cda155ae10de.md) — 把带时间戳的 narration.json 合成为中文解说音频。使用 MiMo TTS（mimo-v2.5-tts）或 Fish Audio（s2.1-pro-free）逐段生成语音， 按时间窗动态适配语速并处理响度；输入输出时间线上的旁白，产出 tts_segments 与 tts_meta.json。 旧版直接剪辑

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#zmm863-commits/dsh-agnes-studio&Date)
