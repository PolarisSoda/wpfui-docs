# PassiveScrollViewer

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

내부 스크롤 끝에서 휠 입력을 상위로 넘길 수 있는 ScrollViewer입니다.

**타입:** `Wpf.Ui.Controls.PassiveScrollViewer` · **기반:** `ScrollViewer`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:PassiveScrollViewer x:Name="Demo" Height="180" IsScrollSpillEnabled="True" VerticalScrollBarVisibility="Auto"><TextBlock Text="긴 콘텐츠" /></ui:PassiveScrollViewer>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsScrollSpillEnabled = false;
Demo.ScrollToTop();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsScrollSpillEnabled` | `bool` | 읽기·쓰기 | `true` | 내부 스크롤이 끝에 도달했을 때 마우스 휠을 상위 스크롤 뷰어로 전달할지 정합니다. 중첩 스크롤의 휠 막힘을 조정합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `VerticalScrollBarVisibility / HorizontalScrollBarVisibility` | `ScrollBarVisibility` | Disabled·Auto·Hidden·Visible 중 방향별 스크롤바 정책입니다. |
| `CanContentScroll` | `bool` | IScrollInfo를 구현하는 콘텐츠에 논리적 스크롤을 위임할지 정합니다. 가상화 패널 구성에서 중요합니다. |
| `VerticalOffset / HorizontalOffset` | `double (읽기)` | 현재 위치입니다. ScrollToVerticalOffset·ScrollToHorizontalOffset으로 이동을 요청합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

일반적인 한 겹 스크롤에서는 기본 ScrollViewer로 충분합니다. 중첩 스크롤의 끝 경계 동작이 필요할 때 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [PassiveScrollViewer.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PassiveScrollViewer.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
