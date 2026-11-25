# TimePicker

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

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

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

색·테두리 리소스를 바꾸더라도 hour·minute·Todo로 남아 있는 시간 선택 기능이 완성되는 것은 아닙니다. 이 문서의 리소스 예제는 외형 조정만 설명하며 실제 시간 선택 기능의 검증 예제로 사용하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example TimePicker_Resources -->
```xml
<ui:TimePicker Width="240" ClockIdentifier="Clock24Hour"  x:Name="ResourceDemo">
    <ui:TimePicker.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:TimePicker.Resources>
</ui:TimePicker>
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
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush |
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `TextControlThemeMinHeight` | Double | 컨트롤.MinHeight |
| `TextControlThemeMinWidth` | Double | 컨트롤.MinWidth |
| `TimePickerButtonBackground` | SolidColorBrush | 컨트롤.Background |
| `TimePickerButtonBackgroundDisabled` | SolidColorBrush | 컨트롤.Background〔IsEnabled=False〕 |
| `TimePickerButtonBackgroundPointerOver` | SolidColorBrush | 컨트롤.Background〔IsMouseOver=True〕 |
| `TimePickerButtonBackgroundPressed` | SolidColorBrush | 컨트롤.Background〔IsPressed=True〕 |
| `TimePickerButtonBorderBrushDisabled` | SolidColorBrush | 컨트롤.BorderBrush〔IsEnabled=False〕 |
| `TimePickerButtonBorderBrushPressed` | SolidColorBrush | 컨트롤.BorderBrush〔IsPressed=True〕 |
| `TimePickerButtonForegroundDefault` | SolidColorBrush | 컨트롤.Foreground |
| `TimePickerButtonForegroundDisabled` | SolidColorBrush | 컨트롤.Foreground〔IsEnabled=False〕 |
| `TimePickerButtonForegroundPointerOver` | SolidColorBrush | 컨트롤.Foreground〔IsMouseOver=True〕 |
| `TimePickerButtonForegroundPressed` | SolidColorBrush | 컨트롤.Foreground〔IsPressed=True〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultUiTimePickerStyle` | Style | Style BasedOn |
| `TimePickerBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiTimePickerStyle` | `controls:TimePicker` | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Width` | `Grid.Width` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `HorizontalAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `VerticalAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `Foreground` | `TextBlock.Foreground` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `BorderBrush` | `Border#GridColumnMinute.BorderBrush` | TemplateBinding | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `TextBlock.Margin` | `6` | 직접 지정 / 현재 템플릿 | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |
| `Border#GridColumnMinute.BorderThickness` | `1,0,1,0` | 직접 지정 / 현재 템플릿 | [TimePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TimePicker/TimePicker.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

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
