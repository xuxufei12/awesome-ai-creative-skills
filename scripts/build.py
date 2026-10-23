"""Build the bilingual Markdown catalogue from data/catalog.json. Standard library only."""
import collections, html, json, pathlib, re, urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
generated=[]
def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8');generated.append(path)
def esc(s):return str(s or '').replace('|','&#124;').replace('\n',' ').replace('[','&#91;').replace(']','&#93;')
def code(text):
 fence='`'*max(4,1+max([len(s) for s in re.findall(r'`+',text)] or [0]))
 return fence+'text\n'+text.rstrip()+'\n'+fence+'\n'
def sources(items):
 out=[]
 for s in items:
  u=s.get('url') or s.get('original_url');label=s.get('repo') or s.get('type') or 'Original source / 原始来源'
  if u:out.append(f'- [{esc(label)}]({u})')
  if s.get('original_url') and s['original_url']!=u:out.append(f"  - [Creator’s post / 作者原帖]({s['original_url']})")
  if s.get('pages'):out.append(f"  - PDF: `opus-deepseek-video-prompts.pdf`, pp. {', '.join(map(str,s['pages']))}; original post not independently verified / 未独立核验原帖。")
 return '\n'.join(out) or '- Source pending / 来源待补充'
def preview(assets,limit=None):
 a=assets[:limit] if limit else assets
 if not a:return '*No directly embeddable result was found in the collected source. Follow the original source above. / 已采集来源中未发现可直接嵌入的效果，请打开上方原始来源。*\n'
 chunks=[]
 for x in a:
  u=x['url'];label=esc(x.get('label','Upstream example'))
  if x['type']=='image':chunks.append(f'<img src="{html.escape(u,quote=True)}" alt="{html.escape(label,quote=True)}" width="640" loading="lazy">\n\n[Open image / 查看原图]({u})')
  elif x['type']=='video':chunks.append(f'[▶ Watch video / 播放视频]({u})\n\n{u}')
  else:chunks.append(f'[↗ {label}]({u})')
 return '\n\n'.join(chunks)+'\n\n*Upstream examples, not generated or reproduced by this catalogue. Some sections include input/reference images. / 上游示例，本项目未复现；部分示例同时含输入参考图。*\n'
categories=[('教学科普与手绘','education','Education & hand-drawn explainers'),('剪辑字幕与数字人','editing','Editing, captions & avatars'),('叙事动画与音乐视频','storytelling','Storytelling, animation & music videos'),('视频框架与程序化成片','video-frameworks','Video frameworks & code rendering'),('广告与产品演示','product-videos','Ads & product demos'),('SVG 与动态图形','motion-graphics','SVG & motion graphics'),('提示词与导演方法','directing','Prompts & directing'),('Blender 与三维建模','blender','Blender & 3D modelling'),('Three.js 与 WebGPU','web-3d','Three.js & WebGPU'),('图像生成与商业视觉','image-generation','Image generation & visual design'),('合集与创作案例','collections','Collections & inspiration'),('ComfyUI 与模型编排','comfyui','ComfyUI & model workflows'),('游戏资产与像素画','game-assets','Game assets & pixel art'),('高斯泼溅与仿真','simulation','Gaussian splatting & simulation')]
catmap={c:(s,e) for c,s,e in categories}
projects=DATA['projects'];prompts=DATA['prompts'];skills=DATA['skills'];cases=DATA['cases'];guides=DATA['guides'];templates=DATA['templates']
rmap={r['repo'].lower():r for r in projects}
for r in projects:
 for a in r['aliases']:rmap[a.lower()]=r
def projectlink(repo,prefix='../'):
 r=rmap.get((repo or '').lower())
 return f"[{esc(repo)}]({prefix}projects/{r['id']}.md)" if r else 'PDF / community source'
