# GridViewColumn

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

ListView의 GridView 열입니다. WPF 열에 최소·최대 너비 제한을 더합니다.

**타입:** `Wpf.Ui.Controls.GridViewColumn` · **기반:** `System.Windows.Controls.GridViewColumn`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ListView x:Name="List">
    <ListView.View><ui:GridView><ui:GridViewColumn x:Name="Demo" Header="이름" Width="180" MinWidth="80" MaxWidth="320" DisplayMemberBinding="{Binding Name}" /></ui:GridView></ListView.View>
</ListView>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Width = 240;
Demo.MinWidth = 100;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `MinWidth` | `double` | 읽기·쓰기 | `0.0` | 열 폭의 하한(DIP)입니다. 사용자 열 크기 조절에서도 너무 좁아지지 않도록 제한합니다. |
| `MaxWidth` | `double` | 읽기·쓰기 | `double.PositiveInfinity` | 열 폭의 상한(DIP)입니다. `MinWidth` 이하로 설정하지 않습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Header` | `object` | 열 제목입니다. |
| `Width` | `double` | 열 폭(DIP)입니다. NaN은 내용 기반 자동 측정입니다. |
| `DisplayMemberBinding` | `BindingBase` | 셀에서 표시할 데이터 멤버 바인딩입니다. |
| `CellTemplate` | `DataTemplate` | 복잡한 셀 구성입니다. DisplayMemberBinding과 동시에 설정할 때 우선순위를 확인합니다. |
| `HeaderTemplate` | `DataTemplate` | 열 헤더 표시 템플릿입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

UIElement가 아니므로 Grid.Children 같은 시각 자식 컬렉션에 넣지 않습니다. 셀 내용은 DisplayMemberBinding·CellTemplate로 정합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [GridViewColumn.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumn.cs)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
