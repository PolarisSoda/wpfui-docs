# ToggleSwitch

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

설정을 켜고 끄는 스위치입니다. 상태별 라벨을 지원합니다.

**타입:** `Wpf.Ui.Controls.ToggleSwitch` · **기반:** `System.Windows.Controls.Primitives.ToggleButton`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ToggleSwitch x:Name="Demo" IsChecked="True" OnContent="알림 켜짐" OffContent="알림 꺼짐" LabelPosition="Right" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsChecked = false;
Demo.OffContent = "알림 받지 않음";
Demo.LabelPosition = ui.ElementPlacement.Left;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `OffContent` | `object?` | 읽기·쓰기 | `null` | 꺼짐(`IsChecked=false`) 상태의 라벨입니다. `Content`가 비어 있을 때 기본 템플릿이 사용합니다. |
| `OnContent` | `object?` | 읽기·쓰기 | `null` | 켜짐(`IsChecked=true`) 상태의 라벨입니다. 고정 `Content`를 지정하면 상태별 라벨보다 우선합니다. |
| `LabelPosition` | `ElementPlacement` | 읽기·쓰기 | `ElementPlacement.Right` | 라벨을 스위치 왼쪽(`Left`) 또는 오른쪽(`Right`)에 둡니다. 기본 템플릿은 두 위치에 따라 열과 라벨 여백을 바꿉니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `IsChecked` | `bool?` | true=선택, false=해제, null=미정 상태입니다. 바인딩 시 Mode=TwoWay를 명시할 수 있습니다. |
| `IsThreeState` | `bool` | 사용자 조작으로 미정 상태까지 순환할지 정합니다. |
| `Command / CommandParameter` | `ICommand / object` | 토글 시 실행할 명령과 전달 값입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ElementPlacement`: `Left`, `Right`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiToggleSwitchStyle |
| `Background` | `{DynamicResource ToggleSwitchFillOn}` | DefaultUiToggleSwitchStyle |
| `Foreground` | `{DynamicResource ToggleSwitchContentForeground}` | DefaultUiToggleSwitchStyle |
| `BorderBrush` | `Transparent` | DefaultUiToggleSwitchStyle |
| `BorderThickness` | `{StaticResource ToggleSwitchBorderThemeThickness}` | DefaultUiToggleSwitchStyle |
| `Padding` | `{StaticResource ToggleSwitchPadding}` | DefaultUiToggleSwitchStyle |
| `HorizontalAlignment` | `Left` | DefaultUiToggleSwitchStyle |
| `VerticalAlignment` | `Center` | DefaultUiToggleSwitchStyle |
| `LabelPosition` | `Right` | DefaultUiToggleSwitchStyle |
| `HorizontalContentAlignment` | `Left` | DefaultUiToggleSwitchStyle |
| `VerticalContentAlignment` | `Center` | DefaultUiToggleSwitchStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiToggleSwitchStyle |
| `FontWeight` | `Normal` | DefaultUiToggleSwitchStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiToggleSwitchStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiToggleSwitchStyle |

상속 이벤트: `Click` · `Checked` · `Unchecked` · `Indeterminate`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

`Content`에 고정 문자열을 넣으면 `OnContent`·`OffContent`보다 우선합니다. 상태를 ViewModel에 저장하려면 `IsChecked="{Binding NotificationsEnabled, Mode=TwoWay}"`를 사용합니다. 이벤트는 `Checked`, `Unchecked`, `Indeterminate`를 상속합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ToggleSwitch.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.cs)
- [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml)
- [Gallery: ToggleSwitchPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ToggleSwitchPage.xaml)
