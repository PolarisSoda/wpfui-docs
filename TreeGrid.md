# TreeGrid

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

트리형 데이터 표를 위한 미완성 공개 타입입니다.

**타입:** `Wpf.Ui.Controls.TreeGrid` · **기반:** `System.Windows.Controls.Primitives.Selector`

> **4.3.0 구현 제한:** 이 타입은 미완성입니다. 아래 주의 사항을 먼저 확인하세요.

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TreeGrid x:Name="Demo" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var headers = Demo.Headers;
// 4.3.0에서 headers.Add(...)는 NotImplementedException을 일으킵니다.
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Headers` | `ObservableCollection<TreeGridHeader>?` | 읽기·쓰기 | `null` | 트리형 열 헤더를 위한 컬렉션입니다. 4.3.0 구현은 컬렉션 변경 시 `NotImplementedException`을 던집니다. 실제 데이터 표에는 사용하지 않습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

미완성 타입입니다. Resources·Style을 바꾸어도 Headers.CollectionChanged의 NotImplementedException이 해결되지는 않습니다. 실사용 기능을 제공하는 조정 예제로 권하지 않습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `VirtualizingPanel.IsVirtualizing` | `VirtualizingStackPanel.IsVirtualizing` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `VirtualizingPanel.VirtualizationMode` | `VirtualizingStackPanel.VirtualizationMode` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `ScrollViewer.CanContentScroll` | `PassiveScrollViewer.CanContentScroll` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `ScrollViewer.HorizontalScrollBarVisibility` | `PassiveScrollViewer.HorizontalScrollBarVisibility` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `ScrollViewer.VerticalScrollBarVisibility` | `PassiveScrollViewer.VerticalScrollBarVisibility` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `UIElement.SnapsToDevicePixels` | `ItemsPresenter.SnapsToDevicePixels` | TemplateBinding | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `Border.Margin` | `0` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `Border.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |
| `TreeViewItem.Padding` | `0` | 직접 지정 / 현재 템플릿 | [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Margin` | `0` | 암시적 스타일 |
| `Padding` | `0` | 암시적 스타일 |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Disabled` | 암시적 스타일 |
| `ScrollViewer.VerticalScrollBarVisibility` | `Auto` | 암시적 스타일 |
| `ScrollViewer.CanContentScroll` | `True` | 암시적 스타일 |
| `VirtualizingPanel.IsVirtualizing` | `True` | 암시적 스타일 |
| `VirtualizingPanel.VirtualizationMode` | `Standard` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

정상적인 데이터 표로 사용할 수 없습니다. Headers.CollectionChanged 처리기가 NotImplementedException을 던집니다. 평면 표는 DataGrid, 계층 데이터는 TreeView를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TreeGrid.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.cs)
- [TreeGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeGrid/TreeGrid.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