def related(items,repo):return [p for p in items if (p.get('repo') or '').lower()==repo.lower() or any((s.get('repo') or '').lower()==repo.lower() for s in p.get('sources',[]))]
def backlink():return '[Home / 首页](../README.md) · [中文](../README.zh-CN.md) · [Full catalogue / 完整目录](../catalog/README.md)\n\n'
for r in projects:
 ps=related(prompts,r['repo']);ss=related(skills,r['repo']);cs=related(cases,r['repo'])
 text=backlink()+f"# {r['repo']}\n\n{r['summary']}\n\n"
 text+='| Field / 字段 | Value / 内容 |\n|---|---|\n'
 for k,v in [('Category / 分类',r['category']),('Type / 类型',r['type']),('Hosts mentioned / 提及宿主',', '.join(r['hosts'])),('Source status / 来源状态',r['status']),('Stars at snapshot / 采集时 Stars',r['stars']),('Snapshot / 来源快照',r['checked_at']),('Pinned commit / 固定提交',r['commit'] or 'Unavailable'),('Upstream license / 上游许可证',r['license']),('Archived upstream / 上游归档','Yes' if r['archived'] else 'No')]:text+=f'| {k} | {esc(v)} |\n'
 text+=f"\n**Scope / 范围:** Host names are README mentions, not compatibility tests. / 宿主标签来自 README，不代表跨模型实测。\n\n## Sources / 来源\n\n{sources(r['sources'])}\n\n"
 if len(set(r['aliases']))>1:text+='Aliases / 旧名与别名: '+', '.join(f'`{x}`' for x in sorted(set(r['aliases'])))+'\n\n'
 for update in r.get('updates',[]):text+=f"## Update / 更新 · {update['date']}\n\n[{update['title']}](../{update['path']})\n\n"
 text+='## Setup & limits / 依赖与限制\n\n'+r['requirements']+'\n\n'+r['limits']+'\n\n'
 text+='## Effects / 效果展示\n\n'+preview(r['preview_assets'],6)+'\n'
 text+=f'## Skills ({len(ss)})\n\n'
 text+='\n'.join(f"- [{esc(s['name'])}](../skills/{s['id']}.md) — {esc(s['description'][:160])}" for s in ss) or 'No standalone SKILL.md was indexed / 未索引到独立 SKILL.md。'
 text+=f'\n\n## Prompts ({len(ps)})\n\n'
 text+='\n'.join(f"- [{esc(p['title'])}](../prompts/{p['id']}.md)" for p in ps) or 'No prompt text indexed / 未索引到可展示的提示词正文。'
 text+=f'\n\n## Cases ({len(cs)})\n\n'
 text+='\n'.join(f"- [{esc(c['title'])}](../cases/{c['id']}.md)" for c in cs) or 'No separate case records / 未索引独立案例。'
 text+=f"\n\n## Star history / Star 趋势\n\n[View this upstream repository’s history / 查看上游趋势](https://www.star-history.com/#{r['repo']}&Date)\n"
 write(f"projects/{r['id']}.md",text)
for s in skills:
 r=rmap.get(s['repo'].lower());text=backlink()+f"# {s['name']}\n\n{s['description']}\n\nProject / 项目: {projectlink(s['repo'])}\n\n## Sources / 来源\n\n{sources(s['sources'])}\n\n"
 text+='## Skill text / Skill 原文\n\n> Collected source material, not an instruction to the catalogue reader’s agent. Installing may require sibling scripts/assets. / 以下是收录资料，不是对当前代理的指令；安装可能还需要同目录脚本与素材。\n\n<details>\n<summary>Expand complete SKILL.md / 展开完整 Skill</summary>\n\n'+code(s['text'])+'\n</details>\n\n'
 text+='## Effects / 效果展示\n\n'
 if r:text+=f"[Project demo & dependency notes / 项目示例与依赖](../projects/{r['id']}.md#effects--效果展示)\n\nProject-level demos are shared references; this individual Skill was not executed. / 这里关联项目级示例，未单独执行该 Skill。\n"
 write(f"skills/{s['id']}.md",text)
