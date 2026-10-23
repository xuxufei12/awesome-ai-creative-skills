[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# Melvynx/video-agent-skills

短视频脚本、研究、字幕及基础剪辑；可扩展配音／图像。

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | 剪辑字幕与数字人 |
| Type / 类型 | Skill／技能包 |
| Hosts mentioned / 提及宿主 | Claude / Opus, Codex |
| Source status / 来源状态 | 已存 README 与 Skill |
| Stars at snapshot / 采集时 Stars |  |
| Snapshot / 来源快照 | 2026-10-22T05:48:40.774558+00:00 |
| Pinned commit / 固定提交 | 4774fa4f2601baa822fd513387202c26e4587902 |
| Upstream license / 上游许可证 | MIT 类许可（见原文） |
| Archived upstream / 上游归档 | No |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot](https://github.com/Melvynx/video-agent-skills/blob/4774fa4f2601baa822fd513387202c26e4587902/README.md)

## Setup & limits / 依赖与限制

FFmpeg、Remotion；部分流程需要外部工具或账号。

其 README 对剪辑复杂度、字幕误识和翻译效果有明确限制。

## Effects / 效果展示

<img src="https://raw.githubusercontent.com/Melvynx/video-agent-skills/4774fa4f2601baa822fd513387202c26e4587902/assets/default-render.png" alt="The default edit: split screen, boards on paper, captions on the seam, comment CTA" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/Melvynx/video-agent-skills/4774fa4f2601baa822fd513387202c26e4587902/assets/default-render.png)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*

## Skills (13)

- [broll](../skills/21e0547b17282562.md) — The creator's own B-roll (their clips, screen recordings, photos) turned into a library any agent can search in one grep - scanned once with ffprobe and ffmpeg 
- [clips](../skills/ab3f228f95e270d5.md) — Turns one long video (YouTube link, podcast, webinar, livestream, or a local file) into finished vertical shorts. Use when the user says long to short, repurpos
- [codex-images](../skills/c8c56ebbf5a016b4.md) — Generates images with Codex (OpenAI's coding agent and its built-in image tool, included in a ChatGPT plan) - YouTube thumbnails, covers, B-roll stills, board i
- [editing](../skills/1c8c1dbd6c3f1428.md) — Entry point for every video job - routes to studio-setup, insta-audit, studio-script, outliers, short-editing, broll, steal, clips, short-translate, codex-image
- [insta-audit](../skills/e3971b76f6c6b239.md) — Audits an Instagram account through Treg. By default the creator's own account, free - installs Treg if needed, connects their Instagram, pulls the last 30 to 5
- [outliers](../skills/16377bf12baac3a3.md) — Finds the outlier reels of Instagram accounts or videos of TikTok accounts (3x their own account's median views or more) through Treg and turns the 5 best into 
- [publish](../skills/c08a69423be2b50f.md) — Gets a finished video out on YouTube (Shorts or long), Instagram Reels and TikTok - picks the video, makes the light export for Instagram and TikTok, the cover,
- [short-editing](../skills/28f01905fbe4bc24.md) — Edits a talking-head take end to end into a paper-style motion design short (1080x1920, also 1:1 and 16:9) with its own render engine (Node + Chrome + ffmpeg, f
- [short-translate](../skills/2078df7665b42c00.md) — Translates a talking-head take (or a finished video) into another language with the creator's own cloned voice through ElevenLabs Dubbing, using their ElevenLab
- [steal](../skills/1c732d6df6c974b2.md) — Copies another creator's editing style into a named style that short-editing applies to your own takes. Use when the user says steal, "copy the style of", "edit
- [studio-script](../skills/c44586f146348a8e.md) — The scriptwriter of the creator's videos - short-form scripts (YouTube Shorts, TikTok, Instagram Reels, 30 to 60 s) in their own voice from video-agent/voice.md
- [studio-setup](../skills/f65095df982e981a.md) — Sets up the creator's video editing studio, for shorts and YouTube videos, on their computer and in their project - tools, the video-agent/ folder, the render e
- [vox](../skills/2222155f4d83ae2a.md) — Turns one photo into a cinematic paper-collage animation in the style of Vox explainer documentaries (halftone cut-outs with a white scissor border, torn paper,

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#Melvynx/video-agent-skills&Date)
