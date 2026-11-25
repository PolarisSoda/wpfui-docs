# NumberBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
