[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# reFresh 酸奶 20 秒卡点广告(完整工程级提示词)

**Category / 分类:** 广告与产品演示  
**Text status / 文本状态:** Prompt / public fragment transcribed from PDF; completeness follows source  
**Origin / 收录方式:** User-provided PDF; Unicode glyphs normalized for reading

Model labels in source / 来源模型标签: Claude / Opus

## Sources / 来源

- [User-provided PDF transcription](https://x.com/exploraX_/status/2108182727966998587)
  - PDF: `opus-deepseek-video-prompts.pdf`, pp. 7, 8, 9, 10; original post not independently verified / 未独立核验原帖。

**Source note / 来源备注:** PDF typography normalized (NFKC and CJK radicals); source wording/typos retained. This does not verify model, cost or performance claims.

## Prompt / 提示词

````text
Create a 20-second, beat-cut motion graphic for reFresh drinking yoghurt (three flavors:
Strawberry, Vanilla, Sweetened; 500ml square-shouldered PET bottles with black caps; made by
Integrated Dairies, Vom, Nigeria). The film is a fast trailer of the brand's scroll website:
thick liquid floods sweep the frame, the bottle changes flavor exactly where the liquid crosses
it, and big soft type slams in on the beat.
DELIVERABLES
- 9:16 master at 1080x1920 plus a 16:9 version at 1920x1080. 30 fps, exactly 20.0 s.
- Real motion blur: render 3 sub-frames per output frame and average 2 of them (240-degree
shutter). Light film grain. A little sharpening where footage is scaled up.
- H.264 (CRF 16, yuv420p), AAC 256 kbps 48 kHz, loudness -14 LUFS integrated, true peak -1 dBTP.
- Sound is effects and sound design only. No music, no voice. Every sound synthesized or
royalty-free.
LOOK
- Palette: Plateau Green #063A2B (hero and finale backgrounds), Milk #FCF3E3, Strawberry Milk
#F1B4C2, Vanilla Butter #F5E7B2, Ripe Berry #D93F4C (accents only), Leaf #4C9A3F, Cap Black
#151515. Colors are sampled from the packaging.
- Headlines: Fraunces Black 900 with SOFT 100, WONK 1, opsz 144; tracking -0.03em; line height
0.9; all caps. Plateau Green on light grounds, Milk on green.
- Handwritten notes and the logo word: Caveat Brush. Small labels: Bricolage Grotesque Bold,
uppercase, tracking 0.22em.
- Keep every word at least 4% inside the frame. In 9:16, break long lines
(THE / ORIGINAL., REP YOUR / FAVE).
- Motion feels viscous: heavy ease-outs, back-overshoot landings with a quick squash and
stretch, type stamps that scale from 1.6x to 1x in 0.2 s with a slight rotation settle, wiggles
as damped sines. Only the marquees move linearly.
PRODUCT RULES
- The bottle is always a real packshot cutout: the three flavors rendered identically and
pixel-aligned, soft shadow baked in. Never animate the bottle or its label with an AI video
model; labels warp.
- Flavor switch: stack the three bottle layers. While a flood rises, show the old flavor above
the liquid line and the new flavor below it, so the label changes exactly at the wave's edge.
- Anything a flood swallows is clipped to that same liquid line (trace the line per frame).
- No people. No health or nutrition claims. No URL on the end card.
TIMING
120 BPM: 10 bars of 2 s, a beat every 0.5 s. Cuts land on downbeats.
BAR 1 (0:00-0:02) SHAKE
Milk background. A line-drawn bottle (green outline, black cap) draws itself in 0.45 s and fills
with pink liquid with a wobbling surface (0.15-1.4 s). It shakes, a damped rotation pivoting near
its base, on 0.5, 1.0 and 1.5 s. "SHAKE" stamps above it at 0.5 s and "WELL" below at 1.0 s
(16:9: left and right of the bottle). At 1.5 s the cap pops off, spins and flies out of frame.
BAR 2 (0:02-0:04) reFRESH
Hard cut to a deep green radial background. The letters F-R-E-S-H drop and slam one per eighth
note (2.0, 2.25, 2.5, 2.75, 3.0 s), each with a squash on landing. A pink brush "re" pops at the
top-left of the F at 3.0 s. The Sweetened and Vanilla bottles drop at 3.0 and 3.25 s and land
behind the F and the H; the F and H stay in front, so the bottles weave through the word. The
Strawberry bottle drops into the centre at 3.5 s and lands at 3.85 s, and cream teardrop
droplets burst out from the landing.
BAR 3 (0:04-0:06) FLOOD
A thick, glossy pink yoghurt wave rises from the bottom, covers the frame by 5.45 s, then
settles. It swallows the word and the side bottles, clipped at the wave's edge. The Strawberry
bottle lifts and rides the wave.
BAR 4 (0:06-0:08) SPLASH
Cut to a macro strawberry plunging into pink yoghurt. It hits on beat 2 (6.33 s), the crown
splash hangs in slow motion until 7.75 s, then settles. "PINK." stamps at 7.0 s and "THICK." at
7.5 s, top-left.
BAR 5 (0:08-0:10) THE SWITCH
The Strawberry bottle sits large in the centre on the pink surface. A butter-yellow vanilla wave
rises (8.0-9.7 s), and the bottle turns Vanilla exactly where the liquid crosses it. A
handwritten note, "watch the label", with an arrow points at the label (8.15-9.9 s).
BAR 6 (0:10-0:12) VANILLA
On the vanilla surface, a giant filled marquee "VANILLA · VANILLA ·" slides left behind the
bottle, and an outline marquee "SMOOTH · CREAMY ·" slides right below it. Eight vanilla pods and
white orchids fly upward past the bottle, some in front and some behind. The bottle sways about
7 degrees each way.
BAR 7 (0:12-0:14) MILK CURL
A milk-white wave curls in from the bottom-left (12.0-13.5 s) and swallows the marquees and
flowers. The bottle switches from Vanilla to Sweetened at the line. "THE ORIGINAL." stamps at
13.5 s.
BAR 8 (0:14-0:16) POUR
Cut to a thick ribbon of white yoghurt pouring and folding into a creamy pile, played at about
2.5x. The Sweetened bottle glides to the bottom-left. "JUST SWEET" stamps at 14.5 s and
"ENOUGH." at 15.0 s.
BAR 9 (0:16-0:18) REP YOUR FAVE
Hard cut to deep green. Three bottles drop and land one per beat (16.25, 16.75, 17.25 s):
Strawberry left, Vanilla centre (slightly larger), Sweetened right. Each landing bursts its
ingredients with gravity: strawberries, halves and slices; orchids and vanilla pods; mint
leaves. "REP YOUR FAVE" in Milk slams at 17.5 s.
BAR 10 (0:18-0:20) END CARD
A Milk-colored drip wipe slides down from the top (18.0-18.55 s). The brush logo "reFresh" with
a small leaf pops in at 18.55 s, "Shake well." rises at 18.95 s, then
"STRAWBERRY · VANILLA · SWEETENED" and "Drinking yoghurt by Integrated Dairies · Vom, Nigeria"
fade in at 19.15 s while three small bottles rise into a row underneath. The logo gives one last
squash at 19.55 s.
SOUND (effects only, synced to the picture)
- 0:00 Rising liquid glugs as the bottle fills; a slosh and a soft thump at 0.5 and 1.0 s; a
slosh and a bright cap pop at 1.5 s; a whoosh into the cut.
- 0:02 A firm stamp on every letter slam; a small pop for "re"; two bottle thuds at 3.38 and
3.63 s; a heavy thud, droplet splats and a low impact at 3.85 s.
- 0:04 A heavy liquid swell under the flood (low rush, churn, glugs); whooshes at 4.9 and 5.82 s.
- 0:06 A crown splash at 6.33 s (impact, liquid body, droplets falling back); stamps at 7.0 and
7.5 s.
- 0:08 A liquid swell under the vanilla wave; a shimmer at 8.95 s as the label flips.
- 0:10 A whoosh on every beat as the type and flowers rush past.
- 0:12 A liquid swell; a whoosh at 12.7 s; a stamp at 13.5 s.
- 0:14 A continuous thick pour with soft plops; stamps at 14.5 and 15.0 s; a whoosh into the cut.
- 0:16 A thud and splats on each bottle landing; an impact and a stamp at 17.5 s.
- 0:18 A soft watery slide under the drip wipe; a pop on the logo; a light stamp on
"Shake well."; a small shimmer; a final cap click at 19.55 s.
````

## Effects / 对应效果

*No directly embeddable result was found in the collected source. Follow the original source above. / 已采集来源中未发现可直接嵌入的效果，请打开上方原始来源。*
