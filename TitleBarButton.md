# TitleBarButton

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

TitleBar가 내부에서 사용하는 창 제어 버튼입니다. 사용자 지정 제목 영역을 만들 때의 저수준 요소입니다.

**타입:** `Wpf.Ui.Controls.TitleBarButton` · **기반:** `Wpf.Ui.Controls.Button`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TitleBarButton x:Name="Demo" ButtonType="Help" Width="46" Height="32" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ButtonType = ui.TitleBarButtonType.Help;
Demo.Click += (_, _) => Demo.ToolTip = "도움말";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ButtonType` | `TitleBarButtonType` | 읽기·쓰기 | `TitleBarButtonType.Unknown` | 최소화·최대화·닫기 등 버튼 종류입니다. 버튼 글리프·강조 스타일에 관여하는 저수준 구성 요소입니다. |
| `ButtonsForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 아이콘 버튼의 기본 전경 브러시입니다. |
| `MouseOverButtonsForeground` | `Brush?` | 읽기·쓰기 | `null` | 포인터가 올라간 동안 사용할 별도 전경 브러시입니다. `null`이면 기본 색 경로를 사용합니다. |
| `RenderButtonsForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 실제 렌더링에 쓰는 전경색입니다. 기본·호버 색에서 계산되므로 일반 코드는 입력 브러시 속성을 설정합니다. |
| `IsHovered` | `bool` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 포인터 강조 상태입니다. `Hover()`·`RemoveHover()`와 마우스 상호작용으로 관리됩니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Icon` | [Button](Button.md) | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `Appearance` | [Button](Button.md) | 테마의 의미별 색을 선택합니다. `Primary`는 강조, `Secondary`는 일반 보조 동작, `Danger`는 위험 동작에 적합합니다. 실제 색은 테마 리소스가 결정합니다. |
| `MouseOverBackground` | [Button](Button.md) | 마우스가 올라간 동안 사용할 배경 브러시입니다. 일반 상태의 `Background`와 구분됩니다. |
| `MouseOverBorderBrush` | [Button](Button.md) | 마우스가 올라간 동안 사용할 테두리 브러시입니다. `BorderThickness`가 0이면 테두리는 보이지 않습니다. |
| `PressedForeground` | [Button](Button.md) | 누르는 동안의 텍스트·아이콘 전경색입니다. |
| `PressedBackground` | [Button](Button.md) | 누르는 동안의 배경 브러시입니다. |
| `PressedBorderBrush` | [Button](Button.md) | 누르는 동안의 테두리 브러시입니다. |
| `CornerRadius` | [Button](Button.md) | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |

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

- `TitleBarButtonType`: `Unknown`, `Minimize`, `Close`, `Maximize`, `Restore`, `Help`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

ButtonsForeground·MouseOverButtonsForeground와 ButtonType을 우선 사용합니다. RenderButtonsForeground는 실제 표시 계산 결과이고 Canvas의 글리프·크기는 종류별 트리거가 설정합니다. 일반 Button 템플릿으로 교체하면 창 버튼 전용 글리프·상태 연결이 사라질 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ButtonForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.ButtonsForeground |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `PaletteRedBrush` | SolidColorBrush | TitleBarButton#PART_CloseButton MouseOverBackground |

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Grid#LayoutRoot.Background` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `RenderButtonsForeground` | `Path#CanvasPath.Fill` | TemplateBinding | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Width` | `44` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `컨트롤.Height` | `30` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Viewbox#ViewBox.Width` | `11` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Viewbox#ViewBox.Height` | `11` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas#Canvas.Width` | `72` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas#Canvas.Height` | `72` | 직접 지정 / 현재 템플릿 | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `ViewBox.Width` | `13` | ButtonType={x:Static controls:TitleBarButtonType.Help} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `ViewBox.Height` | `13` | ButtonType={x:Static controls:TitleBarButtonType.Help} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas.Width` | `24` | ButtonType={x:Static controls:TitleBarButtonType.Help} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas.Height` | `41` | ButtonType={x:Static controls:TitleBarButtonType.Help} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas.Width` | `72` | ButtonType={x:Static controls:TitleBarButtonType.Minimize} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |
| `Canvas.Height` | `8` | ButtonType={x:Static controls:TitleBarButtonType.Minimize} | [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Width` | `44` | 암시적 스타일 |
| `Height` | `30` | 암시적 스타일 |
| `MouseOverBackground` | `{Binding Path=ButtonsBackground, RelativeSource={RelativeSource AncestorType={x:Type controls:TitleBar}}}` | 암시적 스타일 |
| `ButtonsForeground` | `{Binding Path=ButtonsForeground, RelativeSource={RelativeSource AncestorType={x:Type controls:TitleBar}}}` | 암시적 스타일 |
| `MouseOverButtonsForeground` | `{Binding Path=MouseOverButtonsForeground, RelativeSource={RelativeSource Self}}` | 암시적 스타일 |
| `Background` | `Transparent` | 암시적 스타일 |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |
| `Command` | `{Binding Path=TemplateButtonCommand, RelativeSource={RelativeSource AncestorType={x:Type controls:TitleBar}}}` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `True` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `Canvas.ZIndex` | `1` | 암시적 스타일 |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void Hover()` | 창 버튼의 포인터 강조 상태를 켭니다. |
| `void RemoveHover()` | 창 버튼 강조 상태를 끕니다. |
| `void InvokeClick()` | 창 버튼의 Click 경로를 호출합니다. |

## 동작과 주의 사항

버튼만 단독 배치한다고 창 최대화·종료 동작이 자동 구성되는 것은 아닙니다. 일반 앱에서는 TitleBar를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TitleBarButton.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBarButton.cs)
- [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
