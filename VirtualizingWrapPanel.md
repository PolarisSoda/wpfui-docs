# VirtualizingWrapPanel

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

보이는 영역과 캐시 범위의 항목만 생성하는 줄바꿈 패널입니다. ItemsControl.ItemsPanel에 넣습니다.

**타입:** `Wpf.Ui.Controls.VirtualizingWrapPanel` · **기반:** `VirtualizingPanelBase`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ListBox x:Name="Demo" Height="300" ScrollViewer.CanContentScroll="True" VirtualizingPanel.IsVirtualizing="True">
    <ListBox.ItemsPanel><ItemsPanelTemplate><ui:VirtualizingWrapPanel ItemSize="120,48" Orientation="Vertical" SpacingMode="Uniform" /></ItemsPanelTemplate></ListBox.ItemsPanel>
    <ListBox.ItemTemplate><DataTemplate><TextBlock Text="{Binding}" /></DataTemplate></ListBox.ItemTemplate>
</ListBox>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = System.Linq.Enumerable.Range(1, 10000);
// 패널 인스턴스를 템플릿 적용 후 얻은 경우:
// panel.ItemSize = new System.Windows.Size(160, 64);
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `SpacingMode` | `SpacingMode` | 읽기·쓰기 | `SpacingMode.Uniform` | 남는 공간을 항목 사이·가장자리에 나누는 방법입니다. `None`, `Uniform`, `BetweenItemsOnly`, `StartAndEndOnly` 중 선택합니다. |
| `Orientation` | `Orientation` | 읽기·쓰기 | `Orientation.Vertical` | 가상화 배치의 진행 방향입니다. 이 패널은 일반 `WrapPanel`과 방향 해석이 다르므로 아래 배치 설명을 확인합니다. |
| `ItemSize` | `Size` | 읽기·쓰기 | `Size.Empty` | 가상화에 사용할 균일한 항목 크기입니다. `Size.Empty`이면 첫 항목 등을 측정해 크기를 계산합니다. 항목별 가변 크기를 보장하는 설정은 아닙니다. |
| `StretchItems` | `bool` | 읽기·쓰기 | `false` | 가용 공간에 맞춰 항목을 확장할지 정합니다. 일정한 셀 크기를 유지하려면 `false`를 사용합니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `ScrollOwner` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 스크롤 정보를 사용하는 ScrollViewer입니다. 일반적으로 항목 컨트롤 템플릿이 연결합니다. |
| `CanVerticallyScroll` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 세로 스크롤을 허용하는 IScrollInfo 상태입니다. 보통 ScrollViewer가 설정합니다. |
| `CanHorizontallyScroll` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 가로 스크롤을 허용하는 IScrollInfo 상태입니다. |
| `ScrollLineDelta` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 픽셀 스크롤 모드에서 한 줄 명령으로 이동할 거리입니다. |
| `MouseWheelDelta` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 픽셀 스크롤 모드에서 휠 명령으로 이동할 거리입니다. |
| `ScrollLineDeltaItem` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 항목 스크롤 모드에서 한 줄 명령의 항목 단위 변화량입니다. |
| `MouseWheelDeltaItem` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 항목 스크롤 모드에서 휠 명령의 항목 단위 변화량입니다. |
| `ExtentWidth` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 전체 콘텐츠의 계산된 가로 범위입니다. |
| `ExtentHeight` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 전체 콘텐츠의 계산된 세로 범위입니다. |
| `HorizontalOffset` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 현재 가로 스크롤 위치입니다. 변경은 `SetHorizontalOffset()` 등으로 요청합니다. |
| `VerticalOffset` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 현재 세로 스크롤 위치입니다. 변경은 `SetVerticalOffset()` 등으로 요청합니다. |
| `ViewportWidth` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 현재 보이는 영역의 계산된 가로 크기입니다. |
| `ViewportHeight` | [VirtualizingPanelBase](VirtualizingPanelBase.md) | 현재 보이는 영역의 계산된 세로 크기입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `SpacingMode`: `None`, `Uniform`, `BetweenItemsOnly`, `StartAndEndOnly`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Margin` | `0` | 암시적 스타일 |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Disabled` | 암시적 스타일 |
| `ScrollViewer.VerticalScrollBarVisibility` | `Auto` | 암시적 스타일 |
| `ScrollViewer.CanContentScroll` | `True` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

이 예제의 Demo는 소유 ListBox입니다. `Orientation=Vertical`은 행을 가로로 채우고 세로 스크롤합니다. 일반 WrapPanel.Orientation=Horizontal과 비슷한 배치이므로 혼동하지 않습니다. ItemsPanel 외부에 직접 자식을 넣는 사용법과 가상화 항목 생성을 구별합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [VirtualizingWrapPanel.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingWrapPanel/VirtualizingWrapPanel.cs)
- [VirtualizingWrapPanel.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingWrapPanel/VirtualizingWrapPanel.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
