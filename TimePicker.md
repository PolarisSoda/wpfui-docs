# TimePicker

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

시간 선택용 공개 타입이지만 4.3.0의 선택 UI는 미완성입니다.

**타입:** `Wpf.Ui.Controls.TimePicker` · **기반:** `System.Windows.Controls.Primitives.ButtonBase`

> **4.3.0 구현 제한:** 이 타입은 미완성입니다. 아래 주의 사항을 먼저 확인하세요.

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TimePicker x:Name="Demo" Width="240" ClockIdentifier="Clock24Hour" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Time = new System.TimeSpan(9, 30, 0);
Demo.MinuteIncrement = 15;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Header` | `object?` | 읽기·쓰기 | `null` | 시간 입력의 헤더를 위한 저장 속성입니다. 4.3.0 기본 템플릿은 이 값을 표시하지 않습니다. |
| `Time` | `TimeSpan` | 읽기·쓰기 | `TimeSpan.Zero` | 시간 값을 저장하지만 4.3.0 기본 템플릿의 hour·minute 표시에 연결되어 있지 않습니다. |
| `SelectedTime` | `TimeSpan?` | 읽기·쓰기 | `null` | 선택 시간을 위한 nullable 저장 속성입니다. 4.3.0에는 실제 선택 UI·동기화 구현이 없습니다. |
| `MinuteIncrement` | `int` | 읽기·쓰기 | `1` | 분 증가 간격을 위한 저장 속성입니다. 4.3.0 미완성 템플릿에서 분 선택 동작을 제공하지 않습니다. |
| `ClockIdentifier` | `ClockIdentifier` | 읽기·쓰기 | `ClockIdentifier.Clock24Hour` | 12·24시간제 설정입니다. 기본 템플릿의 24시간제 트리거는 AM 열을 숨기지만 실제 시각 표시·선택까지 구현하지는 않습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ClockIdentifier`: `Clock12Hour`, `Clock24Hour`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiTimePickerStyle |
| `ContextMenu` | `{DynamicResource DefaultControlContextMenu}` | DefaultUiTimePickerStyle |
| `Foreground` | `{DynamicResource TimePickerButtonForegroundDefault}` | DefaultUiTimePickerStyle |
| `Background` | `{DynamicResource TimePickerButtonBackground}` | DefaultUiTimePickerStyle |
| `BorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | DefaultUiTimePickerStyle |
| `BorderThickness` | `{StaticResource TimePickerBorderThemeThickness}` | DefaultUiTimePickerStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiTimePickerStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiTimePickerStyle |
| `VerticalAlignment` | `Center` | DefaultUiTimePickerStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiTimePickerStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiTimePickerStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultUiTimePickerStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultUiTimePickerStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiTimePickerStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiTimePickerStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiTimePickerStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiTimePickerStyle |

## 동작과 주의 사항

이 코드는 속성 저장 예제입니다. 화면에는 고정된 `hour`·`minute` 문구와 `Todo` 팝업이 있으며 실제 시간 표시·선택·동기화를 구현하지 않습니다. 실사용 시간 입력에는 검증된 다른 컨트롤 또는 NumberBox 조합을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TimePicker.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.cs)
- [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml)
- [Gallery: TimePickerPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DateAndTime/TimePickerPage.xaml)
