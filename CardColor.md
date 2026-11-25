# CardColor

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

색상과 이름·설명을 함께 보여 주는 색상 표본 카드입니다.

**타입:** `Wpf.Ui.Controls.CardColor` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:CardColor x:Name="Demo" Title="브랜드" Subtitle="#3366CC" Color="#3366CC" Width="200" Height="120" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Color = System.Windows.Media.Colors.Coral;
Demo.Subtitle = "Coral";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Title` | `string` | 읽기·쓰기 | `string.Empty` | 색상 표본의 이름입니다. |
| `Subtitle` | `string` | 읽기·쓰기 | `string.Empty` | 색상 값이나 용도를 표시할 보조 문자열입니다. |
| `SubtitleFontSize` | `double` | 읽기·쓰기 | `11.0d` | 보조 문자열의 글자 크기(DIP)입니다. |
| `Color` | `Color` | 읽기·쓰기 | `Color.FromArgb(0, 0, 0, 0)` | 표시할 단색입니다. 변경 시 새 `SolidColorBrush`를 만들어 `CardBrush`에 저장합니다. |
| `Brush` | `Brush` | 읽기·쓰기 | `Brushes.Transparent` | 그라데이션을 포함해 표시할 브러시입니다. 변경 시 `CardBrush`를 이 브러시로 덮어씁니다. `Color`와 둘 다 변경하면 마지막 변경이 적용됩니다. |
| `CardBrush` | `Brush` | 외부 읽기 전용 | `Brushes.Transparent` | 실제로 색상 표본에 표시하는 브러시입니다. `Color` 또는 `Brush` 변경으로 갱신되며 외부 쓰기는 허용되지 않습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 이 컨트롤의 Resources에서 바꾸기

`CardBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example CardColor_Resources -->
```xml
<ui:CardColor Title="브랜드" Subtitle="#3366CC" Color="#3366CC" Width="200" Height="120"  x:Name="ResourceDemo">
    <ui:CardColor.Resources>
        <SolidColorBrush x:Key="CardBackground" Color="#2563EB" />
    </ui:CardColor.Resources>
</ui:CardColor>
```

```csharp
ResourceDemo.Resources["CardBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `CardBackground` | SolidColorBrush | 컨트롤.Background |
| `CardBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `CardForeground` | SolidColorBrush | 컨트롤.Foreground |
| `CardForegroundPressed` | SolidColorBrush | TextBlock Foreground |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Border#CardBorder.Background` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `BorderBrush` | `Border#CardBorder.BorderBrush` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `CardBrush` | `Border.Background` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Title` | `TextBlock.Text` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `SubtitleFontSize` | `TextBlock.FontSize` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Subtitle` | `TextBlock.Text` | TemplateBinding | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#CardBorder.Padding` | `8` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Border#CardBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Border#CardBorder.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Border.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `Border.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `TextBlock.Margin` | `0,8,0,0` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `TextBlock.FontSize` | `16` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |
| `TextBlock.Margin` | `0` | 직접 지정 / 현재 템플릿 | [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource CardForeground}` | 암시적 스타일 |
| `Background` | `{DynamicResource CardBackground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | 암시적 스타일 |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

`Color`와 `Brush`는 변경 시 공통 출력인 `CardBrush`를 갱신합니다. 두 입력은 마지막 변경이 이깁니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CardColor.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.cs)
- [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
