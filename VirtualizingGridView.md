# VirtualizingGridView

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

가상화된 타일 배치를 제공하는 ListView 파생형입니다. 열 기반 GridView와 이름을 구별합니다.

**타입:** `Wpf.Ui.Controls.VirtualizingGridView` · **기반:** `ListView`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:VirtualizingGridView x:Name="Demo" Height="300" Orientation="Vertical" SpacingMode="Uniform">
    <ui:VirtualizingGridView.ItemTemplate><DataTemplate><Border Width="120" Height="64" Margin="4"><TextBlock Text="{Binding}" /></Border></DataTemplate></ui:VirtualizingGridView.ItemTemplate>
</ui:VirtualizingGridView>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = System.Linq.Enumerable.Range(1, 10000);
Demo.StretchItems = true;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Orientation` | `Orientation` | 읽기·쓰기 | `Orientation.Vertical` | 가상화 배치의 진행 방향입니다. 이 패널은 일반 `WrapPanel`과 방향 해석이 다르므로 아래 배치 설명을 확인합니다. |
| `SpacingMode` | `SpacingMode` | 읽기·쓰기 | `SpacingMode.Uniform` | 남는 공간을 항목 사이·가장자리에 나누는 방법입니다. `None`, `Uniform`, `BetweenItemsOnly`, `StartAndEndOnly` 중 선택합니다. |
| `StretchItems` | `bool` | 읽기·쓰기 | `false` | 가용 공간에 맞춰 항목을 확장할지 정합니다. 일정한 셀 크기를 유지하려면 `false`를 사용합니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `ViewState` | [ListView](ListView.md) | 항목 보기 스타일 상태입니다. `Default`와 `GridView` 등 아래 열거형에 존재하는 값만 사용합니다. 열을 만들려면 별도로 `View`에 `ui:GridView`를 지정합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |
| `SelectedItem` | `object` | 현재 선택한 데이터 항목입니다. 컨테이너와 데이터 객체를 구분합니다. |
| `SelectedIndex` | `int` | 선택 인덱스입니다. -1은 선택 없음입니다. |
| `SelectionMode` | `SelectionMode` | Single·Multiple·Extended 중 선택 정책을 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `SpacingMode`: `None`, `Uniform`, `BetweenItemsOnly`, `StartAndEndOnly`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `ScrollViewer.VerticalScrollBarVisibility` | `Auto` | 암시적 스타일 |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Disabled` | 암시적 스타일 |
| `ScrollViewer.CanContentScroll` | `true` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `VirtualizingPanel.IsVirtualizing` | `True` | 암시적 스타일 |
| `VirtualizingPanel.VirtualizationMode` | `Standard` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

Orientation=Vertical은 가로로 여러 항목을 채운 행을 세로로 스크롤하는 배치입니다. Horizontal은 그 반대입니다. 유한한 뷰포트와 균일한 항목 크기를 유지합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [VirtualizingGridView.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingGridView/VirtualizingGridView.cs)
- [VirtualizingGridView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingGridView/VirtualizingGridView.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
