# Contributing / 参与贡献

Add interesting, actionable creative Skills, prompts, workflows and examples. Videos, image generation, motion design, 3D, shaders, games, sound and emerging creative media are welcome.

欢迎补充有趣、可学习或可复用的创意 Skill、Prompt、工作流与作品，范围包括视频、图像、动效、三维、着色器、游戏和声音。

## Required information / 必填内容

1. Project or prompt name and category / 名称与类别。
2. Creator's original source, plus the collection source if different / 作者原始来源与聚合来源分别提供。
3. Exact public prompt or Skill text when available; mark excerpts, translations and missing text / 标明完整原文、片段、翻译或未公开。
4. A corresponding result image, video or demo URL. Do not substitute an unrelated example / 对应效果链接，不能用无关示例代替。
5. License, dependencies, model/agent used and evidence / 许可、依赖、模型或代理及依据。
6. State whether you reproduced it; include settings and result links if so / 标明是否亲自复现。

## Edit & validate / 修改与检查

The source of truth is `data/catalog.json`. Add or update a record there, then regenerate the Markdown:

```sh
python scripts/build.py
python scripts/validate.py
```

Use a stable ID. Compare repository canonical URLs, normalized prompt text and original post IDs before adding duplicates. Preserve all attributions when merging. Do not silently translate or rewrite an original prompt. Generated detail pages should not be edited by hand.

先比较仓库规范地址、提示词归一化正文和原帖 ID；合并重复项时保留所有出处。不要静默翻译或改写原始提示词。详情页由脚本生成，请修改结构化数据。
