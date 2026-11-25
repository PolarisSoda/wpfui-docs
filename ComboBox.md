# ComboBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
