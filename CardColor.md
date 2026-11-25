# CardColor

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

색상과 이름·설명을 함께 보여 주는 색상 표본 카드입니다.

**타입:** `Wpf.Ui.Controls.CardColor` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:CardColor x:Name="Demo" Title="브랜드" Subtitle="#3366CC" Color="#3366CC" Width="200" Height="120" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Color = System.Windows.Media.Colors.Coral;
Demo.Subtitle = "Coral";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Title` | `string` | 읽기·쓰기 | `string.Empty` | 색상 표본의 이름입니다. |
| `Subtitle` | `string` | 읽기·쓰기 | `string.Empty` | 색상 값이나 용도를 표시할 보조 문자열입니다. |
| `SubtitleFontSize` | `double` | 읽기·쓰기 | `11.0d` | 보조 문자열의 글자 크기(DIP)입니다. |
| `Color` | `Color` | 읽기·쓰기 | `Color.FromArgb(0, 0, 0, 0)` | 표시할 단색입니다. 변경 시 새 `SolidColorBrush`를 만들어 `CardBrush`에 저장합니다. |
| `Brush` | `Brush` | 읽기·쓰기 | `Brushes.Transparent` | 그라데이션을 포함해 표시할 브러시입니다. 변경 시 `CardBrush`를 이 브러시로 덮어씁니다. `Color`와 둘 다 변경하면 마지막 변경이 적용됩니다. |
| `CardBrush` | `Brush` | 외부 읽기 전용 | `Brushes.Transparent` | 실제로 색상 표본에 표시하는 브러시입니다. `Color` 또는 `Brush` 변경으로 갱신되며 외부 쓰기는 허용되지 않습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource CardForeground}` | 암시적 스타일 |
| `Background` | `{DynamicResource CardBackground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | 암시적 스타일 |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

`Color`와 `Brush`는 변경 시 공통 출력인 `CardBrush`를 갱신합니다. 두 입력은 마지막 변경이 이깁니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CardColor.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.cs)
- [CardColor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CardColor/CardColor.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
