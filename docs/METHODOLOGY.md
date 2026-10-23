# Methodology / 收录方法

[Home / 首页](../README.md)

## Scope / 范围

The initial snapshot merges a GitHub research collection from 2026-10-22 with a 45-page user-supplied PDF and the additional GitHub repositories referenced by that document. The project aims for broad coverage of creative Skills, prompts and effects. It does not claim to include everything on GitHub.

初始版本将 2026-10-22 的 GitHub 研究资料与用户提供的 45 页 PDF、PDF 新增仓库的公开资料合并。以广泛覆盖为目标，不宣称穷尽全网。

## Record types / 条目类型

| Type | Meaning / 含义 |
|---|---|
| Project | A source repository, including tools, engines, collections and Skill packs / 来源仓库，含工具、引擎、合集与技能包 |
| Skill | A unique collected SKILL.md text / 去重后的 SKILL.md 文本 |
| Prompt | Public prompt, style specification or explicitly labelled fragment/post text / 公开提示词、风格规格或已标注的片段／帖子文字 |
| Case | A work with an original-post reference; may have no prompt / 有原帖的作品，可能没有提示词 |
| Guide | A community workflow, translation or framework / 社区流程、编译教程或框架 |
| Template | An original synthesis prepared for this catalogue / 本次原创整理模板 |

Projects, Skills, prompts and cases overlap conceptually and must not be added together as a count of independent works. Some Skill packs include non-creative support Skills; these are retained with their parent project for completeness.

项目、Skill、提示词和案例可能互相关联，不能相加称为独立作品总数。技能包中部分支持性 Skill 并非直接创作技能，仍按所属项目保留。

## Deduplication / 去重

- Repositories: canonical GitHub owner/name; preserve redirects and aliases.
- Skills: SHA-256 of collected UTF-8 text; preserve all paths with identical text.
- Prompts: Unicode NFKC, whitespace removal and lowercase comparison; strip surrounding quote marks. Exact normalized matches share one entry. Similar wording, translations and semantically related variants remain separate.
- Cases: X/Twitter numeric status ID, otherwise source URL.
- PDF: restore readable CJK compatibility glyphs, preserve wording and original typos, attach page references. Separate workflows from complete prompts. The private extraction evidence retains the source transcription.

仓库按规范地址、Skill 按文本哈希、提示词按归一化正文、案例按原帖 ID 去重。近似文本保留，不凭主观判断删掉不同版本。PDF 修复排版字符，保留原词句和原有拼写错误。

## Sources and effects / 来源与效果

Where available, GitHub file links pin a commit. `data/source-files.json` records hashes, sizes and retrieval dates of archived text sources. This public repository contains the organized catalogue and relevant prompt/Skill text; it is not a wholesale mirror of every upstream codebase or a package that can install all Skills by itself.

Media references come from the same source record or Markdown section. Record-level mappings take precedence over generic project imagery. Some Markdown sections contain both reference inputs and generated outputs; the page warns about that. Project-level demos are not claimed as a distinct rendering for every Skill in a pack. Missing media is explicitly labelled.

尽可能固定 GitHub 提交，并保留来源文件哈希。公开仓库提供整理后的条目和相关正文，不是所有上游源码的完整镜像，也不是一键安装包。效果优先按同一结构化记录关联；Markdown 同一节可能同时含输入图与输出图。项目级示例不冒充包内每个 Skill 的独立效果。

## Verification boundary / 验证边界

Source collection, parsing, deduplication, local Markdown links and structural checks are performed. Selected public preview URLs are checked separately. A successful URL check proves reachability at that moment, not visual quality, permission, safety or reproducibility. Unavailable URLs stay linked with their provenance; no unrelated images are substituted.

No upstream Skill was installed or run to produce the listed effects. Model labels, costs, timing, quality scores and compatibility statements belong to source authors unless explicitly noted otherwise. PDF social-post claims were not independently audited. Star counts are dated snapshots, while the README Star History chart is external and dynamic.

已执行采集、解析、去重和结构检查；媒体链接的抽查另列。未逐个安装或运行上游 Skill，模型版本、成本、耗时和质量评分均不能当作本项目实测。Star 数是采集快照，首页趋势图为外部动态服务。

## Rebuild / 重建

```sh
python scripts/build.py
python scripts/validate.py
```

Both scripts use the Python standard library and operate only on this repository's data and generated documents. Upstream code is treated as quoted source material, not executed.
