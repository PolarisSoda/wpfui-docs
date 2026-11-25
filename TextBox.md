# TextBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

아이콘·플레이스홀더·지우기 버튼을 더한 단일·여러 줄 입력란입니다.

**타입:** `Wpf.Ui.Controls.TextBox` · **기반:** `System.Windows.Controls.TextBox`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TextBox x:Name="Demo" Width="280" PlaceholderText="이름 입력" ClearButtonEnabled="True">
    <ui:TextBox.Icon><ui:SymbolIcon Symbol="Person24" /></ui:TextBox.Icon>
</ui:TextBox>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Text = "새 이름";
Demo.IconPlacement = ui.ElementPlacement.Right;
Demo.ClearButtonEnabled = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `IconPlacement` | `ElementPlacement` | 읽기·쓰기 | `ElementPlacement.Left` | 아이콘을 입력란 왼쪽 또는 오른쪽에 둡니다. 기본 템플릿은 `Left`·`Right` 배치를 사용합니다. |
| `PlaceholderText` | `string` | 읽기·쓰기 | `string.Empty` | 입력이 비어 있을 때 보여 줄 안내 문구입니다. 실제 입력 문자열과 구분됩니다. |
| `PlaceholderEnabled` | `bool` | 읽기·쓰기 | `true` | 플레이스홀더 기능을 켤지 정합니다. |
| `CurrentPlaceholderEnabled` | `bool` | 외부 읽기 전용 | `true` | 입력 상태와 플레이스홀더 설정을 반영해 계산한 표시 상태입니다. 사용자는 `PlaceholderEnabled`·`PlaceholderText`를 설정합니다. |
| `ClearButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 텍스트 지우기 기능을 허용합니다. 버튼의 실제 표시 여부는 입력 상태에 따라 계산됩니다. |
| `ShowClearButton` | `bool` | 외부 읽기 전용 | `false` | 현재 지우기 버튼이 보여야 하는지 나타내는 상태입니다. 외부에서는 읽기 전용입니다. |
| `IsTextSelectionEnabled` | `bool` | 읽기·쓰기 | `false` | `true`이면 기본 스타일이 읽기 전용·투명 배경·테두리 없는 선택 가능한 텍스트 표시 모드로 바꿉니다. 일반 편집 TextBox도 기본적으로 선택은 가능합니다. 입력을 계속 받으려면 `false`로 둡니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Text` | `string` | 현재 입력 문자열입니다. 실시간 바인딩은 UpdateSourceTrigger=PropertyChanged를 사용합니다. |
| `IsReadOnly` | `bool` | 편집을 막되 읽기·복사를 허용하는 용도입니다. |
| `MaxLength` | `int` | 사용자 입력 문자열의 길이 제한입니다. 0은 제한 없음입니다. |
| `AcceptsReturn / TextWrapping` | `bool / TextWrapping` | 여러 줄 입력과 자동 줄바꿈을 구성합니다. |
| `SelectionStart / SelectionLength` | `int` | 선택 구간의 시작과 길이입니다. 읽기 전용 표시 플래그와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ElementPlacement`: `Left`, `Right`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

TextControlThemePadding·TextControlThemeMinHeight·ControlCornerRadius처럼 DynamicResource로 연결된 크기 리소스를 인스턴스 Resources에서 바꿀 수 있습니다. 배경은 TextControlBackground·TextControlBackgroundPointerOver·TextControlBackgroundFocused·TextControlBackgroundDisabled로 나뉩니다. `IsTextSelectionEnabled=True`의 읽기 전용 표시 스타일은 Padding·Background·BorderThickness·Template까지 변경하므로 일반 입력 스타일의 조정이 그대로 보이지 않을 수 있습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example TextBox_Resources -->
```xml
<ui:TextBox Width="280" PlaceholderText="이름 입력" ClearButtonEnabled="True" x:Name="ResourceDemo">
    <ui:TextBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:TextBox.Resources>
    <ui:TextBox.Icon><ui:SymbolIcon Symbol="Person24" /></ui:TextBox.Icon>
</ui:TextBox>
```

```csharp
ResourceDemo.Resources["ControlCornerRadius"] = new System.Windows.CornerRadius(12);
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 여백·모서리·포커스 배경을 함께 조정

