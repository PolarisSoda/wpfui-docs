# 시작하기

[전체 목차](README.md)

이 문서는 WPF-UI **4.3.0**을 기준으로 합니다. `Wpf.Ui.Controls.Button`처럼 별도 클래스가 있는 컨트롤은 `ui:` 접두사로 선언하고, `CheckBox`·`ComboBox`·`Page`처럼 기본 WPF 타입에 스타일을 적용하는 경우는 기본 태그를 사용합니다.

## 패키지와 프로젝트

Windows용 WPF 프로젝트와 .NET SDK가 필요합니다. 실행 예제는 `net10.0-windows`를 사용합니다. 원본 4.3.0 프로젝트는 .NET 10·9·8 및 일부 .NET Framework 대상을 정의합니다.

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net10.0-windows</TargetFramework>
    <UseWPF>true</UseWPF>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="WPF-UI" Version="4.3.0" />
  </ItemGroup>
</Project>
```

NuGet 패키지 ID는 `WPF-UI`, 어셈블리는 `Wpf.Ui`, C# 네임스페이스는 `Wpf.Ui.Controls`입니다.

## App.xaml에 리소스 추가

스타일을 생략하면 컨트롤의 템플릿·아이콘·색상 리소스가 준비되지 않을 수 있습니다. 테마를 먼저, 컨트롤 사전을 다음 순서로 병합합니다.

```xml
<Application x:Class="QuickStart.App"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml"
    StartupUri="MainWindow.xaml">
    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ui:ThemesDictionary Theme="Light" />
                <ui:ControlsDictionary />
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>
</Application>
```

`ThemesDictionary`는 테마 색상, `ControlsDictionary`는 컨트롤 템플릿과 기본 스타일을 공급합니다. 이 가이드의 속성 설명은 제공되는 기본 템플릿을 전제로 합니다. 사용자 템플릿이 속성을 바인딩하지 않으면 값을 바꾸어도 화면에 반영되지 않습니다.

## Window 또는 UserControl의 네임스페이스

```xml
<Window x:Class="QuickStart.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml"
    xmlns:local="clr-namespace:QuickStart"
    Title="첫 WPF UI 앱" Width="800" Height="500">
    <StackPanel Margin="24">
        <ui:TextBlock Text="환경 설정" FontTypography="Title" />
        <ui:Button x:Name="SaveButton" Content="저장" Appearance="Primary" />
        <CheckBox Content="자동 저장" />
    </StackPanel>
</Window>
```

`local:`은 예제의 가상 내장 타입이 아니라 **자기 앱의 네임스페이스**입니다. `TargetPageType="{x:Type local:HomePage}"`를 쓰려면 같은 이름의 공개 화면 클래스를 만들어야 합니다.

```csharp
using ui = Wpf.Ui.Controls;

// 위 XAML의 코드비하인드에서 InitializeComponent() 이후 사용합니다.
SaveButton.Appearance = ui.ControlAppearance.Success;
SaveButton.Content = "저장 완료";
```

## 속성 설정과 바인딩

XAML과 C# 속성은 같은 컨트롤 상태를 바꿉니다. 그러나 C#의 대입은 기존 바인딩을 덮어쓸 수 있습니다. ViewModel을 바인딩했다면 모델의 값을 바꾸는 방법을 먼저 사용합니다.

```xml
<ui:NumberBox Value="{Binding Quantity, Mode=TwoWay}" Minimum="0" Maximum="100" />
```

```csharp
// 바인딩을 유지하며 컨트롤 값을 갱신해야 할 때의 예입니다.
SaveButton.SetCurrentValue(ui.Button.IsEnabledProperty, false);
```

프로퍼티 변경 통지가 필요하면 ViewModel이 `INotifyPropertyChanged`를 구현해야 합니다. 컬렉션 변경 통지는 `ObservableCollection<T>`를 사용합니다. 문서의 짧은 조각은 이름 있는 컨트롤을 직접 다루며, ViewModel을 준비했다는 숨은 전제를 두지 않습니다.

## 바로 실행하기

[`examples/QuickStart`](examples/QuickStart/README.md)에 탐색·폼·대화상자·스낵바를 함께 구성한 프로젝트가 있습니다. 각 컨트롤 문서의 예제는 분리된 조각이므로 모두 한 화면에 그대로 이어 붙이지 않습니다.

## 기준 소스

- [패키지 대상 프레임워크](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Wpf.Ui.csproj)
- [공식 Gallery App.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/App.xaml)
- [공식 XAML 네임스페이스 매핑](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Properties/AssemblyInfo.cs)
