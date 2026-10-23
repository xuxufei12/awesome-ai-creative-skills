"""Validate catalogue references, generated files, unique IDs and publication hygiene."""
import collections, datetime, json, pathlib, re, sys, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
errors=[];checked_links=0
for kind in ['projects','skills','prompts','cases','guides','templates']:
 ids=[x['id'] for x in d[kind]]
 if len(ids)!=len(set(ids)):errors.append('Duplicate IDs in '+kind)
 for x in d[kind]:
  if not (ROOT/kind/(x['id']+'.md')).exists():errors.append('Missing detail: '+kind+'/'+x['id'])
  if not x.get('sources'):errors.append('Missing sources: '+kind+'/'+x['id'])
promptids={p['id'] for p in d['prompts']}
for c in d['cases']:
 if c.get('prompt_id') and c['prompt_id'] not in promptids:errors.append('Dangling prompt ID: '+c['id'])
for p in d['prompts']:
 if not p['text'].strip():errors.append('Empty prompt: '+p['id'])
for f in ROOT.rglob('*.md'):
 # Quoted prompts and Skills may contain arbitrary source links; validate catalogue navigation only.
 body=f.read_text(encoding='utf-8');body=re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$','',body)
 urls=re.findall(r'\]\(([^\s)]+)\)',body)+re.findall(r'\bhref="([^"]+)"',body)
 for u in urls:
  if re.match(r'^(?:https?://|mailto:|#)',u):continue
  target=urllib.parse.unquote(u.split('#')[0].split('?')[0])
  if not target:continue
  checked_links+=1
  p=(f.parent/target).resolve()
  if not p.is_relative_to(ROOT):errors.append('Escaping link: '+str(f.relative_to(ROOT))+' -> '+u)
  elif not p.exists():errors.append('Broken link: '+str(f.relative_to(ROOT))+' -> '+u)
for f in ROOT.rglob('*'):
 if not f.is_file() or '.git' in f.parts:continue
 if f.stat().st_size>90_000_000:errors.append('Oversized file: '+str(f.relative_to(ROOT)))
 if f.suffix in ['.json','.md','.py','.txt']:
  t=f.read_text(encoding='utf-8',errors='replace')
  if re.search(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)',t):errors.append('Potential secret: '+str(f.relative_to(ROOT)))
  # The catalogue must not disclose the supplied document's local storage path.
  if re.search(r'wxid_s72[a-z0-9]+|[A-Z]:[\\/]+wechat[\\/]+data',t,re.I):errors.append('Private workstation path: '+str(f.relative_to(ROOT)))
pdf=json.loads((ROOT/'data/pdf-merge.json').read_text(encoding='utf-8'))
if len(pdf['entries'])!=45:errors.append('Expected 45 PDF main-text entries')
appendix={s['url'].split('/prompts/')[-1] for p in d['prompts'] for s in p['sources'] if s.get('type')=='Also in supplied PDF appendix'}
if len(appendix)!=18:errors.append('Expected 18 PDF appendix prompt files; got '+str(len(appendix)))
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':{k:len(d[k]) for k in ['projects','skills','prompts','cases','guides','templates']},'local_links_checked':checked_links,'pdf_main_entries':len(pdf['entries']),'pdf_appendix_files':len(appendix),'errors':errors,'runtime_reproduction':False}
(ROOT/'data/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
txt='# Validation / 检查报告\n\n[Home / 首页](../README.md)\n\n'
txt+=f"Checked / 检查时间: {report['checked_at']}\n\n- Local navigation links checked / 已检查本地链接: **{checked_links}**\n- PDF main entries / PDF 正文条目: **{len(pdf['entries'])}**\n- Appendix prompt files / 附录提示词文件: **{len(appendix)}**\n- Structural / link / publication-hygiene errors: **{len(errors)}**\n\n"
txt+='| Record type | Count |\n|---|---:|\n'+''.join(f'| {k} | {v} |\n' for k,v in report['counts'].items())
txt+='\nSource and catalogue checks are distinct from running or reproducing upstream creative tools. No media quality or cross-model compatibility test is claimed. / 资料与目录检查不等于上游工具运行复现；未声称媒体质量或跨模型兼容性实测。\n'
if (ROOT/'data/media-checks.json').exists():txt+='\nSee [preview reachability checks / 效果链接可达性抽查](../data/media-checks.json).\n'
if errors:txt+='\n## Issues / 问题\n\n'+'\n'.join('- '+e for e in errors)
(ROOT/'docs/VALIDATION.md').write_text(txt,encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));sys.exit(bool(errors))
