[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)

# Remotion Product Demo

**Category / 分类:** SVG 与动态图形  
**Text status / 文本状态:** Prompt marked complete by upstream; not independently reproduced  
**Origin / 收录方式:** Upstream structured prompt / post text

Project / 项目: [yihui-dev/awesome-opus5-5-videos](../projects/yihui-dev--awesome-opus5-5-videos.md)

Model labels in source / 来源模型标签: Claude / Opus

## Sources / 来源

- [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/92aee2f586ac0715cb3cbcb6384834f98a33383d/data/videos.json)
  - [Creator’s post / 作者原帖](https://x.com/qianqiongge/status/2105902139902246969)

**Source note / 来源备注:** prompt_partial=False

## Prompt / 提示词

````text
请在当前项目做一支 15 秒的产品使用说明视频，使用 Remotion，竖版 1080×1920、30fps、共 450 帧。只用 assets 目录里提供的商品图和我给出的事实，不下载陌生素材，不补销售数据。

第 0 至 3 秒展示商品与一句使用场景。第 3 至 9 秒演示两步操作，每步只出现一个动作。第 9 至 13 秒展示结果，并保留能看清的停留时间。最后 2 秒显示产品名称，不加购买引导。

先列分镜与素材缺口，再做预览。字幕单独排版，动效以当前帧号计算。不要用真实时钟驱动时间线，也不要使用不固定的随机数。商品、文字、镜头时间分别配置，方便以后替换。

交付可编辑项目、启动与渲染命令、MP4，以及第 1、5、10、14 秒的静帧。缺少必要素材时停止并说明，不用假素材代替。”
````

## Effects / 对应效果

<img src="https://media.skillry.dev/opus-5-5/_prompts/qianqiongge-246969/poster.32f18ca94d.webp" alt="Original result poster" width="640" loading="lazy">

[Open image / 查看原图](https://media.skillry.dev/opus-5-5/_prompts/qianqiongge-246969/poster.32f18ca94d.webp)

*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*
