# PasswordBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

마스킹 입력과 비밀번호 공개 버튼이 있는 입력란입니다. WPF 기본 PasswordBox가 아닌 WPF-UI TextBox 파생형입니다.

**타입:** `Wpf.Ui.Controls.PasswordBox` · **기반:** `TextBox`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:PasswordBox x:Name="Demo" Width="280" PlaceholderText="비밀번호" RevealButtonEnabled="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Password = string.Empty;
Demo.RevealButtonEnabled = false;
Demo.PasswordChanged += (_, _) => { var length = Demo.Password.Length; };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Password` | `string` | 읽기·쓰기 | `string.Empty` | 실제 비밀번호 문자열입니다. 상속된 `Text`는 표시 마스크와 연결되므로 실제 값은 `Password`를 사용합니다. 로그·문서 예제에 실제 비밀번호를 남기지 않습니다. |
| `PasswordChar` | `char` | 읽기·쓰기 | `'*'` | 입력 문자를 가리는 마스크 문자입니다. 기본값은 별표입니다. |
| `IsPasswordRevealed` | `bool` | 외부 읽기 전용 | `false` | 현재 비밀번호가 그대로 보이는지 나타냅니다. 외부 setter가 없고 기본 템플릿의 공개 버튼 동작으로 변경됩니다. |
| `RevealButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 비밀번호 공개 버튼 사용 여부입니다. `false`이면 기본 템플릿에서 공개 동작을 제공하지 않습니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Icon` | [TextBox](TextBox.md) | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `IconPlacement` | [TextBox](TextBox.md) | 아이콘을 입력란 왼쪽 또는 오른쪽에 둡니다. 기본 템플릿은 `Left`·`Right` 배치를 사용합니다. |
| `PlaceholderText` | [TextBox](TextBox.md) | 입력이 비어 있을 때 보여 줄 안내 문구입니다. 실제 입력 문자열과 구분됩니다. |
| `PlaceholderEnabled` | [TextBox](TextBox.md) | 플레이스홀더 기능을 켤지 정합니다. |
| `CurrentPlaceholderEnabled` | [TextBox](TextBox.md) | 입력 상태와 플레이스홀더 설정을 반영해 계산한 표시 상태입니다. 사용자는 `PlaceholderEnabled`·`PlaceholderText`를 설정합니다. |
| `ClearButtonEnabled` | [TextBox](TextBox.md) | 텍스트 지우기 기능을 허용합니다. 버튼의 실제 표시 여부는 입력 상태에 따라 계산됩니다. |
| `ShowClearButton` | [TextBox](TextBox.md) | 현재 지우기 버튼이 보여야 하는지 나타내는 상태입니다. 외부에서는 읽기 전용입니다. |
| `IsTextSelectionEnabled` | [TextBox](TextBox.md) | `true`이면 기본 스타일이 읽기 전용·투명 배경·테두리 없는 선택 가능한 텍스트 표시 모드로 바꿉니다. 일반 편집 TextBox도 기본적으로 선택은 가능합니다. 입력을 계속 받으려면 `false`로 둡니다. |
| `TemplateButtonCommand` | [TextBox](TextBox.md) | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `MaxLength` | `int` | 사용자 입력 길이 제한입니다. |
| `IsReadOnly` | `bool` | 비밀번호 편집을 막습니다. 실제 값은 Password 속성을 사용합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

일반 입력부의 TextControl 계열 DynamicResource와 ControlCornerRadius를 재정의할 수 있습니다. 공개·숨김·지우기 아이콘은 `PasswordBoxRevealIcon`·`PasswordBoxHideIcon`·`PasswordBoxClearIcon`이라는 별도 키를 사용하지만 StaticResource 참조입니다. 키가 있다는 이유로 PasswordBox.Resources에서 언제든 교체할 수 있다고 보장하지 않습니다. 아이콘을 교체하는 템플릿을 만들 때 공유 UIElement의 부모 충돌과 원본 x:Shared=False 조건도 유지합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example PasswordBox_Resources -->
```xml
<ui:PasswordBox Width="280" PlaceholderText="비밀번호" RevealButtonEnabled="True"  x:Name="ResourceDemo">
    <ui:PasswordBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:PasswordBox.Resources>
