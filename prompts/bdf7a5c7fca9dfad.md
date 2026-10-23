[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# Renaissance Naturalist Manuscript Style Video

**Category / 分类:** SVG 与动态图形  
**Text status / 文本状态:** Prompt marked complete by upstream; not independently reproduced  
**Origin / 收录方式:** Upstream structured prompt / post text

Project / 项目: [yihui-dev/awesome-opus5-5-videos](../projects/yihui-dev--awesome-opus5-5-videos.md)

Model labels in source / 来源模型标签: Claude / Opus

## Sources / 来源

- [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/92aee2f586ac0715cb3cbcb6384834f98a33383d/data/videos.json)
  - [Creator’s post / 作者原帖](https://x.com/wangyinrec/status/2103725737551532344)

**Source note / 来源备注:** prompt_partial=False

## Prompt / 提示词

````text
我定的选题、风格，我想要那种文艺复兴博物学家手稿的感觉，查资料、写分镜、写动画、作曲都是  Opus5.5 做的，画是 Codex 照着 Opus5.5 写的需求文档画的。  
唯一让我惊讶的是音乐。它先用 Python 写出一份 MIDI 乐谱，里面有和弦进行，也有两段主旋律：竖笛吹 Claude 的主题，钢片琴弹 GPT 那种绕圈的琶音。名字乱飞那段，羽管键琴的音是用随机走位生成的，每一小节更密一点、更不和谐一点，最后砸一个密集的不协和和弦，然后停住。快版一小节 2 秒，关键切换都卡在小节线上。  

然后用开源合成器 FluidSynth 加一套免费的标准音色库，把乐谱"演奏"成音频。鲁特琴、竖笛、管风琴这些音色都来自这套库。最后用 ffmpeg 统一响度、做淡出，再和画面合成。
````

## Effects / 对应效果

<img src="https://media.skillry.dev/opus-5-5/_prompts/wangyinrec-532344/poster.293b5377df.webp" alt="Original result poster" width="640" loading="lazy">

[Open image / 查看原图](https://media.skillry.dev/opus-5-5/_prompts/wangyinrec-532344/poster.293b5377df.webp)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*
