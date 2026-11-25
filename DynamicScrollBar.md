# DynamicScrollBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

스크롤 중·마우스 상호작용 상태에 따라 외형이 변하는 ScrollBar입니다.

**타입:** `Wpf.Ui.Controls.DynamicScrollBar` · **기반:** `System.Windows.Controls.Primitives.ScrollBar`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:DynamicScrollBar x:Name="Demo" Orientation="Vertical" Minimum="0" Maximum="100" ViewportSize="20" Height="180" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = 40;
Demo.Timeout = 800;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsScrolling` | `bool` | 읽기·쓰기 | `false` | 스크롤 중인 상태입니다. 자동 상태 변경과 타이머에 사용되므로 일반 앱에서 직접 제어하기보다는 상태로 읽습니다. |
| `IsInteracted` | `bool` | 읽기·쓰기 | `false` | 포인터 상호작용 중인 상태입니다. 템플릿에서 스크롤바의 확대·강조에 사용합니다. |
| `Timeout` | `int` | 읽기·쓰기 | `1000` | 상호작용 상태를 해제하기까지의 대기 시간(밀리초)입니다. 0 이상의 값을 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Minimum / Maximum` | `double` | 스크롤 위치 범위입니다. |
| `Value` | `double` | 현재 위치입니다. |
| `ViewportSize` | `double` | 손잡이 크기 계산에 쓰는 뷰포트의 상대 크기입니다. |
| `Orientation` | `Orientation` | 스크롤바 방향입니다. |
| `SmallChange / LargeChange` | `double` | 한 줄·페이지 등 증감 동작의 변화량입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ScrollBarButtonBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example DynamicScrollBar_Resources -->
```xml
<ui:DynamicScrollBar Orientation="Vertical" Minimum="0" Maximum="100" ViewportSize="20" Height="180"  x:Name="ResourceDemo">
    <ui:DynamicScrollBar.Resources>
        <SolidColorBrush x:Key="ScrollBarButtonBackground" Color="#2563EB" />
    </ui:DynamicScrollBar.Resources>
</ui:DynamicScrollBar>
```

```csharp
ResourceDemo.Resources["ScrollBarButtonBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ScrollBarButtonArrowForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ScrollBarButtonBackground` | SolidColorBrush | Border#PART_Border Background / Border#Border Background |
| `ScrollBarThumbFill` | SolidColorBrush | 컨트롤.Background |
| `ScrollBarTrackFillPointerOver` | SolidColorBrush | Border#PART_Border Background |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DynamicButtonHoverAnimationDuration` | Duration | DoubleAnimation Duration〔IsMouseOver=True〕 |
| `DynamicHorizontalScrollBar` | ControlTemplate | 컨트롤.Template〔Orientation=Horizontal〕 |
| `DynamicLineButtonHeight` | Double | 컨트롤.Height |
| `DynamicLineButtonWidth` | Double | 컨트롤.Width |
| `DynamicScrollAnimationDuration` | Duration | DoubleAnimation Duration〔IsMouseOver=True〕 / DoubleAnimation Duration〔IsInteracted=True〕 |
| `DynamicScrollBarLineButton` | Style | RepeatButton#PART_ButtonScrollUp Style / RepeatButton#PART_ButtonScrollDown Style / RepeatButton#PART_ButtonScrollLeft Style / RepeatButton#PART_ButtonScrollRight Style |
| `DynamicScrollBarPageButton` | Style | RepeatButton Style |
| `DynamicScrollBarThumb` | Style | Thumb Style |
| `DynamicVerticalScrollBar` | ControlTemplate | 컨트롤.Template〔Orientation=Vertical〕 |
| `UiDynamicScrollBar` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `UiDynamicScrollBar` | `controls:DynamicScrollBar` | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_Border` (Border), `PART_ButtonScrollDown` (RepeatButton), `PART_ButtonScrollLeft` (RepeatButton), `PART_ButtonScrollRight` (RepeatButton), `PART_ButtonScrollUp` (RepeatButton), `PART_Track` (Track). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `DynamicVerticalScrollBar` | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) · 사전 루트 |
| `DynamicHorizontalScrollBar` | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `RowDefinition.MaxHeight` | `14` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `RowDefinition.Height` | `0.00001*` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Border#PART_Border.Width` | `12` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Border#PART_Border.CornerRadius` | `6` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Track#PART_Track.Width` | `6` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Thumb.Margin` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Thumb.Padding` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `ColumnDefinition.MaxWidth` | `18` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `ColumnDefinition.Width` | `0.00001*` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Border#PART_Border.Height` | `12` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `Track#PART_Track.Height` | `6` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Width` | `Auto` | Orientation=Horizontal | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Height` | `14` | Orientation=Horizontal | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Width` | `14` | Orientation=Vertical | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |
| `컨트롤.Height` | `Auto` | Orientation=Vertical | [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `Transparent` | UiDynamicScrollBar |
| `Margin` | `0` | UiDynamicScrollBar |
| `Padding` | `0` | UiDynamicScrollBar |
| `SnapsToDevicePixels` | `True` | UiDynamicScrollBar |
| `OverridesDefaultStyle` | `True` | UiDynamicScrollBar |

## 동작과 주의 사항

대개 DynamicScrollViewer 템플릿이 스크롤 범위와 값을 연결합니다. 단독 ScrollBar는 다른 콘텐츠를 자동 스크롤하지 않으므로 ValueChanged를 연결해야 합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [DynamicScrollBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.cs)
- [DynamicScrollBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollBar/DynamicScrollBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
