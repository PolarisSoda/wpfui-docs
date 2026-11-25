# FluentWindow

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

Fluent 창 테두리·모서리·배경 재질을 구성하는 Window입니다.

**타입:** `Wpf.Ui.Controls.FluentWindow` · **기반:** `System.Windows.Window`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:FluentWindow x:Class="QuickStart.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml"
    Title="내 앱" Width="900" Height="600" ExtendsContentIntoTitleBar="True" WindowBackdropType="Mica">
    <Grid><ui:TitleBar Title="내 앱" VerticalAlignment="Top" /></Grid>
</ui:FluentWindow>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
ExtendsContentIntoTitleBar = true;
WindowBackdropType = ui.WindowBackdropType.Mica;
WindowCornerPreference = ui.WindowCornerPreference.Round;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `WindowCornerPreference` | `WindowCornerPreference` | 읽기·쓰기 | `WindowCornerPreference.Round` | Windows 창 모서리 선호 설정입니다. `DoNotRound`, `Round`, `RoundSmall` 등을 요청하며 OS 지원·창 상태에 따라 결과가 달라집니다. |
| `WindowBackdropType` | `WindowBackdropType` | 읽기·쓰기 | `WindowBackdropType.None` | 창 배경 재질을 요청합니다. `None`, `Mica`, `Acrylic`, `Auto`, `Tabbed` 등이 있으며 지원 OS와 배경 투명도에 영향을 받습니다. 값 변경이 모든 Windows에서 같은 효과를 보장하지는 않습니다. |
| `ExtendsContentIntoTitleBar` | `bool` | 읽기·쓰기 | `false` | `true`이면 콘텐츠를 타이틀바 영역까지 확장합니다. 창 제어 버튼과 드래그 영역을 제공하려면 `TitleBar` 등을 함께 배치합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Title` | `string` | 창 제목입니다. |
| `Owner` | `Window` | 소유 창입니다. 메시지 창의 활성·표시 관계에 중요합니다. |
| `WindowState` | `WindowState` | Normal·Minimized·Maximized 창 상태입니다. |
| `ResizeMode` | `ResizeMode` | 창 크기 조절·최소화·최대화 허용 범위입니다. |
| `WindowStartupLocation` | `WindowStartupLocation` | 수동·화면 중앙·소유 창 중앙의 초기 배치입니다. |
| `SizeToContent` | `SizeToContent` | 내용에 맞춰 창 크기를 정할지 선택합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `WindowCornerPreference`: `Default`, `DoNotRound`, `Round`, `RoundSmall`.
- `WindowBackdropType`: `None`, `Auto`, `Mica`, `Acrylic`, `Tabbed`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `{DynamicResource WindowBackground}` | DefaultFluentWindowStyle |
| `Foreground` | `{DynamicResource WindowForeground}` | DefaultFluentWindowStyle |
| `BorderBrush` | `Transparent` | DefaultFluentWindowStyle |
| `BorderThickness` | `0` | DefaultFluentWindowStyle |
| `Height` | `600` | DefaultFluentWindowStyle |
| `MinHeight` | `320` | DefaultFluentWindowStyle |
| `Width` | `1100` | DefaultFluentWindowStyle |
| `MinWidth` | `460` | DefaultFluentWindowStyle |
| `Margin` | `0` | DefaultFluentWindowStyle |
| `Padding` | `0` | DefaultFluentWindowStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultFluentWindowStyle |
| `FontWeight` | `Normal` | DefaultFluentWindowStyle |
| `UseLayoutRounding` | `True` | DefaultFluentWindowStyle |
| `SnapsToDevicePixels` | `True` | DefaultFluentWindowStyle |
| `OverridesDefaultStyle` | `True` | DefaultFluentWindowStyle |

## 동작과 주의 사항

C# 조각은 FluentWindow 파생 클래스의 메서드 본문입니다. 루트가 `ui:FluentWindow`이면 코드비하인드도 `: ui.FluentWindow`여야 합니다. 테마 리소스와 OS 지원이 필요합니다. 배경 재질을 적용하는 시점에 ExtendsContentIntoTitleBar가 false이면 InvalidOperationException이 발생할 수 있으므로 먼저 true로 설정합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [FluentWindow.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/FluentWindow/FluentWindow.cs)
- [FluentWindow.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/FluentWindow/FluentWindow.xaml)
- [Gallery: MainWindow](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Windows/MainWindow.xaml)
