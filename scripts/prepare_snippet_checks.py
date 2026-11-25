"""문서의 첫 XAML + 첫 C# 조각을 각 창·뷰로 감싸 컴파일할 프로젝트를 만듭니다.

python scripts/prepare_snippet_checks.py
dotnet build .checks/SnippetChecks.csproj

조각은 실행하지 않습니다. 컴파일은 표시 결과·OS 효과·상호작용 검증과 다릅니다.
"""
import re,json,struct,zlib
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.checks'
OUT.mkdir(exist_ok=True)
manifest=json.loads((ROOT/'source-manifest.json').read_text(encoding='utf-8'))
ns='xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml" xmlns:local="clr-namespace:DocChecks"'
for p in manifest['pages']:
    name=p['name'];text=(ROOT/(name+'.md')).read_text(encoding='utf-8')
    xaml=re.search(r'```xml\n(.*?)\n```',text,re.S)[1]
    cs=re.search(r'```csharp\n(.*?)\n```',text,re.S)[1]
    cl='Check_'+name
    if name in ['FluentWindow','Window','Page','UserControl','MessageBox']:
        base={'FluentWindow':'ui.FluentWindow','Window':'System.Windows.Window','Page':'System.Windows.Controls.Page','UserControl':'System.Windows.Controls.UserControl','MessageBox':'ui.MessageBox'}[name]
        xaml=re.sub(r'\s+x:Class="[^"]+"','',xaml)
        if 'xmlns:x=' not in xaml:
            xaml=xaml.replace('xmlns:ui=', 'xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:ui=',1)
        xaml=re.sub(r'^(<[^\s>]+)',rf'\1 x:Class="DocChecks.{cl}"',xaml,count=1)
    else:
        base='System.Windows.Window'
        xaml=f'<Window x:Class="DocChecks.{cl}" {ns}>\n{xaml}\n</Window>'
    (OUT/(cl+'.xaml')).write_text(xaml,encoding='utf-8')
    (OUT/(cl+'.xaml.cs')).write_text('using System;\nusing System.Threading.Tasks;\nusing ui = Wpf.Ui.Controls;\nnamespace DocChecks;\npublic partial class '+cl+' : '+base+'\n{\n public '+cl+'() { InitializeComponent(); }\n public async Task CheckCodeAsync()\n {\n'+cs+'\n }\n}\n',encoding='utf-8')
(OUT/'Pages.cs').write_text('namespace DocChecks; public class HomePage : System.Windows.Controls.Page { } public class SettingsPage : System.Windows.Controls.UserControl { }',encoding='utf-8')
shutil.copyfile(ROOT/'scripts/SnippetSmoke.cs',OUT/'SnippetSmoke.cs')
def chunk(kind,data):
    return struct.pack('!I',len(data))+kind+data+struct.pack('!I',zlib.crc32(kind+data)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!2I5B',1,1,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(b'\x00\x33\x66\xcc\xff'))+chunk(b'IEND',b'')
(OUT/'Assets').mkdir(exist_ok=True)
for filename in ['photo.png','app.png']:(OUT/'Assets'/filename).write_bytes(png)
(OUT/'SnippetChecks.csproj').write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0-windows</TargetFramework><UseWPF>true</UseWPF><Nullable>enable</Nullable><NoWarn>CS1998;CS0219;CS8981</NoWarn></PropertyGroup><ItemGroup><PackageReference Include="WPF-UI" Version="4.3.0" /><Resource Include="Assets/*.png" /></ItemGroup></Project>',encoding='utf-8')
print(f'Prepared {len(manifest["pages"])} XAML / C# snippet pairs in {OUT}')
