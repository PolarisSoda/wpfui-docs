# Button

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

아이콘과 의미별 색상을 지원하는 실행 버튼입니다. 클릭 한 번으로 작업을 수행할 때 사용합니다.

**타입:** `Wpf.Ui.Controls.Button` · **기반:** `System.Windows.Controls.Button`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Button x:Name="Demo" Content="저장" Appearance="Primary">
    <ui:Button.Icon><ui:SymbolIcon Symbol="Save24" /></ui:Button.Icon>
</ui:Button>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Content = "저장 완료";
Demo.Appearance = ui.ControlAppearance.Success;
Demo.IsEnabled = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `Appearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Primary` | 테마의 의미별 색을 선택합니다. `Primary`는 강조, `Secondary`는 일반 보조 동작, `Danger`는 위험 동작에 적합합니다. 실제 색은 테마 리소스가 결정합니다. |
| `MouseOverBackground` | `Brush` | 읽기·쓰기 | `Border.BackgroundProperty.DefaultMetadata.DefaultValue` | 마우스가 올라간 동안 사용할 배경 브러시입니다. 일반 상태의 `Background`와 구분됩니다. |
| `MouseOverBorderBrush` | `Brush` | 읽기·쓰기 | `Border.BorderBrushProperty.DefaultMetadata.DefaultValue` | 마우스가 올라간 동안 사용할 테두리 브러시입니다. `BorderThickness`가 0이면 테두리는 보이지 않습니다. |
| `PressedForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 누르는 동안의 텍스트·아이콘 전경색입니다. |
| `PressedBackground` | `Brush` | 읽기·쓰기 | `Border.BackgroundProperty.DefaultMetadata.DefaultValue` | 누르는 동안의 배경 브러시입니다. |
| `PressedBorderBrush` | `Brush` | 읽기·쓰기 | `Border.BorderBrushProperty.DefaultMetadata.DefaultValue` | 누르는 동안의 테두리 브러시입니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `default(CornerRadius)` | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Command` | `ICommand` | 실행할 ViewModel 명령입니다. CanExecute=false이면 버튼이 비활성화될 수 있습니다. |
| `CommandParameter` | `object` | 명령에 전달할 데이터입니다. |
| `ClickMode` | `ClickMode` | Release·Press·Hover 중 클릭을 발생시킬 시점을 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ControlAppearance`: `Primary`, `Secondary`, `Info`, `Dark`, `Light`, `Danger`, `Success`, `Caution`, `Transparent`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

모서리는 공개 `CornerRadius` 속성으로 직접 바꾸거나 `Resources["ControlCornerRadius"]`로 기본 스타일 값을 바꿀 수 있습니다. 상태별 색까지 맞추려면 Normal·PointerOver·Pressed·Disabled 키를 구분합니다. `Appearance=Primary`는 AccentButton 계열, `Secondary`는 Button 계열의 색을 주로 사용하므로 ButtonBackground만 바꾸어 Primary 버튼 색이 바뀐다고 가정하지 않습니다. 직접 지정한 Background·CornerRadius 로컬 값은 스타일의 리소스 경로보다 우선할 수 있습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example Button_Resources -->
```xml
<ui:Button Content="저장" Appearance="Primary" x:Name="ResourceDemo">
    <ui:Button.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:Button.Resources>
    <ui:Button.Icon><ui:SymbolIcon Symbol="Save24" /></ui:Button.Icon>
</ui:Button>
```

```csharp
ResourceDemo.Resources["ControlCornerRadius"] = new System.Windows.CornerRadius(12);
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 상태별 강조색을 한 버튼에 적용

