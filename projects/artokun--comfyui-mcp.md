[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# artokun/comfyui-mcp

为编码代理提供 ComfyUI 工作流控制。

| Field / 字段 | Value / 内容 |
|---|---|
| Category / 分类 | ComfyUI 与模型编排 |
| Type / 类型 | Skill／技能包 |
| Hosts mentioned / 提及宿主 | Claude / Opus, Codex, DeepSeek / DSH |
| Source status / 来源状态 | 已存 README 与 Skill |
| Stars at snapshot / 采集时 Stars |  |
| Snapshot / 来源快照 | 2026-10-22T05:51:38.952689+00:00 |
| Pinned commit / 固定提交 | 6996d06ff511dd7b3b05adf89716e7667df2c1b9 |
| Upstream license / 上游许可证 | MIT 类许可（见原文） |
| Archived upstream / 上游归档 | No |

**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。

## Sources / 来源

- [GitHub snapshot](https://github.com/artokun/comfyui-mcp/blob/6996d06ff511dd7b3b05adf89716e7667df2c1b9/README.md)

## Setup & limits / 依赖与限制

可用的 ComfyUI 实例及工作流节点、模型。

MCP 是连接层，不能替代模型权重和自定义节点。

## Effects / 效果展示

<img src="https://raw.githubusercontent.com/artokun/comfyui-mcp/6996d06ff511dd7b3b05adf89716e7667df2c1b9/docs/images/demo-poster.jpg" alt="Upstream example" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/artokun/comfyui-mcp/6996d06ff511dd7b3b05adf89716e7667df2c1b9/docs/images/demo-poster.jpg)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*

## Skills (40)

- [ai-toolkit-trainer](../skills/0deb84398f3e48c6.md) — Train custom LoRAs with ostris AI-Toolkit. Covers WAN 2.2/2.1 (people, styles, video motion) and Z-Image (Turbo & Base, low-VRAM image LoRAs). Use when the user
- [anima-base](../skills/e0f92f7b56076b64.md) — Anime/illustration text-to-image (ANIMA 1.0, ~2B Cosmos DiT). Use for anime, manga, illustrated characters; accepts Danbooru tags + natural language; runs/train
- [anima-lora-trainer](../skills/8b306bf33b30d001.md) — Train a custom anime LoRA on the ANIMA base model with Citron's local Gradio trainer (kohya sd-scripts), <6GB VRAM, character/style LoRAs; covers setup, dataset
- [civitai](../skills/75d1b62cbd442adb.md) — Discover Civitai models with the BUILT-IN download_model action:"search_civitai" and install/generate them locally. Find a checkpoint/LoRA/embedding on Civitai,
- [color-correction](../skills/68891fc396ad7794.md) — Diagnose and fix video/image color OBJECTIVELY with the get_image (action:"analyze_color") tool (scopes/stats such as black/white points, contrast, saturation, 
- [comfyui-launch-flags](../skills/2e0e499eaa5cd874.md) — Pick the right ComfyUI startup flags for VRAM, attention, caching, and speed. The full decision matrix for OOM (--novram / --cache-none / --disable-smart-memory
- [comfyui-node-registry](../skills/d849bcf3e3d7a983.md) — Authoring & publishing ComfyUI custom nodes to the Comfy Registry, covering node structure, pyproject.toml spec, comfy-cli publishing, and CI
- [debug-render](../skills/951df0175c39586c.md) — Debug a WRONG or imperfect render (not a hard error) by inspecting inputs and intermediate steps with run-to-node. Render one branch up to an output, preview-ta
- [director](../skills/6726eac8287fe50c.md) — Full production pipeline covering story to scenes, Z-Image start frames, Qwen Edit end frames, WAN FLF video clips, ffmpeg concatenation
- [ernie-image](../skills/58e66a5ef0bdc2b0.md) — Build Baidu ERNIE-Image / ERNIE-Image-Turbo workflows, primarily TEXT-TO-IMAGE. Pick ERNIE when you need precise multilingual text rendering, posters/signage, m
- [flux-txt2img](../skills/5583e0e25123f040.md) — Build Flux txt2img workflows with Flux.1 Dev (SRPO), Flux 2 Klein 9B, Turbo LoRAs, FluxGuidance, and DualCLIPLoader patterns
- [ideogram-ultra](../skills/f98342c119a4f10d.md) — Build Ideogram 4 (Ideogram Ultra) txt2img and img2img workflows with the local open-weights model, dual conditional/unconditional models with DualModelGuider, Q
- [installer-packs](../skills/9f87ba35c207fd86.md) — Use when installing a model family from an installer pack, or when building/deriving a new pack from an upstream installer or a workflow JSON. Explains the mani
- [krea2-identity-edit](../skills/d122fb451ebf3779.md) — Swap an OUTFIT or transfer CLOTHING onto a person LOCALLY, keeping their face, pose and background. Use for "put this jacket on her", "change his shirt", "cloth
- [krea2-txt2img](../skills/ce5164426caff720.md) — Build Krea 2 Turbo txt2img workflows with the native krea2 CLIPLoader, Qwen3-VL encoder, Qwen image VAE, 8-step turbo settings, and Ideogram-style JSON promptin
- [local-llm-free](../skills/550d9298370cf100.md) — Run the ComfyUI agent locally for FREE with no subscription, no API key, and fully offline, using our gemma4 models fine-tuned on the comfyui-mcp tool suite via
- [lora-manager](../skills/0f778e108fe4ace3.md) — Author ComfyUI-LoRA-Manager nodes from the panel. Use when adding a LoRA Manager loader, stacker, prompt, or text node, or when panel_add_node refuses AUTOCOMPL
- [ltx-director](../skills/19acfd6823a884bf.md) — Drive the LTX Director (Timeline) node. Its Add Image/Text/Audio buttons are DOM-only and cannot be clicked by an agent; edit the hidden timeline_data JSON widg
- [ltxv2-video](../skills/93bac4aa0ebb68b4.md) — Build Lightricks LTX-2 / LTX-2.3 video workflows covering text-to-video, image-to-video, GGUF and bundled checkpoints, distilled model, camera control LoRAs, sy
- [minimax-h3-video](../skills/747f0276507f3747.md) — Build MiniMax H3 (Hailuo) local video workflows with native T2V/I2V/R2V nodes, Comfy-Org INT8 weights, turbo LoRAs for 8GB VRAM, 15-second stereo-audio clips, a
- [model-compatibility](../skills/2b3785acb6159246.md) — Model family compatibility matrix covering loaders, resolutions, samplers, CFG, VAE, ControlNet, and LoRA compatibility for SD 1.5, SDXL, Flux, SD3, and video m
- [model-registry](../skills/594bc882238fb053.md) — Curated download URLs and target directories, organized by family (Flux, WAN, LTX, Qwen, Z-Image, SD15/SDXL), for every model the comfyui-mcp skills reference, 
- [panel-node-pack-sync](../skills/e075ee4250037d2f.md) — Keep the ComfyUI sidebar panel node-pack (comfyui-agent-panel) in step with the orchestrator after comfyui-mcp updates. Use this whenever the orchestrator was j
- [panel-operations](../skills/53f5d8130a9f9813.md) — On-demand procedures for the ComfyUI sidebar panel agent that are too long to sit in the system prompt. Read it when a task lands in one of these areas. subgrap
- [prompt-engineering](../skills/cc46604075a1638d.md) — ComfyUI prompt engineering knowledge covering CLIP text encoding syntax, weight modifiers, model-specific prompting strategies, and best practices
- [qwen-image-edit](../skills/a2b947b6997b6d5c.md) — Build Qwen Image Edit workflows covering model loading, conditioning, LoRAs, prompt patterns, and XY plot testing
- [qwen-txt2img](../skills/96350c8be535c3ce.md) — Build Qwen Image 2512 text-to-image workflows with QwenImageIntegratedKSampler, separate component loading, lightning LoRAs, and fine-tuned model variants
- [report-bug](../skills/88adea18615409af.md) — Issue reporting is disabled during limited maintenance of comfyui-mcp and the local Agent Panel. When the user hits a defect, explain that no report will be fil
- [rgthree](../skills/bd38909a01457459.md) — Configure and author rgthree-comfy nodes — Fast Groups Bypasser/Muter (group toggles), Power Lora Loader, Context/Context Big, Seed, Any Switch. Use when a work
- [train-character-lora](../skills/76e6643f948283d8.md) — Train a character/identity LoRA locally on FLUX.1-dev via the comfyui-mcp train_* tools (GPU Docker + ostris ai-toolkit). Use when the user wants to train a LoR
- [triton-sageattention](../skills/6b6502b2104a81c8.md) — Install Triton + SageAttention to accelerate ComfyUI (the sageattn attention_mode and inductor torch.compile used by WanVideoWrapper / many video graphs). Windo
- [troubleshooting](../skills/eea426b5af1b28c6.md) — Common ComfyUI errors and fixes. OOM, missing nodes, dtype mismatches, black images, and debugging strategies
- [video-extend](../skills/f180c2714b273207.md) — Extend / continue a video temporally with Pusa 2.2 in ComfyUI. Temporal flowmatching (the flowmatch_pusa scheduler + WanVideoAddPusaNoise) on the WanVideoWrappe
- [video-upscale](../skills/43fa4fcb943b1a39.md) — Upscale and restore video in ComfyUI. Both the quick local path (per-frame ESRGAN like 4x_foolhardy_Remacri via ImageUpscaleWithModel + 4x→2x supersample, with 
- [wan-flf-video](../skills/e5645daa24955fd4.md) — Build WAN 2.2 First-Last-Frame video workflows. Native dual hi-lo (required), and WanVideoWrapper VACE approaches
- [wan-multitalk](../skills/f3414ecdb6938502.md) — Build WAN MultiTalk audio-driven talking-avatar / lip-sync video workflows. MeiGen-AI MultiTalk on WAN 2.1 14B I2V via kijai WanVideoWrapper (portrait + audio →
- [wan-scail-replacement](../skills/bf0c31db5b274c4d.md) — SCAIL-2 in-video character replacement on WAN 2.1. WanSCAILToVideo + SCAIL2ColoredMask + SAM3, the reference-image framing→scale rule, and the tuning/compositin
- [wan-t2v-video](../skills/6b76fa161ed06459.md) — Build WAN 2.2 Text-to-Video workflows. Dual hi-lo models, lightning LoRAs, VACE modules, and KSamplerAdvanced two-pass
- [workflow-layout](../skills/abf9127a79368db2.md) — Lay out and organize a ComfyUI workflow cleanly on the live panel canvas. Dependency-layered node placement with no overlaps, subgraphs, colored group boxes, an
- [z-image-txt2img](../skills/19aadbe2b4ddaddc.md) — Build Z-Image txt2img workflows. RedCraft checkpoint, Z-Image Turbo/Base LoRAs, ControlNet, and sampler presets

## Prompts (0)

No prompt text indexed / 未索引到可展示的提示词正文。

## Cases (0)

No separate case records / 未索引独立案例。

## Star history / Star 趋势

[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#artokun/comfyui-mcp&Date)
