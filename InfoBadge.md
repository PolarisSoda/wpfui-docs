# InfoBadge

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

짧은 숫자·문자열·상태 아이콘을 표시하는 작은 배지입니다.

**타입:** `Wpf.Ui.Controls.InfoBadge` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:InfoBadge x:Name="Demo" Value="3" Severity="Attention" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = "99+";
Demo.Severity = ui.InfoBadgeSeverity.Critical;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Severity` | `InfoBadgeSeverity` | 읽기·쓰기 | `InfoBadgeSeverity.Informational` | 의미별 배경색을 고릅니다. 기본 ValueInfoBadgeStyle에서는 텍스트 값 배경이 바뀌며 Severity만으로 상태 아이콘이 자동 생성되지는 않습니다. |
| `Value` | `string` | 읽기·쓰기 | `string.Empty` | 배지 안의 문자열입니다. 숫자 전용 타입이 아니므로 `99+` 같은 짧은 문자열도 사용할 수 있습니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `new CornerRadius(8)` | 등록된 모서리 반지름입니다. 다만 4.3.0 제공 ValueInfoBadgeStyle·IconInfoBadgeStyle은 템플릿 안에서 별도 상수·리소스 반지름을 사용하므로 이 속성 변경이 그대로 반영되지 않습니다. 해당 템플릿·리소스를 수정해야 합니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 아이콘을 저장합니다. 기본 암시적 스타일은 ValueInfoBadgeStyle이므로 아이콘을 보이려면 `Style="{StaticResource IconInfoBadgeStyle}"` 같은 아이콘 템플릿을 명시합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `InfoBadgeSeverity`: `Attention`, `Informational`, `Success`, `Caution`, `Critical`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Focusable` | `False` | DotInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | DotInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | DotInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | DotInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | DotInfoBadgeStyle |
| `FontWeight` | `Normal` | DotInfoBadgeStyle |
| `Focusable` | `False` | IconInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | IconInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | IconInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | IconInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | IconInfoBadgeStyle |
| `FontWeight` | `Normal` | IconInfoBadgeStyle |
| `Focusable` | `False` | ValueInfoBadgeStyle |
| `KeyboardNavigation.IsTabStop` | `False` | ValueInfoBadgeStyle |
| `SnapsToDevicePixels` | `True` | ValueInfoBadgeStyle |
| `Foreground` | `{DynamicResource ButtonForeground}` | ValueInfoBadgeStyle |
| `OverridesDefaultStyle` | `True` | ValueInfoBadgeStyle |
| `FontWeight` | `Normal` | ValueInfoBadgeStyle |

## 동작과 주의 사항

InfoBar의 Severity 타입과 값이 다릅니다. 기본 스타일은 문자열 Value를 표시합니다. 아이콘형은 Style="{StaticResource IconInfoBadgeStyle}"을 지정하고 Icon을 넣습니다. CornerRadius는 제공 템플릿의 반지름 리소스에 연결되어 있지 않아 값 변경만으로 반영되지 않을 수 있습니다. 탐색 메뉴 알림에는 NavigationViewItem.InfoBadge에 배치합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [InfoBadge.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.cs)
- [InfoBadge.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBadge/InfoBadge.xaml)
- [Gallery: InfoBadgePage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/InfoBadgePage.xaml)
