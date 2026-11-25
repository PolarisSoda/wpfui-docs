# PasswordBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

마스킹 입력과 비밀번호 공개 버튼이 있는 입력란입니다. WPF 기본 PasswordBox가 아닌 WPF-UI TextBox 파생형입니다.

**타입:** `Wpf.Ui.Controls.PasswordBox` · **기반:** `TextBox`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:PasswordBox x:Name="Demo" Width="280" PlaceholderText="비밀번호" RevealButtonEnabled="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Password = string.Empty;
Demo.RevealButtonEnabled = false;
Demo.PasswordChanged += (_, _) => { var length = Demo.Password.Length; };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Password` | `string` | 읽기·쓰기 | `string.Empty` | 실제 비밀번호 문자열입니다. 상속된 `Text`는 표시 마스크와 연결되므로 실제 값은 `Password`를 사용합니다. 로그·문서 예제에 실제 비밀번호를 남기지 않습니다. |
| `PasswordChar` | `char` | 읽기·쓰기 | `'*'` | 입력 문자를 가리는 마스크 문자입니다. 기본값은 별표입니다. |
| `IsPasswordRevealed` | `bool` | 외부 읽기 전용 | `false` | 현재 비밀번호가 그대로 보이는지 나타냅니다. 외부 setter가 없고 기본 템플릿의 공개 버튼 동작으로 변경됩니다. |
| `RevealButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 비밀번호 공개 버튼 사용 여부입니다. `false`이면 기본 템플릿에서 공개 동작을 제공하지 않습니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Icon` | [TextBox](TextBox.md) | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `IconPlacement` | [TextBox](TextBox.md) | 아이콘을 입력란 왼쪽 또는 오른쪽에 둡니다. 기본 템플릿은 `Left`·`Right` 배치를 사용합니다. |
| `PlaceholderText` | [TextBox](TextBox.md) | 입력이 비어 있을 때 보여 줄 안내 문구입니다. 실제 입력 문자열과 구분됩니다. |
| `PlaceholderEnabled` | [TextBox](TextBox.md) | 플레이스홀더 기능을 켤지 정합니다. |
| `CurrentPlaceholderEnabled` | [TextBox](TextBox.md) | 입력 상태와 플레이스홀더 설정을 반영해 계산한 표시 상태입니다. 사용자는 `PlaceholderEnabled`·`PlaceholderText`를 설정합니다. |
| `ClearButtonEnabled` | [TextBox](TextBox.md) | 텍스트 지우기 기능을 허용합니다. 버튼의 실제 표시 여부는 입력 상태에 따라 계산됩니다. |
| `ShowClearButton` | [TextBox](TextBox.md) | 현재 지우기 버튼이 보여야 하는지 나타내는 상태입니다. 외부에서는 읽기 전용입니다. |
| `IsTextSelectionEnabled` | [TextBox](TextBox.md) | `true`이면 기본 스타일이 읽기 전용·투명 배경·테두리 없는 선택 가능한 텍스트 표시 모드로 바꿉니다. 일반 편집 TextBox도 기본적으로 선택은 가능합니다. 입력을 계속 받으려면 `false`로 둡니다. |
| `TemplateButtonCommand` | [TextBox](TextBox.md) | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `MaxLength` | `int` | 사용자 입력 길이 제한입니다. |
| `IsReadOnly` | `bool` | 비밀번호 편집을 막습니다. 실제 값은 Password 속성을 사용합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiPasswordBoxStyle |
| `ContextMenu` | `{DynamicResource DefaultPasswordBoxContextMenu}` | DefaultUiPasswordBoxStyle |
| `Foreground` | `{DynamicResource TextControlForeground}` | DefaultUiPasswordBoxStyle |
| `CaretBrush` | `{DynamicResource TextControlForeground}` | DefaultUiPasswordBoxStyle |
| `Background` | `{DynamicResource TextControlBackground}` | DefaultUiPasswordBoxStyle |
| `BorderBrush` | `{DynamicResource TextControlElevationBorderBrush}` | DefaultUiPasswordBoxStyle |
| `BorderThickness` | `{StaticResource PasswordBoxBorderThemeThickness}` | DefaultUiPasswordBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiPasswordBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiPasswordBoxStyle |
| `VerticalAlignment` | `Center` | DefaultUiPasswordBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiPasswordBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiPasswordBoxStyle |
| `MinHeight` | `{DynamicResource TextControlThemeMinHeight}` | DefaultUiPasswordBoxStyle |
| `MinWidth` | `{DynamicResource TextControlThemeMinWidth}` | DefaultUiPasswordBoxStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiPasswordBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiPasswordBoxStyle |
| `ClearButtonEnabled` | `True` | DefaultUiPasswordBoxStyle |
| `RevealButtonEnabled` | `True` | DefaultUiPasswordBoxStyle |
| `IconPlacement` | `Left` | DefaultUiPasswordBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiPasswordBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiPasswordBoxStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `PasswordChanged` | 실제 Password 변경 알림입니다. 표시 마스크 Text와 구분합니다. |

## 동작과 주의 사항

상속된 `Text` 대신 `Password`를 읽고 씁니다. `IsPasswordRevealed`는 외부에서 대입할 수 없습니다. 실제 비밀번호를 평문 예제·로그에 남기지 않습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [PasswordBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.cs)
- [PasswordHelper.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordHelper.cs)
- [PasswordBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/PasswordBox/PasswordBox.xaml)
- [Gallery: PasswordBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/PasswordBoxPage.xaml)
