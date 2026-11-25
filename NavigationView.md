# NavigationView

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

메뉴 패널, 페이지 표시 영역, 뒤로가기, 검색, 경로를 결합한 앱 탐색 컨테이너입니다.

**타입:** `Wpf.Ui.Controls.NavigationView` · **기반:** `System.Windows.Controls.Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:NavigationView x:Name="Demo" PaneTitle="내 앱" PaneDisplayMode="Left" OpenPaneLength="240" IsBackButtonVisible="Auto">
    <ui:NavigationView.MenuItems>
        <ui:NavigationViewItem Content="홈" TargetPageTag="home" TargetPageType="{x:Type local:HomePage}" Icon="{ui:SymbolIcon Home24}" />
    </ui:NavigationView.MenuItems>
    <ui:NavigationView.FooterMenuItems>
        <ui:NavigationViewItem Content="설정" TargetPageTag="settings" TargetPageType="{x:Type local:SettingsPage}" />
    </ui:NavigationView.FooterMenuItems>
</ui:NavigationView>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Loaded += (_, _) => Demo.Navigate(typeof(HomePage));
Demo.IsPaneOpen = false;
bool moved = Demo.Navigate("settings");
if (Demo.CanGoBack) Demo.GoBack();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `SelectedItem` | `INavigationViewItem?` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 현재 선택된 메뉴 항목입니다. 외부 설정 대신 `Navigate()` 또는 메뉴 클릭으로 선택을 바꿉니다. |
| `CanGoBack` | `bool` | 외부 읽기 전용 | `기존 DP 메타데이터 / CLR 계산값` | 탐색 저널에서 뒤로 이동할 수 있는지 계산한 값입니다. `GoBack()` 호출 전 확인합니다. |
| `EnableDebugMessages` | `bool` | 읽기·쓰기 | `false` | 탐색 진단 메시지 활성화 플래그입니다. 화면 모양을 바꾸지 않으며 디버그 진단에 사용합니다. |
| `Header` | `object?` | 읽기·쓰기 | `null` | 헤더 영역에 넣을 문자열 또는 UI 요소입니다. 본문인 `Content`와 별도로 배치됩니다. |
| `HeaderVisibility` | `Visibility` | 읽기·쓰기 | `Visibility.Visible` | 페이지 헤더 영역의 표시 상태입니다. `Collapsed`는 공간도 없애고 `Hidden`은 자리를 유지합니다. |
| `AlwaysShowHeader` | `bool` | 읽기·쓰기 | `false` | 4.3.0에 저장 속성은 있지만 제공 템플릿·구현에서 이를 소비하는 연결을 찾을 수 없습니다. 실제 헤더 표시는 HeaderVisibility와 현재 모드의 템플릿을 사용합니다. |
| `MenuItems` | `IList` | 외부 읽기 전용 (항목 변경 가능) | `null` | 직접 선언하는 메뉴 항목 컬렉션입니다. 컬렉션 참조는 읽기 전용이지만 `Add`, `Remove`, `Clear`는 가능합니다. |
| `MenuItemsSource` | `object?` | 읽기·쓰기 | `null` | 외부 메뉴 데이터의 공급원입니다. 기존 직접 항목을 비우고 새 항목을 복사하며, `INotifyCollectionChanged` 컬렉션의 변경을 구독합니다. 일반 데이터 객체를 넣는 것만으로 페이지형 메뉴가 자동 구성되지는 않습니다. |
| `FooterMenuItems` | `IList` | 외부 읽기 전용 (항목 변경 가능) | `null` | 하단 메뉴 항목 컬렉션입니다. 설정·도움말처럼 본 메뉴와 구분되는 항목을 넣습니다. 참조 교체는 불가하지만 항목 추가·제거는 가능합니다. |
| `FooterMenuItemsSource` | `object?` | 읽기·쓰기 | `null` | 하단 메뉴의 외부 공급원입니다. `MenuItemsSource`와 같은 컬렉션 복사·변경 구독 방식을 사용합니다. |
| `IsTopSeparatorVisible` | `bool` | 읽기·쓰기 | `true` | 상단 구분선 표시 플래그입니다. 실제 위치·소비 여부는 현재 `PaneDisplayMode` 템플릿에 따라 달라집니다. |
| `IsFooterSeparatorVisible` | `bool` | 읽기·쓰기 | `true` | 본문 메뉴와 하단 영역 사이의 구분선 표시 여부입니다. |
| `ContentOverlay` | `object?` | 읽기·쓰기 | `null` | 탐색 콘텐츠 위에 겹치는 영역입니다. 전역 상태·오버레이용 UI 요소를 넣습니다. |
| `IsBackEnabled` | `bool` | 외부 읽기 전용 | `false` | 뒤로가기 버튼의 활성 상태입니다. 내부 탐색 저널 변경으로 갱신되며 CLR setter는 protected입니다. |
| `IsBackButtonVisible` | `NavigationViewBackButtonVisible` | 읽기·쓰기 | `NavigationViewBackButtonVisible.Auto` | 뒤로가기 버튼 표시 정책입니다. 4.3.0 기본 변환기는 `Auto`와 `Visible`을 모두 Visible로 변환합니다. 탐색 가능 여부는 별도 IsBackEnabled가 제어하므로 Auto가 불가능한 뒤로가기를 자동으로 숨기는 것은 아닙니다. |
| `IsPaneToggleVisible` | `bool` | 읽기·쓰기 | `true` | 메뉴 펼침·접힘 버튼 표시 여부입니다. 메뉴 패널 전체의 표시 여부와 다릅니다. |
| `IsPaneOpen` | `bool` | 읽기·쓰기 | `true` | 왼쪽 메뉴 패널의 펼침 상태입니다. 값을 바꾸면 열림·닫힘 이벤트가 발생하고 TitleBar 여백도 연동됩니다. |
| `IsPaneVisible` | `bool` | 읽기·쓰기 | `false` | 공개된 패널 표시 플래그이지만 4.3.0 제공 템플릿·구현에서는 이 값을 소비하는 연결을 찾을 수 없습니다. 이 값만 바꾸어 패널 숨김을 기대하지 말고 모드·템플릿을 검토합니다. |
| `OpenPaneLength` | `double` | 읽기·쓰기 | `0D` | 펼쳐진 메뉴 패널 폭(DIP)입니다. DP 등록값 0 대신 기본 스타일이 실사용 폭을 제공합니다. |
| `CompactPaneLength` | `double` | 읽기·쓰기 | `0D` | 접힌 메뉴 패널 폭(DIP)입니다. 아이콘 공간을 확보하도록 설정합니다. |
| `PaneHeader` | `object?` | 읽기·쓰기 | `null` | 메뉴 패널 상단에 넣는 별도 UI입니다. `Header`는 페이지 콘텐츠의 헤더이므로 서로 다른 영역입니다. |
| `PaneTitle` | `string?` | 읽기·쓰기 | `null` | 메뉴 패널 제목 문자열입니다. |
| `PaneFooter` | `object?` | 읽기·쓰기 | `null` | 메뉴 패널 하단의 임의 콘텐츠입니다. `FooterMenuItems`의 탐색 항목 목록과 구별합니다. |
| `PaneDisplayMode` | `NavigationViewPaneDisplayMode` | 읽기·쓰기 | `NavigationViewPaneDisplayMode.Left` | 패널 배치 방식입니다. `Left`, `LeftMinimal`, `LeftFluent`, `Top`, `Bottom`이 있고 자동 반응형 모드인 `Auto`는 없습니다. `LeftFluent`는 하위 MenuItems를 지원하지 않습니다. |
| `AutoSuggestBox` | `AutoSuggestBox?` | 읽기·쓰기 | `null` | 메뉴 검색용 AutoSuggestBox입니다. 메뉴 후보를 구성하고 선택·검색 이벤트를 탐색과 연결합니다. 일반 검색 상자와 달리 NavigationView가 후보를 관리합니다. |
| `TitleBar` | `TitleBar?` | 읽기·쓰기 | `null` | 현재 창 TitleBar 참조입니다. 패널 상태에 따라 타이틀바와 프레임 여백을 조정합니다. XAML 요소 참조 바인딩으로 연결할 수 있습니다. |
| `BreadcrumbBar` | `BreadcrumbBar?` | 읽기·쓰기 | `null` | 탐색 계층 경로를 표시할 BreadcrumbBar입니다. 계층 탐색과 연결해 경로 항목을 관리합니다. |
| `ItemTemplate` | `ControlTemplate?` | 읽기·쓰기 | `null` | 메뉴 항목의 `ControlTemplate`입니다. 일반 ItemsControl의 `DataTemplate` 속성과 타입이 다릅니다. 항목 외형 전체를 교체할 때 사용합니다. |
| `TransitionDuration` | `int` | 읽기·쓰기 | `200` | 화면 전환 애니메이션의 시간(밀리초)입니다. 짧게 설정하면 더 빠르게 전환됩니다. |
| `Transition` | `Transition` | 읽기·쓰기 | `Transition.FadeInWithSlide` | 콘텐츠가 들어올 때 적용할 애니메이션 종류입니다. 열거형 `Wpf.Ui.Animations.Transition`을 사용합니다. |
| `FrameMargin` | `Thickness` | 읽기·쓰기 | `default(Thickness)` | 탐색 페이지를 표시하는 프레임의 바깥 여백입니다. TitleBar 연결 시 내부에서 변경될 수 있습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `NavigationViewBackButtonVisible`: `Collapsed`, `Visible`, `Auto`.
- `NavigationViewPaneDisplayMode`: `Left`, `LeftMinimal`, `LeftFluent`, `Top`, `Bottom`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

배치·폭은 PaneDisplayMode·OpenPaneLength·CompactPaneLength로 먼저 설정합니다. 메뉴 항목 외형은 ItemTemplate(ControlTemplate), 본문 배경은 NavigationViewContentBackground 등 리소스로 따로 조정합니다. Left·Top·Bottom의 템플릿과 LeftMinimal·LeftFluent의 항목 템플릿이 다르므로 하나를 바꿔 모든 모드가 같아진다고 가정하지 않습니다. NavigationViewConstants의 고정 크기 StaticResource는 로컬 재정의 보장 대상이 아닙니다.

### 이 컨트롤의 Resources에서 바꾸기

`NavigationViewContentBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example NavigationView_Resources -->
```xml
<ui:NavigationView PaneTitle="내 앱" PaneDisplayMode="Left" OpenPaneLength="240" IsBackButtonVisible="Auto" x:Name="ResourceDemo">
    <ui:NavigationView.Resources>
        <SolidColorBrush x:Key="NavigationViewContentBackground" Color="#2563EB" />
    </ui:NavigationView.Resources>
    <ui:NavigationView.MenuItems>
        <ui:NavigationViewItem Content="홈" TargetPageTag="home" TargetPageType="{x:Type local:HomePage}" Icon="{ui:SymbolIcon Home24}" />
    </ui:NavigationView.MenuItems>
    <ui:NavigationView.FooterMenuItems>
        <ui:NavigationViewItem Content="설정" TargetPageTag="settings" TargetPageType="{x:Type local:SettingsPage}" />
    </ui:NavigationView.FooterMenuItems>
</ui:NavigationView>
```