<!-- customization:example Button_Recipe1 -->
```xml
<ui:Button Content="저장" Appearance="Primary">
    <ui:Button.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
        <SolidColorBrush x:Key="AccentButtonBackground" Color="#2563EB" />
        <SolidColorBrush x:Key="AccentButtonBackgroundPointerOver" Color="#1D4ED8" />
        <SolidColorBrush x:Key="AccentButtonBackgroundPressed" Color="#1E40AF" />
    </ui:Button.Resources>
</ui:Button>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | 컨트롤.CornerRadius / 컨트롤.Border.CornerRadius |
| `AccentButtonBackground` | SolidColorBrush | 컨트롤.Background〔Appearance=Primary〕 |
| `AccentButtonBackgroundPointerOver` | SolidColorBrush | 컨트롤.MouseOverBackground〔Appearance=Primary〕 |
| `AccentButtonBackgroundPressed` | SolidColorBrush | 컨트롤.PressedBackground〔Appearance=Primary〕 |
| `AccentButtonForeground` | SolidColorBrush | 컨트롤.Foreground〔Appearance=Primary〕 |
| `AccentButtonForegroundPointerOver` | SolidColorBrush | 컨트롤.PressedForeground〔Appearance=Primary〕 |
| `AccentControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush〔Appearance=Primary〕 / 컨트롤.MouseOverBorderBrush〔Appearance=Primary〕 / 컨트롤.BorderBrush〔Appearance=Dark〕 / 컨트롤.MouseOverBorderBrush〔Appearance=Dark〕 / 외 8곳 |
| `ButtonBackground` | SolidColorBrush | 컨트롤.Background |
| `ButtonBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 / 컨트롤.Background〔IsEnabled=False〕 |
| `ButtonBackgroundPointerOver` | SolidColorBrush | 컨트롤.MouseOverBackground / ContentBorder.Background〔IsMouseOver=True; IsPressed=False〕 |
| `ButtonBackgroundPressed` | SolidColorBrush | 컨트롤.PressedBackground / ContentBorder.Background〔IsMouseOver=True; IsPressed=True〕 |
| `ButtonBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 |
| `ButtonBorderBrushPressed` | SolidColorBrush | 컨트롤.PressedBorderBrush / ContentBorder.BorderBrush〔IsMouseOver=True; IsPressed=True〕 |
| `ButtonForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ButtonForegroundDisabled` | SolidColorBrush | 컨트롤.Foreground〔IsEnabled=False〕 / Icon.TextElement.Foreground〔IsEnabled=False〕 / ContentPresenter.TextElement.Foreground〔IsEnabled=False〕 |
| `ButtonForegroundPressed` | SolidColorBrush | 컨트롤.PressedForeground / ContentPresenter.TextElement.Foreground〔IsMouseOver=True; IsPressed=True〕 |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush / 컨트롤.MouseOverBorderBrush / ContentBorder.BorderBrush〔IsMouseOver=True; IsPressed=False〕 |
| `ControlFillColorTransparentBrush` | SolidColorBrush | 컨트롤.PressedBorderBrush〔Appearance=Primary〕 |
| `ControlStrongFillColorDark` | Color | SolidColorBrush Color〔Appearance=Dark〕 |
| `ControlStrongFillColorLight` | Color | SolidColorBrush Color〔Appearance=Light〕 |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `PaletteGreenColor` | Color | SolidColorBrush Color〔Appearance=Success〕 |
| `PaletteLightBlueColor` | Color | SolidColorBrush Color〔Appearance=Info〕 |
| `PaletteOrangeColor` | Color | SolidColorBrush Color〔Appearance=Caution〕 |
| `PaletteRedColor` | Color | SolidColorBrush Color〔Appearance=Danger〕 |
| `SubtleFillColorSecondaryBrush` | SolidColorBrush | LayoutRoot.Background〔IsMouseOver=True〕 |
| `SubtleFillColorTertiaryBrush` | SolidColorBrush | LayoutRoot.Background〔IsPressed=True〕 |
| `TextFillColorDarkPrimaryBrush` | SolidColorBrush | 컨트롤.Foreground〔Appearance=Light〕 |
| `TextFillColorDarkSecondaryBrush` | SolidColorBrush | 컨트롤.PressedForeground〔Appearance=Light〕 |
| `TextFillColorLightPrimaryBrush` | SolidColorBrush | 컨트롤.Foreground〔Appearance=Dark〕 / 컨트롤.Foreground〔Appearance=Info〕 |
| `TextFillColorLightSecondaryBrush` | SolidColorBrush | 컨트롤.PressedForeground〔Appearance=Dark〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ButtonBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `ButtonIconMargin` | Thickness | ContentPresenter#ControlIcon Margin |
| `ButtonPadding` | Thickness | 컨트롤.Padding |
| `DefaultButtonStyle` | Style | Style BasedOn |
| `DefaultRepeatButtonStyle` | Style | Style BasedOn |
| `DefaultUiButtonStyle` | Style | Style BasedOn |
| `PaneToggleButtonHeight` | Double | 컨트롤.MinHeight |
| `PaneToggleButtonThickness` | Thickness | 컨트롤.BorderThickness |
| `PaneToggleButtonWidth` | Double | 컨트롤.MinWidth |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiButtonStyle` | `controls:Button` | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `BasePaneButtonStyle` | `controls:Button` | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Padding` | `Border#InsetBorder.Padding` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `BorderThickness` | `Border#InsetBorder.BorderThickness` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `CornerRadius` | `Border#InsetBorder.CornerRadius` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Icon` | `ContentPresenter#ControlIcon.Content` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `FontSize` | `ContentPresenter#ControlIcon.TextElement.FontSize` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Foreground` | `ContentPresenter#ControlIcon.TextElement.Foreground` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ContentTemplate` | `ContentPresenter#ContentPresenter.ContentTemplate` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `Foreground` | `ContentPresenter#ContentPresenter.TextElement.Foreground` | TemplateBinding | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `MinWidth` | `Border#LayoutRoot.MinWidth` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `MinHeight` | `Border#LayoutRoot.MinHeight` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Padding` | `Border#LayoutRoot.Padding` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `HorizontalAlignment` | `Border#LayoutRoot.HorizontalAlignment` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `VerticalAlignment` | `Border#LayoutRoot.VerticalAlignment` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `BorderBrush` | `Border#LayoutRoot.BorderBrush` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `BorderThickness` | `Border#LayoutRoot.BorderThickness` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Border.CornerRadius` | `Border#LayoutRoot.CornerRadius` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Icon` | `ContentPresenter#Icon.Content` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Foreground` | `ContentPresenter#Icon.TextElement.Foreground` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Content` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `ContentTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `컨트롤.Background` | `Transparent` | Appearance=Transparent | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `InsetBorder.BorderThickness` | `0` | Appearance=Secondary | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ControlIcon.Margin` | `0` | Content={x:Null} | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ControlIcon.Margin` | `0` | Content= | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `ControlIcon.Margin` | `0` | Icon={x:Null} | [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `컨트롤.FontSize` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `컨트롤.Padding` | `10` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Border#LayoutRoot.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Border#LayoutRoot.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `ColumnDefinition#GridColumn1.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `ColumnDefinition#GridColumn2.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `ContentPresenter#Icon.Margin` | `0,0,20,0` | 직접 지정 / 현재 템플릿 | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `Icon.Margin` | `0` | Content={x:Null} | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `GridColumn1.Width` | `*` | Content={x:Null} | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |
| `GridColumn2.Width` | `0` | Content={x:Null} | [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiButtonStyle |
| `Background` | `{DynamicResource ButtonBackground}` | DefaultUiButtonStyle |
| `MouseOverBackground` | `{DynamicResource ButtonBackgroundPointerOver}` | DefaultUiButtonStyle |
| `PressedBackground` | `{DynamicResource ButtonBackgroundPressed}` | DefaultUiButtonStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | DefaultUiButtonStyle |
| `PressedForeground` | `{DynamicResource ButtonForegroundPressed}` | DefaultUiButtonStyle |
| `BorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | DefaultUiButtonStyle |
| `PressedBorderBrush` | `{DynamicResource ButtonBorderBrushPressed}` | DefaultUiButtonStyle |
| `MouseOverBorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | DefaultUiButtonStyle |
| `BorderThickness` | `{StaticResource ButtonBorderThemeThickness}` | DefaultUiButtonStyle |
| `Padding` | `{StaticResource ButtonPadding}` | DefaultUiButtonStyle |
| `HorizontalAlignment` | `Left` | DefaultUiButtonStyle |
| `VerticalAlignment` | `Center` | DefaultUiButtonStyle |
| `HorizontalContentAlignment` | `Center` | DefaultUiButtonStyle |
| `VerticalContentAlignment` | `Center` | DefaultUiButtonStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiButtonStyle |
| `FontWeight` | `Normal` | DefaultUiButtonStyle |
| `CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiButtonStyle |
| `Appearance` | `Secondary` | DefaultUiButtonStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiButtonStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiButtonStyle |
| `Background` | `Transparent` | BasePaneButtonStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | BasePaneButtonStyle |
| `BorderBrush` | `Transparent` | BasePaneButtonStyle |
| `BorderThickness` | `{StaticResource PaneToggleButtonThickness}` | BasePaneButtonStyle |
| `FontSize` | `16` | BasePaneButtonStyle |
| `MinHeight` | `{StaticResource PaneToggleButtonHeight}` | BasePaneButtonStyle |
| `MinWidth` | `{StaticResource PaneToggleButtonWidth}` | BasePaneButtonStyle |
| `Padding` | `10` | BasePaneButtonStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | BasePaneButtonStyle |
| `HorizontalAlignment` | `Stretch` | BasePaneButtonStyle |
| `VerticalAlignment` | `Top` | BasePaneButtonStyle |
| `HorizontalContentAlignment` | `Center` | BasePaneButtonStyle |
| `VerticalContentAlignment` | `Center` | BasePaneButtonStyle |
| `SnapsToDevicePixels` | `True` | BasePaneButtonStyle |
| `OverridesDefaultStyle` | `True` | BasePaneButtonStyle |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

업무 동작은 상속된 `Click` 또는 `Command`로 연결합니다. `Appearance`별 스타일 트리거와 직접 지정한 브러시가 함께 적용되므로 [공통 속성](CommonProperties.md)의 우선순위를 참고합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Button.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.cs)
- [Button.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Button/Button.xaml)
- [NavigationViewBasePaneButtonStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBasePaneButtonStyle.xaml)
- [Gallery: ButtonPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ButtonPage.xaml)
