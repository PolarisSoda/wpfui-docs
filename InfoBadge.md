# InfoBadge

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

짧은 숫자·문자열·상태 아이콘을 표시하는 작은 배지입니다.

**타입:** `Wpf.Ui.Controls.InfoBadge` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:InfoBadge x:Name="Demo" Value="3" Severity="Attention" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = "99+";
Demo.Severity = ui.InfoBadgeSeverity.Critical;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Severity` | `InfoBadgeSeverity` | 읽기·쓰기 | `InfoBadgeSeverity.Informational` | 의미별 배경색을 고릅니다. 기본 ValueInfoBadgeStyle에서는 텍스트 값 배경이 바뀌며 Severity만으로 상태 아이콘이 자동 생성되지는 않습니다. |
| `Value` | `string` | 읽기·쓰기 | `string.Empty` | 배지 안의 문자열입니다. 숫자 전용 타입이 아니므로 `99+` 같은 짧은 문자열도 사용할 수 있습니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `new CornerRadius(8)` | 등록된 모서리 반지름입니다. 기본 ValueInfoBadgeStyle은 StaticResource로 고정 반지름을 사용하므로 이 속성이 반영되지 않습니다. DotInfoBadgeStyle·IconInfoBadgeStyle은 CornerRadius를 TemplateBinding하므로 반영됩니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 아이콘을 저장합니다. 기본 암시적 스타일은 ValueInfoBadgeStyle이므로 아이콘을 보이려면 `Style="{StaticResource IconInfoBadgeStyle}"` 같은 아이콘 템플릿을 명시합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `InfoBadgeSeverity`: `Attention`, `Informational`, `Success`, `Caution`, `Critical`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

기본 암시적 스타일은 `ValueInfoBadgeStyle`입니다. 숫자 배지 반지름은 **StaticResource `ValueInfoBadgeStyleCornerRadius`**를 사용하므로 `CornerRadius=12` 또는 `InfoBadge.Resources`의 같은 키만으로 바뀐다고 안내해서는 안 됩니다. 숫자형 반지름 변경은 Value 템플릿을 복제·수정합니다.

반면 **`DotInfoBadgeStyle`·`IconInfoBadgeStyle`은 CornerRadius에 TemplateBinding**하므로 공개 CornerRadius가 반영됩니다. 아이콘형은 IconInfoBadgeStyle을 선택한 뒤 Icon을 넣고, 점형은 DotInfoBadgeStyle을 선택합니다. 두 경우는 문자열 Value를 표시하는 스타일과 다릅니다. `InfoBadgeInformationSeverityBackgroundBrush`라는 참조는 원본에서 발견되지만 같은 이름의 정의가 없습니다. 실제 정보 상태에는 `InfoBadgeInformationalSeverityBackgroundBrush`가 사용되므로 발견된 이름을 모두 정상 조정 키로 취급하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ButtonForeground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example InfoBadge_Resources -->
```xml
<ui:InfoBadge Value="3" Severity="Attention"  x:Name="ResourceDemo">
    <ui:InfoBadge.Resources>
        <SolidColorBrush x:Key="ButtonForeground" Color="#2563EB" />
    </ui:InfoBadge.Resources>
</ui:InfoBadge>
```

```csharp
ResourceDemo.Resources["ButtonForeground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 숫자·점·아이콘 스타일을 선택

<!-- customization:example InfoBadge_Recipe1 -->
```xml
<StackPanel Orientation="Horizontal">
    <ui:InfoBadge Value="3" Style="{StaticResource ValueInfoBadgeStyle}" />
    <ui:InfoBadge Margin="8,0" Style="{StaticResource DotInfoBadgeStyle}" Severity="Success" />
    <ui:InfoBadge Style="{StaticResource IconInfoBadgeStyle}" CornerRadius="12"
                  Icon="{ui:SymbolIcon Checkmark24}" />
</StackPanel>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ButtonForeground` | SolidColorBrush | 컨트롤.Foreground |
| `InfoBadgeAttentionSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Attention〕 |
| `InfoBadgeCautionSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Caution〕 |
| `InfoBadgeCriticalSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Critical〕 |
| `InfoBadgeInformationSeverityBackgroundBrush` | **정의 없음** | SolidColorBrush Color |
| `InfoBadgeInformationalSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Informational〕 |
| `InfoBadgeSuccessSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Success〕 |
| `InfoBadgeValueForeground` | SolidColorBrush | ContentPresenter#ControlIcon TextElement.Foreground / TextBlock#TextBlock Foreground |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `IconBadgeMargin` | Thickness | Border#ContentBorder Margin |
| `ValueInfoBadgeStyle` | Style | Style BasedOn |
| `ValueInfoBadgeStyleCornerRadius` | CornerRadius | Border#ContentBorder CornerRadius |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DotInfoBadgeStyle` | `controls:InfoBadge` | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `IconInfoBadgeStyle` | `controls:InfoBadge` | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `ValueInfoBadgeStyle` | `controls:InfoBadge` | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Opacity` | `Border#ContentBorder.Opacity` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Icon` | `ContentPresenter#ControlIcon.Content` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `FontSize` | `ContentPresenter#ControlIcon.TextElement.FontSize` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `FontSize` | `TextBlock#TextBlock.FontSize` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Value` | `TextBlock#TextBlock.Text` | TemplateBinding | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Width` | `6` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Border#ContentBorder.Height` | `6` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Border#ContentBorder.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `ContentPresenter#ControlIcon.Margin` | `10` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Border#ContentBorder.MinWidth` | `16` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Border#ContentBorder.MinHeight` | `16` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |
| `Border#ContentBorder.Padding` | `3,0` | 직접 지정 / 현재 템플릿 | [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Focusable` | `False` | DotInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | DotInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | DotInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | DotInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | DotInfoBadgeStyle |
| `FontWeight` | `Normal` | DotInfoBadgeStyle |
| `Focusable` | `False` | IconInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | IconInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | IconInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | IconInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | IconInfoBadgeStyle |
| `FontWeight` | `Normal` | IconInfoBadgeStyle |
| `Focusable` | `False` | ValueInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | ValueInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | ValueInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | ValueInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | ValueInfoBadgeStyle |
| `FontWeight` | `Normal` | ValueInfoBadgeStyle |

## 동작과 주의 사항

InfoBar의 Severity 타입과 값이 다릅니다. 기본 스타일은 문자열 Value를 표시합니다. 아이콘형은 Style="{StaticResource IconInfoBadgeStyle}"을 지정하고 Icon을 넣습니다. CornerRadius는 기본 숫자형에서는 반영되지 않지만 DotInfoBadgeStyle·IconInfoBadgeStyle에서는 반영됩니다. 탐색 메뉴 알림에는 NavigationViewItem.InfoBadge에 배치합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [InfoBadge.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.cs)
- [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml)
- [Gallery: InfoBadgePage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/InfoBadgePage.xaml)
