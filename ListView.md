# ListView

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

항목 목록과 GridView 열 보기를 제공하는 WPF ListView 파생형입니다.

**타입:** `Wpf.Ui.Controls.ListView` · **기반:** `System.Windows.Controls.ListView`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ListView x:Name="Demo" ViewState="GridView">
    <ui:ListView.View><ui:GridView><ui:GridViewColumn Header="이름" DisplayMemberBinding="{Binding Name}" Width="180" /></ui:GridView></ui:ListView.View>
</ui:ListView>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = new[] { new { Name = "문서 A" }, new { Name = "문서 B" } };
Demo.SelectedIndex = 0;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ViewState` | `ListViewViewState` | 읽기·쓰기 | `ListViewViewState.Default` | 항목 보기 스타일 상태입니다. `Default`와 `GridView` 등 아래 열거형에 존재하는 값만 사용합니다. 열을 만들려면 별도로 `View`에 `ui:GridView`를 지정합니다. |

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

- `ListViewViewState`: `Default`, `GridView`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

ViewState=Default·GridView에 따라 기본 스타일이 다른 템플릿을 선택합니다. 항목 모서리·선택 색은 ListViewItem 쪽에서 조정하고, 열 헤더는 GridViewColumnHeader, 셀은 GridViewColumn.CellTemplate을 사용합니다. ItemsPanel은 배치·가상화에 관여하므로 단순 외형 변경을 위해 스크롤·가상화 패널을 제거하지 않습니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlFillColorDefault`는 `Color` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ListView_Resources -->
```xml
<ui:ListView ViewState="GridView" x:Name="ResourceDemo">
    <ui:ListView.Resources>
        <Color x:Key="ControlFillColorDefault">#2563EB</Color>
    </ui:ListView.Resources>
    <ui:ListView.View><ui:GridView><ui:GridViewColumn Header="이름" DisplayMemberBinding="{Binding Name}" Width="180" /></ui:GridView></ui:ListView.View>
</ui:ListView>
```

```csharp
ResourceDemo.Resources["ControlFillColorDefault"] = System.Windows.Media.Color.FromRgb(37, 99, 235);
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 항목 컨테이너의 모서리와 간격 조정

<!-- customization:example ListView_Recipe1 -->
```xml
<ui:ListView Height="160">
    <ui:ListView.ItemContainerStyle>
        <Style TargetType="{x:Type ui:ListViewItem}"
               BasedOn="{StaticResource {x:Type ui:ListViewItem}}">
            <Setter Property="Margin" Value="0,4" />
            <Setter Property="Border.CornerRadius" Value="10" />
        </Style>
    </ui:ListView.ItemContainerStyle>
    <ui:ListViewItem Content="문서 A" />
    <ui:ListViewItem Content="문서 B" />
</ui:ListView>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlFillColorDefault` | Color | SolidColorBrush Color |
| `ControlFillColorDisabledBrush` | SolidColorBrush | Bd.Background〔IsEnabled=False〕 |
| `GridViewScrollViewerTemplate` | ControlTemplate | PassiveScrollViewer Template |
| `GridViewTemplate` | ControlTemplate | 컨트롤.Template〔{Binding Path=ViewState, RelativeSource={RelativeSource Mode=Self}}={x:Static controls:ListViewViewState.GridView}〕 |
| `NullViewTemplate` | ControlTemplate | 컨트롤.Template〔{Binding Path=ViewState, RelativeSource={RelativeSource Mode=Self}}={x:Static controls:ListViewViewState.Default}〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ListViewStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `ListViewStyle` | `controls:ListView` | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ContentHost` (PassiveScrollViewer), `PART_DisabledVisual` (Rectangle). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `NullViewTemplate` | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) · 사전 루트 |
| `GridViewTemplate` | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `ScrollViewer.CanContentScroll` | `PassiveScrollViewer#PART_ContentHost.CanContentScroll` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `ScrollViewer.HorizontalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentHost.HorizontalScrollBarVisibility` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `ScrollViewer.VerticalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentHost.VerticalScrollBarVisibility` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Border.BorderBrush` | `Border.BorderBrush` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Border.BorderThickness` | `Border.BorderThickness` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Control.Padding` | `PassiveScrollViewer.Padding` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `ScrollViewer.CanContentScroll` | `PassiveScrollViewer.CanContentScroll` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.CacheLength` | `VirtualizingStackPanel.CacheLength` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.CacheLengthUnit` | `VirtualizingStackPanel.CacheLengthUnit` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.IsVirtualizing` | `VirtualizingStackPanel.IsVirtualizing` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.IsVirtualizing` | `VirtualizingStackPanel.IsVirtualizingWhenGrouping` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.ScrollUnit` | `VirtualizingStackPanel.ScrollUnit` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `VirtualizingPanel.VirtualizationMode` | `VirtualizingStackPanel.VirtualizationMode` | TemplateBinding | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Rectangle#PART_DisabledVisual.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Rectangle#PART_DisabledVisual.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Rectangle#PART_DisabledVisual.Stroke` | `Transparent` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Rectangle#PART_DisabledVisual.StrokeThickness` | `0` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `Border.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Margin` | `0` | ListViewStyle |
| `Padding` | `0` | ListViewStyle |
| `ScrollViewer.VerticalScrollBarVisibility` | `Auto` | ListViewStyle |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Auto` | ListViewStyle |
| `ScrollViewer.CanContentScroll` | `True` | ListViewStyle |
| `VerticalContentAlignment` | `Center` | ListViewStyle |
| `VirtualizingPanel.IsVirtualizing` | `True` | ListViewStyle |
| `VirtualizingPanel.IsVirtualizingWhenGrouping` | `True` | ListViewStyle |
| `VirtualizingPanel.VirtualizationMode` | `Standard` | ListViewStyle |
| `SnapsToDevicePixels` | `True` | ListViewStyle |

## 동작과 주의 사항

열을 표시하려면 `ViewState` 설정과 함께 `View`에 실제 GridView·Columns를 구성합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ListView.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.cs)
- [ListView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListView.xaml)
- [Gallery: ListViewPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Collections/ListViewPage.xaml)