```csharp
ResourceDemo.Resources["NavigationViewContentBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `LeftNavigationViewSeparatorBrush` | LinearGradientBrush | Border#PART_TopSeparator Background / Border#PART_FooterSeparator Background |
| `NavigationViewContentBackground` | SolidColorBrush | Border Background |
| `NavigationViewContentGridBorderBrush` | SolidColorBrush | Border BorderBrush |
| `NavigationViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `BackButtonVisibilityToVisibilityConverter` | BackButtonVisibilityToVisibilityConverter | Button#PART_BackButton Visibility |
| `BasePaneButtonStyle` | Style | Button#PART_BackButton Style / Button#PART_ToggleButton Style / Button#PART_AutoSuggestBoxSymbolButton Style |
| `BoolToVisibilityConverter` | BoolToVisibilityConverter | Button#PART_ToggleButton Visibility |
| `BottomCompactNavigationViewItemTemplate` | ControlTemplate | 컨트롤.ItemTemplate〔PaneDisplayMode=Bottom〕 |
| `BottomNavigationViewTemplate` | ControlTemplate | 컨트롤.Template〔PaneDisplayMode=Bottom〕 |
| `DefaultNavigationViewStyle` | Style | Style BasedOn |
| `LeftCompactNavigationViewItemTemplate` | ControlTemplate | 컨트롤.ItemTemplate〔PaneDisplayMode=Left〕 |
| `LeftFluentNavigationViewItemTemplate` | ControlTemplate | 컨트롤.ItemTemplate〔PaneDisplayMode=LeftFluent〕 |
| `LeftMinimalCompactNavigationViewItemTemplate` | ControlTemplate | 컨트롤.ItemTemplate〔PaneDisplayMode=LeftMinimal〕 |
| `LeftNavigationViewTemplate` | ControlTemplate | 컨트롤.Template〔PaneDisplayMode=Left〕 / 컨트롤.Template〔PaneDisplayMode=LeftMinimal〕 / 컨트롤.Template〔PaneDisplayMode=LeftFluent〕 |
| `NavigationViewItemDefaultStyle` | Style | Style BasedOn |
| `TopCompactNavigationViewItemTemplate` | ControlTemplate | 컨트롤.ItemTemplate〔PaneDisplayMode=Top〕 |
| `TopNavigationViewTemplate` | ControlTemplate | 컨트롤.Template〔PaneDisplayMode=Top〕 |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultNavigationViewStyle` | `controls:NavigationView` | [NavigationView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

C# 구현이 이름으로 찾는 부분: `PART_AutoSuggestBoxSymbolButton`, `PART_BackButton`, `PART_FooterMenuItemsItemsControl`, `PART_MenuItemsItemsControl`, `PART_NavigationViewContentPresenter`, `PART_ToggleButton`. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.

원본 템플릿에 정의된 PART: `PART_AutoSuggestBoxSymbolButton` (Button), `PART_BackButton` (Button), `PART_FooterMenuItemsItemsControl` (ItemsControl), `PART_FooterSeparator` (Border), `PART_MenuItemsItemsControl` (ItemsControl), `PART_NavigationViewContentPresenter` (NavigationViewContentPresenter), `PART_ScrollViewer` (DynamicScrollViewer), `PART_ToggleButton` (Button), `PART_TopSeparator` (Border). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `BottomNavigationViewTemplate` | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) · 사전 루트 |
| `LeftNavigationViewTemplate` | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) · 사전 루트 |
| `TopNavigationViewTemplate` | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Header` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `HeaderVisibility` | `ContentPresenter.Visibility` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Padding` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Margin` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `Transition` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Transition` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `TransitionDuration` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.TransitionDuration` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ContentOverlay` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `IsBackEnabled` | `Button#PART_BackButton.IsEnabled` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `IsBackButtonVisible` | `Button#PART_BackButton.Visibility` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `PaneHeader` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `AutoSuggestBox` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `PaneFooter` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `OpenPaneLength` | `Grid#PaneGrid.Width` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `IsBackEnabled` | `Button#PART_BackButton.IsEnabled` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `IsBackButtonVisible` | `Button#PART_BackButton.Visibility` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `IsPaneToggleVisible` | `Button#PART_ToggleButton.Visibility` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `PaneTitle` | `TextBlock.Text` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `PaneHeader` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `AutoSuggestBox` | `ContentPresenter#AutoSuggestBoxContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `AutoSuggestBox.Icon` | `Button#PART_AutoSuggestBoxSymbolButton.Icon` | Binding to TemplatedParent | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `PaneFooter` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `FrameMargin` | `Border.Margin` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Header` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `HeaderVisibility` | `ContentPresenter.Visibility` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Padding` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Padding` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Transition` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Transition` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `TransitionDuration` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.TransitionDuration` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentOverlay` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `OpenPaneLength` | `DoubleAnimation.To` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `OpenPaneLength` | `DoubleAnimation.From` | TemplateBinding | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `IsBackEnabled` | `Button#PART_BackButton.IsEnabled` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `IsBackButtonVisible` | `Button#PART_BackButton.Visibility` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `PaneHeader` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `AutoSuggestBox` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `PaneFooter` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Header` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `HeaderVisibility` | `ContentPresenter.Visibility` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Padding` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Padding` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `Transition` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.Transition` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `TransitionDuration` | `NavigationViewContentPresenter#PART_NavigationViewContentPresenter.TransitionDuration` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentOverlay` | `ContentPresenter.Content` | TemplateBinding | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [NavigationView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml) |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [NavigationView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ContentPresenter.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewBottom.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewBottom.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Grid#PaneGrid.Margin` | `4,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Button#PART_BackButton.Margin` | `0,5,0,5` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Button#PART_ToggleButton.Margin` | `0,0,0,5` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ContentPresenter#AutoSuggestBoxContentPresenter.Margin` | `0,0,0,6` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Button#PART_AutoSuggestBoxSymbolButton.Margin` | `0,0,0,6` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#PART_TopSeparator.Height` | `1` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#PART_TopSeparator.Margin` | `0,4,0,4` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `DynamicScrollViewer#PART_ScrollViewer.Margin` | `0,0,-4,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `DynamicScrollViewer#PART_ScrollViewer.Padding` | `0,0,4,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#PART_FooterSeparator.Height` | `1` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border#PART_FooterSeparator.Margin` | `0,4,0,4` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `ItemsControl#PART_FooterMenuItemsItemsControl.Margin` | `0,0,0,4` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border.BorderThickness` | `1,1,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `Border.CornerRadius` | `8,0,0,0` | 직접 지정 / 현재 템플릿 | [NavigationViewCompact.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewCompact.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `ContentPresenter.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |
| `StackPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [NavigationViewTop.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewTop.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

### C# 코드가 직접 조회하는 리소스

| 키 | 실제 조회 코드 | 소스 |
| --- | --- | --- |
| `NavigationViewItemDataTemplate` | `UiApplication.Current.TryFindResource("NavigationViewItemDataTemplate") as DataTemplate;` | [NavigationView.Properties.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Properties.cs) |

`Application.Current.Resources`를 직접 읽으면 개별 컨트롤 Resources의 같은 키가 대신 사용되는 것은 아닙니다. 조회 시점이 생성자라면 이후 리소스 변경도 자동 바인딩으로 해석하지 않습니다.

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource NavigationViewItemForeground}` | DefaultNavigationViewStyle |
| `Background` | `Transparent` | DefaultNavigationViewStyle |
| `Margin` | `0` | DefaultNavigationViewStyle |
| `Padding` | `0` | DefaultNavigationViewStyle |
| `OpenPaneLength` | `320` | DefaultNavigationViewStyle |
| `CompactPaneLength` | `40` | DefaultNavigationViewStyle |
| `ScrollViewer.CanContentScroll` | `False` | DefaultNavigationViewStyle |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Disabled` | DefaultNavigationViewStyle |
| `ScrollViewer.VerticalScrollBarVisibility` | `Disabled` | DefaultNavigationViewStyle |
| `ScrollViewer.IsDeferredScrollingEnabled` | `False` | DefaultNavigationViewStyle |
| `FocusVisualStyle` | `{x:Null}` | DefaultNavigationViewStyle |
| `IsTabStop` | `False` | DefaultNavigationViewStyle |
| `SnapsToDevicePixels` | `True` | DefaultNavigationViewStyle |
| `OverridesDefaultStyle` | `True` | DefaultNavigationViewStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `PaneOpened` | 패널 펼침 상태로 바뀔 때 발생합니다. |
| `PaneClosed` | 패널 접힘 상태로 바뀔 때 발생합니다. |
| `SelectionChanged` | 탐색 메뉴 선택 상태가 바뀔 때 발생합니다. 현재 `SelectedItem`을 읽습니다. |
| `ItemInvoked` | 탐색 메뉴를 실행할 때 발생합니다. 단순 선택 상태 변화와 구분합니다. |
| `BackRequested` | 뒤로가기 요청입니다. 저널과 GoBack 처리를 함께 확인합니다. |
| `Navigating` | 탐색 직전 알림입니다. `NavigatingCancelEventArgs`로 취소·대상 정보를 다룹니다. |
| `Navigated` | 탐색 완료 알림입니다. 표시된 페이지·선택 상태를 갱신할 때 사용합니다. |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `object? GetHeaderContent(FrameworkElement target)` | FrameworkElement의 페이지 헤더 붙임 속성을 읽습니다. |
| `void SetHeaderContent(FrameworkElement target, object? headerContent)` | FrameworkElement의 페이지 헤더 붙임 속성을 씁니다. |
| `void SetPageProviderService(INavigationViewPageProvider navigationViewPageProvider)` | 페이지 공급 서비스를 연결합니다. |
| `void SetServiceProvider(IServiceProvider serviceProvider)` | 페이지를 생성·조회할 IServiceProvider를 연결합니다. |
| `bool Navigate(Type pageType, object? dataContext = null)` | 페이지 Type 또는 메뉴 Id·태그로 탐색합니다. 반환값으로 성공 여부를 확인합니다. |
| `bool Navigate(string pageIdOrTargetTag, object? dataContext = null)` | 페이지 Type 또는 메뉴 Id·태그로 탐색합니다. 반환값으로 성공 여부를 확인합니다. |
| `bool NavigateWithHierarchy(Type pageType, object? dataContext = null)` | 부모 메뉴 계층을 반영해 대상 페이지로 이동합니다. |
| `bool ReplaceContent(Type? pageTypeToEmbed)` | 표시 콘텐츠를 교체합니다. 일반 메뉴 탐색·저널 갱신과 목적이 다릅니다. |
| `bool ReplaceContent(UIElement pageInstanceToEmbed, object? dataContext = null)` | 표시 콘텐츠를 교체합니다. 일반 메뉴 탐색·저널 갱신과 목적이 다릅니다. |
| `bool GoForward()` | 기록의 다음 항목으로 이동합니다. |
| `bool GoBack()` | 기록의 이전 항목으로 이동합니다. |
| `void ClearJournal()` | 탐색 기록을 비웁니다. 페이지 캐시를 비우는 메서드와 동일시하지 않습니다. |

## 동작과 주의 사항

`local:HomePage`·`SettingsPage`는 앱이 정의하는 공개 Page 또는 UserControl입니다. 이 조각을 그대로 쓰려면 [실행 예제](examples/QuickStart/README.md)를 참고합니다. 기본 스타일의 패널 폭은 펼침 320, 접힘 40 DIP입니다. `LeftMinimal`은 같은 왼쪽 템플릿에 아이콘 중심 항목 템플릿을 사용하고, `LeftFluent`는 큰 아이콘과 아래 라벨을 사용하며 하위 메뉴를 지원하지 않습니다. `Top`·`Bottom`은 메뉴 위치를 바꿉니다. 최초 이동은 템플릿이 준비된 `Loaded` 이후 수행합니다. 페이지 생성과 캐시는 [탐색 구성](NavigationGuide.md)을 참고합니다.

### 페이지별 헤더 붙임 속성

`NavigationView.HeaderContent`는 `FrameworkElement`에 지정하는 공개 붙임 속성입니다. 기본값은 `null`이며 현재 페이지 헤더를 바꾸는 데 사용합니다. `NavigationParent`는 내부 구현이므로 앱에서 설정하지 않습니다.

```xml
<Page ui:NavigationView.HeaderContent="환경 설정" />
```

```csharp
ui.NavigationView.SetHeaderContent(this, "환경 설정");
```

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [NavigationView.AttachedProperties.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.AttachedProperties.cs)
- [NavigationView.Base.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Base.cs)
- [NavigationView.Events.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Events.cs)
- [NavigationView.Navigation.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Navigation.cs)
- [NavigationView.Properties.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Properties.cs)
- [NavigationView.TemplateParts.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.TemplateParts.cs)
- [NavigationView.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml)
- [Gallery: NavigationViewPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Navigation/NavigationViewPage.xaml)
