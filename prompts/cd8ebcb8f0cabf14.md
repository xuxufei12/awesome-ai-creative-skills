[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# 12-Second Code-Based Launch Animation

**Category / 分类:** SVG 与动态图形  
**Text status / 文本状态:** Prompt marked complete by upstream; not independently reproduced  
**Origin / 收录方式:** Upstream structured prompt / post text

Project / 项目: [yihui-dev/awesome-opus5-5-videos](../projects/yihui-dev--awesome-opus5-5-videos.md)

Model labels in source / 来源模型标签: Claude / Opus

## Sources / 来源

- [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/92aee2f586ac0715cb3cbcb6384834f98a33383d/data/videos.json)
  - [Creator’s post / 作者原帖](https://x.com/notdwd/status/2105031774904766641)

**Source note / 来源备注:** prompt_partial=False

## Prompt / 提示词

````text
Make a 12s motion video in code (1920x1080, 30fps, one HTML file drawing every frame from a single seek(t) function, rendered with Playwright + ffmpeg, with original synthesized sound).

Story: a dark prompt pill on an off-white page types "make a launch video" with a real keystroke rhythm → enter, the button flashes orange and the pill slides up → a 12-frame filmstrip stamps in left to right, one frame per beat at 120 BPM; each frame shows one pose of an orange ball's bounce (squash on contact, stretch mid-air, real arcs) → a playhead sweeps the strip while a big viewer above plays the poses as a flipbook, twice, faster the second time → the strip slides away, "every frame is code." fills the screen, and the ball arcs over and lands as the period.

Rules: arrive fast, land soft (cover 12–19% of the remaining distance per frame); nothing ever freezes (slow push on every hold); stagger 2–4 frames; blur only on fast moves; big and readable on a phone; off-white, ink and one orange only. Sound: a tick per key, a click on enter, a rising note per frame stamp, a thump when the ball lands.

Show me 5 stills first (typing, strip half-built, flipbook, headline, last frame), critique them like a harsh motion director, fix the 3 worst problems, then render.
````

## Effects / 对应效果

<img src="https://media.skillry.dev/opus-5-5/_prompts/notdwd-766641/poster.9cda532570.webp" alt="Original result poster" width="640" loading="lazy">

[Open image / 查看原图](https://media.skillry.dev/opus-5-5/_prompts/notdwd-766641/poster.9cda532570.webp)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*
