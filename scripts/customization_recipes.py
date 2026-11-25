"""소스에서 확인한 컨트롤별 조정 경로와 제약. 렌더러가 각 문서에 삽입합니다."""
NOTES={
 'Card':'''가장 간단한 반지름 조정은 `Card.Resources`의 `ControlCornerRadius` 재정의입니다. 기본 스타일의 `Border.CornerRadius` → 내부 `ContentBorder.CornerRadius`로 이어집니다. 별도의 `Card.CornerRadius` CLR 속성은 없습니다.

**Footer가 있으면 예외입니다.** `HasFooter=True` 트리거가 본문을 `4,4,0,0`으로 바꾸고 FooterBorder는 `0,0,4,4`로 고정합니다. 이 경우 Resources·Border.CornerRadius 설정만으로 전체 반지름이 바뀌지 않습니다. [Footer 포함 12 DIP 카드 템플릿](examples/CustomizationLab/CardWithFooter.xaml)은 이 두 부분까지 수정한 완전한 예제입니다. 이 템플릿에 쓰는 `CustomCardTopRadius`·`CustomCardBottomRadius`는 예제가 정의한 키이며 원본 내장 키가 아닙니다.''',
 'Button':'''모서리는 공개 `CornerRadius` 속성으로 직접 바꾸거나 `Resources["ControlCornerRadius"]`로 기본 스타일 값을 바꿀 수 있습니다. 상태별 색까지 맞추려면 Normal·PointerOver·Pressed·Disabled 키를 구분합니다. `Appearance=Primary`는 AccentButton 계열, `Secondary`는 Button 계열의 색을 주로 사용하므로 ButtonBackground만 바꾸어 Primary 버튼 색이 바뀐다고 가정하지 않습니다. 직접 지정한 Background·CornerRadius 로컬 값은 스타일의 리소스 경로보다 우선할 수 있습니다.''',
 'CardAction':'''공개 CornerRadius CLR 속성은 없지만 기본 스타일은 `Border.CornerRadius`와 `ControlCornerRadius`를 연결합니다. 따라서 CardAction.Resources의 ControlCornerRadius를 재정의하거나 Style.Setter의 Border.CornerRadius를 설정합니다. Chevron의 크기·여백은 StaticResource 참조이므로 로컬 Resources에 같은 이름을 추가하는 것만으로 바뀐다고 보장하지 않습니다.''',
 'CardControl':'''모서리는 공개 CornerRadius 또는 ControlCornerRadius 리소스로 조정합니다. 헤더·콘텐츠·아이콘 간격은 템플릿의 서로 다른 슬롯입니다. `CardControlIconMargin`·`CardControlContentMargin`·`CardControlIconSize`는 StaticResource이므로 개별 인스턴스에서 바꾸려면 적용된 템플릿의 연결을 수정하는 방법을 사용합니다. 단순 안쪽 여백은 Padding을 먼저 사용합니다.''',
 'CardExpander':'''공개 CornerRadius·ContentPadding·IsExpanded를 먼저 사용합니다. ControlCornerRadius를 Resources에서 바꾸는 경로도 있습니다. 원본은 CornerRadius·IsExpanded를 MultiBinding과 CornerRadiusSplitConverter에 전달해 헤더와 펼친 본문의 모서리를 위·아래로 분리합니다. Card의 Footer처럼 4로 고정하는 구조와 다릅니다. 아이콘·Chevron 크기 StaticResource는 로컬 재정의를 보장하지 않습니다.''',
 'InfoBadge':'''기본 암시적 스타일은 `ValueInfoBadgeStyle`입니다. 숫자 배지 반지름은 **StaticResource `ValueInfoBadgeStyleCornerRadius`**를 사용하므로 `CornerRadius=12` 또는 `InfoBadge.Resources`의 같은 키만으로 바뀐다고 안내해서는 안 됩니다. 숫자형 반지름 변경은 Value 템플릿을 복제·수정합니다.

반면 **`DotInfoBadgeStyle`·`IconInfoBadgeStyle`은 CornerRadius에 TemplateBinding**하므로 공개 CornerRadius가 반영됩니다. 아이콘형은 IconInfoBadgeStyle을 선택한 뒤 Icon을 넣고, 점형은 DotInfoBadgeStyle을 선택합니다. 두 경우는 문자열 Value를 표시하는 스타일과 다릅니다. `InfoBadgeInformationSeverityBackgroundBrush`라는 참조는 원본에서 발견되지만 같은 이름의 정의가 없습니다. 실제 정보 상태에는 `InfoBadgeInformationalSeverityBackgroundBrush`가 사용되므로 발견된 이름을 모두 정상 조정 키로 취급하지 않습니다.''',
 'TextBox':'''TextControlThemePadding·TextControlThemeMinHeight·ControlCornerRadius처럼 DynamicResource로 연결된 크기 리소스를 인스턴스 Resources에서 바꿀 수 있습니다. 배경은 TextControlBackground·TextControlBackgroundPointerOver·TextControlBackgroundFocused·TextControlBackgroundDisabled로 나뉩니다. `IsTextSelectionEnabled=True`의 읽기 전용 표시 스타일은 Padding·Background·BorderThickness·Template까지 변경하므로 일반 입력 스타일의 조정이 그대로 보이지 않을 수 있습니다.''',
 'PasswordBox':'''일반 입력부의 TextControl 계열 DynamicResource와 ControlCornerRadius를 재정의할 수 있습니다. 공개·숨김·지우기 아이콘은 `PasswordBoxRevealIcon`·`PasswordBoxHideIcon`·`PasswordBoxClearIcon`이라는 별도 키를 사용하지만 StaticResource 참조입니다. 키가 있다는 이유로 PasswordBox.Resources에서 언제든 교체할 수 있다고 보장하지 않습니다. 아이콘을 교체하는 템플릿을 만들 때 공유 UIElement의 부모 충돌과 원본 x:Shared=False 조건도 유지합니다.''',
 'NumberBox':'''TextControl 계열 리소스를 바꾸면 입력부 색·여백·반지름을 조정할 수 있습니다. Inline·Compact·Hidden은 다른 증감 버튼 배치이며 Compact 팝업 영역은 입력 테두리와 별개의 템플릿 부분입니다. 스핀 아이콘·고정 폭까지 바꾸려면 현재 모드의 템플릿을 수정하고 PART 이름과 이벤트 연결을 보존합니다.''',
 'AutoSuggestBox':'''바깥 입력 영역은 ControlCornerRadius·TextControlThemePadding 등에 연결되고 후보 팝업은 FlyoutBackground·FlyoutBorderBrush 등 별도 키를 사용합니다. 입력란과 후보 목록을 한 종류의 Background로 조정한다고 가정하지 않습니다. ItemTemplate·DisplayMemberPath로 후보 표시를 바꾸고 팝업 높이는 MaxSuggestionListHeight를 사용합니다.''',
 'ComboBox':'''입력·선택 영역과 드롭다운 Popup의 색상·테두리·반지름은 서로 다른 템플릿 부분입니다. ControlCornerRadius와 PopupCornerRadius, ComboBoxBackground와 ComboBoxDropDownBackground 등을 구분합니다. IsEditable에 따라 텍스트 입력 템플릿도 달라집니다. ItemTemplate은 데이터 표시, ItemContainerStyle은 ComboBoxItem 외형입니다.''',
 'DropDownButton':'''바깥 버튼은 Button 계열 스타일을 기반으로 하므로 상속된 CornerRadius·Appearance를 우선 사용하고 공통 키는 Button 문서도 확인합니다. Flyout에 연결하는 ContextMenu는 별도 팝업이므로 메뉴 색은 ContextMenu.Resources에서 조정합니다. 메뉴 위치를 바꾸려면 버튼 코드의 Placement.Bottom 설정과도 충돌하는지 확인합니다.''',
 'SplitButton':'''주 버튼과 화살표 토글 버튼이 별도로 구성됩니다. 바깥 모서리·Appearance는 상속 Button 속성을 우선 사용하고, 분리선·화살표 영역의 색·폭은 보조 스타일과 템플릿에서 조정합니다. ControlTemplate 교체 시 `PART_Toggle`(Border)·`PART_ToggleButton`(ToggleButton)을 보존해야 합니다. PART_ToggleButton이 없으면 OnApplyTemplate에서 예외를 던집니다.''',
 'NavigationView':'''배치·폭은 PaneDisplayMode·OpenPaneLength·CompactPaneLength로 먼저 설정합니다. 메뉴 항목 외형은 ItemTemplate(ControlTemplate), 본문 배경은 NavigationViewContentBackground 등 리소스로 따로 조정합니다. Left·Top·Bottom의 템플릿과 LeftMinimal·LeftFluent의 항목 템플릿이 다르므로 하나를 바꿔 모든 모드가 같아진다고 가정하지 않습니다. NavigationViewConstants의 고정 크기 StaticResource는 로컬 재정의 보장 대상이 아닙니다.''',
 'NavigationViewItem':'''메뉴 항목 상태마다 BackgroundPointerOver·BackgroundPressed·BackgroundSelected가 따로 있습니다. ControlCornerRadius 참조가 있는 항목 템플릿과 고정 모서리·폭을 쓰는 다른 표시 모드가 함께 있으므로 사용 중인 NavigationView.PaneDisplayMode와 ItemTemplate을 확인합니다. `Style`만 바꿨는데 모양이 그대로면 상위 NavigationView가 항목 ControlTemplate을 지정하는 경로를 확인합니다.''',
 'NavigationViewContentPresenter':'''IsDynamicScrollViewerEnabled에 따라 서로 다른 ControlTemplate을 선택합니다. 기본 Frame의 ContentTemplate을 바꾸는 것과 스크롤 컨테이너·전환 효과를 구성하는 ControlTemplate 교체를 구별합니다. 실제 앱에서는 상위 NavigationView 템플릿의 PART 연결을 유지합니다.''',
 'ListView':'''ViewState=Default·GridView에 따라 기본 스타일이 다른 템플릿을 선택합니다. 항목 모서리·선택 색은 ListViewItem 쪽에서 조정하고, 열 헤더는 GridViewColumnHeader, 셀은 GridViewColumn.CellTemplate을 사용합니다. ItemsPanel은 배치·가상화에 관여하므로 단순 외형 변경을 위해 스크롤·가상화 패널을 제거하지 않습니다.''',
 'ListViewItem':'''선택·포인터 강조 색과 왼쪽 선택 표시 막대는 ListViewItem 계열 리소스에 연결됩니다. ControlCornerRadius는 이 항목 컨테이너에 적용하는 것이며 소유 ListView 자체의 반지름과 다릅니다. 데이터 목록에서는 ItemContainerStyle을 사용합니다. GridView 모드와 일반 목록 모드의 템플릿도 구분합니다.''',
 'DataGrid':'''표 전체 배경·테두리는 DataGrid에, 행·셀은 RowStyle·CellStyle에, 열 헤더는 ColumnHeaderStyle에 설정합니다. CheckBoxColumnElementStyle 등 고유 속성은 열 내부의 표시·편집 컨트롤 스타일입니다. 테마 키를 재정의할 때 Color와 Brush 타입을 혼동하지 말고, 상태별 선택·포인터 색까지 함께 확인합니다.''',
 'InfoBar':'''ControlCornerRadius는 기본 테두리로 연결됩니다. Severity별 배경·테두리·아이콘 색은 InfoBarInformational/Success/Warning/Error 계열 키로 나뉘며 ContentBorder에 직접 적용되는 트리거도 있습니다. 컨트롤 Background 하나만 바꾸면 모든 Severity 상태가 바뀌는 구조는 아닙니다.''',
 'ProgressRing':'''진행 호는 Foreground, 뒤쪽 링은 CoverRingStroke·CoverRingVisibility로 먼저 조정합니다. 기본 스타일이 ProgressRingForegroundThemeBrush·ProgressRingBackgroundThemeBrush를 DynamicResource로 공급하므로 두 리소스를 따로 재정의할 수도 있습니다. 호 두께·애니메이션 구조는 템플릿의 고정값과 Arc 연결을 수정해야 합니다.''',
 'ProgressBar':'''ProgressBarForeground·ProgressBarBackground와 불확정 상태의 ProgressBarIndeterminateBackground를 구분합니다. 모서리 반지름은 기본 템플릿의 고정값일 수 있으며 ControlCornerRadius라는 키가 다른 컨트롤에서 쓰인다는 이유로 이 막대에도 적용된다고 가정하지 않습니다. 두께는 Height·Width, 진행 비율은 Value로 조정합니다.''',
 'Snackbar':'''생성자에 Presenter가 필요하므로 Snackbar.Resources는 C#에서 채운 뒤 Show를 호출하는 방식이 간단합니다. 키의 실제 대소문자는 `SnackBarBackground`·`SnackBarBorderBrush`·`SnackBarForeground`입니다. Appearance별 트리거는 Palette 계열 Color도 사용하므로 Brush와 Color의 타입을 구별합니다. 스낵바 자체와 Presenter의 위치·Margin을 나눠 조정합니다.''',
 'SnackbarPresenter':'''현재 표시 위치·최대 폭·Margin은 Presenter에, 알림의 배경·아이콘·내용은 Snackbar 인스턴스에 설정합니다. Content는 외부에서 대입할 수 없으므로 스타일 조정을 위해 Content에 새 컨트롤을 직접 넣는 대신 Snackbar 생성자와 Show 경로를 사용합니다.''',
 'ContentDialog':'''대화상자는 PopupCornerRadius, 하단 영역은 DynamicResource DialogFooterCornerRadius, 상단 오버레이는 StaticResource DialogOverlayCornerRadius를 사용합니다. 따라서 PopupCornerRadius 하나를 바꿨다고 모든 내부 레이어가 같은 반지름으로 바뀌지는 않습니다. SmokeFill·본문 배경·하단 배경도 서로 다른 키입니다. 전용 ContentDialogHost 경로에서는 호스트가 배경 격리를 관리하므로 ContentDialogHost 문서도 확인합니다.''',
 'ContentDialogHost':'''전용 호스트의 스모크 배경은 ContentDialogSmokeFill을 사용합니다. 대화상자 본체의 ContentDialogBackground와 구별합니다. 최상위 창 안에서 이 호스트에 Resources를 두면 호스트와 그 자식 대화상자의 조회 범위에 영향을 줄 수 있습니다. 리소스를 앱 전체에 두면 모든 호스트에 영향을 줍니다.''',
 'MessageBox':'''별도 Window이므로 MessageBox.Resources에서 MessageBoxBackground·MessageBoxForeground·MessageBoxTopOverlay 등의 DynamicResource를 재정의할 수 있습니다. 내부 버튼·구분선·오버레이의 고정 레이아웃 값은 외부 Width·Padding만으로 모두 바뀌지 않습니다. 크기·소유 창을 지정한 뒤 ShowDialogAsync를 호출합니다.''',
 'ToggleSwitch':'''켜짐·꺼짐·포인터·눌림·비활성 상태마다 Fill·KnobFill 리소스가 다릅니다. 색 변경은 이 상태 키를 사용하고, 라벨 위치는 LabelPosition으로 설정합니다. 스위치 트랙·손잡이 크기와 모서리는 템플릿의 고정값이므로 ControlCornerRadius를 재정의하는 방식으로 스위치 형태가 바뀌는 것은 아닙니다.''',
 'ToggleButton':'''Checked·Unchecked와 Pressed·Disabled 색상이 구분됩니다. 공개 IsChecked·Content와 Style.Trigger를 먼저 사용하고, 상태별 리소스를 재정의해 테마 색을 바꿉니다. Button의 Appearance 타입 속성이 기본 WPF ToggleButton에 있다고 가정하지 않습니다.''',
 'CheckBox':'''일반 사각 체크박스와 별도 keyed Style이 함께 있습니다. 모양 변경은 원하는 스타일 선택, IsChecked·IsThreeState, 상태별 CheckBoxCheckBackground/Stroke/Glyph 계열 리소스로 구분합니다. 체크 표식 경로·박스의 고정 크기를 바꾸려면 템플릿 수정이 필요합니다.''',
 'RadioButton':'''원·선택점·라벨의 상태별 리소스가 나뉩니다. 그룹 동작은 GroupName·IsChecked를 유지하고 색은 RadioButtonOuterEllipse·CheckGlyph·Foreground 계열 키를 사용합니다. 원의 지름·선택점 크기는 템플릿의 고정값입니다.''',
 'Slider':'''트랙·손잡이·눈금 색은 SliderTrackFill·SliderThumbBackground·SliderTickBarFill 계열 키로 나뉩니다. 큰 막대 두께·손잡이 크기는 템플릿 내 고정 Width·Height를 수정해야 할 수 있습니다. Range의 PART_Track·Thumb·Decrease/Increase 버튼 연결을 유지합니다.''',
 'FluentWindow':'''WindowBackground·WindowForeground는 테마 리소스이며, 시스템 배경 재질은 WindowBackdropType이라는 별도 OS 기능입니다. Resources의 배경색을 바꾸는 것과 Mica가 보이도록 창 배경을 처리하는 것을 구분합니다. 모서리도 내부 콘텐츠 반지름과 시스템 창 WindowCornerPreference가 다릅니다.''',
 'Window':'''WindowBackground·WindowForeground 등은 창 안 콘텐츠의 테마 색입니다. 기본 Window에 WindowBackdropType·WindowCornerPreference가 생기는 것은 아닙니다. 창 크롬·시스템 모서리는 FluentWindow 또는 명시적인 창 크롬 구성이 필요합니다.''',
 'TitleBar':'''제목·중앙·우측 슬롯은 공개 Title·Header·CenterContent·TrailingContent를 사용합니다. 시스템 버튼 색은 ButtonsForeground·ButtonsBackground이며 버튼 템플릿에는 고정된 글리프·크기와 닫기 강조색도 있습니다. TitleBar.Resources에 일반 Button 색을 바꾼다고 모든 시스템 버튼 상태가 같은 색으로 변하지 않습니다.''',
 'TitleBarButton':'''ButtonsForeground·MouseOverButtonsForeground와 ButtonType을 우선 사용합니다. RenderButtonsForeground는 실제 표시 계산 결과이고 Canvas의 글리프·크기는 종류별 트리거가 설정합니다. 일반 Button 템플릿으로 교체하면 창 버튼 전용 글리프·상태 연결이 사라질 수 있습니다.''',
 'Flyout':'''PopupCornerRadius는 팝업 Border에 직접 DynamicResource로 연결됩니다. Flyout.Resources에서 재정의할 수 있으며 FlyoutBackground·FlyoutBorderBrush와 구분합니다. 임의 대상에 연결하는 PlacementTarget 공개 속성이나 ShowAt API가 있는 컨트롤은 아닙니다.''',
 'ContextMenu':'''ContextMenuBackground·BorderBrush·Foreground 리소스는 메뉴 팝업에 적용됩니다. 호출 버튼과 별도 팝업이므로 메뉴 자신의 Resources에 두는 방법이 명확합니다. 항목은 MenuItem 스타일·아이콘으로 조정하며 DataContext는 PlacementTarget에서 별도 연결해야 할 수 있습니다.''',
 'ToolTip':'''ToolTipBackground·ToolTipBorderBrush·ToolTipForeground는 팝업 도움말의 색입니다. 버튼 Resources 범위와 팝업 범위에 의존하기보다 ToolTip 객체의 Resources에 조정 키를 두는 방법을 사용합니다. 표시 지연·지속 시간은 ToolTipService의 붙임 속성입니다.''',
 'TextBlock':'''문자 크기·굵기는 FontTypography 또는 FontSize·FontWeight로 설정합니다. FontTypography는 TextBlockMetadata의 크기·굵기 매핑을 사용하므로 `TitleTextBlockStyle`이라는 키를 Resources에서 바꾸는 것과 같은 경로가 아닙니다. Typography.xaml의 keyed Style을 직접 선택하는 방법도 있으며 FontTypography를 함께 설정했을 때 우선순위를 확인합니다.''',
 'FontIcon':'''기본 생성자는 `UiApplication.Current.Resources["DefaultIconFontSize"]`를 읽습니다. FontIcon.Resources만 재정의하는 경로가 아니라 앱 리소스 조회입니다. 개별 아이콘 크기는 공개 FontSize를 직접 설정하는 방법이 확실합니다. 사용자 폰트는 FontFamily·Glyph를 함께 맞춥니다.''',
 'SymbolIcon':'''개별 크기·아이콘·채움 여부는 FontSize·Symbol·Filled를 직접 설정합니다. MenuItem.xaml 내부에 SymbolIcon용 스타일이 있어도 모든 SymbolIcon에 전역 적용되는 공개 스타일 키라고 해석하지 않습니다. 생성자의 DefaultIconFontSize 조회는 FontIcon 문서의 앱 범위 조건을 따릅니다.''',
 'IconSourceElement':'''일반 UI 컨테이너처럼 템플릿을 교체하는 타입이 아닙니다. Button.Icon 등의 Coerce 경로에서 IconSource.CreateIconElement()로 실제 아이콘을 만듭니다. Resources의 Style 키를 선택하는 방식보다 IconSource의 속성과 생성된 아이콘을 조정합니다.''',
 'Image':'''이미지 모서리는 공개 CornerRadius, 자르기·비율은 Stretch·StretchDirection으로 조정합니다. 이 타입의 기본 스타일에는 ControlCornerRadius를 공급하는 연결이 없으므로 같은 키를 Resources에 추가하는 것만으로 모서리가 바뀐다고 가정하지 않습니다.''',
 'TabView':'''4.3.0의 TabView는 TabControl 파생 빈 클래스이며 독립 WPF UI ControlTemplate을 제공하지 않습니다. 기본 WPF 타입용 암시적 Style은 파생 타입과 정확히 일치하지 않을 수 있으므로 테마 TabControl 스타일을 쓰려면 TabView용 Style을 만들고 BasedOn="{StaticResource {x:Type TabControl}}"으로 명시적으로 연결합니다. TabItem·TabViewItem도 별도로 고려합니다.''',
 'TabViewItem':'''TabItem 파생 빈 클래스입니다. WPF TabItem용 테마를 사용하려면 TabViewItem용 Style의 BasedOn으로 기본 TabItem 스타일을 명시적으로 연결할 수 있습니다. Header·Content·IsSelected는 상속 속성이고 탭 닫기·드래그 재정렬은 별도 구현입니다.''',
 'VirtualizingGridView':'''타일 배치는 Orientation·SpacingMode·StretchItems, 데이터 외형은 ItemTemplate·ItemContainerStyle로 바꿉니다. 큰 데이터를 위해 사용하는 컨트롤이므로 템플릿 수정 시 PassiveScrollViewer·ItemsPresenter·VirtualizingWrapPanel과 CanContentScroll 연결을 유지해야 합니다.''',
 'VirtualizingItemsControl':'''아이템 외형은 ItemTemplate, 간격·배치는 ItemsPanel의 VirtualizingWrapPanel로 조정합니다. 외형을 위해 외부 ScrollViewer로 감싸거나 무한 높이를 주면 가상화가 무력화될 수 있습니다. CacheLengthUnit은 렌더링 모양을 정하는 속성이 아닙니다.''',
 'TimePicker':'''색·테두리 리소스를 바꾸더라도 hour·minute·Todo로 남아 있는 시간 선택 기능이 완성되는 것은 아닙니다. 이 문서의 리소스 예제는 외형 조정만 설명하며 실제 시간 선택 기능의 검증 예제로 사용하지 않습니다.''',
 'TreeGrid':'''미완성 타입입니다. Resources·Style을 바꾸어도 Headers.CollectionChanged의 NotImplementedException이 해결되지는 않습니다. 실사용 기능을 제공하는 조정 예제로 권하지 않습니다.''',
}

