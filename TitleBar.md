# TitleBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

사용자 지정 창 제목 영역과 시스템 창 버튼을 제공합니다.

**타입:** `Wpf.Ui.Controls.TitleBar` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TitleBar x:Name="Demo" Title="문서 편집기" ShowHelp="True">
    <ui:TitleBar.CenterContent><TextBlock Text="프로젝트 A" /></ui:TitleBar.CenterContent>
</ui:TitleBar>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Title = "보고서 - 문서 편집기";
Demo.ShowMaximize = false;
Demo.HelpClicked += (_, _) => Demo.Title = "도움말 요청";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ApplicationTheme` | `Appearance.ApplicationTheme` | 읽기·쓰기 | `Appearance.ApplicationTheme.Unknown` | 시스템 제목 표시줄과 버튼 렌더링에 사용할 테마 상태입니다. 테마 변경과 함께 관리합니다. |
| `Title` | `string?` | 읽기·쓰기 | `null` | 제목 문자열입니다. 창의 `Window.Title`과 구분되므로 필요한 경우 명시적으로 바인딩합니다. |
| `Header` | `object?` | 읽기·쓰기 | `null` | 제목 영역에 넣을 사용자 콘텐츠입니다. |
| `CenterContent` | `object?` | 읽기·쓰기 | `null` | 타이틀바 중앙 영역에 넣는 콘텐츠입니다. 검색 입력 등을 배치할 수 있습니다. |
| `TrailingContent` | `object?` | 읽기·쓰기 | `null` | 오른쪽 시스템 버튼 앞쪽에 넣는 콘텐츠입니다. |
| `ButtonsForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 최소화·최대화·닫기 버튼의 기본 전경 브러시입니다. |
| `ButtonsBackground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlBrush` | 타이틀바 시스템 버튼 배경 브러시입니다. |
| `IsMaximized` | `bool` | 외부 읽기 전용 | `false` | 소유 창이 최대화되어 있는지 나타내는 읽기 전용 상태입니다. |
| `ForceShutdown` | `bool` | 읽기·쓰기 | `false` | 닫기 동작에서 창만 닫는 대신 애플리케이션 종료를 요청할지 정합니다. 여러 창이 있는 앱에서는 종료 범위를 고려합니다. |
| `ShowMaximize` | `bool` | 읽기·쓰기 | `true` | 최대화·복원 버튼을 표시할지 정합니다. |
| `ShowMinimize` | `bool` | 읽기·쓰기 | `true` | 최소화 버튼을 표시할지 정합니다. |
| `ShowHelp` | `bool` | 읽기·쓰기 | `false` | 도움말 버튼을 표시할지 정합니다. 동작은 `HelpClicked`에서 구현합니다. |
| `ShowClose` | `bool` | 읽기·쓰기 | `true` | 닫기 버튼 표시 여부입니다. |
| `CanMaximize` | `bool` | 읽기·쓰기 | `true` | 최대화 동작을 허용할지 정합니다. 버튼 표시 여부인 `ShowMaximize`와 구분됩니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `CloseWindowByDoubleClickOnIcon` | `bool` | 읽기·쓰기 | `false` | 왼쪽 아이콘을 더블클릭할 때 창을 닫을지 정합니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |
| `MaximizeActionOverride` | `Action<TitleBar, System.Windows.Window>?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 최대화 버튼 기본 동작을 대체할 C# 콜백입니다. 일반 XAML 문자열로 지정하는 속성이 아니며 창과 TitleBar를 전달받습니다. |
| `MinimizeActionOverride` | `Action<TitleBar, System.Windows.Window>?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 최소화 버튼 기본 동작을 대체할 C# 콜백입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

