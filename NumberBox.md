# NumberBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

숫자 입력·증감·범위 검사·간단한 식 입력을 제공합니다.

**타입:** `Wpf.Ui.Controls.NumberBox` · **기반:** `Wpf.Ui.Controls.TextBox`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:NumberBox x:Name="Demo" Width="200" Value="3" Minimum="0" Maximum="10" SmallChange="0.5" MaxDecimalPlaces="1" SpinButtonPlacementMode="Inline" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = 7.5;
Demo.SpinButtonPlacementMode = ui.NumberBoxSpinButtonPlacementMode.Compact;
Demo.AcceptsExpression = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Value` | `double?` | 읽기·쓰기 | `null` | 숫자 값(`double?`)입니다. `null`은 빈 입력을 나타냅니다. 화면의 `Text` 대신 계산·바인딩에는 이 속성을 사용합니다. |
| `MaxDecimalPlaces` | `int` | 읽기·쓰기 | `6` | 표시·정규화 시 허용할 최대 소수 자릿수입니다. 표시 반올림에 영향을 주므로 금액 등 정밀도 요구를 별도로 고려합니다. |
| `SmallChange` | `double` | 읽기·쓰기 | `1.0d` | 작은 증감 동작(위·아래 키, 스핀 버튼)의 변화량입니다. |
| `LargeChange` | `double` | 읽기·쓰기 | `10.0d` | 큰 증감 동작(PageUp·PageDown)의 변화량입니다. |
| `Maximum` | `double` | 읽기·쓰기 | `double.MaxValue` | 허용할 숫자의 상한입니다. `Minimum`보다 크거나 같게 설정합니다. 유효성 검사 모드와 함께 적용됩니다. |
| `Minimum` | `double` | 읽기·쓰기 | `double.MinValue` | 허용할 숫자의 하한입니다. |
| `AcceptsExpression` | `bool` | 읽기·쓰기 | `true` | 입력을 수식으로 해석할지 정합니다. 단순 숫자만 받으려면 `false`로 설정합니다. 지원되는 연산식 범위는 내부 계산기를 기준으로 합니다. |
| `NumberFormatter` | `INumberFormatter?` | 읽기·쓰기 | `null` | 표시·파싱에 관여하는 사용자 지정 포맷터입니다. 구현체는 `INumberFormatter`를 제공하며 파싱까지 바꾸려면 관련 `INumberParser` 경로를 확인합니다. |
| `SpinButtonPlacementMode` | `NumberBoxSpinButtonPlacementMode` | 읽기·쓰기 | `NumberBoxSpinButtonPlacementMode.Inline` | 증감 버튼 배치입니다. `Hidden`은 숨김, `Inline`은 입력란 안쪽, `Compact`는 포커스 시 팝업을 사용하는 압축 배치입니다. |
| `ValidationMode` | `NumberBoxValidationMode` | 읽기·쓰기 | `NumberBoxValidationMode.InvalidInputOverwritten` | `InvalidInputOverwritten`은 잘못된 입력을 정규화하고 범위를 적용합니다. `Disabled`는 기본 유효성 검사를 끕니다. 입력 제약이 필요하면 기본 모드를 유지합니다. |

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
| `Text` | `string` | 현재 표시 문자열입니다. 숫자 모델에는 Value를 바인딩합니다. |
| `IsReadOnly` | `bool` | 숫자 입력 편집 여부입니다. 스핀 동작과 전체 활성 상태도 함께 확인합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `NumberBoxSpinButtonPlacementMode`: `Hidden`, `Compact`, `Inline`.
- `NumberBoxValidationMode`: `InvalidInputOverwritten`, `Disabled`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

TextControl 계열 리소스를 바꾸면 입력부 색·여백·반지름을 조정할 수 있습니다. Inline·Compact·Hidden은 다른 증감 버튼 배치이며 Compact 팝업 영역은 입력 테두리와 별개의 템플릿 부분입니다. 스핀 아이콘·고정 폭까지 바꾸려면 현재 모드의 템플릿을 수정하고 PART 이름과 이벤트 연결을 보존합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example NumberBox_Resources -->
```xml
<ui:NumberBox Width="200" Value="3" Minimum="0" Maximum="10" SmallChange="0.5" MaxDecimalPlaces="1" SpinButtonPlacementMode="Inline"  x:Name="ResourceDemo">
    <ui:NumberBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:NumberBox.Resources>
