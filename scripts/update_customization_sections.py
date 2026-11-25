"""customization-manifest.json과 확인한 예제로 105개 문서의 조정 안내를 갱신합니다.

원본 조사는 audit_customization.py로 먼저 실행합니다. 기존 본문·고유 속성 설명은 유지합니다.
"""
import collections,json,re
from pathlib import Path
from customization_recipes import NOTES,EXTRA

ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/'
BEGIN='<!-- customization:start -->'
END='<!-- customization:end -->'
def write(path,text):path.write_bytes((text.rstrip()+'\n').encode('utf-8'))
def code(lang,s):return f'```{lang}\n{s.strip()}\n```\n'
def cell(s):return str(s).replace('|','&#124;').replace('\n',' ')
def table(head,rows):return '| '+' | '.join(head)+' |\n| '+' | '.join('---' for _ in head)+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)
def source(file):return '['+Path(file).name+']('+BASE+file+')'
def types(r):return sorted(set(d['type'] for d in r['definitions']))
def summarize_uses(r):
    out=[]
    for u in r['uses']:
        v=u['where']+(('〔'+u['condition']+'〕') if u['condition'] else '')
        if v not in out:out.append(v)
    return ' / '.join(out[:4])+(' / ほか '+str(len(out)-4)+'箇所' if len(out)>4 else '')

SCALARS={'CornerRadius':('12','new System.Windows.CornerRadius(12)'), 'Thickness':('16,10','new System.Windows.Thickness(16, 10, 16, 10)'), 'Double':('18','18d'), 'SolidColorBrush':('#2563EB','new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235))'), 'Color':('#2563EB','System.Windows.Media.Color.FromRgb(37, 99, 235)')}
def resource_xml(key,typ):
    value=SCALARS[typ][0]
    if typ=='Double':return f'<system:Double x:Key="{key}">{value}</system:Double>'
    if typ=='SolidColorBrush':return f'<SolidColorBrush x:Key="{key}" Color="{value}" />'
    return f'<{typ} x:Key="{key}">{value}</{typ}>'
def choose(c):
    candidates=[]
    for r in c['resources']:
        ts=types(r)
        if len(ts)!=1 or ts[0] not in SCALARS:continue
        good=[u for u in r['uses'] if u['lookup']=='DynamicResource' and u['in_default_graph'] and u['owner'] in ['controls:'+c['name'],c['name']]]
        if not good:continue
        priority={'CornerRadius':0,'Thickness':20,'Double':40,'SolidColorBrush':50,'Color':60}[ts[0]]
        if r['key']=='ControlCornerRadius':priority=-10
        if all(u['condition'] for u in good):priority+=20
        if any(x in r['key'] for x in ['Disabled','PointerOver','Pressed','Selected']):priority+=20
        if r['key'].endswith('Background'):priority-=5
        candidates.append((priority,r['key'],r))
    return min(candidates,key=lambda x:(x[0],x[1]))[2] if candidates else None

def make_example(page,text,r):
    name=page['name'];typ=types(r)[0];key=r['key']
    original=re.search(r'```xml\n(.*?)\n```',text,re.S)[1]
    if name=='Card':original='<ui:Card Padding="16">\n    <TextBlock Text="반지름 12인 카드 (Footer 없음)" />\n</ui:Card>'
    tag=('ui:' if page['kind']=='custom' else '')+name
    match=re.search(r'<'+re.escape(tag)+r'(?=[\s/>])[^>]*>',original,re.S)
    if not match:return None
    opening=match[0]
    if opening.endswith('/>'):opening=opening[:-2]+'>' ; tail='\n</'+tag+'>'
    else:tail=''
    opening=re.sub(r'\s+x:Name="[^"]+"','',opening)
    if 'xmlns=' in opening and 'xmlns:x=' not in opening:opening=opening[:-1]+' xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"'+'>'
    opening=opening[:-1]+' x:Name="ResourceDemo"'+(' xmlns:system="clr-namespace:System;assembly=System.Runtime"' if typ=='Double' and 'xmlns:system=' not in opening else '')+'>'
    block='\n    <'+tag+'.Resources>\n        '+resource_xml(key,typ)+'\n    </'+tag+'.Resources>'
    xml=original[:match.start()]+opening+block+tail+original[match.end():]
    return xml,f'ResourceDemo.Resources["{key}"] = {SCALARS[typ][1]};'

