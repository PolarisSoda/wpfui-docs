# 탐색 화면 만들기

[전체 목차](README.md) · [NavigationView](NavigationView.md) · [NavigationViewItem](NavigationViewItem.md)

NavigationView는 **메뉴 항목**, **현재 페이지**, **탐색 저널**, **페이지 캐시**를 함께 관리합니다. 메뉴 문구를 바꾸는 것과 실제 페이지 이동은 서로 다른 작업입니다.

## 메뉴와 페이지 연결

```xml
<ui:NavigationView x:Name="Navigation" PaneDisplayMode="Left" PaneTitle="내 앱">
    <ui:NavigationView.MenuItems>
        <ui:NavigationViewItem Content="홈" TargetPageTag="home"
            TargetPageType="{x:Type local:HomePage}" Icon="{ui:SymbolIcon Home24}" />
        <ui:NavigationViewItem Content="설정" TargetPageTag="settings"
            TargetPageType="{x:Type local:SettingsPage}" NavigationCacheMode="Enabled" />
    </ui:NavigationView.MenuItems>
</ui:NavigationView>
```

`TargetPageType`은 실제 화면 Type입니다. 단순 문자열 페이지 이름이 아닙니다. `TargetPageTag`는 Type과 별도로 사용할 고유 문자열 경로입니다.

```csharp
// 창 생성자에서 InitializeComponent() 다음에 연결합니다.
Loaded += (_, _) => Navigation.Navigate(typeof(HomePage));

// 버튼 이벤트 등에서 이동합니다.
bool success = Navigation.Navigate("settings");
if (Navigation.CanGoBack)
    Navigation.GoBack();
```

템플릿 적용 전 Navigate를 호출하면 표시 영역이 준비되지 않을 수 있습니다. 최초 탐색은 Loaded 이후 실행합니다. DI를 연결하지 않는 간단한 예제에서는 공개 화면 클래스와 인자 없는 생성자를 사용합니다. 생성자 의존성이 있는 화면은 SetServiceProvider 또는 SetPageProviderService로 생성 경로를 연결해야 합니다.

## 패널의 모양

| PaneDisplayMode | 화면 변화 | 사용 조건 |
| --- | --- | --- |
| Left | 왼쪽 패널과 표준 항목 | IsPaneOpen으로 펼침·접힘을 조절합니다. |
| LeftMinimal | 왼쪽 패널에 아이콘 중심 항목 | 일반 Left와 같은 패널 템플릿에 다른 항목 템플릿을 사용합니다. |
| LeftFluent | 큰 아이콘과 아래 라벨 | 하위 MenuItems 미지원, 스타일에서 OpenPaneLength를 NaN으로 설정합니다. |
| Top | 메뉴가 상단에 위치 | 가로로 길어진 메뉴 수와 공간을 확인합니다. |
| Bottom | 메뉴가 하단에 위치 | 콘텐츠 높이와 하단 영역을 함께 고려합니다. |

```csharp
Navigation.PaneDisplayMode = Wpf.Ui.Controls.NavigationViewPaneDisplayMode.Top;
Navigation.IsPaneOpen = false;
Navigation.OpenPaneLength = 240;
```

4.3.0에는 `PaneDisplayMode=Auto`가 없습니다. `IsPaneVisible`·`AlwaysShowHeader`는 공개 저장 속성이지만 제공 템플릿·구현에서 화면 변화로 이어지는 연결을 찾을 수 없습니다. 속성 이름만 보고 반응형 모드나 전체 패널 숨김이 구현되었다고 가정하지 않습니다.

뒤로가기의 `Auto`는 기본 변환기에서 **Visible**로 처리됩니다. 탐색 불가능할 때 숨기는 정책이 아니라 활성 여부를 `IsBackEnabled`로 따로 나타냅니다.

## 하위 메뉴와 경로

```xml
<ui:NavigationViewItem Content="관리">
    <ui:NavigationViewItem.MenuItems>
        <ui:NavigationViewItem Content="사용자" TargetPageTag="users"
            TargetPageType="{x:Type local:UsersPage}" />
    </ui:NavigationViewItem.MenuItems>
</ui:NavigationViewItem>
```

상위 항목의 MenuItems에 하위 항목을 넣습니다. 계층을 반영한 이동은 `NavigateWithHierarchy(typeof(UsersPage))`를 사용합니다. `UsersPage`는 앱이 정의해야 하는 공개 화면입니다. `LeftFluent`에서는 이 구성을 사용하지 않습니다.

`NavigationView.BreadcrumbBar`에 BreadcrumbBar를 연결하면 계층 탐색 경로와 연동할 수 있습니다. 단독 BreadcrumbBar의 클릭만으로 앱이 이동하는 것은 아니므로 일반 용도에서는 ItemClicked·Command를 직접 처리합니다.

## 캐시와 기록

| 설정 | 4.3.0의 실제 구현 |
| --- | --- |
| NavigationCacheMode.Disabled | 페이지 생성 함수를 매번 호출합니다. 공급 서비스가 싱글턴이면 그 서비스의 수명 정책이 별도로 작동할 수 있습니다. |
| NavigationCacheMode.Enabled | 페이지 Type을 키로 인스턴스를 보관하고 재사용합니다. |
| NavigationCacheMode.Required | 현재 NavigationCache 구현에서는 Enabled와 같은 저장 경로를 사용합니다. 별도 용량·퇴출 정책은 없습니다. |
| ClearJournal() | 이동 기록을 비웁니다. Type 키 페이지 캐시 삭제 메서드는 아닙니다. |

메뉴 항목 둘이 같은 Type을 가리키면 Type 기반 사전·캐시가 겹칠 수 있습니다. 데이터만 다른 화면을 여러 메뉴에 연결할 때는 타입·데이터 전달·페이지 수명을 함께 설계합니다.

## 페이지별 헤더

```xml
<Page ui:NavigationView.HeaderContent="환경 설정">
    <Grid />
</Page>
```

위 조각에는 시작하기의 네임스페이스 선언이 필요합니다. 코드로는 `NavigationView.SetHeaderContent(page, "환경 설정")`를 사용합니다. `NavigationParent`는 내부 연결용 속성입니다.

## 기준 소스

- [탐색 구현](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.Navigation.cs)
- [페이지 캐시](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationCache.cs)
- [뒤로가기 표시 변환기](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Converters/BackButtonVisibilityToVisibilityConverter.cs)
