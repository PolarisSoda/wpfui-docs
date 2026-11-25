# IconSourceElement

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

IconSource를 실제 아이콘으로 변환하기 위한 어댑터입니다. 4.3.0에서는 단독 렌더링이 아닌 아이콘 속성의 강제 변환 경로로 사용합니다.

**타입:** `Wpf.Ui.Controls.IconSourceElement` · **기반:** `IconElement`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Button x:Name="Demo" Content="홈">
    <ui:Button.Icon>
        <ui:IconSourceElement>
            <ui:IconSourceElement.IconSource><ui:SymbolIconSource Symbol="Home24" FontSize="24" /></ui:IconSourceElement.IconSource>
        </ui:IconSourceElement>
    </ui:Button.Icon>
</ui:Button>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
ui.IconSource source = new ui.SymbolIconSource
{
    Symbol = ui.SymbolRegular.Settings24, FontSize = 24
};
Demo.Icon = source.CreateIconElement();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IconSource` | `IconSource?` | 읽기·쓰기 | `null` | 실제 아이콘을 만들 속성 데이터입니다. Button.Icon 등의 강제 변환 경로 또는 CreateIconElement()에서 소비합니다. 4.3.0에서는 이 어댑터를 단독 시각 요소로 배치하면 예외가 날 수 있습니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Foreground` | [IconElement](IconElement.md) | 아이콘에 적용할 전경 브러시입니다. 글꼴 기반 아이콘에 색을 주며, 비트맵 자체의 픽셀색을 다시 칠하는 속성은 아닙니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `IconElement? CreateIconElement()` | 아이콘 속성 데이터로부터 새 시각 아이콘을 만듭니다. |

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

일반 UI 컨테이너처럼 템플릿을 교체하는 타입이 아닙니다. Button.Icon 등의 Coerce 경로에서 IconSource.CreateIconElement()로 실제 아이콘을 만듭니다. Resources의 Style 키를 선택하는 방식보다 IconSource의 속성과 생성된 아이콘을 조정합니다.

<!-- customization:end -->

## 동작과 주의 사항

동일한 FrameworkElement를 여러 버튼에 넣으면 부모 충돌이 생길 수 있습니다. 아이콘 데이터와 시각 인스턴스를 분리하는 이 경로를 사용합니다. 4.3.0의 IconSourceElement는 Grid 등 시각 트리에 단독으로 넣으면 InitializeChildren에서 `Use CreateIconElement` 예외를 던질 수 있습니다. 위 예제처럼 Button.Icon의 강제 변환 경로에 넣거나 C#의 CreateIconElement()로 실제 아이콘을 생성합니다. IconSourceElement가 화면에 직접 그려 주는 컨테이너라고 가정하지 않습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [IconSourceElement.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/IconElement/IconSourceElement.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
