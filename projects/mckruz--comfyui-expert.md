[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# MCKRUZ/ComfyUI-Expert

A session-scoped AI orchestrator for Claude Code that turns Claude into a senior video production technical director. It routes natural-language requests to 13 specialized skill modules covering the full pipeline: character image generation, video production, voice synthesis, LoRA training, and publishing -- all driven by ComfyUI.

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | ComfyUI 与模型编排 |
| Type / 类型 | Skill／技能包 |
| Hosts mentioned / 提及宿主 | Claude / Opus |
| Source status / 来源状态 | 已存 README 与 Skill |
| Stars at snapshot / 采集时 Stars |  |
| Snapshot / 来源快照 | 2026-10-22T05:51:48.232259+00:00 |
| Pinned commit / 固定提交 | dee27dc3d69b609c0006a8a12e71aadfc475ae95 |
| Upstream license / 上游许可证 | MIT 类许可（见原文） |
| Archived upstream / 上游归档 | Yes |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot](https://github.com/MCKRUZ/ComfyUI-Expert/blob/dee27dc3d69b609c0006a8a12e71aadfc475ae95/README.md)

## Setup & limits / 依赖与限制

依赖与安装方式见固定提交的 README；本次未部署。

扩展条目已收集来源说明；功能和效果未逐项运行复验。

## Effects / 效果展示

*No directly embeddable result was found in the collected source. Follow the original source above. / 已采集来源中未发现可直接嵌入的效果，请打开上方原始来源。*

## Skills (15)

- [comfyui-api](../skills/efce79b1633f86e3.md) — Connect to a running ComfyUI instance, queue workflows, monitor execution, and retrieve results. Supports both online (REST API) and offline (JSON export) modes
- [comfyui-character-gen](../skills/b16902d4ef6b2531.md) — Build identity-preserving character generation workflows and pipelines in ComfyUI. Selects the optimal identity method (InfiniteYou, FLUX Kontext, PuLID, Instan
- [comfyui-inventory](../skills/88f79f5ef5e6ceae.md) — Discover and cache all installed ComfyUI models, custom nodes, and system capabilities. Works online (API queries) and offline (directory scanning). Use before 
- [comfyui-lora-training](../skills/20e773ffe2904014.md) — Prepare datasets and configure LoRA training for character consistency. Covers FLUX (AI-Toolkit, SimpleTuner, FluxGym) and SDXL (Kohya_ss) training with step-by
- [comfyui-prompt-engineer](../skills/821deca7374f829d.md) — Craft model-specific prompts optimized for the target checkpoint and identity method. Handles FLUX, SDXL, SD1.5, and Wan video models with proper syntax, qualit
- [comfyui-prompt-interview](../skills/0c47b23079d94e2f.md) — Guided conversational interview to understand a user's creative vision before generating model-appropriate image prompts. Asks clarifying questions about subjec
- [comfyui-research](../skills/bd12787d74760038.md) — Research latest ComfyUI models, techniques, and community discoveries. Monitors YouTube channels, GitHub repos, and HuggingFace. Updates reference files with ti
- [comfyui-troubleshooter](../skills/80e91f25b7bf0f6d.md) — Diagnose ComfyUI errors, workflow failures, and quality issues. Suggests fixes based on error patterns, missing dependencies, and community-known workarounds. U
- [comfyui-video-pipeline](../skills/ae17f8a3a7a9bac3.md) — Generate videos using ComfyUI with Wan 2.2, FramePack, or AnimateDiff. Handles image-to-video, text-to-video, talking heads, and motion-controlled animation. Us
- [comfyui-video-production](../skills/850c89af061debcb.md) — Plan and orchestrate end-to-end video production pipelines in ComfyUI with validation gates and error recovery. Handles img2vid, txt2vid, vid2vid, and multi-sho
- [comfyui-voice-pipeline](../skills/109333340d12ce2d.md) — Generate character voices using TTS, voice cloning, and lip-sync tools. Supports Chatterbox, F5-TTS, TTS Audio Suite, RVC, and ElevenLabs. Use when creating spe
- [comfyui-workflow-builder](../skills/4d0aa17fb3f107e1.md) — Generate, build, create, or design ComfyUI workflow JSON from natural language descriptions. Produces valid node graphs with correct class_types, connections, o
- [project-manager](../skills/bf0fc8a23f9b127b.md) — Manage video production projects including character profiles, project manifests, workflow history, and asset tracking. Use when creating new projects, managing
- [video-assembly](../skills/7e427b58baa3bc57.md) — Assemble final video from generated clips, audio, and assets using FFmpeg or Remotion. Handles concatenation, audio mixing, transitions, titles, and export. Use
- [video-publisher](../skills/8b442c3cc837ddf9.md) — Publish assembled videos to YouTube and other platforms. Orchestrates existing youtube-uploader, youtube-strategy, and youtube-plan-new-video skills. Use when r

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#MCKRUZ/ComfyUI-Expert&Date)
