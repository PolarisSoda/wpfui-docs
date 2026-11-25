# Slider

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

연속·틱 간격의 숫자 범위를 조절합니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Slider x:Name="Demo" Width="240" Minimum="0" Maximum="100" Value="35" TickFrequency="5" IsSnapToTickEnabled="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = 70;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Minimum / Maximum` | `double` | 허용 범위의 하한·상한입니다. |
| `Value` | `double` | 현재 범위 값입니다. |
| `SmallChange / LargeChange` | `double` | 작은·큰 증감 동작의 변화량입니다. |
| `Orientation` | `Orientation` | 가로·세로 배치입니다. |
| `TickFrequency / IsSnapToTickEnabled` | `double / bool` | 틱 간격과 틱에 맞춰 값이 이동할지 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

트랙·손잡이·눈금 색은 SliderTrackFill·SliderThumbBackground·SliderTickBarFill 계열 키로 나뉩니다. 큰 막대 두께·손잡이 크기는 템플릿 내 고정 Width·Height를 수정해야 할 수 있습니다. Range의 PART_Track·Thumb·Decrease/Increase 버튼 연결을 유지합니다.

### 이 컨트롤의 Resources에서 바꾸기

`SliderTickBarFill`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example Slider_Resources -->
```xml
<Slider Width="240" Minimum="0" Maximum="100" Value="35" TickFrequency="5" IsSnapToTickEnabled="True"  x:Name="ResourceDemo">
    <Slider.Resources>
        <SolidColorBrush x:Key="SliderTickBarFill" Color="#2563EB" />
    </Slider.Resources>
</Slider>
```

```csharp
ResourceDemo.Resources["SliderTickBarFill"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `SliderOuterThumbBackground` | SolidColorBrush | 컨트롤.Background |
| `SliderThumbBackground` | SolidColorBrush | 컨트롤.Foreground |
| `SliderThumbBackgroundPointerOver` | SolidColorBrush | Thumb.Foreground〔IsMouseOver=True〕 |
| `SliderTickBarFill` | SolidColorBrush | TickBar#TopTick Fill / TickBar#BottomTick Fill |
| `SliderTrackFill` | SolidColorBrush | Border#TrackBackground Background |
| `SliderTrackFillPointerOver` | SolidColorBrush | TrackBackground.Background〔IsMouseOver=True〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `UiHorizontalSlider` | ControlTemplate | 컨트롤.Template〔Orientation=Horizontal〕 |
| `UiSliderButtonStyle` | Style | RepeatButton Style |
| `UiSliderThumbStyle` | Style | Thumb#Thumb Style |
| `UiVerticalSlider` | ControlTemplate | 컨트롤.Template〔Orientation=Vertical〕 |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_Track` (Track). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `UiHorizontalSlider` | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) · 사전 루트 |
| `UiVerticalSlider` | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `MinHeight` | `RowDefinition.MinHeight` | TemplateBinding | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `MinWidth` | `ColumnDefinition.MinWidth` | TemplateBinding | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `TickBar#TopTick.Height` | `6` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `Border#TrackBackground.Height` | `4` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `Border#TrackBackground.Margin` | `0` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `Border#TrackBackground.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `Border#TrackBackground.CornerRadius` | `2` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `TickBar#BottomTick.Height` | `6` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `TickBar#TopTick.Width` | `6` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `Border#TrackBackground.Width` | `4` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `TickBar#BottomTick.Width` | `6` | 직접 지정 / 현재 템플릿 | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `컨트롤.MinWidth` | `104` | Orientation=Horizontal | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `컨트롤.MinHeight` | `21` | Orientation=Horizontal | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `컨트롤.MinWidth` | `21` | Orientation=Vertical | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |
| `컨트롤.MinHeight` | `104` | Orientation=Vertical | [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Slider.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Slider/Slider.xaml)
- [Gallery: SliderPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/SliderPage.xaml)
