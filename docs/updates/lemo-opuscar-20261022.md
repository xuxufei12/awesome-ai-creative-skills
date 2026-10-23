# Lemo-Opuscar 更新：从选风格，到创建自己的风格

[中文首页](../../README.zh-CN.md) · [English home](../../README.md) · [项目详情](../../projects/lemomo-ai--lemo-opuscar.md)

这次更新让 Lemo-Opuscar 从影片风格库进一步变成个人风格制作工具箱。除了选择现有风格做片，还可以调整某种风格，或从空白设计自己的视觉语言，先看效果，再保存复用。

来源是 Lemomo 于 2026-10-22 发布的[更新帖](https://x.com/lemomo_ai/status/2113195080517562646)及其[完整文章](https://x.com/i/article/2112813136277540864)。文中的更新内容已与上游仓库核对；本页底部提供固定提交与文件索引。

## 这次更新了什么

- 风格库从本资料库原先收录的 51 种增至 **59 种**，新增 **8 种剪辑与纪实风格**。
- 新增自定义风格流程，可以改编库内风格，也可以从自己的描述、参考图或参考片出发设计。
- 通过方案确认、风格图和短片逐步检查效果；满意后才保存为个人风格，以后可以直接点名调用。
- 作者在文章中展示了 Opus 与 Sonnet 制作的样片对照。模型档位和效果评价属于作者的使用经验。

### 八种剪辑与纪实风格

| 风格 | 画面与剪辑方法 | 可以拿来做什么 |
|---|---|---|
| 字幕新闻 Caption News | 大字幕、关键词色块、滚动数字与来源标记 | 热点快讯、数据新闻、静音观看的短视频 |
| 1920s 新闻影片 Newsreel | 复古片头、报纸转场、快节奏播音与爵士配乐 | 历史趣闻、老物件和品牌故事 |
| 实时倒计时分屏 Countdown | 围绕一个明确时刻，分屏逐渐增加，抵达节点时合流 | 发射、终场、发布与倒数 |
| 延时交响 Time-lapse Symphony | 用延时影像、音乐和剪辑密度推进 | 城市影像、品牌形象片、地方纪录 |
| 视觉调查 Visual Investigation | 在共同时间线上对照影像、照片、文档、声音和地图 | 事件复盘、资料分析、调查叙事 |
| 构成主义蒙太奇 Constructivist Montage | 黑、红、纸色的印刷感，斜向排版与节拍剪辑 | 工程史、工业史、群像叙事 |
| 体育战术板 Sports Telestrator | 回放、定格、圈画、箭头与战术图 | 比赛复盘、战术解说、录像拆解 |
| 电视新闻包装 Broadcast News Package | 台标片头、新闻目录、标题条、数据卡片与地图 | 行业周报、栏目播报、团队资讯 |

这批风格围绕真实素材的剪辑、编排与包装展开；具体素材、配音与来源要求见各自的 STYLE 文档。首页的八张画面都能打开对应样片和风格提示词。

## 示例：Swiss Motion → Material Grid

作者保留了瑞士风格的网格、节拍和排版，替换了物件的材质与空间表现。平面形状变成黏土、塑料、毛毡、玻璃和镀铬物件，俯视时仍有海报的秩序，镜头倾斜后露出立体体积。

对比图和 31 秒示范短片见[首页更新展示](../../README.zh-CN.md)。点击对比图可播放作者的原风格与改编风格样片。

这是一份风格制作流程，而非该示范片完整创作对话的逐字公开。完整可复用指令来自上游 `MY-STYLES.md`，已单独收录在本资料库的提示词目录。

## 怎样做出自己的风格

1. **选入口。** 改编一种现有风格，或描述新风格、提供参考图与参考片。空白起步时，Claude 会建议接近的技法基础。
2. **定方案。** 一次讨论一个问题，也可切换自由对话。明确用途、平台、画幅、品牌素材，以及材质、颜色、字体、运动、镜头和声音。改编现有风格时会说明哪些调整保留原有气质、哪些会改变风格本身。
3. **确认变化。** 汇总改前、改后及取舍，得到确认后再实施。
4. **先看风格图。** 按实际绘制代码出图；改编已有风格时可并排比较同一画面。
5. **看示范短片。** 制作带音乐与音效的短片，检查每项改动的表现，再确认保存。通用流程要求 15–30 秒，作者展示的 Material Grid 样片标为 31 秒。
6. **复用个人风格。** 默认保存到 `~/lemo-my-styles/<name>/`，包含风格说明、变更记录、示范片及源码。公共库更新和插件重装不会覆盖这个目录。

### 更新或安装

已有插件的用户按上游说明执行以下命令，然后重启 Claude Code。公共风格库会在下一次制作影片时更新。

```sh
claude plugin marketplace update lemolab
claude plugin update lemo-opuscar@lemolab
```

首次安装：

```sh
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

进入 Skill：

```text
/lemo-opuscar:lemo-opuscar
```

也可直接描述想改的风格或新风格。保存之后，在做片时使用自己起的名字。

## 帖子中的预告

**Lemo Movie Studio 工作台**和**下一批日系动漫风格**在这篇文章中属于后续计划。本次同步将它们记录为预告，当前新增的风格仍以上表八种为准。

## English summary

Lemo-Opuscar now has 59 film styles. This update adds eight editing and documentary approaches, plus a workflow for adapting a library style or creating a personal one. The process moves from creative decisions to a code-rendered style frame, a short demonstration, and explicit confirmation before saving the style outside the shared library.

The creator’s Material Grid example preserves Swiss Motion’s grid, rhythm and type while introducing tactile materials and depth. The homepage shows both versions and links directly to the official films. The complete reusable workflow is indexed from `MY-STYLES.md`; the demonstration’s full creation conversation is not presented as a public prompt.

The announced desktop studio and future anime batch are previews. Code and documentation use MIT; demonstration films and stills use CC BY 4.0 with the upstream voice and third-party asset exclusions. Credit the examples to LemoLab / Lemomo.

## 来源、许可与同步记录

原作者为 **LemoLab / Lemomo**。示例画面与影片以 CC BY 4.0 提供；代码与文档为 MIT。上游对部分配音轨和第三方素材另有说明，尤其电视新闻包装示例的配音轨不可直接按 CC BY 4.0 复用。具体见上游 README 的 Licence 部分。

本次同步固定到提交 [`3961ddb3d24d8876e0e2754f7790d66908acee51`](https://github.com/lemomo-ai/lemo-opuscar/tree/3961ddb3d24d8876e0e2754f7790d66908acee51)。更新了 59 份 STYLE 文本、2 份 SKILL 文本，并补充自定义风格指令、案例、首页展示和来源文件哈希。这里完成的是资料同步与链接检查，示例影片由上游作者制作。

- [更新公告与原文](https://x.com/lemomo_ai/status/2113195080517562646)
- [固定提交的 README](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/README.md)
- [MY-STYLES.md](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/MY-STYLES.md)
- [主 Skill](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/plugin/skills/lemo-opuscar/SKILL.md)
- [结构化同步记录](../../data/featured-update.json)
- [来源文件与哈希](../../data/source-files.json)
