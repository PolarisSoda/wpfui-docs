# TreeViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

기본 TreeViewItem에 아이콘 슬롯을 더한 트리 항목입니다.

**타입:** `Wpf.Ui.Controls.TreeViewItem` · **기반:** `System.Windows.Controls.TreeViewItem`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TreeViewItem x:Name="Demo" Header="문서" IsExpanded="True" Icon="{ui:SymbolIcon Folder24}">
    <ui:TreeViewItem Header="보고서" />
</ui:TreeViewItem>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Header = "내 문서";
Demo.IsExpanded = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Header` | `object` | 트리 노드에 표시할 헤더입니다. |
| `Items / ItemsSource` | `ItemCollection / IEnumerable` | 하위 노드 목록입니다. |
| `IsExpanded` | `bool` | 하위 노드를 펼칠지 정합니다. |
| `IsSelected` | `bool` | 현재 노드 선택 여부입니다. |
| `ItemTemplate` | `DataTemplate` | 하위 데이터의 표시 템플릿입니다. 계층 데이터에는 HierarchicalDataTemplate을 사용합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 이 컨트롤의 Resources에서 바꾸기

`TreeViewItemBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example TreeViewItem_Resources -->
```xml
<ui:TreeViewItem Header="문서" IsExpanded="True" Icon="{ui:SymbolIcon Folder24}" x:Name="ResourceDemo">
    <ui:TreeViewItem.Resources>
        <SolidColorBrush x:Key="TreeViewItemBackground" Color="#2563EB" />
    </ui:TreeViewItem.Resources>
    <ui:TreeViewItem Header="보고서" />
</ui:TreeViewItem>
```

```csharp
ResourceDemo.Resources["TreeViewItemBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `SystemAccentColor` | Color | SolidColorBrush Color |
| `TreeViewItemBackground` | SolidColorBrush | 컨트롤.Background |
| `TreeViewItemBackgroundPointerOver` | SolidColorBrush | Border.Background〔IsMouseOver=True〕 |
| `TreeViewItemBackgroundSelected` | SolidColorBrush | Border.Background〔IsSelected=True〕 |
| `TreeViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |
| `TreeViewItemSelectionIndicatorForeground` | SolidColorBrush | Rectangle#ActiveRectangle Fill |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultTreeViewItemStyle` | Style | Style BasedOn |
| `DefaultUiTreeViewItemStyle` | Style | Style BasedOn |
| `ExpandCollapseToggleButtonStyle` | Style | ToggleButton#Expander Style |
| `TreeViewItemChevronSize` | Double | SymbolIcon#ChevronIcon FontSize |
| `TreeViewItemFocusVisual` | 정의 없음 | 컨트롤.FocusVisualStyle |
| `TreeViewItemFontSize` | Double | 컨트롤.FontSize |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiTreeViewItemStyle` | `controls:TreeViewItem` | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_Header` (ContentPresenter). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Grid.Background` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `Padding` | `Border#Bd.Padding` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `BorderBrush` | `Border#Bd.BorderBrush` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `BorderThickness` | `Border#Bd.BorderThickness` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `Icon` | `ContentPresenter#SymbolIcon.Content` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `Foreground` | `ContentPresenter#SymbolIcon.TextElement.Foreground` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#PART_Header.HorizontalAlignment` | TemplateBinding | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Padding` | `4` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `ContentPresenter#SymbolIcon.Margin` | `0,0,8,0` | 직접 지정 / 현재 템플릿 | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `SymbolIcon.Margin` | `0` | Icon={x:Null} | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `PART_Header.MinWidth` | `75` | HasHeader=False; Width=Auto | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |
| `PART_Header.MinHeight` | `19` | HasHeader=False; Height=Auto | [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource TreeViewItemForeground}` | DefaultUiTreeViewItemStyle |
| `Background` | `{DynamicResource TreeViewItemBackground}` | DefaultUiTreeViewItemStyle |
| `Padding` | `4` | DefaultUiTreeViewItemStyle |
| `FocusVisualStyle` | `{StaticResource TreeViewItemFocusVisual}` | DefaultUiTreeViewItemStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiTreeViewItemStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiTreeViewItemStyle |

## 동작과 주의 사항

이 항목은 기본 `<TreeView>` 안에 배치합니다. 데이터 바인딩 트리에는 HierarchicalDataTemplate와 ItemContainerStyle을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TreeViewItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.cs)
- [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
