# NavigationViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

NavigationView의 클릭 가능한 메뉴 항목입니다. 페이지 타입·문자열 태그·아이콘·배지·하위 메뉴를 설정합니다.

**타입:** `Wpf.Ui.Controls.NavigationViewItem` · **기반:** `System.Windows.Controls.Primitives.ButtonBase`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:NavigationViewItem x:Name="Demo" Content="설정" TargetPageTag="settings" TargetPageType="{x:Type local:SettingsPage}" NavigationCacheMode="Enabled">
    <ui:NavigationViewItem.Icon><ui:SymbolIcon Symbol="Settings24" /></ui:NavigationViewItem.Icon>
    <ui:NavigationViewItem.InfoBadge><ui:InfoBadge Value="3" /></ui:NavigationViewItem.InfoBadge>
</ui:NavigationViewItem>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Content = "환경 설정";
Demo.InfoBadge = new ui.InfoBadge { Value = "5" };
Demo.NavigationCacheMode = ui.NavigationCacheMode.Enabled;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `MenuItems` | `IList` | 외부 읽기 전용 (항목 변경 가능) | `null` | 직접 선언하는 메뉴 항목 컬렉션입니다. 컬렉션 참조는 읽기 전용이지만 `Add`, `Remove`, `Clear`는 가능합니다. |
| `MenuItemsSource` | `object?` | 읽기·쓰기 | `null` | 외부 메뉴 데이터의 공급원입니다. 기존 직접 항목을 비우고 새 항목을 복사하며, `INotifyCollectionChanged` 컬렉션의 변경을 구독합니다. 일반 데이터 객체를 넣는 것만으로 페이지형 메뉴가 자동 구성되지는 않습니다. |
| `HasMenuItems` | `bool` | 외부 읽기 전용 | `false` | 하위 메뉴가 있는지 계산한 상태입니다. `MenuItems` 또는 `MenuItemsSource`를 변경해 간접 갱신합니다. |
| `IsActive` | `bool` | 읽기·쓰기 | `false` | 선택된 탐색 경로의 활성 표시입니다. 메뉴 선택·페이지 이동과 연결되므로 `Navigate()`로 실제 탐색을 수행합니다. |
| `IsExpanded` | `bool` | 읽기·쓰기 | `false` | 하위 메뉴가 펼쳐져 있는지 정합니다. 하위 항목이 있고 이를 지원하는 표시 모드일 때 의미가 있습니다. |
| `IsPaneOpen` | `bool` | 읽기·쓰기 | `false` | 상위 NavigationView 패널의 열림 상태와 연결되는 항목 표시 상태입니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `TargetPageTag` | `string` | 읽기·쓰기 | `string.Empty` | 문자열로 탐색할 식별 태그입니다. `Navigate("settings")`처럼 호출할 수 있도록 메뉴별로 고유하게 정합니다. |
| `TargetPageType` | `Type?` | 읽기·쓰기 | `null` | 클릭 시 만들거나 찾을 페이지의 `Type`입니다. XAML에서 `{x:Type local:SettingsPage}`를 지정합니다. DI가 없으면 생성 가능한 공개 페이지가 필요합니다. |
| `InfoBadge` | `InfoBadge?` | 읽기·쓰기 | `null` | 메뉴 옆 알림 배지입니다. `new InfoBadge { Value = "3" }`처럼 생성해 넣습니다. |
| `NavigationCacheMode` | `NavigationCacheMode` | 읽기·쓰기 | `NavigationCacheMode.Disabled` | 페이지 인스턴스 재사용 정책입니다. `Disabled`는 일반적으로 다시 만들고 `Enabled`·`Required`는 캐시 재사용 경로를 사용합니다. 4.3.0의 차이는 아래 주의 사항을 확인합니다. |
| `NavigationViewItemParent` | `INavigationViewItem?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 계층 탐색에서 상위 메뉴 항목 참조입니다. 일반적으로 메뉴를 중첩해 구성하면 라이브러리가 관리합니다. |
| `IsMenuElement` | `bool` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 탐색 메뉴 요소로 취급하는지 나타내는 내부 협력용 CLR 속성입니다. 화면 제목·페이지 타입을 대신하지 않습니다. |
| `Id` | `string` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 항목 인스턴스의 고유 식별 문자열입니다. 사용자가 정하는 안정적인 문자열 경로는 `TargetPageTag`를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Command` | `ICommand` | 실행할 ViewModel 명령입니다. CanExecute=false이면 버튼이 비활성화될 수 있습니다. |
| `CommandParameter` | `object` | 명령에 전달할 데이터입니다. |
| `ClickMode` | `ClickMode` | Release·Press·Hover 중 클릭을 발생시킬 시점을 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `NavigationCacheMode`: `Disabled`, `Enabled`, `Required`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

