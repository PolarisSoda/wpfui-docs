# IconElement

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

시각 아이콘들의 추상 기반 클래스입니다. Foreground와 아이콘 변환 경로를 공유합니다.

**타입:** `Wpf.Ui.Controls.IconElement` · **기반:** `FrameworkElement` · **추상 클래스: 직접 생성 불가**

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:SymbolIcon x:Name="Demo" Symbol="Home24" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
ui.IconElement icon = Demo;
icon.Foreground = System.Windows.Media.Brushes.Coral;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Foreground` | `Brush` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 아이콘에 적용할 전경 브러시입니다. 글꼴 기반 아이콘에 색을 주며, 비트맵 자체의 픽셀색을 다시 칠하는 속성은 아닙니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

이 타입에 연결된 별도 WPF UI XAML 리소스·기본 스타일은 이번 소스 조사에서 발견되지 않았습니다. 이름을 추측해 키를 추가하기보다 위 공개 속성·콘텐츠 템플릿·상위 컨트롤을 먼저 설정합니다. WPF-UI 기반 클래스에서 상속한 설정은 해당 기반 클래스 문서도 확인합니다.

<!-- customization:end -->

## 동작과 주의 사항

`IconElement`는 abstract이므로 직접 `<ui:IconElement />` 또는 `new IconElement()`로 만들 수 없습니다. SymbolIcon·FontIcon·ImageIcon을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [IconElement.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/IconElement/IconElement.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
