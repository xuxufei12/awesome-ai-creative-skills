[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# fengyungithub/dsh-short-video-studio

画布、媒体资产与 ComfyUI 场景生产工作流。

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | 视频框架与程序化成片 |
| Type / 类型 | Skill／技能包 |
| Hosts mentioned / 提及宿主 | DeepSeek / DSH |
| Source status / 来源状态 | 已存 README 与 Skill |
| Stars at snapshot / 采集时 Stars |  |
| Snapshot / 来源快照 | 2026-10-22T05:50:32.296322+00:00 |
| Pinned commit / 固定提交 | 9f7443661fb1b577753ca057f547e119b2abe974 |
| Upstream license / 上游许可证 | Apache-2.0（见原文） |
| Archived upstream / 上游归档 | No |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot](https://github.com/fengyungithub/dsh-short-video-studio/blob/9f7443661fb1b577753ca057f547e119b2abe974/README.md)

## Setup & limits / 依赖与限制

DSH、ComfyUI；可选第三方服务。

宿主版本和工作流节点需匹配。

## Effects / 效果展示

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/styles/style-preview.jpg" alt="七套内置视觉风格示例" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/styles/style-preview.jpg)

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/harness-dialogue-1.png" alt="会话截图1" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/harness-dialogue-1.png)

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/harness-dialogue-2.png" alt="画布真实截图" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/harness-dialogue-2.png)

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-video.png" alt="ui-video" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-video.png)

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-image-t2i.png" alt="ui-image-t2i" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-image-t2i.png)

<img src="https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-image-i2i.png" alt="ui-image-i2i" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/fengyungithub/dsh-short-video-studio/9f7443661fb1b577753ca057f547e119b2abe974/examples/ui/ui-image-i2i.png)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*

## Skills (5)

- [brand-promo-video-generator](../skills/183e49fac1b2ca43.md) — 把可核验的品牌素材与推广目标转化为一条完整的品牌宣传短片生产流程，依次完成素材收集、品牌事实表、来源清单、品牌资产上画布、创意方向、六列标准镜头表、镜头表自检门、生成前硬确认、逐镜视频生成（视频原生音频 + 画面内原生文案）、拼接成片与最终交付复查。全程走本地 ComfyUI 能力注册表（图片文生图 + 视频 AV 模
- [h3-prompt-writing](../skills/4c3caa49ddaa4fd7.md) — Write MiniMax H3 video generation prompts for T2VA, I2VA, FL2VA, L2VA, and Ref2VA. Use when rewriting multimodal requests into H3 prompt structures, composing i
- [image-generate](../skills/ca56ff2c0eaf0b23.md) — 
- [story-short-generator](../skills/713d6e6a4f0a3d13.md) — 将一句故事创意转化为完整的风格化短片：依次完成项目简报、故事大纲、角色卡（**形态随视频档位**：`fast` 单视图正面全身 / `balanced`·`quality` 三视图横排）、无人物场景卡、单视图道具卡、七列标准镜头表（含「续接」列）、镜头表自检门、单文本分镜文档（可选铅笔分镜）、逐镜视频生成与最终交付复查
- [video-generate](../skills/a5a6dabf07bf5b22.md) — 把「提示词 + 参考图/首帧图 + 尺寸/档位/时长/比例」等参数生成为一段单镜头视频。支持 r2v（参考图生成，ref_nodes 绑定角色/场景）与 i2v（首帧/末帧生成，first/last_frame 串联）。适用于「输入框手动生成」这条轻量链路：用户在输入框用 `/video-generate` 斜杠命令加

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#fengyungithub/dsh-short-video-studio&Date)