메뉴 항목 상태마다 BackgroundPointerOver·BackgroundPressed·BackgroundSelected가 따로 있습니다. ControlCornerRadius 참조가 있는 항목 템플릿과 고정 모서리·폭을 쓰는 다른 표시 모드가 함께 있으므로 사용 중인 NavigationView.PaneDisplayMode와 ItemTemplate을 확인합니다. `Style`만 바꿨는데 모양이 그대로면 상위 NavigationView가 항목 ControlTemplate을 지정하는 경로를 확인합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example NavigationViewItem_Resources -->
```xml
<ui:NavigationViewItem Content="설정" TargetPageTag="settings" TargetPageType="{x:Type local:SettingsPage}" NavigationCacheMode="Enabled" x:Name="ResourceDemo">
    <ui:NavigationViewItem.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:NavigationViewItem.Resources>
    <ui:NavigationViewItem.Icon><ui:SymbolIcon Symbol="Settings24" /></ui:NavigationViewItem.Icon>
    <ui:NavigationViewItem.InfoBadge><ui:InfoBadge Value="3" /></ui:NavigationViewItem.InfoBadge>
</ui:NavigationViewItem>
```

```csharp
ResourceDemo.Resources["ControlCornerRadius"] = new System.Windows.CornerRadius(12);
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `FlyoutBackground` | SolidColorBrush | Border#SubMenuBorder Background |
| `FlyoutBorderBrush` | SolidColorBrush | Border#SubMenuBorder BorderBrush |
| `NavigationViewItemBackground` | SolidColorBrush | 컨트롤.Background / Border#MainBorder Background |
| `NavigationViewItemBackgroundPointerOver` | SolidColorBrush | MainBorder.Background〔IsMouseOver=True〕 |
| `NavigationViewItemBackgroundPressed` | SolidColorBrush | MainBorder.Background〔IsPressed=True〕 |
| `NavigationViewItemBackgroundSelected` | SolidColorBrush | MainBorder.Background〔IsActive=True〕 |
| `NavigationViewItemBackgroundSelectedLeftFluent` | SolidColorBrush | MainBorder.Background〔IsActive=True〕 / MainBorder.Background〔IsMouseOver=True〕 |
| `NavigationViewItemBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `NavigationViewItemForeground` | SolidColorBrush | ContentPresenter#IconContentPresenter TextElement.Foreground / SymbolIcon#ChevronIcon Foreground / 컨트롤.Foreground / ContentControl#IconContentPresenter Foreground / 외 3곳 |
| `NavigationViewItemForegroundLeftFluent` | SolidColorBrush | ContentPresenter#IconContentPresenter TextElement.Foreground / ContentPresenter#ElementContentPresenter TextElement.Foreground |
| `NavigationViewItemForegroundPointerOver` | SolidColorBrush | IconContentPresenter.TextElement.Foreground〔IsMouseOver=True; IsActive=False〕 / ElementContentPresenter.TextElement.Foreground〔IsMouseOver=True; IsActive=False〕 |
| `NavigationViewItemForegroundPointerOverLeftFluent` | SolidColorBrush | IconContentPresenter.TextElement.Foreground〔IsMouseOver=True; IsActive=False〕 / ContentGrid.TextElement.Foreground〔IsMouseOver=True; IsActive=False〕 |
| `NavigationViewItemThickness` | Thickness | Border#MainBorder BorderThickness |
| `NavigationViewSelectionIndicatorForeground` | SolidColorBrush | Rectangle#ActiveRectangle Fill / IconContentPresenter.TextElement.Foreground〔IsActive=True〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `NavigationViewFluentIconSize` | Double | ContentPresenter#IconContentPresenter TextElement.FontSize / Grid#ContentGrid Height / DoubleAnimation From〔IsActive=True〕 / DoubleAnimation To〔IsActive=True〕 |
| `NavigationViewItemChevronSize` | Double | SymbolIcon#ChevronIcon FontSize |
| `NavigationViewItemDefaultStyle` | Style | Style BasedOn |
| `NullToVisibilityConverter` | NullToVisibilityConverter | ContentPresenter#IconContentPresenter Visibility |
| `PaneFluentButtonHeight` | Double | Border#MainBorder Height |
| `PaneFluentButtonWidth` | Double | Border#MainBorder MinWidth |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `NavigationViewItemDefaultStyle` | `controls:NavigationViewItem` | [NavigationViewItemDefaultStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewItemDefaultStyle.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

