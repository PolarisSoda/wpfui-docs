# TextBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
