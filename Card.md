# Card

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

본문과 선택적 하단 영역을 담는 카드 컨테이너입니다.

**타입:** `Wpf.Ui.Controls.Card` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Card x:Name="Demo" Padding="16">
    <TextBlock Text="최근 프로젝트" />
    <ui:Card.Footer><TextBlock Text="마지막 수정: 오늘" /></ui:Card.Footer>
</ui:Card>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Footer = "파일 3개";
Demo.Content = new System.Windows.Controls.TextBlock { Text = "프로젝트 목록" };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Footer` | `object?` | 읽기·쓰기 | `null` | 카드 아래쪽 별도 영역의 콘텐츠입니다. 본문과 구분된 상태·보조 설명을 넣습니다. |
| `HasFooter` | `bool` | 외부 읽기 전용 | `false` | `Footer`가 `null`이 아닌지에 따라 계산되는 상태입니다. 외부에서 직접 설정하지 않습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

가장 간단한 반지름 조정은 `Card.Resources`의 `ControlCornerRadius` 재정의입니다. 기본 스타일의 `Border.CornerRadius` → 내부 `ContentBorder.CornerRadius`로 이어집니다. 별도의 `Card.CornerRadius` CLR 속성은 없습니다.

**Footer가 있으면 예외입니다.** `HasFooter=True` 트리거가 본문을 `4,4,0,0`으로 바꾸고 FooterBorder는 `0,0,4,4`로 고정합니다. 이 경우 Resources·Border.CornerRadius 설정만으로 전체 반지름이 바뀌지 않습니다. [Footer 포함 12 DIP 카드 템플릿](examples/CustomizationLab/CardWithFooter.xaml)은 이 두 부분까지 수정한 완전한 예제입니다. 이 템플릿에 쓰는 `CustomCardTopRadius`·`CustomCardBottomRadius`는 예제가 정의한 키이며 원본 내장 키가 아닙니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example Card_Resources -->
```xml
<ui:Card Padding="16" x:Name="ResourceDemo">
    <ui:Card.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:Card.Resources>
    <TextBlock Text="반지름 12인 카드 (Footer 없음)" />
</ui:Card>
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
| `CardBackground` | SolidColorBrush | 컨트롤.Background |
| `CardBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `CardFooterBackground` | SolidColorBrush | Border#FooterBorder Background |
| `CardForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `CardBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `CardPadding` | Thickness | 컨트롤.Padding |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `Border#ContentBorder.Padding` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Padding` | `Border#FooterBorder.Padding` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `BorderBrush` | `Border#FooterBorder.BorderBrush` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Footer` | `ContentPresenter#FooterContentPresenter.Content` | TemplateBinding | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Border#FooterBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `Border#FooterBorder.CornerRadius` | `0,0,4,4` | 직접 지정 / 현재 템플릿 | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `ContentBorder.CornerRadius` | `4,4,0,0` | HasFooter=True | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |
| `ContentBorder.BorderThickness` | `1,1,1,0` | HasFooter=True | [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `{DynamicResource CardBackground}` | 암시적 스타일 |
| `Foreground` | `{DynamicResource CardForeground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | 암시적 스타일 |
| `BorderThickness` | `{StaticResource CardBorderThemeThickness}` | 암시적 스타일 |
| `Padding` | `{StaticResource CardPadding}` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalAlignment` | `Center` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `False` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

카드 자체는 실행 버튼이 아닙니다. 클릭 동작이 필요하면 CardAction·CardControl을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Card.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.cs)
- [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