def render():
    audit=json.loads((ROOT/'customization-manifest.json').read_text(encoding='utf-8'))
    manifest=json.loads((ROOT/'source-manifest.json').read_text(encoding='utf-8'))
    pages={p['name']:p for p in manifest['pages']}
    examples=[];catalog=[];overview=[]
    for c in audit['controls']:
        name=c['name'];file=ROOT/(name+'.md');text=file.read_text(encoding='utf-8')
        text=re.sub(re.escape(BEGIN)+r'.*?'+re.escape(END)+r'\n*','',text,flags=re.S)
        s=BEGIN+'\n## 속성 외에 모양을 바꾸는 방법\n\n'
        s+='[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)\n\n'
        if name in NOTES:s+=NOTES[name]+'\n\n'
        elif not c['resources'] and not c['styles']:
            s+='이 타입에 연결된 별도 WPF UI XAML 리소스·기본 스타일은 이번 소스 조사에서 발견되지 않았습니다. 이름을 추측해 키를 추가하기보다 위 공개 속성·콘텐츠 템플릿·상위 컨트롤을 먼저 설정합니다. WPF-UI 기반 클래스에서 상속한 설정은 해당 기반 클래스 문서도 확인합니다.\n\n'
        else:
            s+='화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.\n\n'
        r=choose(c)
        ex=make_example(pages[name],text,r) if r else None
        if ex:
            typ=types(r)[0];key=r['key'];xml,cs=ex
            id=name+'_Resources'
            s+='### 이 컨트롤의 Resources에서 바꾸기\n\n'
            s+=f'`{key}`는 `{typ}` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.\n\n'
            s+=f'<!-- customization:example {id} -->\n'+code('xml',xml)+'\n'+code('csharp',cs)+'\n<!-- customization:example-end -->\n\n'
            s+='C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.\n\n'
            examples.append({'id':id,'page':name,'kind':'resource','key':key,'type':typ})
        if name=='Snackbar':
            s+='### C#에서 알림별 리소스를 지정\n\n'
            cs='var notice = new ui.Snackbar(Presenter)\n{\n    Title = "완료", Content = "저장했습니다.",\n    Appearance = ui.ControlAppearance.Secondary\n};\nnotice.Resources["SnackBarBackground"] = System.Windows.Media.Brushes.MidnightBlue;\nnotice.Show();'
            s+='<!-- customization:csharp-only Snackbar_Resources -->\n'+code('csharp',cs)+'\n<!-- customization:example-end -->\n\n'
            examples.append({'id':'Snackbar_Resources','page':name,'kind':'csharp'})
        for i,(title,xml) in enumerate(EXTRA.get(name,[])):
            id=name+'_Recipe'+str(i+1)
            s+='### '+title+'\n\n'+f'<!-- customization:example {id} -->\n'+code('xml',xml)+'\n<!-- customization:example-end -->\n\n'
            examples.append({'id':id,'page':name,'kind':'recipe'})
        if c['resources']:
            dynamic=[r for r in c['resources'] if any(u['lookup']=='DynamicResource' for u in r['uses'])]
            static=[r for r in c['resources'] if all(u['lookup']=='StaticResource' for u in r['uses'])]
            primary=sorted(dynamic,key=lambda r:(0 if r['key'] in ['ControlCornerRadius','PopupCornerRadius','TextControlThemePadding'] else 1,r['key']))
            if primary:
                s+='### 재정의할 수 있는 동적 리소스\n\n'
                s+='참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.\n\n'
                s+=table(['키','타입','쓰이는 영역·조건'],[(f'`{r["key"]}`',' / '.join(types(r)) or '**정의 없음**',summarize_uses(r)) for r in primary])+'\n'
            if static:
                s+='<details>\n<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>\n\n'
                s+=table(['키','타입','쓰이는 위치'],[(f'`{r["key"]}`',' / '.join(types(r)) or '정의 없음',summarize_uses(r)) for r in static])+'\n'
                s+='StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.\n\n</details>\n\n'
        publicstyles=[st for st in c['styles'] if st['key'] and st['scope']=='dictionary root']
        if publicstyles:
            s+='### 선택·확장할 수 있는 스타일 키\n\n'
            s+=table(['키','대상','정의'],[(f'`{st["key"]}`',f'`{st["target"]}`',source(st['file'])) for st in publicstyles])+'\n'
            s+='`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.\n\n'
            if any(st['key'].startswith('{') for st in publicstyles):s+='`{x:Static ...}`·`{x:Type ...}` 형태는 문자열 키가 아닌 객체 키입니다. 예를 들어 ToolBar.ButtonStyleKey를 읽을 때는 `Style="{StaticResource {x:Static ToolBar.ButtonStyleKey}}"`처럼 중첩 마크업을 사용합니다. 일반 문자열처럼 같은 이름을 추가하는 방식과 다릅니다. [복합 키 사용 예](CustomizationGuide.md)를 확인합니다.\n\n'
        if c['templates'] or c['parts']:
            s+='### 템플릿을 바꿀 때 유지할 연결\n\n'
            if c['parts']:s+='C# 구현이 이름으로 찾는 부분: '+', '.join('`'+p['name']+'`' for p in c['parts'])+'. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.\n\n'
            if c.get('xaml_parts'):
                rows=sorted(set((p['name'],p['type']) for p in c['xaml_parts']))
                s+='원본 템플릿에 정의된 PART: '+', '.join(f'`{name}` ({typ})' for name,typ in rows)+'. WPF 기반 클래스가 사용하는 연결도 보존합니다.\n\n'
            if c['templates']:
                s+=table(['템플릿 키','소스·범위'],[(f'`{t["key"]}`' if t['key'] else '(Style 내부 템플릿)',source(t['file'])+' · '+t['scope']) for t in c['templates']])+'\n'
            s+='리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.\n\n'
        if c['template_bindings']:
            s+='<details>\n<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>\n\n'
            rows=[];seen=set()
            for b in c['template_bindings']:
                key=(b['property'],b['target'],b.get('kind',''),b['file'])
                if key in seen:continue
                seen.add(key);rows.append((f'`{b["property"]}`',f'`{b["target"]}`',b.get('kind','TemplateBinding'),source(b['file'])))
            s+=table(['입력 속성','내부 반영 위치','연결 방식','정의'],rows)+'\n</details>\n\n'
        if c['fixed_values']:
            s+='<details>\n<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>\n\n'
            rows=[];seen=set()
            for f in c['fixed_values']:
                key=(f['where'],f['value'],f['condition'],f['file'])
                if key in seen:continue
                seen.add(key)
                rows.append((f'`{f["where"]}`',f'`{f["value"]}`',f['condition'] or '직접 지정 / 현재 템플릿',source(f['file'])))
            s+=table(['위치','고정값','적용 조건','정의'],rows)+'\n'
            s+='표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.\n\n</details>\n\n'
        if c['clr_resources']:
            s+='### C# 코드가 직접 조회하는 리소스\n\n'+table(['키','실제 조회 코드','소스'],[(f'`{v["key"]}`',f'`{v["code"]}`',source(v['file'])) for v in c['clr_resources']])+'\n'
            s+='`Application.Current.Resources`를 직접 읽으면 개별 컨트롤 Resources의 같은 키가 대신 사용되는 것은 아닙니다. 조회 시점이 생성자라면 이후 리소스 변경도 자동 바인딩으로 해석하지 않습니다.\n\n'
        s+=END+'\n\n'
        where=text.find('## 기본 스타일에서 설정하는 값')
        if where<0:where=text.find('## 동작과 주의 사항')
        if where<0:where=text.find('## 확인한 소스')
        text=text[:where]+s+text[where:]
        # Correct the older overgeneralization: Icon style actually binds CornerRadius.
        if name=='InfoBadge':
            text=text.replace('다만 4.3.0 제공 ValueInfoBadgeStyle·IconInfoBadgeStyle은 템플릿 안에서 별도 상수·리소스 반지름을 사용하므로 이 속성 변경이 그대로 반영되지 않습니다. 해당 템플릿·리소스를 수정해야 합니다.','기본 ValueInfoBadgeStyle은 StaticResource로 고정 반지름을 사용하므로 이 속성이 반영되지 않습니다. DotInfoBadgeStyle·IconInfoBadgeStyle은 CornerRadius를 TemplateBinding하므로 반영됩니다.')
            text=text.replace('CornerRadius는 제공 템플릿의 반지름 리소스에 연결되어 있지 않아 값 변경만으로 반영되지 않을 수 있습니다.','CornerRadius는 기본 숫자형에서는 반영되지 않지만 DotInfoBadgeStyle·IconInfoBadgeStyle에서는 반영됩니다.')
        nav='[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)'
        if nav+' · [Resources' not in text:text=text.replace(nav,nav+' · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)',1)
        write(file,text.replace('ほか ','외 ').replace('箇所','곳').replace('dictionary root','사전 루트').replace('nested resources','내부 정의'))
        overview.append((f'[{name}]({name}.md)',str(len(c['resources'])),str(len(publicstyles)),('Resources 예제' if ex else '속성·스타일·상위 구성')+(' · 상세 제약' if name in NOTES else '')))
    write(ROOT/'customization-examples.json',json.dumps(examples,ensure_ascii=False,indent=2))
    # Complete resource-definition index with use sites grouped by control, not claimed as a public API.
    uses=collections.defaultdict(set)
    for c in audit['controls']:
        for r in c['resources']:uses[r['key']].add(c['name'])
        for r in c['clr_resources']:uses[r['key']].add(c['name'])
    catalogtext='# 리소스 키 전체 사전\n\n[목차](README.md) · [조정 방법](CustomizationGuide.md) · [컨트롤별 조사 결과](CustomizationIndex.md)\n\n'
    catalogtext+='기준 4.3.0의 Wpf.Ui XAML에 정의된 키 881개(문자열 862개·복합 키 19개)와 문서 대상의 참조를 함께 모았습니다. **키의 존재가 개별 컨트롤 Resources 재정의나 안정된 공개 API를 보장하지 않습니다.** StaticResource·중첩 범위·선택 스타일·미정의 이름을 개별 문서에서 확인합니다. x:Static·x:Type·ComponentResourceKey는 객체 키이므로 문자열과 사용 문법이 다릅니다. 자동 참조 추적은 문자열 키를 대상으로 하며 복합 키는 정의 목록과 수작업 사용 예제로 보완합니다. 라이브러리 외부 앱 리소스는 포함하지 않습니다.\n\n'
    sections=collections.defaultdict(str)
    keyrows=[]
    for key in sorted(set(audit['definitions'])|set(uses)):
        group=key[0].upper() if key[0].isalpha() and key[0].isascii() else 'Other'
        anchor=re.sub(r'[^\w\- ]','',key).lower().replace(' ','-')
        ds=audit['definitions'].get(key,[])
        detail='## '+key+'\n\n'
        if ds:
            rows=[];seen=set()
            for d in ds:
                signature=(d['type'],d['value'],d['file'],d['scope'])
                if signature in seen:continue
                seen.add(signature)
                rows.append((d['type'],('`'+d['value']+'`') if d['value'] else '객체 / 테마 정의',d['scope'].replace('dictionary root','사전 루트').replace('nested resources','내부 정의'),source(d['file'])))
            detail+=table(['타입','값','정의 범위','출처'],rows)+'\n'
        else:detail+='**원본 XAML에서 정의를 찾지 못한 참조 키입니다.** 정상 사용 키로 권장하지 않습니다.\n\n'
        names=sorted(uses.get(key,[]))
        detail+='문서 대상의 참조: '+(', '.join(f'[{n}](../{n}.md)' for n in names) if names else '직접 참조 없음 / 공통 사전·기타 정의')+'.\n\n'
        sections[group]+=detail
        keyrows.append((f'[{key}](resources/{group}.md#{anchor})',' / '.join(sorted(set(d['type'] for d in ds))) or '**정의 없음**',str(len(names))))
    (ROOT/'resources').mkdir(exist_ok=True)
    for group,detail in sections.items():
        write(ROOT/'resources'/(group+'.md'),'# 리소스 사전: '+group+'\n\n[전체 리소스 목차](../ResourceCatalog.md) · [조정 방법](../CustomizationGuide.md)\n\n'+detail)
    catalogtext+='파일 내 검색(Ctrl+F)으로 키를 찾은 뒤 링크를 열면 기본값·타입·정의 범위·사용 컨트롤을 확인할 수 있습니다. 큰 문서가 GitHub 표시 제한에 걸리지 않도록 세부 정의를 알파벳별 파일로 나눴습니다.\n\n'
    catalogtext+=table(['키 → 정의·사용처','타입','참조 문서 수'],keyrows)
    write(ROOT/'ResourceCatalog.md',catalogtext)
    index='# 컨트롤별 조정 방법 조사\n\n[목차](README.md) · [공통 조정 안내](CustomizationGuide.md)\n\n고유 속성뿐 아니라 기본 스타일·보조 스타일·상태별 참조·TemplateBinding·고정값을 조사했습니다. 리소스 수는 참조 문자열 키 개수이며 사용할 수 있는 공개 속성 개수가 아닙니다.\n\n'
    index+=table(['컨트롤','참조 키','사전 루트 스타일 키','안내'],overview)
    missing=collections.defaultdict(list)
    for control in audit['controls']:
        for resource in control['resources']:
            if not resource['definitions']:missing[resource['key']].append(control['name'])
    if missing:
        index+='\n## 원본 XAML에서 정의가 없는 참조 이름\n\n문자열 참조는 있지만 Wpf.Ui XAML의 정의를 찾지 못한 이름입니다. 외부 사전에서 별도로 제공할 수도 있지만 기본 제공 조정 키로 권장하지 않습니다.\n\n'
        index+=table(['이름','발견한 컨트롤'],[(f'`{key}`',', '.join(f'[{name}]({name}.md)' for name in sorted(set(names)))) for key,names in sorted(missing.items())])
    write(ROOT/'CustomizationIndex.md',index)
    print('Updated',len(pages),'pages;',len(examples),'additional examples;',len(audit['definitions']),'defined resource keys')

if __name__=='__main__':render()