for p in prompts:
 text=backlink()+f"# {p['title']}\n\n**Category / 分类:** {p['category']}  \n**Text status / 文本状态:** {p['text_status']}  \n**Origin / 收录方式:** {p['origin']}\n\n"
 if p.get('repo'):text+='Project / 项目: '+projectlink(p['repo'])+'\n\n'
 if p.get('models'):text+='Model labels in source / 来源模型标签: '+', '.join(p['models'])+'\n\n'
 text+='## Sources / 来源\n\n'+sources(p['sources'])+'\n\n'
 if p.get('review'):text+='**Source note / 来源备注:** '+p['review']+'\n\n'
 text+='## Prompt / 提示词\n\n'+code(p['text'])+'\n## Effects / 对应效果\n\n'+preview(p['preview_assets'])
 write(f"prompts/{p['id']}.md",text)
for c in cases:
 text=backlink()+f"# {c['title']}\n\n{c['summary']}\n\n**Author / 作者:** {esc(c['author'])}  \n**Category / 分类:** {c['category']}  \n**Prompt status / 提示词状态:** {c['prompt_status']}\n\n## Sources / 来源\n\n{sources(c['sources'])}\n\n[Original post / 原帖]({c['source']})\n\n"
 if c.get('prompt_id'):text+=f"## Prompt / 提示词\n\n[Open text / 展开正文](../prompts/{c['prompt_id']}.md)\n\n"
 else:text+='## Prompt / 提示词\n\nNo complete public prompt was collected for this case. / 此案例未采集到完整公开提示词。\n\n'
 text+='## Effects / 对应效果\n\n'+preview(c['preview_assets'])
 write(f"cases/{c['id']}.md",text)
for g in guides:
 write(f"guides/{g['id']}.md",backlink()+f"# {g['title']}\n\n{g['summary']}\n\n**{g['text_status']}**\n\n## Sources / 来源\n\n{sources(g['sources'])}\n\n## Collected text / 收录正文\n\n"+code(g['text']))
for t in templates:
 write(f"templates/{t['id']}.md",backlink()+f"# {t['title']}\n\n**Original synthesis by this catalogue, not a quotation from GitHub or a tested result. / 本次原创整理，不是 GitHub 原文，也不是实测结果。**\n\n"+code(t['text'])+'\n## Related sources / 相关来源\n\n'+'\n'.join('- '+projectlink(r) for r in t['sources']))

# Compact navigational pages; every item has a stable detail page.
category_counts=[]
for cat,slug,en in categories:
 rs=[r for r in projects if r['category']==cat];category_counts.append((cat,slug,en,len(rs)))
 text=f'[All categories / 全部分类](README.md)\n\n# {en} / {cat}\n\n| Project / 项目 | Description / 简介 | Skills | Prompts |\n|---|---|---:|---:|\n'
 for r in sorted(rs,key=lambda r:(not r['curated'],r['repo'].lower())):text+=f"| [{esc(r['repo'])}](../projects/{r['id']}.md) | {esc(r['summary'][:220])} | {len(related(skills,r['repo']))} | {len(related(prompts,r['repo']))} |\n"
 write(f'catalog/{slug}.md',text)