</ui:NumberBox>
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
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `DefaultTextBoxScrollViewerStyle` | Style | PassiveScrollViewer#PART_ContentHost Style |
| `TextControlBackground` | SolidColorBrush | 컨트롤.Background |
| `TextControlBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `TextControlBackgroundFocused` | SolidColorBrush | ContentBorder.Background〔IsFocused=True〕 |
| `TextControlBackgroundPointerOver` | SolidColorBrush | ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsFocused=False〕 |
| `TextControlBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 / AccentBorder.BorderBrush〔IsEnabled=False〕 |
| `TextControlButtonForeground` | SolidColorBrush | Button#PART_ClearButton Foreground / Button#PART_CompactIncrementDecrementButton Foreground / RepeatButton#PART_InlineIncrementButton Foreground / RepeatButton#PART_InlineDecrementButton Foreground |
| `TextControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush |
| `TextControlFocusedBorderBrush` | SolidColorBrush | AccentBorder.BorderBrush〔IsFocused=True〕 |
| `TextControlForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.CaretBrush |
| `TextControlForegroundDisabled` | SolidColorBrush | ControlIconLeft.Foreground〔IsEnabled=False〕 / ControlIconRight.Foreground〔IsEnabled=False〕 / PlaceholderTextBox.Foreground〔IsEnabled=False〕 / 컨트롤.Foreground〔IsEnabled=False〕 |
| `TextControlPlaceholderForeground` | SolidColorBrush | TextBlock#PlaceholderTextBox Foreground |
| `TextControlThemeMinHeight` | Double | 컨트롤.MinHeight |
| `TextControlThemeMinWidth` | Double | 컨트롤.MinWidth |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultUiNumberBoxStyle` | Style | Style BasedOn |
| `NumberBoxAccentBorderThemeThickness` | Thickness | Border#AccentBorder BorderThickness |
| `NumberBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `NumberBoxButtonHeight` | Double | Button#PART_ClearButton Width / Button#PART_ClearButton Height / Button#PART_CompactIncrementDecrementButton Width / Button#PART_CompactIncrementDecrementButton Height / 외 4곳 |
| `NumberBoxButtonIconSize` | Double | SymbolIcon FontSize / RepeatButton#PART_InlineDecrementButton FontSize |
| `NumberBoxButtonMargin` | Thickness | Button#PART_ClearButton Margin / Button#PART_CompactIncrementDecrementButton Margin / RepeatButton#PART_InlineIncrementButton Margin / RepeatButton#PART_InlineDecrementButton Margin |
| `NumberBoxButtonPadding` | Thickness | Button#PART_ClearButton Padding / Button#PART_CompactIncrementDecrementButton Padding / RepeatButton#PART_InlineIncrementButton Padding / RepeatButton#PART_InlineDecrementButton Padding |
| `NumberBoxLeftIconMargin` | Thickness | ContentControl#ControlIconLeft Margin |
| `NumberBoxRightIconMargin` | Thickness | ContentControl#ControlIconRight Margin |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiNumberBoxStyle` | `controls:NumberBox` | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ClearButton` (Button), `PART_CompactDecrementButton` (Button), `PART_CompactIncrementButton` (Button), `PART_CompactIncrementDecrementButton` (Button), `PART_CompactIncrementDecrementFlyout` (Flyout), `PART_ContentHost` (PassiveScrollViewer), `PART_InlineDecrementButton` (RepeatButton), `PART_InlineIncrementButton` (RepeatButton). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `VerticalAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Icon` | `ContentControl#ControlIconLeft.Content` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Foreground` | `ContentControl#ControlIconLeft.Foreground` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Padding` | `Grid.Margin` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Foreground` | `PassiveScrollViewer#PART_ContentHost.TextElement.Foreground` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PlaceholderText` | `TextBlock#PlaceholderTextBox.Text` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Icon` | `ContentControl#ControlIconRight.Content` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Foreground` | `ContentControl#ControlIconRight.Foreground` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Border.CornerRadius` | `Border#AccentBorder.CornerRadius` | TemplateBinding | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Grid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ContentControl#ControlIconLeft.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ContentControl#ControlIconLeft.FontSize` | `16` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Grid#TextContentArea.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `TextBlock#PlaceholderTextBox.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `TextBlock#PlaceholderTextBox.Padding` | `1,0` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `StackPanel.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Button#PART_ClearButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `Button#PART_CompactIncrementDecrementButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `RepeatButton#PART_InlineIncrementButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `RepeatButton#PART_InlineDecrementButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ContentControl#ControlIconRight.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ContentControl#ControlIconRight.FontSize` | `16` | 직접 지정 / 현재 템플릿 | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_ClearButton.Margin` | `0` | ShowClearButton=False | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_ClearButton.Margin` | `0` | ClearButtonEnabled=False | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_InlineIncrementButton.Margin` | `0` | SpinButtonPlacementMode=Hidden | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_InlineDecrementButton.Margin` | `0` | SpinButtonPlacementMode=Hidden | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_CompactIncrementDecrementButton.Margin` | `0` | SpinButtonPlacementMode=Hidden | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_InlineIncrementButton.Margin` | `0` | SpinButtonPlacementMode=Compact | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_InlineDecrementButton.Margin` | `0` | SpinButtonPlacementMode=Compact | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_CompactIncrementDecrementButton.Margin` | `0` | SpinButtonPlacementMode=Inline | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ControlIconRight.Margin` | `0` | IconPlacement=Left | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ControlIconLeft.Margin` | `0` | IconPlacement=Right | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ControlIconRight.Margin` | `0` | Icon={x:Null} | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `ControlIconLeft.Margin` | `0` | Icon={x:Null} | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `AccentBorder.BorderThickness` | `0,0,0,2` | IsFocused=True | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |
| `PART_ClearButton.Margin` | `0` | IsReadOnly=True | [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiNumberBoxStyle |
| `ContextMenu` | `{DynamicResource DefaultControlContextMenu}` | DefaultUiNumberBoxStyle |
| `Foreground` | `{DynamicResource TextControlForeground}` | DefaultUiNumberBoxStyle |
| `CaretBrush` | `{DynamicResource TextControlForeground}` | DefaultUiNumberBoxStyle |
| `Cursor` | `Arrow` | DefaultUiNumberBoxStyle |
| `Background` | `{DynamicResource TextControlBackground}` | DefaultUiNumberBoxStyle |
| `BorderBrush` | `{DynamicResource TextControlElevationBorderBrush}` | DefaultUiNumberBoxStyle |
| `BorderThickness` | `{StaticResource NumberBoxBorderThemeThickness}` | DefaultUiNumberBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiNumberBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiNumberBoxStyle |
| `VerticalAlignment` | `Center` | DefaultUiNumberBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiNumberBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiNumberBoxStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultUiNumberBoxStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultUiNumberBoxStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiNumberBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiNumberBoxStyle |
| `ClearButtonEnabled` | `True` | DefaultUiNumberBoxStyle |
| `IconPlacement` | `Left` | DefaultUiNumberBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiNumberBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiNumberBoxStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `ValueChanged` | 숫자·별점 값 변경을 알립니다. 현재 값은 컨트롤의 `Value`를 읽습니다. |

## 동작과 주의 사항

`Value`는 `double?`이므로 빈 입력을 `null`로 처리합니다. 입력 텍스트와 숫자 변환 시점은 다르며 포커스를 잃을 때 정규화되는 경로도 있습니다. ViewModel은 `Value="{Binding Quantity, Mode=TwoWay}"`에 연결합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [NumberBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.cs)
- [NumberBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NumberBox/NumberBox.xaml)
- [Gallery: NumberBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/NumberBoxPage.xaml)
