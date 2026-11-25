# Arc

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

시작·끝 각도로 원호를 그리는 Shape입니다. ProgressRing 등의 시각 요소에 사용합니다.

**타입:** `Wpf.Ui.Controls.Arc` · **기반:** `Shape`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Arc x:Name="Demo" Width="80" Height="80" StartAngle="0" EndAngle="270" Stroke="CornflowerBlue" StrokeThickness="5" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.EndAngle = 180;
Demo.SweepDirection = System.Windows.Media.SweepDirection.Counterclockwise;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `StartAngle` | `double` | 읽기·쓰기 | `0.0d` | 호의 시작 각도(도)입니다. 중심·반지름은 요소 크기로 계산됩니다. |
| `EndAngle` | `double` | 읽기·쓰기 | `0.0d` | 호의 끝 각도(도)입니다. 시작 각도와의 차이가 그려지는 호 길이를 결정합니다. |
| `SweepDirection` | `SweepDirection` | 읽기·쓰기 | `SweepDirection.Clockwise` | 시작점에서 끝점으로 도는 방향입니다. `Clockwise`는 시계 방향입니다. |
| `IsLargeArc` | `bool` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 호의 각도 차이가 큰 호에 해당하는지 계산한 상태입니다. `StartAngle`·`EndAngle`을 통해 간접 변경합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Stroke / StrokeThickness` | `Brush / double` | 윤곽선의 브러시와 두께입니다. |
| `Fill` | `Brush` | 형상 내부 채움입니다. 열린 호에는 Stroke가 주로 사용됩니다. |
| `Stretch` | `Stretch` | 형상을 가용 영역에 맞추는 방식입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

그리려면 Stroke·StrokeThickness와 크기를 지정합니다. 배경을 채우는 일반 Border가 아니며 각도는 도 단위입니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Arc.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Arc/Arc.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
