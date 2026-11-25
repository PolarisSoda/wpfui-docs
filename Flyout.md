# Flyout

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

주변 UI 위에 짧은 정보나 보조 동작을 표시하는 팝업 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.Flyout` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<StackPanel>
    <ui:Flyout x:Name="Demo" Placement="Bottom">
        <TextBlock Text="빠른 도움말" Margin="12" />
    </ui:Flyout>
    <TextBlock Text="아래 C#에서 Demo.Show()를 호출합니다." />
</StackPanel>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Show();
Demo.Placement = System.Windows.Controls.Primitives.PlacementMode.Top;
Demo.Hide();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsOpen` | `bool` | 읽기·쓰기 | `false` | 팝업 표시 여부입니다. `Show()`·`Hide()`도 이 상태를 변경합니다. `Opened`·`Closed` 이벤트로 실제 팝업 상태를 관찰합니다. |
| `Placement` | `PlacementMode` | 읽기·쓰기 | `PlacementMode.Top` | 이 Flyout의 템플릿에 연결된 팝업 배치 방향입니다. `Top`, `Bottom` 등 `PlacementMode` 값을 사용합니다. WinUI의 독립 Flyout처럼 임의 대상에 `ShowAt`하는 API는 없습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `{DynamicResource FlyoutBackground}` | DefaultFlyoutStyle |
| `BorderBrush` | `{DynamicResource FlyoutBorderBrush}` | DefaultFlyoutStyle |
| `Margin` | `0` | DefaultFlyoutStyle |
| `MinWidth` | `20` | DefaultFlyoutStyle |
| `MinHeight` | `20` | DefaultFlyoutStyle |
| `Padding` | `12` | DefaultFlyoutStyle |
| `VerticalAlignment` | `Bottom` | DefaultFlyoutStyle |
| `HorizontalAlignment` | `Left` | DefaultFlyoutStyle |
| `VerticalContentAlignment` | `Stretch` | DefaultFlyoutStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultFlyoutStyle |
| `Placement` | `Top` | DefaultFlyoutStyle |
| `Popup.AllowsTransparency` | `True` | DefaultFlyoutStyle |
| `Popup.StaysOpen` | `False` | DefaultFlyoutStyle |
| `Popup.PopupAnimation` | `Fade` | DefaultFlyoutStyle |
| `Popup.VerticalOffset` | `1` | DefaultFlyoutStyle |
| `Focusable` | `False` | DefaultFlyoutStyle |
| `KeyboardNavigation.IsTabStop` | `False` | DefaultFlyoutStyle |
| `SnapsToDevicePixels` | `True` | DefaultFlyoutStyle |
| `OverridesDefaultStyle` | `True` | DefaultFlyoutStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `Opened` | 열림 상태 또는 표시 완료 경로에서 발생합니다. 컨트롤별 실제 팝업·상태 변경 시점은 구현을 확인합니다. |
| `Closed` | 닫힌 후 발생합니다. ContentDialog는 결과가 이벤트 인자에 들어갑니다. |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void Show()` | Flyout은 팝업을 열고 Snackbar는 Presenter 큐에 추가합니다. MessageBox의 이 메서드는 예외를 던집니다. |
| `void Hide()` | ContentDialog를 지정 결과로 닫도록 요청합니다. Closing에서 취소될 수 있습니다. Flyout은 팝업을 닫습니다. |

## 동작과 주의 사항

현재 요소 위치를 기준으로 템플릿의 Popup이 열립니다. WinUI의 `Flyout.ShowAt` 같은 API는 제공하지 않습니다. `DropDownButton.Flyout`에는 이 타입 대신 ContextMenu를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Flyout.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Flyout/Flyout.cs)
- [Flyout.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Flyout/Flyout.xaml)
- [Gallery: FlyoutPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DialogsAndFlyouts/FlyoutPage.xaml)