제목·중앙·우측 슬롯은 공개 Title·Header·CenterContent·TrailingContent를 사용합니다. 시스템 버튼 색은 ButtonsForeground·ButtonsBackground이며 버튼 템플릿에는 고정된 글리프·크기와 닫기 강조색도 있습니다. TitleBar.Resources에 일반 Button 색을 바꾼다고 모든 시스템 버튼 상태가 같은 색으로 변하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ButtonForeground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example TitleBar_Resources -->
```xml
<ui:TitleBar Title="문서 편집기" ShowHelp="True" x:Name="ResourceDemo">
    <ui:TitleBar.Resources>
        <SolidColorBrush x:Key="ButtonForeground" Color="#2563EB" />
    </ui:TitleBar.Resources>
    <ui:TitleBar.CenterContent><TextBlock Text="프로젝트 A" /></ui:TitleBar.CenterContent>
</ui:TitleBar>
```

```csharp
ResourceDemo.Resources["ButtonForeground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ButtonForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.ButtonsForeground |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `PaletteRedBrush` | SolidColorBrush | TitleBarButton#PART_CloseButton MouseOverBackground |

### 템플릿을 바꿀 때 유지할 연결

C# 구현이 이름으로 찾는 부분: `PART_CloseButton`, `PART_HelpButton`, `PART_Icon`, `PART_MainGrid`, `PART_MaximizeButton`, `PART_MinimizeButton`, `PART_RestoreButton`. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.

원본 템플릿에 정의된 PART: `PART_CloseButton` (TitleBarButton), `PART_HelpButton` (TitleBarButton), `PART_Icon` (ContentPresenter), `PART_MainGrid` (Grid), `PART_MaximizeButton` (TitleBarButton), `PART_MinimizeButton` (TitleBarButton). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Grid#PART_MainGrid.HorizontalAlignment` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `VerticalContentAlignment` | `Grid#PART_MainGrid.VerticalAlignment` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Background` | `Grid#PART_MainGrid.Background` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Padding` | `Grid#TitleGrid.Margin` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Icon` | `ContentPresenter#PART_Icon.Content` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Header` | `ContentPresenter.Content` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter.HorizontalAlignment` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `VerticalContentAlignment` | `ContentPresenter.VerticalAlignment` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `CenterContent` | `ContentPresenter.Content` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `TrailingContent` | `ContentPresenter.Content` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `컨트롤.Padding` | `16,4,16,4` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `컨트롤.FontSize` | `12` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `컨트롤.Height` | `48` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `ContentPresenter#PART_Icon.Height` | `16` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `PART_Icon.Margin` | `0` | Icon={x:Null} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `Transparent` | 암시적 스타일 |
| `Foreground` | `{DynamicResource ButtonForeground}` | 암시적 스타일 |
| `ButtonsForeground` | `{DynamicResource ButtonForeground}` | 암시적 스타일 |
| `VerticalAlignment` | `Top` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `Padding` | `16,4,16,4` | 암시적 스타일 |
| `FontSize` | `12` | 암시적 스타일 |
| `Height` | `48` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `VerticalContentAlignment` | `Stretch` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `WndProcInvoked` | 창 메시지 후크 알림입니다. 저수준 창 동작을 다룰 때만 사용합니다. |
| `CloseClicked` | 닫기 버튼 클릭 알림입니다. 기본 종료 정책은 ForceShutdown 등을 따릅니다. |
| `MaximizeClicked` | 최대화 버튼 클릭 알림입니다. 사용자 지정 동작은 MaximizeActionOverride로 구성합니다. |
| `MinimizeClicked` | 최소화 버튼 클릭 알림입니다. 사용자 지정 동작은 MinimizeActionOverride로 구성합니다. |
| `HelpClicked` | 도움말 버튼 클릭 알림입니다. 표시 설정은 ShowHelp입니다. |

## 동작과 주의 사항

`FluentWindow.ExtendsContentIntoTitleBar=True`와 함께 최상단에 배치합니다. 중앙·우측 콘텐츠의 입력 가능 영역과 창 드래그 영역이 겹치지 않는지 확인합니다. `ForceShutdown`은 전체 앱 종료에 영향을 줍니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TitleBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.cs)
- [TitleBar.WindowResize.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.WindowResize.cs)
- [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
