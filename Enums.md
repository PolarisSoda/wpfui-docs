# 열거형 값과 의미

[전체 목차](README.md)

아래 목록은 4.3.0 소스에서 읽은 값입니다. 값이 비슷해 보여도 서로 다른 타입을 대입할 수는 없습니다. 특히 Button.Appearance는 ControlAppearance, TextBlock.Appearance는 TextColor입니다.

## AutoSuggestionBoxTextChangeReason

`UserInput`, `ProgrammaticChange`, `SuggestionChosen`.

UserInput=실제 타이핑, ProgrammaticChange=코드 변경, SuggestionChosen=후보 복사입니다. 필터 처리 시 구별합니다.

## ContentDialogButton

`Primary`, `Secondary`, `Close`.

버튼 종류입니다. None 값은 없고 닫기 버튼은 Close입니다.

## ContentDialogResult

`None`, `Primary`, `Secondary`.

대화상자 결과입니다. 취소·닫기는 None입니다. Close라는 결과 값은 없습니다.

## ControlAppearance

`Primary`, `Secondary`, `Info`, `Dark`, `Light`, `Danger`, `Success`, `Caution`, `Transparent`.

Primary=강조, Secondary=보조, Info=정보, Danger=위험, Success=성공, Caution=주의, Dark·Light=색상 계열, Transparent=투명 계열입니다. 컨트롤별 템플릿이 실제 소비하는 값을 확인합니다.

## ElementPlacement

`Left`, `Right`.

아이콘·라벨의 좌우 배치입니다. Top·Bottom 값은 없습니다.

## FontTypography

`Caption`, `Body`, `BodyStrong`, `Subtitle`, `Title`, `TitleLarge`, `Display`.

Caption=작은 보조 글자, Body=본문, BodyStrong=강조 본문, Subtitle=소제목, Title·TitleLarge=제목, Display=큰 표시입니다. 구체 크기는 타이포그래피 메타데이터를 따릅니다.

## InfoBadgeSeverity

`Attention`, `Informational`, `Success`, `Caution`, `Critical`.

Attention=주의를 끄는 표시, Informational=정보, Success=성공, Caution=경계, Critical=중요·오류 계열입니다. InfoBar의 Severity와 타입·이름이 다릅니다.

## InfoBarSeverity

`Informational`, `Success`, `Warning`, `Error`.

정보·성공·경고·오류의 페이지 알림 색상과 아이콘을 고릅니다.

## ListViewViewState

`Default`, `GridView`.

Default=일반 목록 상태, GridView=열 보기용 상태입니다. 실제 Columns는 View에 따로 구성합니다.

## MessageBoxButton

`Primary`, `Secondary`, `Close`.

메시지 창의 버튼 식별자입니다. 버튼 텍스트와 표시 여부는 별도 속성입니다.

## MessageBoxResult

`None`, `Primary`, `Secondary`.

메시지 창 결과입니다. 닫기는 None입니다.

## NavigationCacheMode

`Disabled`, `Enabled`, `Required`.

Disabled=생성 함수 재호출, Enabled·Required=Type 키 캐시 재사용입니다. 4.3.0 구현은 두 캐시 모드를 같은 경로로 처리합니다.

## NavigationViewBackButtonVisible

`Collapsed`, `Visible`, `Auto`.

Collapsed=공간까지 숨김, Visible=표시입니다. 4.3.0 기본 변환기는 Auto도 Visible로 처리하며 활성 여부는 IsBackEnabled로 따로 제어합니다.

## NavigationViewPaneDisplayMode

`Left`, `LeftMinimal`, `LeftFluent`, `Top`, `Bottom`.

Left=왼쪽 일반, LeftMinimal=아이콘 중심, LeftFluent=큰 아이콘과 아래 라벨, Top·Bottom=상단·하단입니다. Auto는 없습니다. LeftFluent는 하위 메뉴를 지원하지 않습니다.

## NumberBoxSpinButtonPlacementMode

`Hidden`, `Compact`, `Inline`.

Hidden=증감 버튼 숨김, Compact=포커스 시 압축 팝업, Inline=인라인 증감 버튼입니다.

## NumberBoxValidationMode

`InvalidInputOverwritten`, `Disabled`.

InvalidInputOverwritten=입력 정규화·범위 적용, Disabled=기본 검사 끔입니다.

## ScrollDirection

`Vertical`, `Horizontal`.

가상화·스크롤 내부의 세로·가로 방향입니다. WrapPanel 방향 이름과 배치 해석을 구별합니다.

## SpacingMode

`None`, `Uniform`, `BetweenItemsOnly`, `StartAndEndOnly`.

None=남는 공간 분배 없음, Uniform=항목 사이와 양끝에 균등 분배, BetweenItemsOnly=항목 사이만, StartAndEndOnly=양끝만 분배합니다.

## TextColor

`Primary`, `Secondary`, `Tertiary`, `Disabled`.

Primary=주요 글자, Secondary=보조, Tertiary=더 약한 보조, Disabled=비활성 글자입니다. ui:TextBlock.Appearance의 타입입니다.

## ThumbRateState

`None`, `Liked`, `Disliked`.

None=미선택, Liked=좋아요, Disliked=싫어요입니다.

## ClockIdentifier

`Clock12Hour`, `Clock24Hour`.

12·24시간제입니다. TimePicker는 4.3.0에서 미완성이라 실제 시각 선택 동작까지 제공하지 않습니다.

## TitleBarButtonType

`Unknown`, `Minimize`, `Close`, `Maximize`, `Restore`, `Help`.

창 버튼 종류를 고릅니다. Unknown은 미지정, Restore는 최대화 복원입니다.

## WindowBackdropType

`None`, `Auto`, `Mica`, `Acrylic`, `Tabbed`.

None=배경 효과 없음, Auto=시스템 요청, Mica·Acrylic·Tabbed=재질 요청입니다. OS 지원과 ExtendsContentIntoTitleBar 조건을 확인합니다.

## WindowCornerPreference

`Default`, `DoNotRound`, `Round`, `RoundSmall`.

Default=시스템 기본, DoNotRound=각진 모서리 요청, Round=둥글게, RoundSmall=작게 둥글게 요청입니다. 지원 OS·창 상태에 따라 달라집니다.

WPF 기본 열거형(Visibility·Orientation·Stretch·Dock 등)은 해당 기본 타입을 사용합니다. 전환 애니메이션은 `Wpf.Ui.Animations.Transition` 네임스페이스에 있습니다.

기준: [4.3.0 컨트롤 소스](https://github.com/lepoco/wpfui/tree/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls).
