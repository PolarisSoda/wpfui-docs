# CheckBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

독립적인 참·거짓·미정 선택입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<CheckBox x:Name="Demo" Content="자동 저장" IsChecked="True" IsThreeState="False" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsChecked = false;
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

일반 사각 체크박스와 별도 keyed Style이 함께 있습니다. 모양 변경은 원하는 스타일 선택, IsChecked·IsThreeState, 상태별 CheckBoxCheckBackground/Stroke/Glyph 계열 리소스로 구분합니다. 체크 표식 경로·박스의 고정 크기를 바꾸려면 템플릿 수정이 필요합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example CheckBox_Resources -->
```xml
<CheckBox Content="자동 저장" IsChecked="True" IsThreeState="False"  x:Name="ResourceDemo">
    <CheckBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </CheckBox.Resources>
</CheckBox>
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
| `CheckBoxBackground` | SolidColorBrush | 컨트롤.Background |
| `CheckBoxBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `CheckBoxCheckBackgroundFillChecked` | SolidColorBrush | ControlBorderIconPresenter.Background〔IsChecked={x:Null}〕 / ControlBorderIconPresenter.Background〔IsChecked=True〕 |
| `CheckBoxCheckBackgroundFillCheckedPointerOver` | SolidColorBrush | ControlBorderIconPresenter.Background〔IsMouseOver=True; IsPressed=False; IsChecked={x:Null}〕 / ControlBorderIconPresenter.Background〔IsMouseOver=True; IsPressed=False; IsChecked=True〕 |
| `CheckBoxCheckBackgroundFillCheckedPressed` | SolidColorBrush | ControlBorderIconPresenter.Background〔IsMouseOver=True; IsPressed=True; IsChecked={x:Null}〕 / ControlBorderIconPresenter.Background〔IsMouseOver=True; IsPressed=True; IsChecked=True〕 |
| `CheckBoxCheckBackgroundFillUncheckedDisabled` | SolidColorBrush | ControlBorderIconPresenter.Background〔IsEnabled=False〕 |
| `CheckBoxCheckBackgroundFillUncheckedPointerOver` | SolidColorBrush | StrokeBorder.Background〔IsMouseOver=True; IsPressed=False; IsChecked=False〕 |
| `CheckBoxCheckBackgroundFillUncheckedPressed` | SolidColorBrush | StrokeBorder.Background〔IsMouseOver=True; IsPressed=True; IsChecked=False〕 |
| `CheckBoxCheckBackgroundStrokeUncheckedDisabled` | SolidColorBrush | StrokeBorder.BorderBrush〔IsEnabled=False〕 |
| `CheckBoxCheckBorderBrush` | SolidColorBrush | StrokeBorder.BorderBrush〔IsChecked={x:Null}〕 / StrokeBorder.BorderBrush〔IsChecked=True〕 / StrokeBorder.BorderBrush〔IsMouseOver=True; IsPressed=False; IsChecked={x:Null}〕 / StrokeBorder.BorderBrush〔IsMouseOver=True; IsPressed=True; IsChecked={x:Null}〕 / 외 2곳 |
| `CheckBoxCheckGlyphForeground` | SolidColorBrush | SymbolIcon#ControlIcon Foreground |
| `CheckBoxForeground` | SolidColorBrush | 컨트롤.Foreground |
| `CheckBoxForegroundUncheckedDisabled` | SolidColorBrush | ControlIcon.Foreground〔IsEnabled=False〕 |
| `CheckBoxHeight` | Double | Border#ControlBorderIconPresenter Width |
| `CheckBoxIconSize` | Double | SymbolIcon#ControlIcon FontSize |
| `CheckBoxWidth` | Double | Border#ControlBorderIconPresenter Height |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlElevationBorderBrush` | LinearGradientBrush / SolidColorBrush | 컨트롤.BorderBrush / 컨트롤.HorizontalGridLinesBrush / 컨트롤.VerticalGridLinesBrush |
| `DefaultControlContextMenu` | ContextMenu | 컨트롤.ContextMenu |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
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
| `TextFillColorDisabledBrush` | SolidColorBrush | 컨트롤.Foreground〔IsEnabled=False〕 / DiscreteObjectKeyFrame Value / 컨트롤.TextElement.Foreground〔IsEnabled=False〕 |
| `TextFillColorSecondaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |
| `TextFillColorTertiaryBrush` | SolidColorBrush | DiscreteObjectKeyFrame Value |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `BodyTextBlockStyle` | Style | Style BasedOn |
| `BooleanToVisibilityConverter` | BooleanToVisibilityConverter | Control Visibility |
| `CheckBoxAnimationDuration` | Duration | DoubleAnimation Duration〔IsChecked=True〕 |
| `CheckBoxAnimationOffset` | TimeSpan | SeekStoryboard Offset〔Visibility=Visible〕 / SeekStoryboard Offset |
| `CheckBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `CheckBoxContentMargin` | Thickness | ContentPresenter#ContentPresenter Margin |
| `CheckBoxPadding` | Thickness | 컨트롤.Padding |
| `ClipConverter` | ClipConverter | MultiBinding Converter |
| `ColumnHeaderGripperStyle` | Style | Thumb#PART_LeftHeaderGripper Style / Thumb#PART_RightHeaderGripper Style |
| `ComboBoxChevronMargin` | Thickness | SymbolIcon Margin |
| `ComboBoxChevronSize` | Double | SymbolIcon FontSize |
| `DefaultCheckBoxStyle` | Style | Style BasedOn |
| `DefaultComboBoxStyle` | Style | Style BasedOn |
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
| `ToolBarButtonBaseStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultCheckBoxStyle` | `CheckBox` | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `DefaultDataGridCheckBoxElementStyle` | `CheckBox` | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `DefaultDataGridCheckBoxEditingElementStyle` | `CheckBox` | [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml) |
| `{x:Static ToolBar.CheckBoxStyleKey}` | `CheckBox` | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

