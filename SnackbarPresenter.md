# SnackbarPresenter

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

Snackbar의 현재 표시·대기열·자동 숨김을 관리하는 표시 영역입니다.

**타입:** `Wpf.Ui.Controls.SnackbarPresenter` · **기반:** `System.Windows.Controls.ContentPresenter`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:SnackbarPresenter x:Name="Demo" VerticalAlignment="Bottom" Margin="16" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
new ui.Snackbar(Demo) { Title = "업로드 완료", Content = "파일을 전송했습니다." }.Show();
// 현재 알림을 명시적으로 숨기려면 async 메서드에서:
await Demo.HideCurrent();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Content` | `Snackbar?` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 표시 중인 Snackbar입니다. CLR setter는 protected입니다. 직접 대입하지 말고 Snackbar를 이 Presenter로 생성한 다음 `Show()`를 호출합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void AddToQue(Snackbar snackbar)` | 스낵바를 대기열에 넣습니다. 철자는 API와 동일합니다. |
| `Task ImmediatelyDisplay(Snackbar snackbar)` | 현재 표시를 숨기고 지정한 스낵바를 즉시 표시합니다. |
| `Task HideCurrent()` | 현재 스낵바의 숨김 처리를 기다립니다. |

## 동작과 주의 사항

`AddToQue`는 실제 API의 철자입니다. 큐 순서가 필요하면 Snackbar.Show()를 사용하고 새 알림을 바로 보이게 하려면 ImmediatelyDisplay를 사용합니다. `Content`는 외부 대입이 제한됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [SnackbarPresenter.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/SnackbarPresenter.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