<!-- customization:example TextBox_Recipe1 -->
```xml
<ui:TextBox Width="280" PlaceholderText="이름 입력">
    <ui:TextBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">10</CornerRadius>
        <Thickness x:Key="TextControlThemePadding">16,10</Thickness>
        <SolidColorBrush x:Key="TextControlBackgroundFocused" Color="#EFF6FF" />
    </ui:TextBox.Resources>
</ui:TextBox>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius |
| `TextControlThemePadding` | Thickness | 컨트롤.Padding |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlStrokeColorDefaultBrush` | SolidColorBrush | Border#AccentBorder BorderBrush |
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `DefaultTextBoxScrollViewerStyle` | Style | PassiveScrollViewer#PART_ContentHost Style |
| `SubtleFillColorSecondaryBrush` | SolidColorBrush | Button#ClearButton MouseOverBackground |
| `SubtleFillColorTertiaryBrush` | SolidColorBrush | Button#ClearButton PressedBackground |
| `TextControlBackground` | SolidColorBrush | 컨트롤.Background |
| `TextControlBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `TextControlBackgroundFocused` | SolidColorBrush | ContentBorder.Background〔IsFocused=True〕 |
| `TextControlBackgroundPointerOver` | SolidColorBrush | ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsFocused=False; IsFocused=False〕 / ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsFocused=False〕 |
| `TextControlBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 / AccentBorder.BorderBrush〔IsEnabled=False〕 |
| `TextControlButtonForeground` | SolidColorBrush | Button#ClearButton Foreground |
| `TextControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush |
| `TextControlFocusedBorderBrush` | SolidColorBrush | AccentBorder.BorderBrush〔IsFocused=True〕 |
| `TextControlForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.CaretBrush |
| `TextControlForegroundDisabled` | SolidColorBrush | ControlIconLeft.TextElement.Foreground〔IsEnabled=False〕 / ControlIconRight.TextElement.Foreground〔IsEnabled=False〕 / PlaceholderTextBox.Foreground〔IsEnabled=False〕 / 컨트롤.Foreground〔IsEnabled=False〕 |
| `TextControlPlaceholderForeground` | SolidColorBrush | TextBlock#PlaceholderTextBox Foreground |
| `TextControlThemeMinHeight` | Double | 컨트롤.MinHeight |
| `TextControlThemeMinWidth` | Double | 컨트롤.MinWidth |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultTextBoxStyle` | Style | Style BasedOn |
| `DefaultUiTextBoxControlTemplate` | ControlTemplate | 컨트롤.Template〔IsTextSelectionEnabled=False〕 |
| `DefaultUiTextBoxStyle` | Style | Style BasedOn |
| `DefaultUiTextBoxTextSelectionEnabledControlTemplate` | ControlTemplate | 컨트롤.Template〔IsTextSelectionEnabled=True〕 |
| `TextBoxAccentBorderThemeThickness` | Thickness | Border#AccentBorder BorderThickness |
| `TextBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `TextBoxClearButtonHeight` | Double | Button#ClearButton MinWidth / Button#ClearButton MinHeight |
| `TextBoxClearButtonMargin` | Thickness | Button#ClearButton Margin |
| `TextBoxClearButtonPadding` | Thickness | Button#ClearButton Padding |
| `TextBoxLeftIconMargin` | Thickness | ContentPresenter#ControlIconLeft Margin |
| `TextBoxRightIconMargin` | Thickness | ContentPresenter#ControlIconRight Margin |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiTextBoxStyle` | `controls:TextBox` | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ContentHost` (PassiveScrollViewer). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `DefaultUiTextBoxControlTemplate` | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) · 사전 루트 |
| `DefaultUiTextBoxTextSelectionEnabledControlTemplate` | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `VerticalAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Icon` | `ContentPresenter#ControlIconLeft.Content` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `FontSize` | `ContentPresenter#ControlIconLeft.TextElement.FontSize` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Foreground` | `ContentPresenter#ControlIconLeft.TextElement.Foreground` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Padding` | `Grid.Margin` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ScrollViewer.CanContentScroll` | `PassiveScrollViewer#PART_ContentHost.CanContentScroll` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ScrollViewer.HorizontalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentHost.HorizontalScrollBarVisibility` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ScrollViewer.IsDeferredScrollingEnabled` | `PassiveScrollViewer#PART_ContentHost.IsDeferredScrollingEnabled` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ScrollViewer.IsTabStop` | `PassiveScrollViewer#PART_ContentHost.IsTabStop` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Foreground` | `PassiveScrollViewer#PART_ContentHost.TextElement.Foreground` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ScrollViewer.VerticalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentHost.VerticalScrollBarVisibility` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `FontSize` | `TextBlock#PlaceholderTextBox.FontSize` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `PlaceholderText` | `TextBlock#PlaceholderTextBox.Text` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `TemplateButtonCommand` | `Button#ClearButton.Command` | Binding to TemplatedParent | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `FontSize` | `SymbolIcon.FontSize` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Icon` | `ContentPresenter#ControlIconRight.Content` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `FontSize` | `ContentPresenter#ControlIconRight.TextElement.FontSize` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Foreground` | `ContentPresenter#ControlIconRight.TextElement.Foreground` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Border.CornerRadius` | `Border#AccentBorder.CornerRadius` | TemplateBinding | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `TextBlock#PlaceholderTextBox.Margin` | `0` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `TextBlock#PlaceholderTextBox.Padding` | `1,0` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Button#ClearButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `Button#ClearButton.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ClearButton.Margin` | `0` | ShowClearButton=False | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ClearButton.Margin` | `0` | ClearButtonEnabled=False | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ControlIconRight.Margin` | `0` | IconPlacement=Left | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ControlIconLeft.Margin` | `0` | IconPlacement=Right | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ControlIconRight.Margin` | `0` | Icon={x:Null} | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ControlIconLeft.Margin` | `0` | Icon={x:Null} | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `AccentBorder.BorderThickness` | `0,0,0,2` | IsFocused=True | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `ClearButton.Margin` | `0` | IsReadOnly=True | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `컨트롤.Background` | `Transparent` | IsTextSelectionEnabled=True | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `컨트롤.Padding` | `0` | IsTextSelectionEnabled=True | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |
| `컨트롤.BorderThickness` | `0` | IsTextSelectionEnabled=True | [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiTextBoxStyle |
| `ContextMenu` | `{DynamicResource DefaultControlContextMenu}` | DefaultUiTextBoxStyle |
| `Foreground` | `{DynamicResource TextControlForeground}` | DefaultUiTextBoxStyle |
| `CaretBrush` | `{DynamicResource TextControlForeground}` | DefaultUiTextBoxStyle |
| `Background` | `{DynamicResource TextControlBackground}` | DefaultUiTextBoxStyle |
| `BorderBrush` | `{DynamicResource TextControlElevationBorderBrush}` | DefaultUiTextBoxStyle |
| `BorderThickness` | `{StaticResource TextBoxBorderThemeThickness}` | DefaultUiTextBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiTextBoxStyle |
| `ScrollViewer.CanContentScroll` | `False` | DefaultUiTextBoxStyle |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Hidden` | DefaultUiTextBoxStyle |
| `ScrollViewer.VerticalScrollBarVisibility` | `Hidden` | DefaultUiTextBoxStyle |
| `ScrollViewer.IsDeferredScrollingEnabled` | `False` | DefaultUiTextBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiTextBoxStyle |
| `VerticalAlignment` | `Stretch` | DefaultUiTextBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiTextBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiTextBoxStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultUiTextBoxStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultUiTextBoxStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiTextBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiTextBoxStyle |
| `ClearButtonEnabled` | `True` | DefaultUiTextBoxStyle |
| `IconPlacement` | `Left` | DefaultUiTextBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiTextBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiTextBoxStyle |

## 동작과 주의 사항

`IsTextSelectionEnabled=True`는 선택을 켜기만 하는 속성이 아니라 읽기 전용 텍스트 표시 스타일로 전환합니다. 실시간 입력 바인딩은 `Text="{Binding Name, UpdateSourceTrigger=PropertyChanged}"`로 설정합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TextBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.cs)
- [TextBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBox/TextBox.xaml)
- [Gallery: TextBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/TextBoxPage.xaml)
