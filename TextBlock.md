# TextBlock

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

Fluent 타이포그래피와 의미별 글자색을 지원하는 텍스트 표시 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.TextBlock` · **기반:** `System.Windows.Controls.TextBlock`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TextBlock x:Name="Demo" Text="환경 설정" FontTypography="Title" Appearance="Primary" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Text = "저장되었습니다";
Demo.FontTypography = ui.FontTypography.Body;
Demo.Appearance = ui.TextColor.Secondary;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `FontTypography` | `FontTypography?` | 읽기·쓰기 | `null` | 제목·본문 등 타이포그래피 프리셋입니다. 글자 크기·굵기·행 높이 메타데이터를 적용합니다. `null`은 프리셋 미지정입니다. |
| `Appearance` | `TextColor?` | 읽기·쓰기 | `null` | 의미별 텍스트 색(`TextColor`)입니다. `Primary`·`Secondary` 등 리소스 색을 선택하며 Button의 `ControlAppearance`와 타입이 다릅니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Text` | `string` | 표시할 문자열입니다. |
| `TextWrapping` | `TextWrapping` | Wrap이면 가용 폭에 맞춰 줄바꿈합니다. |
| `TextTrimming` | `TextTrimming` | 넘치는 텍스트를 CharacterEllipsis·WordEllipsis 등으로 생략합니다. |
| `TextAlignment` | `TextAlignment` | 문단 안에서 문자열을 정렬합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `FontTypography`: `Caption`, `Body`, `BodyStrong`, `Subtitle`, `Title`, `TitleLarge`, `Display`.
- `TextColor`: `Primary`, `Secondary`, `Tertiary`, `Disabled`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

문자 크기·굵기는 FontTypography 또는 FontSize·FontWeight로 설정합니다. FontTypography는 TextBlockMetadata의 크기·굵기 매핑을 사용하므로 `TitleTextBlockStyle`이라는 키를 Resources에서 바꾸는 것과 같은 경로가 아닙니다. Typography.xaml의 keyed Style을 직접 선택하는 방법도 있으며 FontTypography를 함께 설정했을 때 우선순위를 확인합니다.

<!-- customization:end -->

## 동작과 주의 사항

`ui:Button.Appearance`와 이 컨트롤의 `Appearance`는 타입이 다릅니다. `FontTypography` 변경은 글꼴 메타데이터를 바꾸므로 개별 `FontSize`·`FontWeight`와의 적용 순서도 확인합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TextBlock.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TextBlock/TextBlock.cs)
- [Gallery: TextBlockPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/TextBlockPage.xaml)
