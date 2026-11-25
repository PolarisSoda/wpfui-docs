# ListViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

ListView가 선택·포커스·콘텐츠 표시를 위해 생성하는 항목 컨테이너입니다.

**타입:** `Wpf.Ui.Controls.ListViewItem` · **기반:** `System.Windows.Controls.ListViewItem`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ListViewItem x:Name="Demo" Content="문서 A" IsSelected="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Content = "문서 B";
Demo.IsSelected = false;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `IsSelected` | `bool` | 소유 목록에서 이 항목의 선택 여부입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource ListViewItemForeground}` | DefaultAutoSuggestBoxItemContainerStyle |
| `Background` | `Transparent` | DefaultAutoSuggestBoxItemContainerStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultAutoSuggestBoxItemContainerStyle |
| `Margin` | `0,0,0,2` | DefaultAutoSuggestBoxItemContainerStyle |
| `Padding` | `4` | DefaultAutoSuggestBoxItemContainerStyle |
| `OverridesDefaultStyle` | `True` | DefaultAutoSuggestBoxItemContainerStyle |
| `Foreground` | `{DynamicResource ListViewItemForeground}` | ListViewItemStyle |
| `Background` | `Transparent` | ListViewItemStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | ListViewItemStyle |
| `Margin` | `0,0,0,2` | ListViewItemStyle |
| `Padding` | `4` | ListViewItemStyle |

## 동작과 주의 사항

ItemsSource를 사용하는 목록에서는 항목 객체와 컨테이너를 구별합니다. 대부분 ItemContainerStyle로 외형을 설정합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ListViewItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.cs)
- [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml)
- [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