C# 구현이 이름으로 찾는 부분: `PART_ChevronGrid`. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.

원본 템플릿에 정의된 PART: `PART_ChevronGrid` (Grid), `PART_InfoBadge` (ContentPresenter). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `LeftFluentNavigationViewItemTemplate` | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) · 사전 루트 |
| `BottomCompactNavigationViewItemTemplate` | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) · 사전 루트 |
| `LeftCompactNavigationViewItemTemplate` | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) · 사전 루트 |
| (Style 내부 템플릿) | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) · 내부 정의 |
| `LeftMinimalCompactNavigationViewItemTemplate` | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) · 사전 루트 |
| (Style 내부 템플릿) | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) · 내부 정의 |
| `TopCompactNavigationViewItemTemplate` | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) · 사전 루트 |
| (Style 내부 템플릿) | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `BorderBrush` | `Border#MainBorder.BorderBrush` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Content` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Content` | `ContentPresenter#ElementContentPresenter.Content` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `ContentTemplate` | `ContentPresenter#ElementContentPresenter.ContentTemplate` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `FontSize` | `ContentPresenter#ElementContentPresenter.TextElement.FontSize` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `InfoBadge` | `ContentPresenter#PART_InfoBadge.Content` | TemplateBinding | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Content` | `ContentPresenter#ElementContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ContentTemplate` | `ContentPresenter#ElementContentPresenter.ContentTemplate` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Foreground` | `ContentPresenter#ElementContentPresenter.TextElement.Foreground` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `InfoBadge` | `ContentPresenter#PART_InfoBadge.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `BorderBrush` | `Border#MainBorder.BorderBrush` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border.CornerRadius` | `Border#MainBorder.CornerRadius` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Content` | `ContentPresenter#ElementContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentTemplate` | `ContentPresenter#ElementContentPresenter.ContentTemplate` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Foreground` | `ContentPresenter#ElementContentPresenter.TextElement.Foreground` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `InfoBadge` | `ContentPresenter#PART_InfoBadge.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `MenuItems` | `ItemsControl#MenuItemsPresenter.ItemsSource` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Visibility` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `InfoBadge` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `BorderBrush` | `Border#MainBorder.BorderBrush` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border.CornerRadius` | `Border#MainBorder.CornerRadius` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Icon` | `ContentControl#IconContentPresenter.Content` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Content` | `ContentPresenter#ElementContentPresenter.Content` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ContentTemplate` | `ContentPresenter#ElementContentPresenter.ContentTemplate` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Foreground` | `ContentPresenter#ElementContentPresenter.TextElement.Foreground` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `InfoBadge` | `ContentPresenter#PART_InfoBadge.Content` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `MenuItemsSource` | `ItemsControl.ItemsSource` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Content` | TemplateBinding | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Icon` | `ContentPresenter#IconContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Content` | `ContentPresenter#ElementContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentTemplate` | `ContentPresenter#ElementContentPresenter.ContentTemplate` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Foreground` | `ContentPresenter#ElementContentPresenter.TextElement.Foreground` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `InfoBadge` | `ContentPresenter#PART_InfoBadge.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `MenuItems` | `ItemsControl#SubMenuItemsPresenter.ItemsSource` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#MainBorder.Padding` | `4` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Border#MainBorder.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Border#MainBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Border#MainBorder.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Rectangle#ActiveRectangle.Width` | `3` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Rectangle#ActiveRectangle.Height` | `24` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `-4,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Grid#ContentGrid.Margin` | `0,2,0,0` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `ContentPresenter#PART_InfoBadge.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `ElementContentPresenter.Margin` | `0` | IsActive=True | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `PART_InfoBadge.Margin` | `0` | InfoBadge={x:Null} | [NavigationLeftFluent.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationLeftFluent.xaml) |
| `Border#MainBorder.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Grid.Margin` | `12,8,12,8` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `0,0,6,0` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ContentPresenter#PART_InfoBadge.Margin` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Rectangle#ActiveRectangle.Width` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Rectangle#ActiveRectangle.Height` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0,0,0,-4` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `IconContentPresenter.Margin` | `0` | Content={x:Null} | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `IconContentPresenter.Margin` | `0` | Content= | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.MinWidth` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.MinHeight` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Grid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ColumnDefinition.Width` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `-1,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Rectangle#ActiveRectangle.Width` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Rectangle#ActiveRectangle.Height` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter#PART_InfoBadge.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Grid#PART_ChevronGrid.Width` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `SymbolIcon#ChevronIcon.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.Height` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#MainBorder.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Grid.Margin` | `30,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ColumnDefinition.MinWidth` | `180` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `6,0,3,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter#ElementContentPresenter.Margin` | `10,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `PART_InfoBadge.Margin` | `0` | InfoBadge={x:Null} | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `PART_ChevronGrid.Width` | `40` | HasMenuItems=True | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewItemDefaultStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewItemDefaultStyle.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewItemDefaultStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewItemDefaultStyle.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.MinWidth` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.MinHeight` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ColumnDefinition.Width` | `40` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ContentControl#IconContentPresenter.Margin` | `-1,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Rectangle#ActiveRectangle.Width` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Rectangle#ActiveRectangle.Height` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ContentPresenter#PART_InfoBadge.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `Border#MainBorder.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ColumnDefinition.MinWidth` | `180` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `-1,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `ChevronIcon.Margin` | `8,0,8,0` | HasMenuItems=True | [NavigationViewLeftMinimalCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewLeftMinimalCompact.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Grid.Margin` | `8,8,8,8` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `0,0,6,0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Grid#PART_ChevronGrid.Width` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentPresenter#PART_InfoBadge.Margin` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Width` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Height` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0,0,0,-4` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#SubMenuBorder.Margin` | `12,0,12,18` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#SubMenuBorder.Padding` | `0,3,0,3` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#SubMenuBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#SubMenuBorder.CornerRadius` | `8` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.Height` | `25` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Border#MainBorder.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Grid.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `15` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.MinWidth` | `120` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Width` | `3` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Height` | `16` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentPresenter#IconContentPresenter.Margin` | `0,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentPresenter#ElementContentPresenter.Margin` | `5,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `PART_ChevronGrid.Width` | `20` | HasMenuItems=True | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `IconContentPresenter.Margin` | `0` | Content={x:Null} | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `IconContentPresenter.Margin` | `0` | Content= | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | NavigationViewItemDefaultStyle |
| `Margin` | `0` | NavigationViewItemDefaultStyle |
| `Padding` | `0` | NavigationViewItemDefaultStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | NavigationViewItemDefaultStyle |
| `Cursor` | `Hand` | NavigationViewItemDefaultStyle |
| `VerticalAlignment` | `Center` | NavigationViewItemDefaultStyle |
| `HorizontalContentAlignment` | `Stretch` | NavigationViewItemDefaultStyle |
| `Background` | `{DynamicResource NavigationViewItemBackground}` | NavigationViewItemDefaultStyle |
| `Foreground` | `{DynamicResource NavigationViewItemForeground}` | NavigationViewItemDefaultStyle |
| `BorderBrush` | `{DynamicResource NavigationViewItemBorderBrush}` | NavigationViewItemDefaultStyle |
| `KeyboardNavigation.IsTabStop` | `True` | NavigationViewItemDefaultStyle |
| `Focusable` | `True` | NavigationViewItemDefaultStyle |
| `SnapsToDevicePixels` | `True` | NavigationViewItemDefaultStyle |
| `OverridesDefaultStyle` | `True` | NavigationViewItemDefaultStyle |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void Activate(INavigationView navigationView)` | 메뉴 항목을 NavigationView의 활성 상태로 연결합니다. |
| `void Deactivate(INavigationView navigationView)` | 메뉴 항목의 활성 탐색 연결을 해제합니다. |

## 동작과 주의 사항

이 XAML은 `NavigationView.MenuItems`·`FooterMenuItems` 안에 둡니다. 같은 페이지 Type을 여러 항목이 공유하면 타입 기반 사전·캐시가 겹칠 수 있습니다. 4.3.0 캐시 구현은 `Disabled`만 별도 처리하고 `Enabled`·`Required`는 같은 Type 키 캐시 경로를 사용합니다. `IsActive`만 바꿔도 페이지를 탐색하는 것은 아닙니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [NavigationViewItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewItem.cs)
- [NavigationViewItemDefaultStyle.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewItemDefaultStyle.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
