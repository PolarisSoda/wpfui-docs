# Button

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