`{x:Static ...}`·`{x:Type ...}` 형태는 문자열 키가 아닌 객체 키입니다. 예를 들어 ToolBar.ButtonStyleKey를 읽을 때는 `Style="{StaticResource {x:Static ToolBar.ButtonStyleKey}}"`처럼 중첩 마크업을 사용합니다. 일반 문자열처럼 같은 이름을 추가하는 방식과 다릅니다. [복합 키 사용 예](CustomizationGuide.md)를 확인합니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `BulletDecorator.Margin` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `HorizontalAlignment` | `BulletDecorator.HorizontalAlignment` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `VerticalAlignment` | `BulletDecorator.VerticalAlignment` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `Background` | `Border#ControlBorderIconPresenter.Background` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `Border.CornerRadius` | `Border#ControlBorderIconPresenter.CornerRadius` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `BorderBrush` | `Border#StrokeBorder.BorderBrush` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `BorderThickness` | `Border#StrokeBorder.BorderThickness` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `Border.CornerRadius` | `Border#StrokeBorder.CornerRadius` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.MinWidth` | `120` | 직접 지정 / 현재 템플릿 | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `컨트롤.MinHeight` | `32` | 직접 지정 / 현재 템플릿 | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `BulletDecorator.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `ContentPresenter.Margin` | `0` | Content={x:Null} | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `컨트롤.MinWidth` | `30` | Content={x:Null} | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `ContentPresenter.Margin` | `0` | Content= | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |
| `컨트롤.MinWidth` | `30` | Content= | [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultCheckBoxStyle |
| `Background` | `{DynamicResource CheckBoxBackground}` | DefaultCheckBoxStyle |
| `Foreground` | `{DynamicResource CheckBoxForeground}` | DefaultCheckBoxStyle |
| `BorderBrush` | `{DynamicResource CheckBoxBorderBrush}` | DefaultCheckBoxStyle |
| `BorderThickness` | `{StaticResource CheckBoxBorderThemeThickness}` | DefaultCheckBoxStyle |
| `Padding` | `{StaticResource CheckBoxPadding}` | DefaultCheckBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultCheckBoxStyle |
| `HorizontalAlignment` | `Left` | DefaultCheckBoxStyle |
| `VerticalAlignment` | `Center` | DefaultCheckBoxStyle |
| `HorizontalContentAlignment` | `Left` | DefaultCheckBoxStyle |
| `VerticalContentAlignment` | `Center` | DefaultCheckBoxStyle |
| `Cursor` | `Hand` | DefaultCheckBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultCheckBoxStyle |
| `FontWeight` | `Normal` | DefaultCheckBoxStyle |
| `KeyboardNavigation.IsTabStop` | `True` | DefaultCheckBoxStyle |
| `Focusable` | `True` | DefaultCheckBoxStyle |
| `MinWidth` | `120` | DefaultCheckBoxStyle |
| `MinHeight` | `32` | DefaultCheckBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultCheckBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultCheckBoxStyle |
| `HorizontalAlignment` | `Center` | DefaultDataGridCheckBoxElementStyle |
| `IsHitTestVisible` | `False` | DefaultDataGridCheckBoxElementStyle |
| `Focusable` | `False` | DefaultDataGridCheckBoxElementStyle |
| `HorizontalAlignment` | `Center` | DefaultDataGridCheckBoxEditingElementStyle |

상속 이벤트: `Click` · `Checked` · `Unchecked` · `Indeterminate`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CheckBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CheckBox/CheckBox.xaml)
- [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml)
- [Gallery: CheckBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/CheckBoxPage.xaml)
