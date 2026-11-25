# NavigationViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

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
