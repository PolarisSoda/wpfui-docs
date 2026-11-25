# ProgressRing

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

원형 진행률 또는 회전하는 대기 상태를 표시합니다.

**타입:** `Wpf.Ui.Controls.ProgressRing` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ProgressRing x:Name="Demo" Width="48" Height="48" Progress="35" IsIndeterminate="False" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Progress = 80;
Demo.IsIndeterminate = true;
Demo.CoverRingVisibility = System.Windows.Visibility.Collapsed;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Progress` | `double` | 읽기·쓰기 | `50d` | 진행률(0~100)입니다. 변경 시 그리는 각도를 계산하며 범위 밖 값은 그릴 때만 제한합니다. `Progress` 자체가 보정되는 것은 아닙니다. |
| `IsIndeterminate` | `bool` | 읽기·쓰기 | `false` | `true`이면 완료 비율 대신 회전하는 대기 표시를 사용합니다. 계산 가능한 진행률이 있으면 `false`로 둡니다. |
| `EngAngle` | `double` | 읽기·쓰기 | `180.0d` | 실제 API 이름이 `EngAngle`입니다. 확정 진행률의 끝 각도이며 `Progress` 변경 시 덮어씁니다. 일반 코드는 `Progress`를 설정합니다. |
| `IndeterminateAngle` | `double` | 읽기·쓰기 | `180.0d` | 불확정 상태의 호 끝 각도입니다. 기본 애니메이션이 관여하므로 템플릿 조정 시 사용합니다. |
| `CoverRingStroke` | `Brush` | 읽기·쓰기 | `Brushes.Black` | 뒤쪽 전체 링의 브러시입니다. 진행 호의 전경색과 구별합니다. |
| `CoverRingVisibility` | `System.Windows.Visibility` | 읽기·쓰기 | `System.Windows.Visibility.Visible` | 뒤쪽 전체 링의 표시 상태입니다. `Collapsed`로 설정하면 진행 호만 남깁니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

진행 호는 Foreground, 뒤쪽 링은 CoverRingStroke·CoverRingVisibility로 먼저 조정합니다. 기본 스타일이 ProgressRingForegroundThemeBrush·ProgressRingBackgroundThemeBrush를 DynamicResource로 공급하므로 두 리소스를 따로 재정의할 수도 있습니다. 호 두께·애니메이션 구조는 템플릿의 고정값과 Arc 연결을 수정해야 합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ProgressRingBackgroundThemeBrush`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ProgressRing_Resources -->
```xml
<ui:ProgressRing Width="48" Height="48" Progress="35" IsIndeterminate="False"  x:Name="ResourceDemo">
    <ui:ProgressRing.Resources>
        <SolidColorBrush x:Key="ProgressRingBackgroundThemeBrush" Color="#2563EB" />
    </ui:ProgressRing.Resources>
</ui:ProgressRing>
```

```csharp
ResourceDemo.Resources["ProgressRingBackgroundThemeBrush"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 진행 호와 뒤쪽 링을 따로 조정

<!-- customization:example ProgressRing_Recipe1 -->
```xml
<ui:ProgressRing Progress="65" Width="48" Height="48">
    <ui:ProgressRing.Resources>
        <SolidColorBrush x:Key="ProgressRingForegroundThemeBrush" Color="#2563EB" />
        <SolidColorBrush x:Key="ProgressRingBackgroundThemeBrush" Color="#DBEAFE" />
    </ui:ProgressRing.Resources>
</ui:ProgressRing>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ProgressRingBackgroundThemeBrush` | SolidColorBrush | 컨트롤.CoverRingStroke |
| `ProgressRingForegroundThemeBrush` | SolidColorBrush | 컨트롤.Foreground |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ProgressThicknessConverter` | ProgressThicknessConverter | Arc StrokeThickness / Arc StrokeThickness〔IsIndeterminate=True〕 / Arc#Arc StrokeThickness〔IsIndeterminate=True〕 |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Width` | `Grid.Width` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `Height` | `Grid.Height` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `CoverRingStroke` | `Arc.Stroke` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `Height` | `Arc.StrokeThickness` | Binding to TemplatedParent | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `CoverRingVisibility` | `Arc.Visibility` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `EngAngle` | `Arc.EndAngle` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `Foreground` | `Arc.Stroke` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `IndeterminateAngle` | `Arc#Arc.EndAngle` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `Foreground` | `Arc#Arc.Stroke` | TemplateBinding | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `Height` | `Arc#Arc.StrokeThickness` | Binding to TemplatedParent | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Height` | `60` | 직접 지정 / 현재 템플릿 | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |
| `컨트롤.Width` | `60` | 직접 지정 / 현재 템플릿 | [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Height` | `60` | 암시적 스타일 |
| `Width` | `60` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `Foreground` | `{DynamicResource ProgressRingForegroundThemeBrush}` | 암시적 스타일 |
| `CoverRingStroke` | `{DynamicResource ProgressRingBackgroundThemeBrush}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

일반 WPF ProgressBar의 `Value`가 아니라 `Progress`를 사용합니다. 값이 100 이상이면 완전한 호 대신 359도로 그리는 구현입니다. 실제 속성 이름 `EngAngle`은 오타처럼 보여도 그대로 사용해야 합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ProgressRing.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.cs)
- [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml)
- [Gallery: ProgressRingPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/ProgressRingPage.xaml)
