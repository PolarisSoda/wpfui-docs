# VirtualizingPanelBase

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

VirtualizingWrapPanel의 추상 기반 클래스이며 IScrollInfo를 구현합니다.

**타입:** `Wpf.Ui.Controls.VirtualizingPanelBase` · **기반:** `VirtualizingPanel` · **추상 클래스: 직접 생성 불가**

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:VirtualizingWrapPanel x:Name="Demo" ScrollLineDelta="24" MouseWheelDelta="72" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
ui.VirtualizingPanelBase panel = Demo;
panel.ScrollLineDelta = 32;
panel.MouseWheelDeltaItem = 4;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ScrollOwner` | `ScrollViewer?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 스크롤 정보를 사용하는 ScrollViewer입니다. 일반적으로 항목 컨트롤 템플릿이 연결합니다. |
| `CanVerticallyScroll` | `bool` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 세로 스크롤을 허용하는 IScrollInfo 상태입니다. 보통 ScrollViewer가 설정합니다. |
| `CanHorizontallyScroll` | `bool` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 가로 스크롤을 허용하는 IScrollInfo 상태입니다. |
| `ScrollLineDelta` | `double` | 읽기·쓰기 | `16.0` | 픽셀 스크롤 모드에서 한 줄 명령으로 이동할 거리입니다. |
| `MouseWheelDelta` | `double` | 읽기·쓰기 | `48.0` | 픽셀 스크롤 모드에서 휠 명령으로 이동할 거리입니다. |
| `ScrollLineDeltaItem` | `int` | 읽기·쓰기 | `1` | 항목 스크롤 모드에서 한 줄 명령의 항목 단위 변화량입니다. |
| `MouseWheelDeltaItem` | `int` | 읽기·쓰기 | `3` | 항목 스크롤 모드에서 휠 명령의 항목 단위 변화량입니다. |
| `ExtentWidth` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 전체 콘텐츠의 계산된 가로 범위입니다. |
| `ExtentHeight` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 전체 콘텐츠의 계산된 세로 범위입니다. |
| `HorizontalOffset` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 가로 스크롤 위치입니다. 변경은 `SetHorizontalOffset()` 등으로 요청합니다. |
| `VerticalOffset` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 세로 스크롤 위치입니다. 변경은 `SetVerticalOffset()` 등으로 요청합니다. |
| `ViewportWidth` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 보이는 영역의 계산된 가로 크기입니다. |
| `ViewportHeight` | `double` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 보이는 영역의 계산된 세로 크기입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

abstract이므로 직접 생성할 수 없습니다. 이 XAML은 파생 패널 속성 예시이며 실사용은 ItemsPanelTemplate 안에 배치합니다. 픽셀·항목 스크롤 단위에 따라 사용되는 delta 속성이 다릅니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [VirtualizingPanelBase.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingWrapPanel/VirtualizingPanelBase.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
