"""커스터마이징 문서의 추가 XAML/C# 예제 전체를 별도 WPF 프로젝트로 검증합니다."""
import json,re,struct,zlib,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.customization-checks'
OUT.mkdir(exist_ok=True)
examples=json.loads((ROOT/'customization-examples.json').read_text(encoding='utf-8'))
ns='xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml" xmlns:local="clr-namespace:DocCustom"'
for item in examples:
    name=item['id'];text=(ROOT/(item['page']+'.md')).read_text(encoding='utf-8')
    marker='csharp-only' if item['kind']=='csharp' else 'example'
    body=re.search(r'<!-- customization:'+marker+' '+re.escape(name)+r' -->\n(.*?)<!-- customization:example-end -->',text,re.S)[1]
    xml=re.search(r'```xml\n(.*?)\n```',body,re.S)
    xaml=xml[1] if xml else re.search(r'```xml\n(.*?)\n```',text,re.S)[1]
    cs=re.search(r'```csharp\n(.*?)\n```',body,re.S)
    cs=cs[1] if cs else ''
    cl='Customize_'+name
    root=re.match(r'<([\w:]+)',xaml)[1]
    if root in ['ui:FluentWindow','Window','Page','UserControl','ui:MessageBox']:
        base={'ui:FluentWindow':'ui.FluentWindow','Window':'System.Windows.Window','Page':'System.Windows.Controls.Page','UserControl':'System.Windows.Controls.UserControl','ui:MessageBox':'ui.MessageBox'}[root]
        xaml=re.sub(r'\s+x:Class="[^"]+"','',xaml)
        if 'xmlns:x=' not in xaml:xaml=xaml.replace('xmlns:ui=','xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:ui=',1)
        xaml=re.sub(r'^(<[^\s>]+)',rf'\1 x:Class="DocCustom.{cl}"',xaml,count=1)
    else:base='System.Windows.Window';xaml=f'<Window x:Class="DocCustom.{cl}" {ns}>\n{xaml}\n</Window>'
    (OUT/(cl+'.xaml')).write_text(xaml,encoding='utf-8')
    (OUT/(cl+'.xaml.cs')).write_text('using System; using System.Threading.Tasks; using ui = Wpf.Ui.Controls; namespace DocCustom; public partial class '+cl+' : '+base+' { public '+cl+'() { InitializeComponent(); } public async Task VerifySnippetAsync() {\n'+cs+'\n} }',encoding='utf-8')
(OUT/'Pages.cs').write_text('namespace DocCustom; public class HomePage : System.Windows.Controls.Page {} public class SettingsPage : System.Windows.Controls.UserControl {}',encoding='utf-8')
shutil.copyfile(ROOT/'scripts/CustomizationSmoke.cs',OUT/'CustomizationSmoke.cs')
(OUT/'Fixtures').mkdir(exist_ok=True)
shutil.copyfile(ROOT/'examples/CustomizationLab/CardWithFooter.xaml',OUT/'Fixtures/CardWithFooter.xaml')
(OUT/'CustomizationChecks.csproj').write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0-windows</TargetFramework><UseWPF>true</UseWPF><Nullable>enable</Nullable><NoWarn>CS1998;CS0219;CS8981</NoWarn></PropertyGroup><ItemGroup><PackageReference Include="WPF-UI" Version="4.3.0" /></ItemGroup></Project>',encoding='utf-8')
print('Prepared',len(examples),'customization examples')
