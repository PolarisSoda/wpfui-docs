"""고정 버전 WPF-UI의 리소스 참조·스타일·템플릿 연결을 추출합니다.

python scripts/audit_customization.py --source C:/path/to/wpfui
이 결과는 참조 목록입니다. StaticResource를 인스턴스 Resources로 덮어쓸 수 있다는 뜻이 아닙니다.
"""
import argparse,collections,json,re,subprocess,xml.etree.ElementTree as ET
from pathlib import Path

P='{http://schemas.microsoft.com/winfx/2006/xaml/presentation}'
X='{http://schemas.microsoft.com/winfx/2006/xaml}'
SHA='153baadeaf475875a81a4605881ca5c2dbe53972'
def tag(e):return e.tag.split('}')[-1]
def typename(s):
    m=re.fullmatch(r'\{x:Type\s+([^}]+)\}',s or '')
    return m[1] if m else s
REF=re.compile(r'\{(DynamicResource|StaticResource)\s+([^{}]+)\}')

def run(source,repo):
    source=source.resolve()
    revision=subprocess.run(['git','-c','safe.directory='+source.as_posix(),'-C',str(source),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
    if revision!=SHA:raise SystemExit('Expected WPF UI 4.3.0 commit '+SHA+'; got '+revision)
    manifest=json.loads((repo/'source-manifest.json').read_text(encoding='utf-8'))
    pages={p['name']:p for p in manifest['pages']}
    defs=collections.defaultdict(list);docs=[];styles=[];templates=[]
    parents={};ownerinfo={};refs=[];bindings=[];fixed=[]
    for file in sorted((source/'src/Wpf.Ui').rglob('*.xaml')):
        root=ET.parse(file).getroot();rel=file.relative_to(source).as_posix();docs.append((rel,root))
        parents.update({child:e for e in root.iter() for child in e})
        for e in root.iter():
            key=e.get(X+'Key')
            if key:
                defs[key].append({'key':key,'type':tag(e),'value':(e.text or '').strip() if len(e)==0 else '', 'file':rel,'scope':'dictionary root' if parents.get(e) is root else 'nested resources','node':e})
            if tag(e) in ['Style','ControlTemplate','DataTemplate','ItemsPanelTemplate']:
                t=typename(e.get('TargetType',e.get('DataType','')))
                ownerinfo[e]={'target':t,'key':key,'kind':tag(e),'file':rel,'scope':'dictionary root' if parents.get(e) is root else 'nested resources','node':e}
                if tag(e)=='Style':styles.append(ownerinfo[e])
                elif tag(e)=='ControlTemplate':templates.append(ownerinfo[e])
        def context(e):
            chain=[];cur=e
            while cur is not None:
                chain.append(cur);cur=parents.get(cur)
            owner=next((ownerinfo[x] for x in chain if x in ownerinfo and ownerinfo[x]['target']),None)
            cond=[]
            for x in reversed(chain):
                if tag(x) in ['Trigger','DataTrigger']:
                    cond.append(x.get('Property',x.get('Binding','?'))+'='+x.get('Value','?'))
                elif tag(x)=='Condition':cond.append(x.get('Property','?')+'='+x.get('Value','?'))
            # MultiTrigger conditions are siblings, not ancestors of Setters.
            for x in chain:
                if tag(x) in ['MultiTrigger','MultiDataTrigger']:
                    cond.extend(c.get('Property',c.get('Binding','?'))+'='+c.get('Value','?') for c in x.iter() if tag(c)=='Condition')
            name=e.get(X+'Name',e.get('TargetName',''))
            where=tag(e)+('#'+name if name else '')
            if tag(e)=='Setter':where=e.get('TargetName','컨트롤')+'.'+e.get('Property','?')
            return owner,where,'; '.join(cond)
        for e in root.iter():
            owner,where,condition=context(e)
            for attr,value in e.attrib.items():
                if attr in [X+'Key',X+'Name']:continue
                for m in REF.finditer(value):
                    refs.append({'key':m[2].strip(),'lookup':m[1],'file':rel,'owner':owner['target'] if owner else '', 'style_or_template':owner['key'] if owner else None,'where':where+(' '+attr if tag(e)!='Setter' else ''),'condition':condition,'node':e})
                for m in re.finditer(r'\{TemplateBinding\s+([^},]+)',value):
                    bindings.append({'owner':owner['target'] if owner else '', 'file':rel,'target':where+'.'+attr,'property':m[1].strip(),'condition':condition,'kind':'TemplateBinding'})
                if '{Binding' in value and 'TemplatedParent' in value:
                    bm=re.search(r'\bPath=([\w.]+)',value)
                    if bm:bindings.append({'owner':owner['target'] if owner else '', 'file':rel,'target':where+'.'+attr,'property':bm[1],'condition':condition,'kind':'Binding to TemplatedParent'})
                prop=e.get('Property') if tag(e)=='Setter' and attr=='Value' else attr
                if owner and not value.startswith('{') and (prop in ['CornerRadius','Border.CornerRadius','BorderThickness','Padding','Margin','Width','Height','MinWidth','MinHeight','MaxWidth','MaxHeight','FontSize','Background','Foreground','RadiusX','RadiusY','StrokeThickness','Fill','Stroke']):
                    fixed.append({'owner':owner['target'],'file':rel,'style_or_template':owner['key'],'where':where+('.'+attr if tag(e)!='Setter' else ''),'property':prop,'value':value,'condition':condition,'node':e})
            if tag(e)=='Binding' and 'TemplatedParent' in e.get('RelativeSource',''):
                parent=parents.get(e);grand=parents.get(parent)
                where2=tag(grand) if grand is not None else '?'
                converter=parent.get('Converter','') if parent is not None else ''
                bindings.append({'owner':owner['target'] if owner else '', 'file':rel,'target':where2,'property':e.get('Path','?'),'condition':condition,'kind':'Binding / '+converter})

    def public(d):return {k:v for k,v in d.items() if k!='node'}
    def matches(target,name):
        p=pages[name]
        return target==('controls:'+name if p['kind']=='custom' else name)
    docmap=dict(docs)
    global_files=set()
    def load_merged(path):
        if path in global_files or path not in docmap:return
        global_files.add(path)
        root=docmap[path]
        for merged in root.findall(P+'ResourceDictionary.MergedDictionaries'):
            for d in merged:
                src=d.get('Source','')
                if ';component/' in src:child='src/Wpf.Ui/'+src.split(';component/',1)[1]
                else:child=(Path(path).parent/src).as_posix()
                load_merged(child)
    load_merged('src/Wpf.Ui/Resources/Wpf.Ui.xaml')
    # Build a resource graph from globally imported implicit styles.
    def reachable(name):
        roots=[s['node'] for s in styles if matches(s['target'],name) and not s['key'] and s['scope']=='dictionary root' and s['file'] in global_files]
        seen=set();nodes=set();todo=list(roots)
        while todo:
            root=todo.pop()
            if root in seen:continue
            seen.add(root);nodes.update(root.iter())
            for e in root.iter():
                for v in e.attrib.values():
                    for m in REF.finditer(v):
                        for d in defs.get(m[2].strip(),[]):
                            if d['type'] in ['Style','ControlTemplate','ItemsPanelTemplate','DataTemplate']:todo.append(d['node'])
        return nodes
    result={'upstream':manifest['upstream'],'scope':'Wpf.Ui XAML resources; direct references grouped by owning Style/ControlTemplate plus defining control files','controls':[],'definitions':{k:[public(d) for d in v] for k,v in sorted(defs.items())}}
    for name,p in sorted(pages.items()):
        files=set(p['source_files'])
        active=reachable(name)
        direct=[r for r in refs if matches(r['owner'],name)]
        # Include helper templates defined in this control's source files, but label owners.
        nearby=[r for r in refs if r['file'] in files and r not in direct]
        rs=direct+nearby
        grouped=[]
        for key in sorted(set(r['key'] for r in rs)):
            uses=[r for r in rs if r['key']==key]
            grouped.append({'key':key,'definitions':[public(d) for d in defs.get(key,[])], 'uses':[dict(public(r),in_default_graph=r['node'] in active) for r in uses]})
        # Explicitly show styles/templates for this target, including non-default variants.
        ss=[public(s) for s in styles if matches(s['target'],name)]
        ts=[public(t) for t in templates if matches(t['target'],name)]
        bs=[b for b in bindings if matches(b['owner'],name)]
        fs=[public(f) for f in fixed if matches(f['owner'],name)]
        # CLR resource reads may use application resources and cannot be overridden locally.
        clr=[]
        for f in files:
            if not f.endswith('.cs'):continue
            code=(source/f).read_text(encoding='utf-8-sig')
            for i,line in enumerate(code.splitlines(),1):
                for m in re.finditer(r'(?:Resources\[|FindResource\(|SetResourceReference\([^,]+,)\s*"([^"]+)"',line):clr.append({'key':m[1],'file':f,'line':i,'code':line.strip()})
        parts=[]
        for f in files:
            if not f.endswith('.cs'):continue
            cs=(source/f).read_text(encoding='utf-8-sig')
            parts.extend({'name':n,'file':f} for n in sorted(set(re.findall(r'"(PART_[\w]+)"',cs))))
        xaml_parts=[]
        for t in templates:
            if not matches(t['target'],name):continue
            for e in t['node'].iter():
                part=e.get(X+'Name','')
                if part.startswith('PART_'):xaml_parts.append({'name':part,'type':tag(e),'file':t['file'],'template':t['key']})
        result['controls'].append({'name':name,'resources':grouped,'styles':ss,'templates':ts,'template_bindings':bs,'fixed_values':fs,'clr_resources':clr,'parts':parts,'xaml_parts':xaml_parts})
    (repo/'customization-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Controls:',len(result['controls']),'keys:',len(defs),'references:',len(refs),'template bindings:',len(bindings),'fixed layout/state values:',len(fixed))
    for c in result['controls']:
        dynamic=[r['key'] for r in c['resources'] if any(u['lookup']=='DynamicResource' and u['in_default_graph'] for u in r['uses'])]
        print(c['name']+': '+', '.join(dynamic[:9])+' | '+str(len(c['resources']))+' keys; '+str(len(c['styles']))+' styles; '+str(len(c['fixed_values']))+' fixed')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);args=ap.parse_args()
    run(args.source,Path(__file__).resolve().parents[1])
