# WPF UI 한국어 컨트롤 가이드

WPF UI 컨트롤을 **무엇에 쓰는지, 어떤 요소로 구성되는지, 속성을 바꾸면 무엇이 달라지는지** 예제로 설명하는 비공식 문서입니다. Gallery를 실행하지 않아도 XAML과 C# 코드로 시작할 수 있도록 작성했습니다.

**기준 버전:** WPF-UI `4.3.0` · **확인일:** 2026-11-25 · **원본 커밋:** [`153baad`](https://github.com/lepoco/wpfui/tree/153baadeaf475875a81a4605881ca5c2dbe53972)

컨트롤·뷰·아이콘 기반 타입 **105개**를 각각 `컨트롤이름.md`로 제공합니다. 이 중 WPF-UI 공개 클래스는 75개이며 직접 선언한 공개 속성 312개(인스턴스 311개·정적 1개)를 설명합니다. 기본 WPF 타입은 테마와 함께 실제 사용되는 핵심 상속 속성을 설명합니다.

## 먼저 읽기

- [시작하기: 설치·리소스·네임스페이스](GettingStarted.md)
- [공통 속성: 크기·여백·스타일·바인딩](CommonProperties.md)
- [탐색 화면 만들기](NavigationGuide.md)
- [대화상자·호스트 구성](DialogGuide.md)
- [열거형 값과 의미](Enums.md)
- [실행 가능한 QuickStart 예제](examples/QuickStart/README.md)
- [검증 범위와 재검사 방법](VALIDATION.md)

## 필요한 컨트롤 찾기

| 목적 | 권장 문서 |
| --- | --- |
| 앱 메뉴·페이지 이동 | [NavigationView](NavigationView.md), [NavigationViewItem](NavigationViewItem.md) |
| 설정 행·접기 | [CardControl](CardControl.md), [CardExpander](CardExpander.md), [ToggleSwitch](ToggleSwitch.md) |
| 숫자·문자열 입력 | [NumberBox](NumberBox.md), [TextBox](TextBox.md), [PasswordBox](PasswordBox.md) |
| 검색 후보 | [AutoSuggestBox](AutoSuggestBox.md) |
| 확인 대화상자 | [ContentDialog](ContentDialog.md), [ContentDialogHost](ContentDialogHost.md), [MessageBox](MessageBox.md) |
| 잠깐 표시하는 결과·페이지 알림 | [Snackbar](Snackbar.md), [InfoBar](InfoBar.md) |
| 큰 데이터 목록 | [VirtualizingGridView](VirtualizingGridView.md), [VirtualizingWrapPanel](VirtualizingWrapPanel.md) |
| 페이지·재사용 뷰·창 | [Page](Page.md), [UserControl](UserControl.md), [FluentWindow](FluentWindow.md) |

## 기본 입력

| 컨트롤 | 설명 |
| --- | --- |
| [Anchor](Anchor.md) | HyperlinkButton을 그대로 상속한 호환 이름입니다. 별도 고유 속성이나 새 탐색 기능은 없습니다. |
| [Button](Button.md) | 아이콘과 의미별 색상을 지원하는 실행 버튼입니다. 클릭 한 번으로 작업을 수행할 때 사용합니다. |
| [CheckBox](CheckBox.md) | 독립적인 참·거짓·미정 선택입니다. |
| [ComboBox](ComboBox.md) | 목록에서 값을 선택하는 드롭다운입니다. |
| [DropDownButton](DropDownButton.md) | 버튼을 눌러 선택 메뉴를 여는 컨트롤입니다. |
| [HyperlinkButton](HyperlinkButton.md) | 웹 주소를 여는 버튼입니다. 화면 안의 페이지 전환 버튼과 달리 외부 URI를 엽니다. |
| [RadioButton](RadioButton.md) | 그룹에서 하나를 선택합니다. |
| [RatingControl](RatingControl.md) | 별 아이콘으로 평점을 표시하고 입력받습니다. |
| [Slider](Slider.md) | 연속·틱 간격의 숫자 범위를 조절합니다. |
| [SplitButton](SplitButton.md) | 주 실행 영역과 메뉴 화살표를 분리한 버튼입니다. |
| [ThumbRate](ThumbRate.md) | 좋아요·싫어요의 두 선택지를 제공합니다. |
| [ToggleButton](ToggleButton.md) | 눌린 상태가 유지되는 버튼입니다. |
| [ToggleSwitch](ToggleSwitch.md) | 설정을 켜고 끄는 스위치입니다. 상태별 라벨을 지원합니다. |

## 텍스트

| 컨트롤 | 설명 |
| --- | --- |
| [AccessText](AccessText.md) | 액세스 키 밑줄을 해석하는 텍스트입니다. `_저장`처럼 표기하며 보통 Label·Button 템플릿에서 사용합니다. |
| [AutoSuggestBox](AutoSuggestBox.md) | 입력 문자열을 기준으로 후보를 필터링하고 선택하거나 검색을 제출하는 컨트롤입니다. |
| [Label](Label.md) | 입력 컨트롤의 라벨과 액세스 키를 제공합니다. |
| [NumberBox](NumberBox.md) | 숫자 입력·증감·범위 검사·간단한 식 입력을 제공합니다. |
| [PasswordBox](PasswordBox.md) | 마스킹 입력과 비밀번호 공개 버튼이 있는 입력란입니다. WPF 기본 PasswordBox가 아닌 WPF-UI TextBox 파생형입니다. |
| [RichTextBox](RichTextBox.md) | FlowDocument 문단·서식을 표시하거나 편집하는 WPF RichTextBox에 선택용 표시 스타일을 더합니다. |
| [TextBlock](TextBlock.md) | Fluent 타이포그래피와 의미별 글자색을 지원하는 텍스트 표시 컨트롤입니다. |
| [TextBox](TextBox.md) | 아이콘·플레이스홀더·지우기 버튼을 더한 단일·여러 줄 입력란입니다. |

## 탐색

| 컨트롤 | 설명 |
| --- | --- |
| [BreadcrumbBar](BreadcrumbBar.md) | 현재 위치를 상위 경로부터 순서대로 보여 주는 경로 표시줄입니다. |
| [BreadcrumbBarItem](BreadcrumbBarItem.md) | BreadcrumbBar가 생성하거나 직접 사용하는 경로 항목 컨테이너입니다. |
| [ContextMenu](ContextMenu.md) | 우클릭·드롭다운 버튼에서 사용하는 팝업 메뉴입니다. |
| [Frame](Frame.md) | Page·콘텐츠를 표시하는 기본 WPF 탐색 프레임입니다. NavigationView와는 별개 탐색 스택입니다. |
| [Menu](Menu.md) | 상단 메뉴 항목을 가로로 배치합니다. |
| [MenuItem](MenuItem.md) | 기본 메뉴 항목에 IconElement 타입 아이콘 슬롯을 적용한 파생형입니다. |
| [NavigationView](NavigationView.md) | 메뉴 패널, 페이지 표시 영역, 뒤로가기, 검색, 경로를 결합한 앱 탐색 컨테이너입니다. |
| [NavigationViewContentPresenter](NavigationViewContentPresenter.md) | NavigationView 내부에서 페이지와 전환 애니메이션을 표시하는 Frame 파생 컨트롤입니다. |
| [NavigationViewItem](NavigationViewItem.md) | NavigationView의 클릭 가능한 메뉴 항목입니다. 페이지 타입·문자열 태그·아이콘·배지·하위 메뉴를 설정합니다. |
| [NavigationViewItemHeader](NavigationViewItemHeader.md) | 탐색 메뉴의 그룹 제목입니다. 페이지를 여는 버튼 대신 그룹을 구분할 때 사용합니다. |
| [NavigationViewItemSeparator](NavigationViewItemSeparator.md) | 탐색 메뉴 항목 사이의 시각적 구분선입니다. |
| [TabControl](TabControl.md) | 탭 중 하나의 본문을 선택해 표시합니다. |
| [TabItem](TabItem.md) | 기본 WPF TabControl의 탭 항목입니다. |
| [TabView](TabView.md) | 기본 WPF TabControl·TabItem을 감싼 탭 컨테이너입니다. 4.3.0에는 추가 고유 속성이 없습니다. |
| [TabViewItem](TabViewItem.md) | 기본 WPF TabControl·TabItem을 감싼 탭 항목입니다. 4.3.0에는 추가 고유 속성이 없습니다. |

## 레이아웃

| 컨트롤 | 설명 |
| --- | --- |
| [Arc](Arc.md) | 시작·끝 각도로 원호를 그리는 Shape입니다. ProgressRing 등의 시각 요소에 사용합니다. |
| [Card](Card.md) | 본문과 선택적 하단 영역을 담는 카드 컨테이너입니다. |
| [CardAction](CardAction.md) | 카드 전체가 클릭 가능한 이동·실행 항목입니다. 오른쪽 화살표로 후속 동작을 표현합니다. |
| [CardColor](CardColor.md) | 색상과 이름·설명을 함께 보여 주는 색상 표본 카드입니다. |
| [CardControl](CardControl.md) | 아이콘·헤더·오른쪽 콘텐츠로 설정 행을 만드는 카드형 버튼입니다. |
| [CardExpander](CardExpander.md) | 설정 헤더와 접을 수 있는 본문을 결합한 카드형 Expander입니다. |
| [EffectThicknessDecorator](EffectThicknessDecorator.md) | 효과가 요소 밖으로 나갈 공간과 열림 애니메이션을 관리하는 Decorator입니다. |
| [Expander](Expander.md) | 헤더 아래 본문을 접고 펼칩니다. |
| [Separator](Separator.md) | 인접 영역을 구분하는 시각적 선입니다. |
| [ToolBar](ToolBar.md) | 작업 버튼을 묶어 표시하는 도구 모음입니다. |

## 창과 대화상자

| 컨트롤 | 설명 |
| --- | --- |
| [ClientAreaBorder](ClientAreaBorder.md) | FluentWindow 템플릿에서 클라이언트 영역과 시스템 창 테두리를 보정하는 Border입니다. |
| [ContentDialog](ContentDialog.md) | 현재 창 위에 겹쳐 표시하는 비동기 대화상자입니다. 별도 최상위 Window를 만들지 않습니다. |
| [ContentDialogHost](ContentDialogHost.md) | ContentDialog를 창 안에 올리고 포커스·형제 요소 격리를 관리하는 전용 호스트입니다. |
| [FluentWindow](FluentWindow.md) | Fluent 창 테두리·모서리·배경 재질을 구성하는 Window입니다. |
| [Flyout](Flyout.md) | 주변 UI 위에 짧은 정보나 보조 동작을 표시하는 팝업 컨트롤입니다. |
| [MessageBox](MessageBox.md) | 별도 Window로 표시하는 비동기 메시지 창입니다. ContentDialog와 달리 화면 안 호스트를 요구하지 않습니다. |
| [TitleBar](TitleBar.md) | 사용자 지정 창 제목 영역과 시스템 창 버튼을 제공합니다. |
| [TitleBarButton](TitleBarButton.md) | TitleBar가 내부에서 사용하는 창 제어 버튼입니다. 사용자 지정 제목 영역을 만들 때의 저수준 요소입니다. |

## 상태와 알림

| 컨트롤 | 설명 |
| --- | --- |
| [Badge](Badge.md) | 짧은 텍스트나 UI 콘텐츠에 의미별 색상 배경을 제공하는 배지입니다. |
| [InfoBadge](InfoBadge.md) | 짧은 숫자·문자열·상태 아이콘을 표시하는 작은 배지입니다. |
| [InfoBar](InfoBar.md) | 페이지 안에 유지되는 정보·성공·경고·오류 메시지입니다. |
| [LoadingScreen](LoadingScreen.md) | 라이브러리에 정의된 ContentControl 파생형입니다. 4.3.0에는 별도 고유 속성·진행 상태 API가 없습니다. |
| [ProgressBar](ProgressBar.md) | 가로·세로 막대로 진행률 또는 불확정 대기를 표시합니다. |
| [ProgressRing](ProgressRing.md) | 원형 진행률 또는 회전하는 대기 상태를 표시합니다. |
| [Snackbar](Snackbar.md) | 작업 결과를 잠시 보여 주고 자동으로 숨기는 알림입니다. SnackbarPresenter가 표시 순서를 관리합니다. |
| [SnackbarPresenter](SnackbarPresenter.md) | Snackbar의 현재 표시·대기열·자동 숨김을 관리하는 표시 영역입니다. |
| [StatusBar](StatusBar.md) | 창 하단의 상태 항목을 표시합니다. |
| [ToolTip](ToolTip.md) | 포인터가 머무를 때 표시하는 짧은 도움말입니다. |

## 날짜와 시간

| 컨트롤 | 설명 |
| --- | --- |
| [Calendar](Calendar.md) | 월·연도 달력을 직접 표시하고 날짜를 선택합니다. |
| [CalendarDatePicker](CalendarDatePicker.md) | 버튼을 누르면 달력을 열어 날짜를 고르는 컨트롤입니다. |
| [DatePicker](DatePicker.md) | 텍스트 입력과 달력 팝업이 결합된 기본 WPF 날짜 선택기입니다. |
| [TimePicker](TimePicker.md) | 시간 선택용 공개 타입이지만 4.3.0의 선택 UI는 미완성입니다. |

## 아이콘과 미디어

| 컨트롤 | 설명 |
| --- | --- |
| [FontIcon](FontIcon.md) | 지정한 글꼴의 유니코드 글리프를 아이콘으로 표시합니다. |
| [FontIconSource](FontIconSource.md) | 글꼴 아이콘의 재사용 가능한 속성 데이터입니다. |
| [IconElement](IconElement.md) | 시각 아이콘들의 추상 기반 클래스입니다. Foreground와 아이콘 변환 경로를 공유합니다. |
| [IconSource](IconSource.md) | 아이콘 생성에 사용할 속성 데이터의 추상 기반 클래스입니다. 시각 요소 자체는 아닙니다. |
| [IconSourceElement](IconSourceElement.md) | IconSource를 실제 아이콘으로 변환하기 위한 어댑터입니다. 4.3.0에서는 단독 렌더링이 아닌 아이콘 속성의 강제 변환 경로로 사용합니다. |
| [Image](Image.md) | 비율 조정과 둥근 모서리를 지원하는 이미지 컨트롤입니다. |
| [ImageIcon](ImageIcon.md) | 이미지 파일을 IconElement 슬롯에 넣는 어댑터입니다. |
| [SymbolIcon](SymbolIcon.md) | WPF UI에 포함된 Fluent System Icons 글꼴의 아이콘을 표시합니다. |
| [SymbolIconSource](SymbolIconSource.md) | Fluent 심볼 아이콘의 재사용 가능한 속성 데이터입니다. |

## 목록과 데이터

| 컨트롤 | 설명 |
| --- | --- |
| [DataGrid](DataGrid.md) | 기본 WPF 표에 자동·추가 열의 표시·편집 스타일 연결을 더한 컨트롤입니다. |
| [GridView](GridView.md) | ListView.View에 연결하는 열 기반 보기입니다. 단독으로 배치하는 UIElement는 아닙니다. |
| [GridViewColumn](GridViewColumn.md) | ListView의 GridView 열입니다. WPF 열에 최소·최대 너비 제한을 더합니다. |
| [GridViewColumnHeader](GridViewColumnHeader.md) | GridView 열의 헤더를 표시하고 크기 조절·클릭을 제공하는 기본 WPF 컨테이너입니다. |
| [GridViewHeaderRowPresenter](GridViewHeaderRowPresenter.md) | GridView의 헤더 행을 템플릿 안에서 그리는 프레젠터입니다. 고유 속성은 없습니다. |
| [GridViewRowPresenter](GridViewRowPresenter.md) | GridView의 행을 템플릿 안에서 그리는 프레젠터입니다. 고유 속성은 없습니다. |
| [ItemsControl](ItemsControl.md) | 항목 데이터를 ItemTemplate로 반복 표시합니다. 선택·스크롤은 기본 기능이 아닙니다. |
| [ListBox](ListBox.md) | 항목 선택과 스크롤을 제공하는 기본 목록입니다. |
| [ListBoxItem](ListBoxItem.md) | ListBox의 선택 가능한 항목 컨테이너입니다. |
| [ListView](ListView.md) | 항목 목록과 GridView 열 보기를 제공하는 WPF ListView 파생형입니다. |
| [ListViewItem](ListViewItem.md) | ListView가 선택·포커스·콘텐츠 표시를 위해 생성하는 항목 컨테이너입니다. |
| [TreeView](TreeView.md) | 계층 항목을 표시하는 기본 트리입니다. |
| [TreeViewItem](TreeViewItem.md) | 기본 TreeViewItem에 아이콘 슬롯을 더한 트리 항목입니다. |

## 가상화와 스크롤

| 컨트롤 | 설명 |
| --- | --- |
| [DynamicScrollBar](DynamicScrollBar.md) | 스크롤 중·마우스 상호작용 상태에 따라 외형이 변하는 ScrollBar입니다. |
| [DynamicScrollViewer](DynamicScrollViewer.md) | 스크롤 활동에 따라 스크롤바 상태를 바꾸는 PassiveScrollViewer 파생형입니다. |
| [PassiveScrollViewer](PassiveScrollViewer.md) | 내부 스크롤 끝에서 휠 입력을 상위로 넘길 수 있는 ScrollViewer입니다. |
| [ScrollBar](ScrollBar.md) | 스크롤 위치를 범위 값으로 조작하는 저수준 컨트롤입니다. |
| [ScrollViewer](ScrollViewer.md) | 단일 콘텐츠가 뷰포트보다 클 때 스크롤합니다. |
| [VirtualizingGridView](VirtualizingGridView.md) | 가상화된 타일 배치를 제공하는 ListView 파생형입니다. 열 기반 GridView와 이름을 구별합니다. |
| [VirtualizingItemsControl](VirtualizingItemsControl.md) | 가상화 패널을 사용하는 대량 항목 표시용 ItemsControl입니다. |
| [VirtualizingPanelBase](VirtualizingPanelBase.md) | VirtualizingWrapPanel의 추상 기반 클래스이며 IScrollInfo를 구현합니다. |
| [VirtualizingWrapPanel](VirtualizingWrapPanel.md) | 보이는 영역과 캐시 범위의 항목만 생성하는 줄바꿈 패널입니다. ItemsControl.ItemsPanel에 넣습니다. |

## 실험적 타입

| 컨트롤 | 설명 |
| --- | --- |
| [TreeGrid](TreeGrid.md) | 트리형 데이터 표를 위한 미완성 공개 타입입니다. |
| [TreeGridHeader](TreeGridHeader.md) | 미완성 TreeGrid의 헤더 데이터·요소 타입입니다. |
| [TreeGridItem](TreeGridItem.md) | 미완성 TreeGrid의 항목 타입입니다. 고유 속성·완성된 항목 동작이 없습니다. |

## 뷰

| 컨트롤 | 설명 |
| --- | --- |
| [Page](Page.md) | Frame 또는 NavigationView에서 표시하는 화면 단위입니다. WPF 기본 타입에 테마 스타일을 적용합니다. |
| [UserControl](UserControl.md) | 재사용 화면·부분 뷰를 만드는 기본 WPF 컨테이너입니다. NavigationView의 페이지로도 사용할 수 있습니다. |
| [Window](Window.md) | 기본 WPF 최상위 창입니다. WPF UI 테마는 사용할 수 있지만 FluentWindow 전용 속성은 없습니다. |

## 문서 범위와 읽는 방법

- 핵심 패키지 `WPF-UI`의 `Wpf.Ui.Controls` 공개 시각 컨트롤, 관련 아이콘 데이터·추상 기반 타입과 기본 WPF 테마 컨트롤을 다룹니다. 뷰는 Page·UserControl·Window·FluentWindow로 설명합니다.
- `NavigationView.HeaderContent`와 [ContentDialogHostBehavior](ContentDialogHostBehavior.md)처럼 화면 구성에 필요한 공개 붙임 속성도 설명합니다.
- 개별 파일에는 사용 목적, XAML, C# 변경 예제, 고유 속성 전체, 자주 쓰는 상속 속성, 스타일 Setter, 이벤트·주요 메서드, 구현상 제한과 커밋 고정 소스 링크를 제공합니다.
- 기본 WPF의 수백 개 상속 API·이벤트를 모두 복제하지는 않습니다. 공통 규칙과 실사용 핵심 속성을 설명하고 WPF-UI에서 추가한 인스턴스 속성은 모두 포함합니다.
- Gallery 앱 자체의 화면·ViewModel·샘플 전용 컨트롤, 서비스·DI 전체 API, 별도 패키지 `Wpf.Ui.Tray`는 이번 범위에 포함하지 않습니다.
- `ColorPicker`·`VirtualizingUniformGrid`는 4.3.0에서 internal이므로 앱용 공개 컨트롤 문서에서 제외합니다. `NavigationViewBreadcrumbItem`도 내부 구현입니다.
- 공개 타입이어도 TimePicker·TreeGrid 계열은 미완성입니다. 각 페이지에서 제한을 먼저 확인하세요.

등록 기본값은 **스타일 적용 전 값**이며 실제 값과 다를 수 있습니다. 예를 들어 NavigationView.OpenPaneLength의 등록값은 0이지만 기본 스타일은 320 DIP를 설정합니다. 코드 조각의 Demo·Presenter·DialogHost는 같은 페이지의 XAML에서 선언한 이름입니다. HomePage·SettingsPage와 이미지 파일은 앱이 준비해야 합니다.

## 출처·유지보수

원본: [lepoco/wpfui](https://github.com/lepoco/wpfui) · [공식 API 문서](https://wpfui.lepo.co/api/Wpf.Ui.Controls.html) · [릴리스 4.3.0](https://github.com/lepoco/wpfui/releases/tag/4.3.0).

이 문서는 소스의 설명 주석을 단순 번역한 API 목록이 아니라 구현·스타일·Gallery를 함께 확인한 사용 가이드입니다. 최신 main의 미출시 변경은 섞지 않습니다. 버전을 올릴 때는 `source-manifest.json`과 소스·스타일·예제를 함께 갱신해야 합니다.

[원본 라이선스 및 출처 고지](THIRD_PARTY_NOTICES.md)를 참고하세요.
