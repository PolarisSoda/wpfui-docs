# ThumbRate

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

좋아요·싫어요의 두 선택지를 제공합니다.

**타입:** `Wpf.Ui.Controls.ThumbRate` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ThumbRate x:Name="Demo" State="None" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.State = ui.ThumbRateState.Liked;
Demo.StateChanged += (_, _) => { var current = Demo.State; };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `State` | `ThumbRateState` | 읽기·쓰기 | `ThumbRateState.None` | 좋아요·싫어요 선택 상태입니다. `None`, `Liked`, `Disliked` 중 선택하며 같은 버튼을 다시 누르면 선택 해제 경로를 사용합니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ThumbRateState`: `None`, `Liked`, `Disliked`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `Transparent` | DefaultUiThumbRateStyle |
| `Foreground` | `{DynamicResource ThumbRateForeground}` | DefaultUiThumbRateStyle |
| `FontSize` | `24` | DefaultUiThumbRateStyle |
| `Focusable` | `False` | DefaultUiThumbRateStyle |
| `KeyboardNavigation.IsTabStop` | `False` | DefaultUiThumbRateStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiThumbRateStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiThumbRateStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `StateChanged` | ThumbRate의 선택 상태 변경입니다. 현재 `State`를 읽습니다. |

## 동작과 주의 사항

선택 상태는 `State`이며 `IsChecked`가 아닙니다. `StateChanged` 이벤트에서 저장 요청 등을 수행합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ThumbRate.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ThumbRate/ThumbRate.cs)
- [ThumbRate.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ThumbRate/ThumbRate.xaml)
- [Gallery: ThumbRatePage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ThumbRatePage.xaml)