</ui:PasswordBox>
```

```csharp
ResourceDemo.Resources["ControlCornerRadius"] = new System.Windows.CornerRadius(12);
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius |
| `TextControlThemePadding` | Thickness | 컨트롤.Padding |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlStrokeColorDefaultBrush` | SolidColorBrush | Border#AccentBorder BorderBrush |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `DefaultPasswordBoxContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultTextBoxScrollViewerStyle` | Style | PassiveScrollViewer#PART_ContentHost Style |
| `SubtleFillColorSecondaryBrush` | SolidColorBrush | Button#ClearButton MouseOverBackground / Button#RevealButton MouseOverBackground |
| `SubtleFillColorTertiaryBrush` | SolidColorBrush | Button#ClearButton PressedBackground / Button#RevealButton PressedBackground |
| `TextControlBackground` | SolidColorBrush | 컨트롤.Background |
| `TextControlBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `TextControlBackgroundFocused` | SolidColorBrush | ContentBorder.Background〔IsFocused=True〕 |
| `TextControlBackgroundPointerOver` | SolidColorBrush | ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsFocused=False; IsFocused=False〕 / ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsFocused=False〕 |
| `TextControlBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 / AccentBorder.BorderBrush〔IsEnabled=False〕 |
| `TextControlButtonForeground` | SolidColorBrush | Button#ClearButton Foreground / Button#RevealButton Foreground |
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
| `DefaultPasswordBoxStyle` | Style | Style BasedOn |
| `DefaultUiPasswordBoxStyle` | Style | Style BasedOn |
| `PasswordBoxAccentBorderThemeThickness` | Thickness | Border#AccentBorder BorderThickness |
| `PasswordBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `PasswordBoxButtonHeight` | Double | Button#ClearButton Width / Button#ClearButton Height / Button#RevealButton Width / Button#RevealButton Height |
| `PasswordBoxButtonMargin` | Thickness | Button#ClearButton Margin / Button#RevealButton Margin |
| `PasswordBoxButtonPadding` | Thickness | Button#ClearButton Padding / Button#RevealButton Padding |
| `PasswordBoxClearIcon` | SymbolIcon | Button#ClearButton Icon |
| `PasswordBoxHideIcon` | SymbolIcon | RevealButton.Icon〔IsPasswordRevealed=True〕 |
| `PasswordBoxLeftIconMargin` | Thickness | ContentPresenter#ControlIconLeft Margin |
| `PasswordBoxRevealIcon` | SymbolIcon | Button#RevealButton Icon |
| `PasswordBoxRightIconMargin` | Thickness | ContentPresenter#ControlIconRight Margin |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiPasswordBoxStyle` | `controls:PasswordBox` | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ContentHost` (PassiveScrollViewer). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `VerticalAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Icon` | `ContentPresenter#ControlIconLeft.Content` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Foreground` | `ContentPresenter#ControlIconLeft.TextElement.Foreground` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Padding` | `Grid.Margin` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Foreground` | `PassiveScrollViewer#PART_ContentHost.TextElement.Foreground` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `PlaceholderText` | `TextBlock#PlaceholderTextBox.Text` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `TemplateButtonCommand` | `Button#ClearButton.Command` | Binding to TemplatedParent | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `TemplateButtonCommand` | `Button#RevealButton.Command` | Binding to TemplatedParent | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Icon` | `ContentPresenter#ControlIconRight.Content` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Foreground` | `ContentPresenter#ControlIconRight.TextElement.Foreground` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Border.CornerRadius` | `Border#AccentBorder.CornerRadius` | TemplateBinding | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `TextBlock#PlaceholderTextBox.Margin` | `0` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `TextBlock#PlaceholderTextBox.Padding` | `1,0` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Button#ClearButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Button#ClearButton.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Button#RevealButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `Button#RevealButton.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ClearButton.Margin` | `0` | ShowClearButton=False | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ClearButton.Margin` | `0` | ClearButtonEnabled=False | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `RevealButton.Margin` | `0` | RevealButtonEnabled=False | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ControlIconRight.Margin` | `0` | IconPlacement=Left | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ControlIconLeft.Margin` | `0` | IconPlacement=Right | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ControlIconRight.Margin` | `0` | Icon={x:Null} | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `ControlIconLeft.Margin` | `0` | Icon={x:Null} | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |
| `AccentBorder.BorderThickness` | `0,0,0,2` | IsFocused=True | [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiPasswordBoxStyle |
| `ContextMenu` | `{DynamicResource DefaultPasswordBoxContextMenu}` | DefaultUiPasswordBoxStyle |
| `Foreground` | `{DynamicResource TextControlForeground}` | DefaultUiPasswordBoxStyle |
| `CaretBrush` | `{DynamicResource TextControlForeground}` | DefaultUiPasswordBoxStyle |
| `Background` | `{DynamicResource TextControlBackground}` | DefaultUiPasswordBoxStyle |
| `BorderBrush` | `{DynamicResource TextControlElevationBorderBrush}` | DefaultUiPasswordBoxStyle |
| `BorderThickness` | `{StaticResource PasswordBoxBorderThemeThickness}` | DefaultUiPasswordBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiPasswordBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiPasswordBoxStyle |
| `VerticalAlignment` | `Center` | DefaultUiPasswordBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiPasswordBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiPasswordBoxStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultUiPasswordBoxStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultUiPasswordBoxStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiPasswordBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiPasswordBoxStyle |
| `ClearButtonEnabled` | `True` | DefaultUiPasswordBoxStyle |
| `RevealButtonEnabled` | `True` | DefaultUiPasswordBoxStyle |
| `IconPlacement` | `Left` | DefaultUiPasswordBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiPasswordBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiPasswordBoxStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `PasswordChanged` | 실제 Password 변경 알림입니다. 표시 마스크 Text와 구분합니다. |

## 동작과 주의 사항

상속된 `Text` 대신 `Password`를 읽고 씁니다. `IsPasswordRevealed`는 외부에서 대입할 수 없습니다. 실제 비밀번호를 평문 예제·로그에 남기지 않습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [PasswordBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.cs)
- [PasswordHelper.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordHelper.cs)
- [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml)
- [Gallery: PasswordBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/PasswordBoxPage.xaml)
