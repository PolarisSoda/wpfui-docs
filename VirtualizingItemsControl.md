# VirtualizingItemsControl

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

가상화 패널을 사용하는 대량 항목 표시용 ItemsControl입니다.

**타입:** `Wpf.Ui.Controls.VirtualizingItemsControl` · **기반:** `System.Windows.Controls.ItemsControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:VirtualizingItemsControl x:Name="Demo" Height="300" VirtualizingPanel.IsVirtualizing="True" VirtualizingPanel.CacheLength="1" CacheLengthUnit="Page">
    <ui:VirtualizingItemsControl.ItemTemplate><DataTemplate><TextBlock Width="120" Height="40" Text="{Binding}" /></DataTemplate></ui:VirtualizingItemsControl.ItemTemplate>
</ui:VirtualizingItemsControl>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = System.Linq.Enumerable.Range(1, 10000);
Demo.CacheLengthUnit = System.Windows.Controls.VirtualizationCacheLengthUnit.Item;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `CacheLengthUnit` | `VirtualizationCacheLengthUnit` | 읽기·쓰기 | `VirtualizationCacheLengthUnit.Page` | 가상화 캐시 길이의 단위입니다. `Page`, `Item`, `Pixel`을 사용하며 실제 캐시 길이는 `VirtualizingPanel.CacheLength` 붙임 속성으로 정합니다. |

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

화면을 무한 높이로 측정하는 외부 StackPanel·ScrollViewer 구성은 가상화를 무력화할 수 있습니다. 유한한 높이와 내부 스크롤 호스트를 유지합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [VirtualizingItemsControl.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingItemsControl/VirtualizingItemsControl.cs)
- [VirtualizingItemsControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/VirtualizingItemsControl/VirtualizingItemsControl.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
