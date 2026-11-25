# ToggleButton

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

눌린 상태가 유지되는 버튼입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ToggleButton x:Name="Demo" Content="고정" IsChecked="False" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsChecked = true;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `IsChecked` | `bool?` | true=선택, false=해제, null=미정 상태입니다. 바인딩 시 Mode=TwoWay를 명시할 수 있습니다. |
| `IsThreeState` | `bool` | 사용자 조작으로 미정 상태까지 순환할지 정합니다. |
| `Command / CommandParameter` | `ICommand / object` | 토글 시 실행할 명령과 전달 값입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

Checked·Unchecked와 Pressed·Disabled 색상이 구분됩니다. 공개 IsChecked·Content와 Style.Trigger를 먼저 사용하고, 상태별 리소스를 재정의해 테마 색을 바꿉니다. Button의 Appearance 타입 속성이 기본 WPF ToggleButton에 있다고 가정하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ToggleButton_Resources -->
```xml
<ToggleButton Content="고정" IsChecked="False"  x:Name="ResourceDemo">
    <ToggleButton.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ToggleButton.Resources>
</ToggleButton>
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
| `PopupCornerRadius` | CornerRadius | Border#DropDownBorder CornerRadius |
| `AccentControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush〔IsEnabled=True; IsChecked=True〕 |
| `ButtonBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `ButtonBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 |
| `ButtonForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ButtonForegroundDisabled` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=False〕 |
| `ComboBoxBackground` | SolidColorBrush | 컨트롤.Background |
| `ComboBoxBackgroundDisabled` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `ComboBoxBackgroundFocused` | SolidColorBrush | ContentBorder.Background〔IsEnabled=True; IsKeyboardFocusWithin=True; IsEditable=True〕 |
| `ComboBoxBackgroundPointerOver` | SolidColorBrush | ContentBorder.Background〔IsEnabled=True; IsMouseOver=True; IsKeyboardFocusWithin=False〕 |
| `ComboBoxBorderBrushDisabled` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 |
| `ComboBoxBorderBrushFocused` | SolidColorBrush | Border#AccentBorder BorderBrush |
| `ComboBoxDropDownBackground` | SolidColorBrush | Border#DropDownBorder Background |
| `ComboBoxDropDownBorderBrush` | SolidColorBrush | Border#DropDownBorder BorderBrush |
| `ComboBoxDropDownGlyphForeground` | SolidColorBrush | SymbolIcon#ChevronIcon Foreground |
| `ComboBoxForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.CaretBrush |
| `ComboBoxForegroundDisabled` | SolidColorBrush | 컨트롤.Foreground〔IsEnabled=False〕 |
| `ComboBoxItemBackgroundSelected` | SolidColorBrush | ContentBorder.Background〔IsHighlighted=True〕 |
| `ComboBoxItemForegroundSelected` | SolidColorBrush | PART_ContentPresenter.TextElement.Foreground〔IsSelected=True〕 |
| `ComboBoxItemMargin` | Thickness | Border Margin |
| `ComboBoxItemPillFillBrush` | SolidColorBrush | Rectangle#ActiveRectangle Fill |
| `ComboBoxPadding` | Thickness | 컨트롤.Padding |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush |
| `ControlFillColorDefault` | Color | SolidColorBrush Color |
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `DefaultSplitButtonToggleButtonStyle` | Style | ToggleButton Style |
| `DefaultTextBoxScrollViewerStyle` | Style | PassiveScrollViewer#PART_ContentHost Style |
| `MenuBorderColorDefaultBrush` | **정의 없음** | Border#DropDownBorder BorderBrush |
| `SystemAccentColor` | Color | SolidColorBrush Color |
| `SystemFillColorSolidNeutralBackground` | Color | SolidColorBrush Color |
| `TextControlThemeMinHeight` | Double | 컨트롤.MinHeight |
| `TextControlThemeMinWidth` | Double | 컨트롤.MinWidth |
| `TextFillColorTertiary` | Color | SolidColorBrush Color |
| `ToggleButtonBackground` | SolidColorBrush | 컨트롤.Background |
| `ToggleButtonBackgroundChecked` | SolidColorBrush | 컨트롤.Background〔IsEnabled=True; IsChecked=True〕 |
| `ToggleButtonBackgroundCheckedDisabled` | SolidColorBrush | 컨트롤.Background〔IsEnabled=False; IsChecked=True〕 |
| `ToggleButtonBackgroundCheckedPressed` | SolidColorBrush | 컨트롤.Background〔IsPressed=True; IsChecked=True〕 |
| `ToggleButtonBackgroundDisabled` | SolidColorBrush | 컨트롤.Background〔IsEnabled=False; IsChecked=False〕 |
| `ToggleButtonBackgroundPointerOver` | SolidColorBrush | 컨트롤.Background〔IsMouseOver=True; IsChecked=False〕 |
| `ToggleButtonBackgroundPressed` | SolidColorBrush | 컨트롤.Background〔IsPressed=True; IsChecked=False〕 |
| `ToggleButtonBorderBrushCheckedDisabled` | SolidColorBrush | 컨트롤.BorderBrush〔IsEnabled=False; IsChecked=True〕 |
| `ToggleButtonBorderBrushCheckedPressed` | SolidColorBrush | 컨트롤.BorderBrush〔IsPressed=True; IsChecked=True〕 |
| `ToggleButtonBorderBrushDisabled` | SolidColorBrush | 컨트롤.BorderBrush〔IsEnabled=False; IsChecked=False〕 |
| `ToggleButtonBorderBrushPressed` | SolidColorBrush | 컨트롤.BorderBrush〔IsPressed=True; IsChecked=False〕 |
| `ToggleButtonForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ToggleButtonForegroundChecked` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=True; IsChecked=True〕 |
| `ToggleButtonForegroundCheckedDisabled` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=False; IsChecked=True〕 |
| `ToggleButtonForegroundCheckedPointerOver` | SolidColorBrush | 컨트롤.Background〔IsMouseOver=True; IsChecked=True〕 |
| `ToggleButtonForegroundCheckedPressed` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsPressed=True; IsChecked=True〕 |
| `ToggleButtonForegroundDisabled` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=False; IsChecked=False〕 |
| `ToggleButtonForegroundPressed` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsPressed=True; IsChecked=False〕 |
| `TreeViewItemBackground` | SolidColorBrush | 컨트롤.Background |
| `TreeViewItemBackgroundPointerOver` | SolidColorBrush | Border.Background〔IsMouseOver=True〕 |
| `TreeViewItemBackgroundSelected` | SolidColorBrush | Border.Background〔IsSelected=True〕 |
| `TreeViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |
| `TreeViewItemSelectionIndicatorForeground` | SolidColorBrush | Rectangle#ActiveRectangle Fill |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ButtonIconMargin` | Thickness | ContentPresenter#ControlIcon Margin |
| `CardExpanderChevronSize` | Double | SymbolIcon#ControlChevronIcon FontSize |
| `ComboBoxAccentBorderThemeThickness` | Thickness | Border#AccentBorder BorderThickness |
| `ComboBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `ComboBoxChevronMargin` | Thickness | Grid Margin |
| `ComboBoxChevronSize` | Double | SymbolIcon#ChevronIcon FontSize |
| `ComboBoxItemContentMargin` | Thickness | 컨트롤.Padding |
| `ComboBoxPopupMinHeight` | Double | DropDownBorder.MinHeight〔HasItems=False〕 |
| `DefaultComboBoxItemStyle` | Style | Style BasedOn |
| `DefaultComboBoxStyle` | Style | Style BasedOn |
| `DefaultComboBoxTextBoxStyle` | Style | TextBox#PART_EditableTextBox Style |
| `DefaultComboBoxToggleButtonStyle` | Style | ToggleButton Style |
| `DefaultToggleButtonStyle` | Style | Style BasedOn |
| `DefaultTreeViewItemStyle` | Style | Style BasedOn |
| `DefaultUiButtonStyle` | Style | Style BasedOn |
| `DefaultUiSplitButtonStyle` | Style | Style BasedOn |
| `DefaultUiTreeViewItemStyle` | Style | Style BasedOn |
| `ExpandCollapseToggleButtonStyle` | Style | ToggleButton#Expander Style |
| `ExpanderChevronSize` | Double | SymbolIcon#ControlChevronIcon FontSize |
| `LeftSplitCornerRadiusConverter` | LeftSplitCornerRadiusConverter | Border CornerRadius |
| `LeftSplitThicknessConverter` | LeftSplitThicknessConverter | Border BorderThickness |
| `RightSplitCornerRadiusConverter` | RightSplitCornerRadiusConverter | Border CornerRadius |
| `RightSplitThicknessConverter` | RightSplitThicknessConverter | Border BorderThickness |
| `ToggleButtonBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `ToggleButtonPadding` | Thickness | 컨트롤.Padding |
| `ToolBarButtonBaseStyle` | Style | Style BasedOn |
| `ToolBarOverflowButtonStyle` | Style | ToggleButton Style |
| `ToolBarThumbStyle` | Style | Thumb#ToolBarThumb Style |
| `TreeViewItemChevronSize` | Double | SymbolIcon#ChevronIcon FontSize |
| `TreeViewItemFocusVisual` | 정의 없음 | 컨트롤.FocusVisualStyle |
| `TreeViewItemFontSize` | Double | 컨트롤.FontSize |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultComboBoxToggleButtonStyle` | `ToggleButton` | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `DefaultSplitButtonToggleButtonStyle` | `ToggleButton` | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `DefaultToggleButtonStyle` | `ToggleButton` | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `{x:Static ToolBar.ToggleButtonStyleKey}` | `ToggleButton` | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `ToolBarOverflowButtonStyle` | `ToggleButton` | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `ExpandCollapseToggleButtonStyle` | `ToggleButton` | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

`{x:Static ...}`·`{x:Type ...}` 형태는 문자열 키가 아닌 객체 키입니다. 예를 들어 ToolBar.ButtonStyleKey를 읽을 때는 `Style="{StaticResource {x:Static ToolBar.ButtonStyleKey}}"`처럼 중첩 마크업을 사용합니다. 일반 문자열처럼 같은 이름을 추가하는 방식과 다릅니다. [복합 키 사용 예](CustomizationGuide.md)를 확인합니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ContentHost` (ContentPresenter). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `DefaultUiCardExpanderToggleButtonStyle` | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) · 사전 루트 |
| (Style 내부 템플릿) | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) · 내부 정의 |
| `DefaultExpanderToggleButtonStyle` | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) · 사전 루트 |
| (Style 내부 템플릿) | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `Border.Padding` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Foreground` | `SymbolIcon#ControlChevronIcon.Foreground` | TemplateBinding | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Content` | `ContentPresenter#PART_ContentHost.Content` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ContentTemplate` | `ContentPresenter#PART_ContentHost.ContentTemplate` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ContentTemplateSelector` | `ContentPresenter#PART_ContentHost.ContentTemplateSelector` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Padding` | `Grid.Margin` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `FontSize` | `ContentPresenter#ContentPresenter.TextElement.FontSize` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `Foreground` | `SymbolIcon#ControlChevronIcon.Foreground` | TemplateBinding | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `Content` | `ContentPresenter#PART_ContentHost.Content` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `ContentTemplate` | `ContentPresenter#PART_ContentHost.ContentTemplate` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `ContentTemplateSelector` | `ContentPresenter#PART_ContentHost.ContentTemplateSelector` | TemplateBinding | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Padding` | `Border.Padding` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `BorderThickness` | `Border.BorderThickness` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Border.CornerRadius` | `Border.CornerRadius` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `FontSize` | `ContentPresenter#ContentPresenter.TextElement.FontSize` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Foreground` | `ContentPresenter#ContentPresenter.TextElement.Foreground` | TemplateBinding | [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml) |
| `Background` | `Border#Border.Background` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Foreground` | `SymbolIcon.Foreground` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Grid#ChevronGrid.Margin` | `0` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `Grid#ChevronGrid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [CardExpander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardExpander/CardExpander.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `컨트롤.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `컨트롤.Border.CornerRadius` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Grid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `Grid#ChevronGrid.Margin` | `0` | 직접 지정 / 현재 템플릿 | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `Grid#ChevronGrid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [Expander.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Expander/Expander.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `컨트롤.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `컨트롤.Border.CornerRadius` | `0` | 직접 지정 / 현재 템플릿 | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `Border#ContentBorder.Padding` | `11,0` | 직접 지정 / 현재 템플릿 | [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#Border.CornerRadius` | `0,3,3,0` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `SymbolIcon.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `컨트롤.Width` | `0` | IsEnabled=False | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Grid#ChevronContainer.Width` | `15` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `Grid#ChevronContainer.Height` | `15` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `Grid#ChevronContainer.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{x:Null}` | DefaultComboBoxToggleButtonStyle |
| `Foreground` | `{DynamicResource ComboBoxForeground}` | DefaultComboBoxToggleButtonStyle |
| `Background` | `Transparent` | DefaultComboBoxToggleButtonStyle |
| `BorderBrush` | `Transparent` | DefaultComboBoxToggleButtonStyle |
| `BorderThickness` | `0` | DefaultComboBoxToggleButtonStyle |
| `Border.CornerRadius` | `0` | DefaultComboBoxToggleButtonStyle |
| `SnapsToDevicePixels` | `True` | DefaultComboBoxToggleButtonStyle |
| `OverridesDefaultStyle` | `True` | DefaultComboBoxToggleButtonStyle |
| `FocusVisualStyle` | `{x:Null}` | DefaultSplitButtonToggleButtonStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | DefaultSplitButtonToggleButtonStyle |
| `Background` | `Transparent` | DefaultSplitButtonToggleButtonStyle |
| `BorderBrush` | `Transparent` | DefaultSplitButtonToggleButtonStyle |
| `BorderThickness` | `0` | DefaultSplitButtonToggleButtonStyle |
| `Border.CornerRadius` | `0` | DefaultSplitButtonToggleButtonStyle |
| `SnapsToDevicePixels` | `True` | DefaultSplitButtonToggleButtonStyle |
| `OverridesDefaultStyle` | `True` | DefaultSplitButtonToggleButtonStyle |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultToggleButtonStyle |
| `Background` | `{DynamicResource ToggleButtonBackground}` | DefaultToggleButtonStyle |
| `Foreground` | `{DynamicResource ToggleButtonForeground}` | DefaultToggleButtonStyle |
| `BorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | DefaultToggleButtonStyle |
| `BorderThickness` | `{StaticResource ToggleButtonBorderThemeThickness}` | DefaultToggleButtonStyle |
| `Padding` | `{StaticResource ToggleButtonPadding}` | DefaultToggleButtonStyle |
| `HorizontalAlignment` | `Left` | DefaultToggleButtonStyle |
| `VerticalAlignment` | `Center` | DefaultToggleButtonStyle |
| `HorizontalContentAlignment` | `Center` | DefaultToggleButtonStyle |
| `VerticalContentAlignment` | `Center` | DefaultToggleButtonStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultToggleButtonStyle |
| `FontWeight` | `Normal` | DefaultToggleButtonStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultToggleButtonStyle |
| `SnapsToDevicePixels` | `True` | DefaultToggleButtonStyle |
| `OverridesDefaultStyle` | `True` | DefaultToggleButtonStyle |
| `Background` | `Transparent` | ToolBarOverflowButtonStyle |
| `Cursor` | `Hand` | ToolBarOverflowButtonStyle |
| `SnapsToDevicePixels` | `True` | ToolBarOverflowButtonStyle |
| `OverridesDefaultStyle` | `True` | ToolBarOverflowButtonStyle |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | ExpandCollapseToggleButtonStyle |
| `Focusable` | `False` | ExpandCollapseToggleButtonStyle |
| `OverridesDefaultStyle` | `True` | ExpandCollapseToggleButtonStyle |
| `SnapsToDevicePixels` | `True` | ExpandCollapseToggleButtonStyle |

상속 이벤트: `Click` · `Checked` · `Unchecked` · `Indeterminate`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml)
- [SplitButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/SplitButton/SplitButton.xaml)
- [ToggleButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleButton/ToggleButton.xaml)
- [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml)
- [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml)
- [Gallery: ToggleButtonPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ToggleButtonPage.xaml)
