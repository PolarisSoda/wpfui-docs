# InfoBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

페이지 안에 유지되는 정보·성공·경고·오류 메시지입니다.

**타입:** `Wpf.Ui.Controls.InfoBar` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:InfoBar x:Name="Demo" IsOpen="True" Severity="Warning" Title="연결 끊김" Message="네트워크를 확인하세요." IsClosable="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Severity = ui.InfoBarSeverity.Success;
Demo.Title = "다시 연결됨";
Demo.Message = "정상적으로 사용할 수 있습니다.";
Demo.IsOpen = true;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsClosable` | `bool` | 읽기·쓰기 | `true` | 닫기 버튼 표시 여부입니다. `false`이면 사용자가 닫기 버튼으로 숨길 수 없습니다. |
| `IsOpen` | `bool` | 읽기·쓰기 | `false` | 알림 표시 여부입니다. 닫기 동작은 컨트롤을 삭제하지 않고 이 값을 `false`로 바꿉니다. |
| `Title` | `string` | 읽기·쓰기 | `string.Empty` | 짧은 제목 문자열입니다. |
| `Message` | `string` | 읽기·쓰기 | `string.Empty` | 제목 옆·아래에 표시할 설명 문자열입니다. 줄바꿈은 템플릿과 할당 폭에 영향을 받습니다. |
| `Severity` | `InfoBarSeverity` | 읽기·쓰기 | `InfoBarSeverity.Informational` | `Informational`, `Success`, `Warning`, `Error`에 따라 배경·아이콘·전경 리소스를 바꿉니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `InfoBarSeverity`: `Informational`, `Success`, `Warning`, `Error`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource InfoBarTitleForeground}` | 암시적 스타일 |
| `Padding` | `{StaticResource InfoBarPadding}` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalAlignment` | `Center` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource InfoBarBorderBrush}` | 암시적 스타일 |
| `BorderThickness` | `{StaticResource InfoBarBorderThemeThickness}` | 암시적 스타일 |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `False` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

Snackbar처럼 자동 숨김 타이머를 제공하지 않습니다. `IsOpen=False`면 숨김 상태로 남아 있으므로 다시 표시할 수 있습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [InfoBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.cs)
- [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml)
- [Gallery: InfoBarPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/InfoBarPage.xaml)
