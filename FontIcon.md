# FontIcon

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

지정한 글꼴의 유니코드 글리프를 아이콘으로 표시합니다.

**타입:** `Wpf.Ui.Controls.FontIcon` · **기반:** `IconElement`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:FontIcon x:Name="Demo" FontFamily="Segoe MDL2 Assets" Glyph="&#xE80F;" FontSize="24" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Glyph = "\uE713";
Demo.FontSize = 32;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `FontFamily` | `FontFamily` | 읽기·쓰기 | `SystemFonts.MessageFontFamily` | 글리프를 해석할 글꼴입니다. 원하는 문자나 아이콘이 실제로 들어 있는 폰트를 지정해야 합니다. |
| `FontSize` | `double` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 문자·글리프의 크기(DIP)입니다. 요소의 `Width`·`Height`와 별개입니다. |
| `FontStyle` | `FontStyle` | 읽기·쓰기 | `FontStyles.Normal` | 보통체·기울임꼴 등 글꼴 스타일입니다. 글꼴이 해당 스타일을 제공해야 원하는 모양이 나옵니다. |
| `FontWeight` | `FontWeight` | 읽기·쓰기 | `FontWeights.Normal` | 글자의 굵기입니다. `Normal`, `SemiBold`, `Bold` 등으로 시각적 강조를 조정합니다. |
| `Glyph` | `string` | 읽기·쓰기 | `string.Empty` | 선택한 글꼴에서 표시할 문자입니다. XAML에서는 유니코드 문자 또는 문자 엔터티를 사용할 수 있습니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Foreground` | [IconElement](IconElement.md) | 아이콘에 적용할 전경 브러시입니다. 글꼴 기반 아이콘에 색을 주며, 비트맵 자체의 픽셀색을 다시 칠하는 속성은 아닙니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

기본 생성자는 `UiApplication.Current.Resources["DefaultIconFontSize"]`를 읽습니다. FontIcon.Resources만 재정의하는 경로가 아니라 앱 리소스 조회입니다. 개별 아이콘 크기는 공개 FontSize를 직접 설정하는 방법이 확실합니다. 사용자 폰트는 FontFamily·Glyph를 함께 맞춥니다.

### C# 코드가 직접 조회하는 리소스

| 키 | 실제 조회 코드 | 소스 |
| --- | --- | --- |
| `DefaultIconFontSize` | `SetCurrentValue(FontSizeProperty, UiApplication.Current.Resources["DefaultIconFontSize"]);` | [FontIcon.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/IconElement/FontIcon.cs) |

`Application.Current.Resources`를 직접 읽으면 개별 컨트롤 Resources의 같은 키가 대신 사용되는 것은 아닙니다. 조회 시점이 생성자라면 이후 리소스 변경도 자동 바인딩으로 해석하지 않습니다.

<!-- customization:end -->

## 동작과 주의 사항

폰트가 설치되어 있거나 앱에 포함되어 있어야 합니다. 문자열을 문자 그대로 `\uE713`로 넣지 말고 C# 유니코드 이스케이프를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [FontIcon.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/IconElement/FontIcon.cs)
- [Gallery: IconsPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DesignGuidance/IconsPage.xaml)
