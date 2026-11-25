# TitleBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

사용자 지정 창 제목 영역과 시스템 창 버튼을 제공합니다.

**타입:** `Wpf.Ui.Controls.TitleBar` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TitleBar x:Name="Demo" Title="문서 편집기" ShowHelp="True">
    <ui:TitleBar.CenterContent><TextBlock Text="프로젝트 A" /></ui:TitleBar.CenterContent>
</ui:TitleBar>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Title = "보고서 - 문서 편집기";
Demo.ShowMaximize = false;
Demo.HelpClicked += (_, _) => Demo.Title = "도움말 요청";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ApplicationTheme` | `Appearance.ApplicationTheme` | 읽기·쓰기 | `Appearance.ApplicationTheme.Unknown` | 시스템 제목 표시줄과 버튼 렌더링에 사용할 테마 상태입니다. 테마 변경과 함께 관리합니다. |
| `Title` | `string?` | 읽기·쓰기 | `null` | 제목 문자열입니다. 창의 `Window.Title`과 구분되므로 필요한 경우 명시적으로 바인딩합니다. |
| `Header` | `object?` | 읽기·쓰기 | `null` | 제목 영역에 넣을 사용자 콘텐츠입니다. |
| `CenterContent` | `object?` | 읽기·쓰기 | `null` | 타이틀바 중앙 영역에 넣는 콘텐츠입니다. 검색 입력 등을 배치할 수 있습니다. |
| `TrailingContent` | `object?` | 읽기·쓰기 | `null` | 오른쪽 시스템 버튼 앞쪽에 넣는 콘텐츠입니다. |
| `ButtonsForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 최소화·최대화·닫기 버튼의 기본 전경 브러시입니다. |
| `ButtonsBackground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlBrush` | 타이틀바 시스템 버튼 배경 브러시입니다. |
| `IsMaximized` | `bool` | 외부 읽기 전용 | `false` | 소유 창이 최대화되어 있는지 나타내는 읽기 전용 상태입니다. |
| `ForceShutdown` | `bool` | 읽기·쓰기 | `false` | 닫기 동작에서 창만 닫는 대신 애플리케이션 종료를 요청할지 정합니다. 여러 창이 있는 앱에서는 종료 범위를 고려합니다. |
| `ShowMaximize` | `bool` | 읽기·쓰기 | `true` | 최대화·복원 버튼을 표시할지 정합니다. |
| `ShowMinimize` | `bool` | 읽기·쓰기 | `true` | 최소화 버튼을 표시할지 정합니다. |
| `ShowHelp` | `bool` | 읽기·쓰기 | `false` | 도움말 버튼을 표시할지 정합니다. 동작은 `HelpClicked`에서 구현합니다. |
| `ShowClose` | `bool` | 읽기·쓰기 | `true` | 닫기 버튼 표시 여부입니다. |
| `CanMaximize` | `bool` | 읽기·쓰기 | `true` | 최대화 동작을 허용할지 정합니다. 버튼 표시 여부인 `ShowMaximize`와 구분됩니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `CloseWindowByDoubleClickOnIcon` | `bool` | 읽기·쓰기 | `false` | 왼쪽 아이콘을 더블클릭할 때 창을 닫을지 정합니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |
| `MaximizeActionOverride` | `Action<TitleBar, System.Windows.Window>?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 최대화 버튼 기본 동작을 대체할 C# 콜백입니다. 일반 XAML 문자열로 지정하는 속성이 아니며 창과 TitleBar를 전달받습니다. |
| `MinimizeActionOverride` | `Action<TitleBar, System.Windows.Window>?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 최소화 버튼 기본 동작을 대체할 C# 콜백입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `Transparent` | 암시적 스타일 |
| `Foreground` | `{DynamicResource ButtonForeground}` | 암시적 스타일 |
| `ButtonsForeground` | `{DynamicResource ButtonForeground}` | 암시적 스타일 |
| `VerticalAlignment` | `Top` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `Padding` | `16,4,16,4` | 암시적 스타일 |
| `FontSize` | `12` | 암시적 스타일 |
| `Height` | `48` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `VerticalContentAlignment` | `Stretch` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `WndProcInvoked` | 창 메시지 후크 알림입니다. 저수준 창 동작을 다룰 때만 사용합니다. |
| `CloseClicked` | 닫기 버튼 클릭 알림입니다. 기본 종료 정책은 ForceShutdown 등을 따릅니다. |
| `MaximizeClicked` | 최대화 버튼 클릭 알림입니다. 사용자 지정 동작은 MaximizeActionOverride로 구성합니다. |
| `MinimizeClicked` | 최소화 버튼 클릭 알림입니다. 사용자 지정 동작은 MinimizeActionOverride로 구성합니다. |
| `HelpClicked` | 도움말 버튼 클릭 알림입니다. 표시 설정은 ShowHelp입니다. |

## 동작과 주의 사항

`FluentWindow.ExtendsContentIntoTitleBar=True`와 함께 최상단에 배치합니다. 중앙·우측 콘텐츠의 입력 가능 영역과 창 드래그 영역이 겹치지 않는지 확인합니다. `ForceShutdown`은 전체 앱 종료에 영향을 줍니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TitleBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.cs)
- [TitleBar.WindowResize.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.WindowResize.cs)
- [TitleBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TitleBar/TitleBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
