"""구조·상대 링크·속성 누락·펜스·예제 XML 및 소스 경로를 검증합니다.

python scripts/validate_docs.py [--source PATH_TO_WPFUI_4_3_0]
"""
import argparse,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
args=argparse.ArgumentParser()
args.add_argument('--source',type=Path)
args=args.parse_args()
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'source-manifest.json').read_text(encoding='utf-8'))
errors=[];links=0;props=0;xmls=0
for file in root.rglob('*.md'):
    if any(x in file.parts for x in ['.git','.checks','.customization-checks','bin','obj']):continue
    text=file.read_text(encoding='utf-8')
    if len(re.findall(r'^```',text,re.M))%2:errors.append(f'{file.name}: unclosed fence')
    plain=re.sub(r'```.*?```','',text,flags=re.S)
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',plain):
        if re.match(r'[a-zA-Z]+:',target) or target.startswith('#'):continue
        target=target.split('#')[0]
        if not (file.parent/target).exists():errors.append(f'{file.name}: broken link {target}')
        links+=1
    for snippet in re.findall(r'```xml\n(.*?)\n```',text,re.S):
        try:
            # Standalone documents may contain x:Class and namespace declarations.
            if 'xmlns=' in snippet:ET.fromstring(snippet)
            else:ET.fromstring('<Root xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml" xmlns:local="clr-namespace:QuickStart">'+snippet+'</Root>')
            xmls+=1
        except ET.ParseError as e:errors.append(f'{file.name}: XML {e}')
for page in manifest['pages']:
    file=root/(page['name']+'.md')
    if not file.exists():errors.append('Missing page '+page['name']);continue
    s=file.read_text(encoding='utf-8')
    for prop in page['properties']:
        if not re.search(r'^\| `'+re.escape(prop['name'])+r'` \|',s,re.M):errors.append(f'{page["name"]}: missing property {prop["name"]}')
        props+=1
    if args.source:
        for p in page['source_files']+page['gallery_files']:
            if not (args.source/p).is_file():errors.append(f'{page["name"]}: source missing {p}')
        for prop in page['properties']:
            source=(args.source/prop['file']).read_text(encoding='utf-8-sig')
            if not re.search(r'\b'+re.escape(prop['name'])+r'\b',source):errors.append('Source property missing '+prop['name'])
audit_file=root/'customization-manifest.json'
if audit_file.exists():
    audit=json.loads(audit_file.read_text(encoding='utf-8'))
    if len(audit['controls'])!=len(manifest['pages']):errors.append('Customization control count mismatch')
    for control in audit['controls']:
        page=(root/(control['name']+'.md')).read_text(encoding='utf-8')
        if '<!-- customization:start -->' not in page:errors.append('Missing customization section '+control['name'])
        for resource in control['resources']:
            if '`'+resource['key']+'`' not in page:errors.append('Missing resource '+control['name']+'.'+resource['key'])
        if args.source:
            for resource in control['resources']:
                for use in resource['uses']:
                    source=(args.source/use['file']).read_text(encoding='utf-8-sig')
                    if resource['key'] not in source:errors.append('Invalid resource source '+resource['key'])
    examples=json.loads((root/'customization-examples.json').read_text(encoding='utf-8'))
    for ex in examples:
        text=(root/(ex['page']+'.md')).read_text(encoding='utf-8')
        kind='csharp-only' if ex['kind']=='csharp' else 'example'
        if '<!-- customization:'+kind+' '+ex['id']+' -->' not in text:errors.append('Missing example '+ex['id'])
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(manifest["pages"])} control/view pages, {props} declared properties, {links} relative links, {xmls} XML examples')
