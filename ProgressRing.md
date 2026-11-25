# ProgressRing

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

원형 진행률 또는 회전하는 대기 상태를 표시합니다.

**타입:** `Wpf.Ui.Controls.ProgressRing` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ProgressRing x:Name="Demo" Width="48" Height="48" Progress="35" IsIndeterminate="False" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Progress = 80;
Demo.IsIndeterminate = true;
Demo.CoverRingVisibility = System.Windows.Visibility.Collapsed;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Progress` | `double` | 읽기·쓰기 | `50d` | 진행률(0~100)입니다. 변경 시 그리는 각도를 계산하며 범위 밖 값은 그릴 때만 제한합니다. `Progress` 자체가 보정되는 것은 아닙니다. |
| `IsIndeterminate` | `bool` | 읽기·쓰기 | `false` | `true`이면 완료 비율 대신 회전하는 대기 표시를 사용합니다. 계산 가능한 진행률이 있으면 `false`로 둡니다. |
| `EngAngle` | `double` | 읽기·쓰기 | `180.0d` | 실제 API 이름이 `EngAngle`입니다. 확정 진행률의 끝 각도이며 `Progress` 변경 시 덮어씁니다. 일반 코드는 `Progress`를 설정합니다. |
| `IndeterminateAngle` | `double` | 읽기·쓰기 | `180.0d` | 불확정 상태의 호 끝 각도입니다. 기본 애니메이션이 관여하므로 템플릿 조정 시 사용합니다. |
| `CoverRingStroke` | `Brush` | 읽기·쓰기 | `Brushes.Black` | 뒤쪽 전체 링의 브러시입니다. 진행 호의 전경색과 구별합니다. |
| `CoverRingVisibility` | `System.Windows.Visibility` | 읽기·쓰기 | `System.Windows.Visibility.Visible` | 뒤쪽 전체 링의 표시 상태입니다. `Collapsed`로 설정하면 진행 호만 남깁니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Height` | `60` | 암시적 스타일 |
| `Width` | `60` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `Foreground` | `{DynamicResource ProgressRingForegroundThemeBrush}` | 암시적 스타일 |
| `CoverRingStroke` | `{DynamicResource ProgressRingBackgroundThemeBrush}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

일반 WPF ProgressBar의 `Value`가 아니라 `Progress`를 사용합니다. 값이 100 이상이면 완전한 호 대신 359도로 그리는 구현입니다. 실제 속성 이름 `EngAngle`은 오타처럼 보여도 그대로 사용해야 합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ProgressRing.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.cs)
- [ProgressRing.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ProgressRing/ProgressRing.xaml)
- [Gallery: ProgressRingPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/ProgressRingPage.xaml)
