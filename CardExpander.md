# CardExpander

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
