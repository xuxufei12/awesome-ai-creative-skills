[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# Kinetic Typography JFK Speech Film

**Category / 分类:** Three.js 与 WebGPU  
**Text status / 文本状态:** Prompt marked complete by upstream; not independently reproduced  
**Origin / 收录方式:** Upstream structured prompt / post text

Project / 项目: [yihui-dev/awesome-opus5-5-videos](../projects/yihui-dev--awesome-opus5-5-videos.md)

Model labels in source / 来源模型标签: Claude / Opus

## Sources / 来源

- [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/92aee2f586ac0715cb3cbcb6384834f98a33383d/data/videos.json)
  - [Creator’s post / 作者原帖](https://x.com/Gdgtify/status/2105669567036989608)

**Source note / 来源备注:** prompt_partial=False

## Prompt / 提示词

````text
Create a 20.00-second kinetic typography film titled “ESCAPE THE ORBIT,” based on John F. Kennedy’s Rice University address, September 12, 1962.

The central experience: a sentence discovers that it can change its own trajectory.

Deliver one complete, self-contained HTML file. Composition: 1080×1080. Target: 60fps. Use Canvas, SVG, or embedded WebGL. Embed required assets and libraries. The film must work without audio.

EXACT DISPLAY TEXT
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
Preserve this order. The bracketed ellipsis explicitly indicates omitted speech. Attribution is separate from the excerpt. No additional slogans.
ART DIRECTION
Background: midnight # 080D23.
Primary type: warm white # FFF4DD.
Trajectory: electric coral # FF654F.
Secondary orbital geometry: blue # 6685FF.
Use a broad, confident grotesque for the speech and a sharply drawn italic for the final emphatic word. Avoid the appearance of a spacecraft dashboard. No rockets, astronaut illustrations, starfield wallpaper, lens flares, or decorative telemetry.
The frame should resemble an exceptionally refined astronomical instrument that has become expressive.

CENTRAL VISUAL RULE
The baseline of the sentence is a trajectory.

At first it is trapped in a closed orbit. A rhetorical decision changes that orbit into an open path. The letters remain the same travelers throughout.
Use an abstract orbital metaphor; do not present invented mission data or imply a physically accurate flight simulation.
STORYBOARD
0.00–3.50
The opening excerpt appears across the center, large and horizontal. Reveal it in three meaningful phrase groups.
A single hairline ellipse passes behind the baseline. A small circular lunar mark occupies its distant focus.
Hold the completed phrase motionless for 700ms.

3.50–6.00
The camera pulls back. The previously straight baseline reveals a shallow curvature.

The phrase travels along the ellipse as a coherent unit. Keep its glyphs upright during the initial movement. Only after the reading hold may they progressively adopt the tangent of the path.

The viewer realizes the sentence is circling rather than advancing.
6.00–7.00
Show the bracketed omission in an uncluttered central opening. The orbital movement decelerates.

7.00–10.50
Reveal the next clause on the near side of the orbit. Its final word travels through one smooth, effortless arc and returns toward where it started.

This ease should feel elegant but unproductive. Avoid comic bouncing.

10.50–14.50
Reveal the final clause horizontally before transforming it.
At its emphasis, the ellipse opens at one precise point. The same tracked letter group takes the new tangent and departs.
Perform one deliberate 70-degree camera roll. Counter-rotate the active phrase so it remains readable while the orbital field changes orientation around it.

The trajectory sweeps from lower left to upper right. Acceleration is conveyed by expanding spacing between its trailing marks, not by shaking the camera.

14.50–17.00
The camera matches the departing phrase’s velocity. The phrase becomes visually still while the old orbit recedes beneath it.

The lunar mark enlarges into a restrained crescent through geometric overlap. The crescent brackets the destination without becoming a cartoon illustration.
17.00–20.00
Resolve into a spacious editorial composition containing the selected excerpt in reading order, including its omission marker.

The open trajectory runs through the margins and exits the frame. Hold the entire image completely still for the final 1.2 seconds.

CHOREOGRAPHY
Use only three camera operations: pullback, roll, velocity match.
Give each operation a rhetorical purpose.
Keep the currently read phrase at least 64px high in the 1080px composition.
Motion blur may affect trailing geometry, never the active text.
No word may begin its ornamental travel before its reading hold finishes.

IMPLEMENTATION
Represent the ellipse and departure path analytically. Blend position and tangent continuously at the departure point; no teleportation.
Use arc-length sampling for consistent spacing along curves.
Separate camera transforms from glyph orientation.
Cache glyph rendering and static geometry.
Expose window.ready and window. seek(t). Seeking must pause playback and render any time from 0 through 20 deterministically, including out-of-order calls.
Provide window.frame(n) for n=0…1199 at t=n/60.
Render t=20 as the final held composition.
Use no accumulated physics or runtime randomness.

QUALITY GATE
Inspect frames at 0, 3, 5, 7.5, 10.5, 13, 16, and 19 seconds.
Verify that the same tracked phrase visibly follows its own trajectory.
````

## Effects / 对应效果

<img src="https://media.skillry.dev/opus-5-5/_prompts/gdgtify-989608/poster.094984c36d.webp" alt="Original result poster" width="640" loading="lazy">

[Open image / 查看原图](https://media.skillry.dev/opus-5-5/_prompts/gdgtify-989608/poster.094984c36d.webp)

<img src="https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/8560da8f7e1b5cea4ee50cf835545222d057fac8/assets/covers/2105669567036989608.jpg" alt="Upstream result frame" width="640" loading="lazy">

[Open image / 查看原图](https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/8560da8f7e1b5cea4ee50cf835545222d057fac8/assets/covers/2105669567036989608.jpg)

[▶ Watch video / 播放视频](https://video.twimg.com/amplify_video/2105125811946770432/vid/avc1/1080x1080/40PB0DJ1q4l6xIXc.mp4?tag=29)

https://video.twimg.com/amplify_video/2105125811946770432/vid/avc1/1080x1080/40PB0DJ1q4l6xIXc.mp4?tag=29

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*
