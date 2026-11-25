# TreeGridHeader

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

미완성 TreeGrid의 헤더 데이터·요소 타입입니다.

**타입:** `Wpf.Ui.Controls.TreeGridHeader` · **기반:** `System.Windows.FrameworkElement`

> **4.3.0 구현 제한:** 이 타입은 미완성입니다. 아래 주의 사항을 먼저 확인하세요.

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TreeGridHeader x:Name="Demo" Title="이름" Group="기본 정보" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Title = "파일 이름";
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Title` | `string` | 읽기·쓰기 | `string.Empty` | 실험적 트리 헤더 제목 저장 속성입니다. 완성된 열 렌더러를 제공하지 않습니다. |
| `Group` | `string` | 읽기·쓰기 | `string.Empty` | 실험적 헤더 그룹 식별 문자열입니다. 실제 그룹 배치가 완성된 API로 해석하지 않습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

이 타입에 연결된 별도 WPF UI XAML 리소스·기본 스타일은 이번 소스 조사에서 발견되지 않았습니다. 이름을 추측해 키를 추가하기보다 위 공개 속성·콘텐츠 템플릿·상위 컨트롤을 먼저 설정합니다. WPF-UI 기반 클래스에서 상속한 설정은 해당 기반 클래스 문서도 확인합니다.

<!-- customization:end -->

## 동작과 주의 사항

저장 속성이 있다고 실제 열·그룹 표시 기능이 완성된 것은 아닙니다. TreeGrid.Headers에 추가하면 현재 구현에서 예외가 발생합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TreeGridHeader.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGridHeader.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
