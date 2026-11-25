# BreadcrumbBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

현재 위치를 상위 경로부터 순서대로 보여 주는 경로 표시줄입니다.

**타입:** `Wpf.Ui.Controls.BreadcrumbBar` · **기반:** `System.Windows.Controls.ItemsControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:BreadcrumbBar x:Name="Demo" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = new[] { "홈", "문서", "보고서" };
Demo.ItemClicked += (_, e) =>
{
    var clicked = e.Item;
};
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |
| `Command` | `ICommand?` | 읽기·쓰기 | `null` | 경로 항목을 눌렀을 때 실행할 명령입니다. 클릭된 항목을 처리해 실제 폴더·페이지 이동을 직접 수행합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `ItemClicked` | 경로 항목 클릭입니다. `e.Item`·`e.Index`로 클릭 위치를 확인합니다. |

## 동작과 주의 사항

클릭만으로 파일 시스템이나 페이지가 자동 이동하지는 않습니다. `ItemClicked` 또는 `Command`에서 앱 이동을 구현합니다. NavigationView의 `BreadcrumbBar` 속성에 넣으면 계층 탐색용으로 연동할 수 있습니다. 4.3.0의 OnItemClicked는 Command에 항목을 전달하는 경로와 null을 전달하는 경로를 모두 검사합니다. 두 CanExecute가 모두 true이면 두 번 실행될 수 있으므로 명령 구현에서 인자를 구별하거나 ItemClicked 한 경로를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [BreadcrumbBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/BreadcrumbBar/BreadcrumbBar.cs)
- [Gallery: BreadcrumbBarPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Navigation/BreadcrumbBarPage.xaml)
