# CardExpander

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

설정 헤더와 접을 수 있는 본문을 결합한 카드형 Expander입니다.

**타입:** `Wpf.Ui.Controls.CardExpander` · **기반:** `System.Windows.Controls.Expander`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:CardExpander x:Name="Demo" Header="고급 설정" IsExpanded="False" ContentPadding="16">
    <StackPanel><CheckBox Content="진단 정보 수집" /></StackPanel>
</ui:CardExpander>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsExpanded = true;
Demo.ContentPadding = new System.Windows.Thickness(24);
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `new CornerRadius(4)` | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |
| `ContentPadding` | `Thickness` | 읽기·쓰기 | `default(Thickness)` | 펼쳐진 본문 안쪽 여백입니다. 카드 전체 `Padding`과 헤더 영역을 따로 조정할 때 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Header` | `object` | 접힌 상태에서도 보이는 제목입니다. |
| `IsExpanded` | `bool` | 본문을 펼칠지 정합니다. |
| `ExpandDirection` | `ExpandDirection` | 본문이 확장되는 방향입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

공개 CornerRadius·ContentPadding·IsExpanded를 먼저 사용합니다. ControlCornerRadius를 Resources에서 바꾸는 경로도 있습니다. 원본은 CornerRadius·IsExpanded를 MultiBinding과 CornerRadiusSplitConverter에 전달해 헤더와 펼친 본문의 모서리를 위·아래로 분리합니다. Card의 Footer처럼 4로 고정하는 구조와 다릅니다. 아이콘·Chevron 크기 StaticResource는 로컬 재정의를 보장하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example CardExpander_Resources -->
```xml
<ui:CardExpander Header="고급 설정" IsExpanded="False" ContentPadding="16" x:Name="ResourceDemo">
    <ui:CardExpander.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:CardExpander.Resources>
    <StackPanel><CheckBox Content="진단 정보 수집" /></StackPanel>
</ui:CardExpander>
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
| `ControlCornerRadius` | CornerRadius | 컨트롤.CornerRadius |
| `CardBackground` | SolidColorBrush | 컨트롤.Background / Border#ContentPresenterBorder Background |
| `CardBackgroundDisabled` | SolidColorBrush | 컨트롤.Background〔IsEnabled=False〕 |
| `CardBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `CardBorderBrushDisabled` | SolidColorBrush | 컨트롤.BorderBrush〔IsEnabled=False〕 |
| `CardForeground` | SolidColorBrush | 컨트롤.Foreground |
| `CardForegroundDisabled` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=False〕 / ExpanderToggleButton.Foreground〔IsEnabled=False〕 |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `AnimationFactorToValueConverter` | AnimationFactorToValueConverter | MultiBinding Converter |
| `CardExpanderBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `CardExpanderChevronSize` | Double | SymbolIcon#ControlChevronIcon FontSize |
| `CardExpanderIconMargin` | Thickness | ContentControl#ControlIcon Margin |
| `CardExpanderIconSize` | Double | ContentControl#ControlIcon FontSize |
| `CardExpanderPadding` | Thickness | 컨트롤.Padding / 컨트롤.ContentPadding |
| `CornerRadiusSplitConverter` | CornerRadiusSplitConverter | MultiBinding Converter |
| `DefaultUiCardExpanderStyle` | Style | Style BasedOn |
| `DefaultUiCardExpanderToggleButtonStyle` | ControlTemplate | ToggleButton#ExpanderToggleButton Template |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiCardExpanderStyle` | `controls:CardExpander` | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Border#ToggleButtonBorder.Background` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `BorderBrush` | `Border#ToggleButtonBorder.BorderBrush` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `CornerRadius` | `Border.CornerRadius` | Binding / {StaticResource CornerRadiusSplitConverter} | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `IsExpanded` | `Border.CornerRadius` | Binding / {StaticResource CornerRadiusSplitConverter} | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Padding` | `ToggleButton#ExpanderToggleButton.Padding` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `VerticalContentAlignment` | `ToggleButton#ExpanderToggleButton.VerticalAlignment` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `FontSize` | `ToggleButton#ExpanderToggleButton.FontSize` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Foreground` | `ToggleButton#ExpanderToggleButton.Foreground` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `IsEnabled` | `ToggleButton#ExpanderToggleButton.IsEnabled` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Icon` | `ContentControl#ControlIcon.Content` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Foreground` | `ContentControl#ControlIcon.Foreground` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Header` | `ContentPresenter#HeaderContentPresenter.Content` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Foreground` | `ContentPresenter#HeaderContentPresenter.TextElement.Foreground` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `BorderBrush` | `Border#ContentPresenterBorder.BorderBrush` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ContentPadding` | `ContentPresenter#ContentPresenter.Margin` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Border#ToggleButtonBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ToggleButton#ExpanderToggleButton.Margin` | `0` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Border#ContentPresenterBorder.BorderThickness` | `1,0,1,1` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ControlIcon.Margin` | `0` | Icon={x:Null} | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiCardExpanderStyle |
| `Background` | `{DynamicResource CardBackground}` | DefaultUiCardExpanderStyle |
| `Foreground` | `{DynamicResource CardForeground}` | DefaultUiCardExpanderStyle |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | DefaultUiCardExpanderStyle |
| `BorderThickness` | `{StaticResource CardExpanderBorderThemeThickness}` | DefaultUiCardExpanderStyle |
| `Padding` | `{StaticResource CardExpanderPadding}` | DefaultUiCardExpanderStyle |
| `ContentPadding` | `{StaticResource CardExpanderPadding}` | DefaultUiCardExpanderStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiCardExpanderStyle |
| `VerticalAlignment` | `Center` | DefaultUiCardExpanderStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiCardExpanderStyle |
| `VerticalContentAlignment` | `Center` | DefaultUiCardExpanderStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiCardExpanderStyle |
| `FontWeight` | `Normal` | DefaultUiCardExpanderStyle |
| `CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiCardExpanderStyle |
| `IsExpanded` | `False` | DefaultUiCardExpanderStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiCardExpanderStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiCardExpanderStyle |

## 동작과 주의 사항

열림 상태는 상속된 `IsExpanded`입니다. `Expanded`·`Collapsed` 이벤트를 사용할 수 있습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CardExpander.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.cs)
- [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
