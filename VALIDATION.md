# 검증 범위와 재검사

[전체 목차](README.md)

기준: WPF-UI **4.3.0**, 원본 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`, 확인일 **2026-11-25**.

## 수행한 검사

| 검사 | 결과 | 검증하는 내용 |
| --- | --- | --- |
| 개별 컨트롤·뷰 페이지 | 105개 | 요청한 `타입이름.md` 형식과 README 연결 |
| WPF-UI 클래스 | 75개 | 공개 시각 타입·아이콘 데이터·추상 기반 타입의 문서 포함 |
| 고유 공개 속성 | 312개 | 인스턴스 311개·정적 1개, 실제 NuGet 어셈블리 리플렉션과 선언·setter 접근·정적 여부 대조 |
| 대표 XAML + C# 조각 | 105쌍 빌드 통과 | 문서 첫 XAML과 첫 C# 조각을 창·뷰로 감싼 컴파일 검사 |
| XAML 생성 | 105개 통과 | 테마·ControlsDictionary를 로드하고 XAML 인스턴스 생성, 리소스·생성 오류 검사 |
| QuickStart | 빌드 통과 | 실제 WPF 프로젝트의 XAML·코드비하인드·NuGet 연결 |
| 문서 구조 | 검사 스크립트 통과 | 상대 링크·코드 펜스·XML 문법·속성 표의 누락 여부 |
| 조정 방법 재조사 | 105개 문서 | 동적·정적 리소스, Style 키, 템플릿 연결, 고정값·트리거 조건 |
| 리소스 정의 | 881개 (문자열 862·복합 키 19) | Wpf.Ui XAML의 정의 타입·값·범위와 컨트롤별 문자열 참조 위치 |
| 추가 조정 예제 | 70개 빌드·XAML 생성 통과 | Resources 재정의·상태별 색·별도 스타일·파생 타입 BasedOn·ToolBar 객체 키 |
| 조정 동작 | 22개 단언 통과 | 실제 템플릿 요소의 값, 런타임 리소스 교체·우선순위·범위·Footer 제약 |
| CustomizationLab | 빌드 통과 | 기본 카드·Footer 수정 템플릿·입력·배지·진행률의 독립 실행 프로젝트 |

검사 환경은 Windows x64, .NET SDK 10.0.404, `net10.0-windows`, NuGet `WPF-UI=4.3.0`입니다. 조각 검사용 프로젝트는 학습용 `ui` 소문자 별칭 경고와 `async` 조각 래퍼의 무해한 경고를 제외하도록 구성했습니다.

## 검사 범위의 한계

컴파일·XAML 생성은 모든 마우스·키보드 상호작용, 접근성, DPI, 테마 조합, Windows 배경 재질의 시각 결과를 보장하지 않습니다. 검사 과정에서 별도 창을 사용자 화면에 띄우거나 예제의 저장·탐색·팝업 메서드를 자동 실행하지 않았습니다. `TimePicker`·`TreeGrid`의 미완성 기능도 완성 기능으로 간주하지 않습니다.

추가한 조정 동작 검사는 컨트롤을 초기화·측정하고 템플릿 내부 Border의 실제 값을 읽습니다. Card.Resources의 반지름 반영과 동적 교체, 로컬 DP 우선순위와 ClearValue, 원본 Footer의 4 고정, 수정한 Footer 템플릿의 12 반영, CardAction, CardExpander의 위·아래 반지름 분할, 부모·개별 Resources 범위, TextBox 여백·반지름, InfoBadge 숫자형의 정적 반지름과 아이콘형의 속성 연결, ProgressRing의 두 브러시, FontIcon의 앱 범위 조회를 확인했습니다. 모든 리소스 키·색상 상태의 시각 결과를 자동 검증한 것은 아닙니다.

소스 고정 링크는 로컬 4.3.0 체크아웃에 해당 경로가 존재하는지 확인했습니다. 웹 주소 전체의 실시간 HTTP 상태를 모두 요청한 검사는 아닙니다. WPF 기본 API의 전체 멤버를 복제하지 않으며 고유 속성은 모두 포함하고 상속 속성은 실사용 핵심 목록으로 설명합니다.

## 재검사

Python 3와 Windows용 .NET 10 SDK에서 저장소 루트 기준으로 실행합니다.

```powershell
python scripts/validate_docs.py
python scripts/prepare_snippet_checks.py
dotnet build .checks/SnippetChecks.csproj
dotnet .checks/bin/Debug/net10.0-windows/SnippetChecks.dll source-manifest.json
dotnet build examples/QuickStart/QuickStart.csproj
python scripts/prepare_customization_checks.py
dotnet build .customization-checks/CustomizationChecks.csproj
dotnet .customization-checks/bin/Debug/net10.0-windows/CustomizationChecks.dll
dotnet build examples/CustomizationLab/CustomizationLab.csproj
```

소스 경로도 대조하려면 다음처럼 원본 체크아웃을 지정합니다.

```powershell
python scripts/validate_docs.py --source C:\path\to\wpfui
```

원본 소스는 `git checkout 4.3.0` 상태여야 합니다. 검사 스크립트는 문서를 자동으로 최신 버전으로 바꾸지 않습니다. `.checks`는 생성되는 임시 검사 프로젝트이며 Git에 포함하지 않습니다. 이미지 예제용 PNG는 검사기가 생성하는 1픽셀 테스트 리소스입니다. 실제 앱에는 문서에서 안내한 이미지 자산을 준비해야 합니다.

`.customization-checks`도 생성물이며 Git에서 제외합니다. 추가 예제는 customization-examples.json에 기록된 주석 구간으로 찾아 원문 XAML·C#을 컴파일합니다. 코드 조각의 Show·저장 동작은 자동 실행하지 않습니다.

## 리소스 조사 재생성

고정 버전의 체크아웃을 준비한 뒤 다음 순서로 실행합니다. 소스 커밋이 4.3.0 기준과 다르면 조사기가 중단됩니다.

```powershell
python scripts/audit_customization.py --source C:\path\to\wpfui
python scripts/update_customization_sections.py
python scripts/validate_docs.py --source C:\path\to\wpfui
```

audit_customization.py는 XAML 키 정의·문자열 키의 정적/동적 참조·Style·ControlTemplate·부모 속성 바인딩·고정 레이아웃·색 값과 C#의 일부 직접 리소스 조회를 추출합니다. 복합 키는 정의 목록에 포함하지만 자동 참조 추적 범위는 아닙니다. 라이브러리 외부 리소스나 모든 변환기의 임의 코드를 해석하는 정적 분석기는 아닙니다. 고정값 표의 조건은 소스 선언이며 모든 Style·상태를 계산한 최종 값 표가 아닙니다.

update_customization_sections.py는 `<!-- customization:start -->` 구간과 리소스 사전을 갱신합니다. 수작업으로 확인한 예제·제약은 scripts/customization_recipes.py에 있으며, 원본 본문·고유 속성 설명은 유지합니다. 이후 위 컴파일·동작 검사까지 실행합니다.

## 구현과 대조하며 반영한 주요 차이

- DropDownButton·SplitButton의 Flyout은 실제로 ContextMenu를 연결합니다. IsDropDownOpen만 대입해 여는 구현은 없습니다.
- NavigationView의 Auto 뒤로가기 표시는 기본 변환기에서 Visible입니다. IsPaneVisible·AlwaysShowHeader는 제공 템플릿에서 소비하지 않습니다.
- IconSourceElement는 독립 시각 자식으로 렌더링하지 않고 Button.Icon의 강제 변환 또는 CreateIconElement를 통해 사용합니다.
- InfoBadge 기본 Value 스타일은 정적 반지름을 사용하지만 Icon·Dot 스타일은 CornerRadius를 TemplateBinding합니다. 숫자형과 아이콘형을 동일하게 설명했던 내용을 바로잡았습니다.
- TextBox·RichTextBox의 IsTextSelectionEnabled는 읽기 전용 표시 스타일로 전환합니다.
- TimePicker의 실제 시간 선택 UI는 미완성이고 TreeGrid.Headers 변경 처리기는 예외를 던집니다.
- ContentDialog에는 새 ContentDialogHost 경로와 오래된 ContentPresenter 경로가 함께 있으며 오래된 ContentPresenter 자동 속성만으로 실제 호스트가 연결되지는 않습니다.

세부 사항과 커밋 고정 근거는 해당 컨트롤 페이지에 연결했습니다.
