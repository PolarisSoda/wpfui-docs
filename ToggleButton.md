# ToggleButton

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
