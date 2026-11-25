# ComboBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

목록에서 값을 선택하는 드롭다운입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ComboBox x:Name="Demo" Width="200" SelectedIndex="0"><ComboBoxItem Content="자동" /><ComboBoxItem Content="수동" /></ComboBox>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.SelectedIndex = 1;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |
| `SelectedItem / SelectedValue` | `object` | 선택 데이터 또는 SelectedValuePath로 지정한 멤버 값입니다. |
| `SelectedValuePath` | `string` | 선택 데이터에서 결과 값으로 사용할 멤버 경로입니다. |
| `IsEditable` | `bool` | 목록 외 문자열을 입력할 수 있게 합니다. |
| `IsDropDownOpen` | `bool` | 선택 팝업의 열림 상태입니다. |
| `Text` | `string` | 편집 가능한 ComboBox의 입력·표시 문자열입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

입력·선택 영역과 드롭다운 Popup의 색상·테두리·반지름은 서로 다른 템플릿 부분입니다. ControlCornerRadius와 PopupCornerRadius, ComboBoxBackground와 ComboBoxDropDownBackground 등을 구분합니다. IsEditable에 따라 텍스트 입력 템플릿도 달라집니다. ItemTemplate은 데이터 표시, ItemContainerStyle은 ComboBoxItem 외형입니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ComboBox_Resources -->
```xml
<ComboBox Width="200" SelectedIndex="0" x:Name="ResourceDemo">
    <ComboBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ComboBox.Resources><ComboBoxItem Content="자동" /><ComboBoxItem Content="수동" /></ComboBox>
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
| `ControlCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius / Border#DGR_Border CornerRadius / Border#HeaderBorder CornerRadius / Border CornerRadius |
| `PopupCornerRadius` | CornerRadius | Border#DropDownBorder CornerRadius |
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
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush / 컨트롤.HorizontalGridLinesBrush / 컨트롤.VerticalGridLinesBrush |
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `DefaultTextBoxScrollViewerStyle` | Style | PassiveScrollViewer#PART_ContentHost Style |
| `ListViewItemBackgroundPointerOver` | SolidColorBrush | DGR_Border.Background〔IsEnabled=True; IsMouseOver=True〕 / DGR_Border.Background〔IsSelected=True〕 / HeaderBorder.Background〔IsMouseOver=True〕 |
| `ListViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ListViewItemPillFillBrush` | SolidColorBrush | Rectangle#ActiveRectangle Fill |
| `SubtleFillColorDisabledBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |
| `SubtleFillColorSecondaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |
| `SubtleFillColorTertiaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value / HeaderBorder.Background〔IsPressed=True〕 / 컨트롤.Background |
| `SubtleFillColorTransparentBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |
| `SystemFillColorCriticalBrush` | SolidColorBrush | SymbolIcon Foreground |
| `TextControlForeground` | SolidColorBrush | 컨트롤.Foreground |
| `TextControlThemeMinHeight` | Double | 컨트롤.MinHeight |
| `TextControlThemeMinWidth` | Double | 컨트롤.MinWidth |
| `TextFillColorDisabledBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value / 컨트롤.TextElement.Foreground〔IsEnabled=False〕 |
| `TextFillColorSecondaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |
| `TextFillColorTertiaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `BodyTextBlockStyle` | Style | Style BasedOn |
| `BooleanToVisibilityConverter` | BooleanToVisibilityConverter | Control Visibility |
| `ColumnHeaderGripperStyle` | Style | Thumb#PART_LeftHeaderGripper Style / Thumb#PART_RightHeaderGripper Style |
| `ComboBoxAccentBorderThemeThickness` | Thickness | Border#AccentBorder BorderThickness |
| `ComboBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `ComboBoxChevronMargin` | Thickness | Grid Margin / SymbolIcon Margin |
| `ComboBoxChevronSize` | Double | SymbolIcon#ChevronIcon FontSize / SymbolIcon FontSize |
| `ComboBoxItemContentMargin` | Thickness | 컨트롤.Padding |
| `ComboBoxPopupMinHeight` | Double | DropDownBorder.MinHeight〔HasItems=False〕 |
| `DefaultCheckBoxStyle` | Style | Style BasedOn |
| `DefaultComboBoxItemStyle` | Style | Style BasedOn |
| `DefaultComboBoxStyle` | Style | Style BasedOn |
| `DefaultComboBoxTextBoxStyle` | Style | TextBox#PART_EditableTextBox Style |
| `DefaultComboBoxToggleButtonStyle` | Style | ToggleButton Style |
| `DefaultDataGridCellStyle` | Style | 컨트롤.CellStyle / Style BasedOn |
| `DefaultDataGridCheckBoxEditingElementStyle` | Style | 컨트롤.CheckBoxColumnEditingElementStyle |
| `DefaultDataGridCheckBoxElementStyle` | Style | 컨트롤.CheckBoxColumnElementStyle |
| `DefaultDataGridColumnHeaderStyle` | Style | 컨트롤.ColumnHeaderStyle / Style BasedOn |
| `DefaultDataGridColumnHeadersPresenterStyle` | Style | Style BasedOn |
| `DefaultDataGridComboBoxEditingElementStyle` | Style | 컨트롤.ComboBoxColumnEditingElementStyle |
| `DefaultDataGridComboBoxElementStyle` | Style | 컨트롤.ComboBoxColumnElementStyle |
| `DefaultDataGridFontSize` | Double | 컨트롤.FontSize |
| `DefaultDataGridRowHeaderStyle` | Style | 컨트롤.RowHeaderStyle |
| `DefaultDataGridRowStyle` | Style | 컨트롤.RowStyle |
| `DefaultDataGridStyle` | Style | Style BasedOn |
| `DefaultDataGridTextEditingElementStyle` | Style | 컨트롤.TextColumnEditingElementStyle |
| `DefaultDataGridTextElementStyle` | Style | 컨트롤.TextColumnElementStyle |
| `DefaultDragIndicatorStyleStyle` | Style | 컨트롤.DragIndicatorStyle |
| `DefaultDropLocationIndicatorStyle` | Style | 컨트롤.DropLocationIndicatorStyle |
| `DefaultTextBoxStyle` | Style | Style BasedOn |
| `DefaultUiDataGridCellStyle` | Style | 컨트롤.CellStyle |
| `DefaultUiDataGridColumnHeaderStyle` | Style | 컨트롤.ColumnHeaderStyle |
| `DefaultUiDataGridStyle` | Style | Style BasedOn |
| `GridViewHeaderRowIndicatorTemplate` | ControlTemplate | 컨트롤.Template |
| `RowHeaderGripperStyle` | Style | Thumb#PART_TopHeaderGripper Style / Thumb#PART_BottomHeaderGripper Style |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultComboBoxStyle` | `ComboBox` | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `DefaultDataGridComboBoxElementStyle` | `ComboBox` | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `DefaultDataGridComboBoxEditingElementStyle` | `ComboBox` | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_EditableTextBox` (TextBox). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `VerticalAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Padding` | `Grid.Margin` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `SelectionBoxItem` | `ContentPresenter.Content` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `SelectionBoxItemTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ItemTemplateSelector` | `ContentPresenter.ContentTemplateSelector` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Foreground` | `ContentPresenter.TextElement.Foreground` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Foreground` | `ToggleButton.Foreground` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `IsDropDownOpen` | `ToggleButton.IsChecked` | Binding to TemplatedParent | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `FontSize` | `TextBox#PART_EditableTextBox.FontSize` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Foreground` | `TextBox#PART_EditableTextBox.Foreground` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `IsReadOnly` | `TextBox#PART_EditableTextBox.IsReadOnly` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `IsDropDownOpen` | `Popup#Popup.IsOpen` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Popup.Placement` | `Popup#Popup.Placement` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Popup.PopupAnimation` | `Popup#Popup.PopupAnimation` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ActualWidth` | `Border#DropDownBorder.MinWidth` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `MaxDropDownHeight` | `DynamicScrollViewer.MaxHeight` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ScrollViewer.HorizontalScrollBarVisibility` | `DynamicScrollViewer.HorizontalScrollBarVisibility` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `FontSize` | `DynamicScrollViewer.TextElement.FontSize` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `FontWeight` | `DynamicScrollViewer.TextElement.FontWeight` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Foreground` | `DynamicScrollViewer.TextElement.Foreground` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ScrollViewer.VerticalScrollBarVisibility` | `DynamicScrollViewer.VerticalScrollBarVisibility` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `FontSize` | `ItemsPresenter.TextElement.FontSize` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border.CornerRadius` | `Border#AccentBorder.CornerRadius` | TemplateBinding | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `Padding` | `ContentPresenter.Margin` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter.HorizontalAlignment` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `VerticalContentAlignment` | `ContentPresenter.VerticalAlignment` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `SelectionBoxItem` | `ContentPresenter.Content` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `SelectionBoxItemTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `ItemTemplateSelector` | `ContentPresenter.ContentTemplateSelector` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `Foreground` | `ContentPresenter.TextElement.Foreground` | TemplateBinding | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `SymbolIcon#ChevronIcon.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Grid.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border#DropDownBorder.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border#DropDownBorder.Padding` | `0,4,0,6` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `Border#DropDownBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `DynamicScrollViewer.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `DropDownBorder.CornerRadius` | `0` | Popup.AllowsTransparency=False | [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultComboBoxStyle |
| `ContextMenu` | `{DynamicResource DefaultControlContextMenu}` | DefaultComboBoxStyle |
| `Foreground` | `{DynamicResource ComboBoxForeground}` | DefaultComboBoxStyle |
| `Background` | `{DynamicResource ComboBoxBackground}` | DefaultComboBoxStyle |
| `BorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | DefaultComboBoxStyle |
| `BorderThickness` | `{StaticResource ComboBoxBorderThemeThickness}` | DefaultComboBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultComboBoxStyle |
| `ScrollViewer.CanContentScroll` | `False` | DefaultComboBoxStyle |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Hidden` | DefaultComboBoxStyle |
| `ScrollViewer.VerticalScrollBarVisibility` | `Hidden` | DefaultComboBoxStyle |
| `ScrollViewer.IsDeferredScrollingEnabled` | `False` | DefaultComboBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultComboBoxStyle |
| `VerticalAlignment` | `Center` | DefaultComboBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultComboBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultComboBoxStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultComboBoxStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultComboBoxStyle |
| `Padding` | `{DynamicResource ComboBoxPadding}` | DefaultComboBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultComboBoxStyle |
| `Popup.PopupAnimation` | `None` | DefaultComboBoxStyle |
| `Popup.Placement` | `Bottom` | DefaultComboBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultComboBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultComboBoxStyle |
| `Background` | `{x:Null}` | DefaultDataGridComboBoxElementStyle |
| `BorderBrush` | `{x:Null}` | DefaultDataGridComboBoxElementStyle |
| `IsTabStop` | `False` | DefaultDataGridComboBoxElementStyle |
| `IsSynchronizedWithCurrentItem` | `False` | DefaultDataGridComboBoxElementStyle |
| `IsSynchronizedWithCurrentItem` | `False` | DefaultDataGridComboBoxEditingElementStyle |
| `IsDropDownOpen` | `True` | DefaultDataGridComboBoxEditingElementStyle |

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ComboBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ComboBox/ComboBox.xaml)
- [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml)
- [Gallery: ComboBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ComboBoxPage.xaml)
