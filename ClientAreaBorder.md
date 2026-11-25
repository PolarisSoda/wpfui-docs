# ClientAreaBorder

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

FluentWindow 템플릿에서 클라이언트 영역과 시스템 창 테두리를 보정하는 Border입니다.

**타입:** `Wpf.Ui.Controls.ClientAreaBorder` · **기반:** `System.Windows.Controls.Border`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ClientAreaBorder x:Name="Demo"><Grid><TextBlock Text="창 콘텐츠" /></Grid></ui:ClientAreaBorder>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ApplicationTheme = Wpf.Ui.Appearance.ApplicationTheme.Dark;
var frame = ui.ClientAreaBorder.ResizeFrameBorderThickness;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ApplicationTheme` | `ApplicationTheme` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 창 클라이언트 영역 계산에 사용할 앱 테마입니다. 일반 앱에서는 `FluentWindow`가 내부에서 관리합니다. |
| `PaddedBorderThickness` | `Thickness` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 시스템에서 계산한 추가 창 테두리 두께입니다. 직접 설정할 수 없습니다. |
| `ResizeFrameBorderThickness` | `Thickness` | 정적 · 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 시스템 창 크기 조절 프레임의 두께입니다. DPI·시스템 메트릭에 따라 달라집니다. |
| `WindowChromeNonClientFrameThickness` | `Thickness` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 비클라이언트 프레임을 보정할 계산 결과입니다. 창 크롬 내부 레이아웃용 읽기 전용 값입니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Child` | `UIElement` | 테두리 안의 단일 자식입니다. |
| `Background / BorderBrush` | `Brush` | 배경과 테두리 브러시입니다. |
| `BorderThickness / Padding` | `Thickness` | 테두리 두께와 내부 여백입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

이 타입에 연결된 별도 WPF UI XAML 리소스·기본 스타일은 이번 소스 조사에서 발견되지 않았습니다. 이름을 추측해 키를 추가하기보다 위 공개 속성·콘텐츠 템플릿·상위 컨트롤을 먼저 설정합니다. WPF-UI 기반 클래스에서 상속한 설정은 해당 기반 클래스 문서도 확인합니다.

<!-- customization:end -->

## 동작과 주의 사항

대개 FluentWindow 템플릿이 관리합니다. ResizeFrameBorderThickness는 타입 이름으로 읽는 정적 속성이고 나머지 두 계산 속성은 인스턴스 속성입니다. 일반 카드·패널의 테두리에는 기본 Border를 사용하는 편이 간단합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ClientAreaBorder.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ClientAreaBorder/ClientAreaBorder.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
