# ContentDialogHost

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

ContentDialog를 창 안에 올리고 포커스·형제 요소 격리를 관리하는 전용 호스트입니다.

**타입:** `Wpf.Ui.Controls.ContentDialogHost` · **기반:** `ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Grid>
    <Grid><TextBlock Text="일반 화면" /></Grid>
    <ui:ContentDialogHost x:Name="Demo" IsDisableSiblingsEnabled="True" />
</Grid>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var dialog = new ui.ContentDialog(Demo) { Title = "확인", CloseButtonText = "닫기" };
await dialog.ShowAsync();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsDisableSiblingsEnabled` | `bool` | 읽기·쓰기 | `false` | 다이얼로그가 활성인 동안 같은 부모의 형제 요소를 비활성화할지 정합니다. 창 전체를 격리하려면 최상위 Grid에서 오버레이 호스트와 앱 콘텐츠를 형제로 배치합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `{DynamicResource ContentDialogSmokeFill}` | DefaultContentDialogHostStyle |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `ContentDialogHost? GetForWindow(Window? window)` | 현재 창에 등록된 ContentDialogHost를 찾습니다. 없으면 null입니다. |

## 동작과 주의 사항

창당 등록할 수 있는 호스트는 하나입니다. 중복 호스트는 예외를 일으킵니다. 최상위 Grid의 마지막 자식으로 두어 콘텐츠 전체를 덮게 합니다. 표시된 창의 호스트는 `ContentDialogHost.GetForWindow(window)`로 찾을 수 있습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ContentDialogHost.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialogHost.cs)
- [ContentDialogHost.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialogHost.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
