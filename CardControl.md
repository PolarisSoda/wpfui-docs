# CardControl

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

아이콘·헤더·오른쪽 콘텐츠로 설정 행을 만드는 카드형 버튼입니다.

**타입:** `Wpf.Ui.Controls.CardControl` · **기반:** `System.Windows.Controls.Primitives.ButtonBase`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:CardControl x:Name="Demo" Header="자동 저장" Icon="{ui:SymbolIcon Save24}">
    <ui:ToggleSwitch IsChecked="True" />
</ui:CardControl>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Header = "자동 저장 간격";
Demo.CornerRadius = new System.Windows.CornerRadius(8);
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Header` | `object?` | 읽기·쓰기 | `null` | 헤더 영역에 넣을 문자열 또는 UI 요소입니다. 본문인 `Content`와 별도로 배치됩니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `new CornerRadius(0)` | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |

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

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiCardControlStyle |
| `Background` | `{DynamicResource CardBackground}` | DefaultUiCardControlStyle |
| `Foreground` | `{DynamicResource CardForeground}` | DefaultUiCardControlStyle |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | DefaultUiCardControlStyle |
| `BorderThickness` | `{StaticResource CardControlBorderThemeThickness}` | DefaultUiCardControlStyle |
| `Padding` | `{StaticResource CardControlPadding}` | DefaultUiCardControlStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiCardControlStyle |
| `VerticalAlignment` | `Center` | DefaultUiCardControlStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiCardControlStyle |
| `VerticalContentAlignment` | `Center` | DefaultUiCardControlStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiCardControlStyle |
| `FontWeight` | `Normal` | DefaultUiCardControlStyle |
| `CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiCardControlStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiCardControlStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiCardControlStyle |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

본문에 별도 입력 컨트롤을 넣을 수 있습니다. 부모 카드의 Click과 자식 입력 동작이 겹치지 않도록 업무 명령을 배치합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CardControl.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardControl/CardControl.cs)
- [CardControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardControl/CardControl.xaml)
- [Gallery: CardControlPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Layout/CardControlPage.xaml)