def paginated_index(items,kind,title,labelfield):
 text=f'[Home / 首页](../../README.md)\n\n# {title}\n\n{len(items)} records / 条记录。每条提供独立详情和来源。\n\n'
 pages=[]
 for offset in range(0,len(items),80):
  num=offset//80+1;path=f'catalog/{kind}/page-{num:02}.md';pages.append(path)
  page=f'[Index / 索引](README.md) · [Home / 首页](../../README.md)\n\n# {title} · {num}\n\n| Entry / 条目 | Category / 分类 | Source / 来源 |\n|---|---|---|\n'
  for x in items[offset:offset+80]:page+=f"| [{esc(x[labelfield])}](../../{kind}/{x['id']}.md) | {esc(x['category'])} | {esc(x.get('repo') or 'PDF / community')} |\n"
  page+='\n'+' · '.join(f'[Page {n+1}](page-{n+1:02}.md)' for n in range((len(items)+79)//80))+'\n';write(path,page)
  text+=f'- [Page {num} · {offset+1}–{min(offset+80,len(items))}](page-{num:02}.md)\n'
 write(f'catalog/{kind}/README.md',text)
paginated_index(sorted(prompts,key=lambda p:(p['category'],p['title'])),'prompts','Prompts & style recipes / 提示词与风格配方','title')
paginated_index(sorted(skills,key=lambda s:(s['category'],s['name'])),'skills','Skills / 技能','name')
paginated_index(sorted(cases,key=lambda c:(c['category'],c['title'])),'cases','Cases & effects / 案例与效果','title')
write('catalog/guides.md','[Home / 首页](../README.md)\n\n# Workflows & original templates / 工作流与原创模板\n\n## Community workflows / 社区流程\n\n'+'\n'.join(f"- [{esc(g['title'])}](../guides/{g['id']}.md)" for g in guides)+'\n\n## Original synthesis / 原创整理模板\n\n'+'\n'.join(f"- [{esc(t['title'])}](../templates/{t['id']}.md)" for t in templates))
write('catalog/README.md','[English home](../README.md) · [中文首页](../README.zh-CN.md)\n\n# Complete catalogue / 完整目录\n\n'+'\n'.join(f'- [{en} / {cn}]({s}.md) — {n}' for cn,s,en,n in category_counts)+'\n\n## Browse by record type / 按记录类型\n\n- [Prompts / 提示词](prompts/README.md)\n- [Skills / 技能](skills/README.md)\n- [Cases / 案例](cases/README.md)\n- [Workflows & templates / 工作流与模板](guides.md)\n- [PDF merge / PDF 合并记录](../docs/PDF-MERGE.md)\n- [Source file manifest / 来源文件清单](../data/source-files.json)')

featured_names=['alchaincyf/huashu-motion','alchaincyf/huashu-art-motion','Kianzzz/xilo-opus-video','threerocks/sweety-handdraw-video','remotion-dev/skills','heygen-com/hyperframes','lemomo-ai/lemo-opuscar','cth9191/animate','op7418/guizang-product-video-skill','dexhunter/seedance2-skill','eternityspring/shuohao-skills','ahujasid/mcp-for-blender','MCKRUZ/ComfyUI-Expert','yihui-dev/awesome-opus5-5-videos','joeseesun/opus-video-prompts','Vincentwei1021/mg-styles-15']
featured=[rmap[n.lower()] for n in featured_names if n.lower() in rmap]
gallery=json.loads((ROOT/'data/featured-gallery.json').read_text(encoding='utf-8'))
promptmap={p['id']:p for p in prompts}
def featured_update(zh):
 path=ROOT/'data/featured-update.json'
 if not path.exists():return ''
 f=json.loads(path.read_text(encoding='utf-8'))
 text='## '+('新玩法 · 把喜欢的风格，变成自己的' if zh else 'New · Make a style your own')+'\n\n'
 text+=('Lemo-Opuscar 已更新到 **59 种影片风格**，新增 **8 种剪辑与纪实**。还可以改编现有风格，或从空白设计一套自己的视觉语言，确认后保存，接着用来做下一支片。' if zh else 'Lemo-Opuscar now offers **59 film styles**, including **8 new editing and documentary styles**. Adapt a library style or design your own, preview it, and save it for your next film.')+'\n\n'
 text+=('下面是作者的改编示例。保留瑞士风格的网格、节拍和排版，把平面图形变成黏土、毛毡、玻璃和镀铬物件。**俯视是一张海报，镜头一转，就是一个立体世界。**' if zh else 'The creator’s example keeps the Swiss grid, beat and typography, turning flat shapes into clay, felt, glass and chrome objects. **From above it reads as a poster; tilt the camera and it becomes a 3D world.**')+'\n\n'
 text+='<table>\n<tr>\n'
 for image,video,label in [(f['before'],f['before_video'],'原风格 · Swiss Motion' if zh else 'Original · Swiss Motion'),(f['after'],f['after_video'],'我的风格 · Material Grid · 31 秒' if zh else 'Custom · Material Grid · 31 seconds')]:
  text+=f'<td width="50%" align="center" valign="top"><a href="{video}"><img src="{image}" width="480" alt="{label}"></a><br><a href="{video}"><b>▶ {label}</b></a></td>\n'
 text+='</tr>\n</table>\n\n'
 text+=f"[{'制作流程与更新说明' if zh else 'Workflow & update notes'}]({f['detail_path']}) · [{'自定义风格完整指令' if zh else 'Complete custom-style instructions'}](prompts/{f['custom_workflow_prompt_id']}.md) · [{'作者原帖' if zh else 'Creator’s announcement'}]({f['source_post']})\n\n"
 text+='### '+('8 种新风格，点图看片' if zh else '8 new styles · click a frame to watch')+'\n\n<table>\n'
 for i,s in enumerate(f['added_styles']):
  if i%3==0:text+='<tr>\n'
  label=s['title_zh' if zh else 'title_en']
  text+=f'<td width="33%" align="center" valign="top"><a href="{s["video"]}"><img src="{s["image"]}" width="300" alt="{html.escape(label)}"></a><br><b>{html.escape(label)}</b><br><sub><a href="{s["video"]}">▶ {"样片" if zh else "Film"}</a> · <a href="prompts/{s["prompt_id"]}.md">{"风格提示词" if zh else "Style prompt"}</a></sub></td>\n'
  if i%3==2 or i==len(f['added_styles'])-1:text+='</tr>\n'
 text+='</table>\n\n'
 text+=f"<sub>{'示例与画面' if zh else 'Films & frames'} © LemoLab / Lemomo · CC BY 4.0 · <a href=\"https://github.com/{f['upstream_repo']}\">lemo-opuscar</a></sub>\n\n"
 return text
for zh,name in [(False,'README.md'),(True,'README.zh-CN.md')]:
 text='![awesome-ai-creative-skills — Curated skills & prompts for AI image and video generation](assets/banner.png)\n\n# Awesome AI Creative Skills\n\n'
 text+='[English](README.md) · [简体中文](README.zh-CN.md)\n\n'
 text+='> '+('把想法变成视频、图像、动效和三维世界的 Skill、Prompt、工具与作品资料库。' if zh else 'Skills, prompts, tools and examples that turn ideas into videos, images, motion graphics and 3D worlds.')+'\n\n'
 text+='[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Stars](https://img.shields.io/github/stars/'+DATA['repository']+'?style=flat)](https://github.com/'+DATA['repository']+'/stargazers)\n\n'
 text+=('这里收录了一些用 AI 制作创意图片、视频、动效和 3D 场景的方法，包括可直接参考的提示词、可复用的 Skill，以及对应的作品效果。从一张有趣的图片到一段完整的动画，希望你能在这里找到灵感，也找到动手创作的起点。' if zh else 'Explore ways to create imaginative images, videos, motion graphics and 3D scenes with AI. This collection brings together prompts, reusable Skills and examples of what they can make—from a playful image to a complete animation, with inspiration and practical starting points for your own creations.')+'\n\n'
 text+=f"**{'资料快照' if zh else 'Snapshot'}: {DATA['snapshot_date']}** · **{len(projects)}** {'项目' if zh else 'projects'} · **{len(skills)}** Skills · **{len(prompts)}** {'提示词／风格文本' if zh else 'prompt / style texts'} · **{len(cases)}** {'案例' if zh else 'cases'}\n\n"
 text+=featured_update(zh)
 text+='## '+('开始浏览' if zh else 'Explore')+'\n\n'
 text+='| '+('入口 | 内容' if zh else 'Entry | Contents')+' |\n|---|---|\n'
 links=[('完整分类目录','Complete catalogue','catalog/README.md','14 个创作方向','14 creative categories'),('提示词正文','Prompt text','catalog/prompts/README.md','可复制正文、来源与对应效果','Copyable text, sources and corresponding effects'),('Skill 原文','Skill text','catalog/skills/README.md','独立 Skill 页面与上游安装依赖','Individual Skill pages and upstream dependencies'),('案例与效果','Cases & effects','catalog/cases/README.md','预览图、视频与公开提示词状态','Posters, videos and prompt availability'),('工作流与原创模板','Workflows & templates','catalog/guides.md','社区教程与原创模板分别标注','Community guides distinguished from original templates'),('PDF 合并记录','PDF merge report','docs/PDF-MERGE.md','页码、去重映射与新增仓库','Page references, deduplication and added repositories')]
 for cn,en,url,cnd,end in links:text+=f'| [{cn if zh else en}]({url}) | {cnd if zh else end} |\n'
 text+='\n## '+('效果画廊' if zh else 'Effect gallery')+'\n\n'
 text+=('先看看这些创意能做成什么样。点击图片或标题，查看提示词、制作方法和作者来源；视频案例的详情页还提供播放入口。' if zh else 'See what these ideas can become. Open an image or title for its prompt, creative method and creator credits. Video entries also link to the films.')+'\n\n'
 for group in gallery:
  text+='### '+group['title_zh' if zh else 'title_en']+'\n\n<table>\n'
  for i,item in enumerate(group['items']):
   if i%3==0:text+='<tr>\n'
   p=promptmap[item['prompt_id']];a=next(a for a in p['preview_assets'] if a['type']=='image');label=item['title_zh' if zh else 'title_en'];target=f"prompts/{p['id']}.md"
   text+=f'<td width="33%" valign="top" align="center"><a href="{target}"><img src="{html.escape(a["url"],quote=True)}" width="300" alt="{html.escape(label,quote=True)}"></a><br><a href="{target}"><b>{html.escape(label)}</b></a><br><sub><a href="{html.escape(p["sources"][0]["url"],quote=True)}">{html.escape(p["repo"])}</a></sub></td>\n'
   if i%3==2 or i==len(group['items'])-1:text+='</tr>\n'
  text+='</table>\n\n'
 text+='## '+('重点项目' if zh else 'Featured projects')+'\n\n| Project | '+('方向' if zh else 'Category')+' |\n|---|---|\n'
 for r in featured:
  label=r['category'] if zh else catmap.get(r['category'],('',r['category']))[1]
  text+=f"| [{r['repo']}](projects/{r['id']}.md) | {label} |\n"
 text+='\n## '+('按方向查找' if zh else 'Browse by category')+'\n\n| '+('方向 | 项目数' if zh else 'Category | Projects')+' |\n|---|---:|\n'
 for cn,s,en,n in category_counts:text+=f'| [{cn if zh else en}](catalog/{s}.md) | {n} |\n'
 text+='\n## '+('如何使用' if zh else 'How to use')+'\n\n'
 text+=('1. 先按用途选项目，再打开对应的 Skill 或提示词。\n2. 核对原始来源、许可证、依赖和输入素材；宿主标签只表示来源提及。\n3. 先做静帧或 5–10 秒小样，再扩大到完整作品。\n4. 作品效果属于上游作者；缺少公开正文、效果或复现证据的条目会明确说明。\n' if zh else '1. Pick a category, then open a project, Skill or prompt.\n2. Check the original source, license, dependencies and required inputs. Host labels reflect upstream mentions only.\n3. Start with still frames or a 5–10 second draft before rendering a complete piece.\n4. Results belong to upstream creators. Missing text, media or reproduction evidence is explicitly labelled.\n')
 text+='\n## '+('来源与维护' if zh else 'Sources & maintenance')+'\n\n'
 text+='- [Methodology / 收录方法](docs/METHODOLOGY.md)\n- [Attribution & licenses / 来源与许可](THIRD_PARTY_NOTICES.md)\n- [Contribute / 参与贡献](CONTRIBUTING.md)\n- [Machine-readable catalogue / 结构化数据](data/catalog.json)\n- [Validation report / 检查报告](docs/VALIDATION.md)\n\n'
 text+='## Star History / Star 趋势\n\n'
 text+=f'[![Star History Chart](https://api.star-history.com/svg?repos={DATA["repository"]}&type=Date)](https://www.star-history.com/#{DATA["repository"]}&Date)\n\n'
 text+=('新仓库需要积累 Star 后才会形成曲线；图表由 Star History 动态提供。项目详情页也有各上游仓库的趋势入口。' if zh else 'A new repository needs stars before a meaningful curve appears. The chart is served dynamically by Star History. Each project page also links to its upstream star history.')+'\n'
 write(name,text)

pdf=json.loads((ROOT/'data/pdf-merge.json').read_text(encoding='utf-8'))
text='# PDF merge / PDF 合并记录\n\n[Home / 首页](../README.md)\n\n'
text+=f"Source document / 来源文档: `opus-deepseek-video-prompts.pdf` · {pdf['page_count']} pages  \nSHA-256: `{pdf['sha256']}`\n\n"
text+='The supplied PDF is not redistributed. Its public links, relevant prompt text and page references are merged here. / 不上传原 PDF，仅合并相关提示词、公开链接和页码。\n\nPDF cost, model-version and performance statements remain attributed community claims. They are not independent measurements by this project. / PDF 的价格、版本与性能说法属于来源陈述，未作为本项目实测结论。\n\n## Repository references / 仓库对照\n\n| Repository | Merge / 合并 |\n|---|---|\n'
for r in pdf['repository_references']:text+=f"| {projectlink(r['repo'])} | {'Already indexed / 已有，合并来源' if r['existing'] else 'Added / 新增'} |\n"
text+='\n## Main-text entries / 正文条目\n\n| Pages / 页码 | Entry / 条目 | Type / 类型 | Text / 正文 |\n|---|---|---|---|\n'
for e in pdf['entries']:
 links=[f"[Prompt {i+1}](../prompts/{pid}.md)" for i,pid in enumerate(e['prompt_ids'])]
 if e['guide_id']:links.append(f"[Guide](../guides/{e['guide_id']}.md)")
 text+=f"| {', '.join(map(str,e['pages']))} | [{esc(e['title'])}]({e['source']}) | {e['kind']} | {' / '.join(links) or 'No complete prompt / 未公开完整提示词'} |\n"
text+='\n## Appendix / 附录\n\nThe 18 prompts on pages 33–41 are indexed from the pinned files in [joeseesun/opus-video-prompts](../projects/joeseesun--opus-video-prompts.md). Identical text is merged while retaining source aliases. / 第 33–41 页的 18 份提示词优先按固定提交的上游文件收录；相同正文保留一个条目并合并来源。\n\n## Other catalogues / 补充索引\n\n'
text+='\n'.join(f"- [{s['name']}]({s['url']}) — {s['verification']}" for s in DATA['external_catalogues'])
text+='\n\n## PDF bibliography / PDF 原帖索引\n\n'+'\n'.join(f"- [{s['url']}]({s['url']}) — p. {s['pages'][0]}" for s in DATA['pdf_bibliography'])
write('docs/PDF-MERGE.md',text)
stats={k:len(DATA[k]) for k in ['projects','skills','prompts','cases','guides','templates']}
stats.update({'prompt_records_with_media':sum(bool(p['preview_assets']) for p in prompts),'case_records_with_media':sum(bool(c['preview_assets']) for c in cases),'project_records_with_media':sum(bool(r['preview_assets']) for r in projects),'snapshot_date':DATA['snapshot_date']})
write('data/statistics.json',json.dumps(stats,ensure_ascii=False,indent=2))
write('data/generated-files.json',json.dumps(generated,ensure_ascii=False,indent=2))
print(json.dumps(stats,ensure_ascii=False))
