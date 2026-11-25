# SymbolIcon

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

WPF UI에 포함된 Fluent System Icons 글꼴의 아이콘을 표시합니다.

**타입:** `Wpf.Ui.Controls.SymbolIcon` · **기반:** `FontIcon`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:SymbolIcon x:Name="Demo" Symbol="Home24" FontSize="32" Filled="False" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Symbol = ui.SymbolRegular.Settings24;
Demo.Filled = true;
Demo.Foreground = System.Windows.Media.Brushes.CornflowerBlue;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Symbol` | `SymbolRegular` | 읽기·쓰기 | `SymbolRegular.Empty` | Fluent 아이콘 이름(`SymbolRegular`)입니다. `Home24`, `Save24`처럼 열거형에 실제 존재하는 이름을 사용합니다. |
| `Filled` | `bool` | 읽기·쓰기 | `false` | `true`이면 채워진 Fluent 아이콘 글꼴을 사용합니다. 기본값은 선형 아이콘입니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `FontFamily` | [FontIcon](FontIcon.md) | 글리프를 해석할 글꼴입니다. 원하는 문자나 아이콘이 실제로 들어 있는 폰트를 지정해야 합니다. |
| `FontSize` | [FontIcon](FontIcon.md) | 문자·글리프의 크기(DIP)입니다. 요소의 `Width`·`Height`와 별개입니다. |
| `FontStyle` | [FontIcon](FontIcon.md) | 보통체·기울임꼴 등 글꼴 스타일입니다. 글꼴이 해당 스타일을 제공해야 원하는 모양이 나옵니다. |
| `FontWeight` | [FontIcon](FontIcon.md) | 글자의 굵기입니다. `Normal`, `SemiBold`, `Bold` 등으로 시각적 강조를 조정합니다. |
| `Glyph` | [FontIcon](FontIcon.md) | 선택한 글꼴에서 표시할 문자입니다. XAML에서는 유니코드 문자 또는 문자 엔터티를 사용할 수 있습니다. |
| `Foreground` | [IconElement](IconElement.md) | 아이콘에 적용할 전경 브러시입니다. 글꼴 기반 아이콘에 색을 주며, 비트맵 자체의 픽셀색을 다시 칠하는 속성은 아닙니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

아이콘 이름의 24·16 등은 심볼 식별자의 일부입니다. 실제 표시 크기는 `FontSize`로 조절합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [SymbolIcon.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/IconElement/SymbolIcon.cs)
- [Gallery: IconsPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DesignGuidance/IconsPage.xaml)