# 문서에서 그대로 복사해 쓸 수 있는 추가 예제. 기본 첫 예제와 이름 범위를 분리합니다.
EXTRA={
 'ToolBar':[('문자열이 아닌 ToolBar.ButtonStyleKey로 자식 버튼 스타일 지정', '''<ToolBar>
    <ToolBar.Resources>
        <Style x:Key="{x:Static ToolBar.ButtonStyleKey}"
               TargetType="{x:Type Button}"
               BasedOn="{StaticResource {x:Type Button}}">
            <Setter Property="MinWidth" Value="100" />
        </Style>
    </ToolBar.Resources>
    <Button Content="저장" />
</ToolBar>''')],
 'Button': [('상태별 강조색을 한 버튼에 적용', '''<ui:Button Content="저장" Appearance="Primary">
    <ui:Button.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
        <SolidColorBrush x:Key="AccentButtonBackground" Color="#2563EB" />
        <SolidColorBrush x:Key="AccentButtonBackgroundPointerOver" Color="#1D4ED8" />
        <SolidColorBrush x:Key="AccentButtonBackgroundPressed" Color="#1E40AF" />
    </ui:Button.Resources>
</ui:Button>''')],
 'TextBox':[('여백·모서리·포커스 배경을 함께 조정', '''<ui:TextBox Width="280" PlaceholderText="이름 입력">
    <ui:TextBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">10</CornerRadius>
        <Thickness x:Key="TextControlThemePadding">16,10</Thickness>
        <SolidColorBrush x:Key="TextControlBackgroundFocused" Color="#EFF6FF" />
    </ui:TextBox.Resources>
</ui:TextBox>''')],
 'InfoBadge':[('숫자·점·아이콘 스타일을 선택', '''<StackPanel Orientation="Horizontal">
    <ui:InfoBadge Value="3" Style="{StaticResource ValueInfoBadgeStyle}" />
    <ui:InfoBadge Margin="8,0" Style="{StaticResource DotInfoBadgeStyle}" Severity="Success" />
    <ui:InfoBadge Style="{StaticResource IconInfoBadgeStyle}" CornerRadius="12"
                  Icon="{ui:SymbolIcon Checkmark24}" />
</StackPanel>''')],
 'ListView':[('항목 컨테이너의 모서리와 간격 조정', '''<ui:ListView Height="160">
    <ui:ListView.ItemContainerStyle>
        <Style TargetType="{x:Type ui:ListViewItem}"
               BasedOn="{StaticResource {x:Type ui:ListViewItem}}">
            <Setter Property="Margin" Value="0,4" />
            <Setter Property="Border.CornerRadius" Value="10" />
        </Style>
    </ui:ListView.ItemContainerStyle>
    <ui:ListViewItem Content="문서 A" />
    <ui:ListViewItem Content="문서 B" />
</ui:ListView>''')],
 'ProgressRing':[('진행 호와 뒤쪽 링을 따로 조정', '''<ui:ProgressRing Progress="65" Width="48" Height="48">
    <ui:ProgressRing.Resources>
        <SolidColorBrush x:Key="ProgressRingForegroundThemeBrush" Color="#2563EB" />
        <SolidColorBrush x:Key="ProgressRingBackgroundThemeBrush" Color="#DBEAFE" />
    </ui:ProgressRing.Resources>
</ui:ProgressRing>''')],
 'ToggleSwitch':[('켜짐·꺼짐 트랙 색 조정', '''<ui:ToggleSwitch IsChecked="True" OnContent="켜짐" OffContent="꺼짐">
    <ui:ToggleSwitch.Resources>
        <SolidColorBrush x:Key="ToggleSwitchFillOn" Color="#2563EB" />
        <SolidColorBrush x:Key="ToggleSwitchFillOff" Color="#CBD5E1" />
    </ui:ToggleSwitch.Resources>
</ui:ToggleSwitch>''')],
 'TabView':[('기본 TabControl 테마 스타일을 명시적으로 연결', '''<ui:TabView>
    <ui:TabView.Style>
        <Style TargetType="{x:Type ui:TabView}" BasedOn="{StaticResource {x:Type TabControl}}" />
    </ui:TabView.Style>
    <TabItem Header="일반"><TextBlock Text="일반 설정" /></TabItem>
    <TabItem Header="고급"><TextBlock Text="고급 설정" /></TabItem>
</ui:TabView>''')],
 'TabViewItem':[('TabItem 스타일을 기반으로 사용', '''<ui:TabViewItem Header="문서">
    <ui:TabViewItem.Style>
        <Style TargetType="{x:Type ui:TabViewItem}" BasedOn="{StaticResource {x:Type TabItem}}" />
    </ui:TabViewItem.Style>
    <TextBlock Text="문서 본문" />
</ui:TabViewItem>''')],
}
