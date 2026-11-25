# AutoSuggestBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

입력 문자열을 기준으로 후보를 필터링하고 선택하거나 검색을 제출하는 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.AutoSuggestBox` · **기반:** `ItemsControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:AutoSuggestBox x:Name="Demo" Width="280" PlaceholderText="도시 검색" MaxSuggestionListHeight="240" ClearButtonEnabled="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.OriginalItemsSource = new[] { "서울", "부산", "대전" };
Demo.QuerySubmitted += (_, e) =>
{
    string query = e.QueryText;
};
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `OriginalItemsSource` | `IList` | 읽기·쓰기 | `Array.Empty<object>()` | 필터링 전의 전체 후보 목록입니다. 기본 필터를 사용하려면 이 속성에 원본 목록을 넣습니다. `ItemsSource`는 필터 결과가 들어가는 표시 목록입니다. |
| `IsSuggestionListOpen` | `bool` | 읽기·쓰기 | `false` | 후보 팝업의 열림 상태입니다. 사용자 입력 시 열리고 Enter·Escape·포커스 이동 시 닫힙니다. |
| `Text` | `string` | 읽기·쓰기 | `string.Empty` | 현재 검색 입력 문자열입니다. 코드에서 변경한 경우 `TextChanged`의 이유는 `ProgrammaticChange`가 됩니다. |
| `PlaceholderText` | `string` | 읽기·쓰기 | `string.Empty` | 입력이 비었을 때 표시할 안내 문구입니다. 실제 `Text` 값으로 저장되지 않습니다. |
| `MaxSuggestionListHeight` | `double` | 읽기·쓰기 | `0d` | 후보 목록의 최대 높이(DIP)입니다. 너무 긴 목록은 내부에서 스크롤합니다. 등록값 0과 스타일의 실제 설정을 구분합니다. |
| `UpdateTextOnSelect` | `bool` | 읽기·쓰기 | `true` | `true`이면 선택한 후보의 표시 문자열을 입력란에 복사합니다. 후보 선택을 별도 작업에 쓰려면 `false` 또는 이벤트의 `Handled`를 사용합니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `ClearButtonEnabled` | `bool` | 읽기·쓰기 | `false` | 내부 입력란의 지우기 버튼 사용 여부입니다. |
| `FocusCommand` | `ICommand` | 외부 읽기 전용 | `null` | 내부 텍스트 입력란으로 포커스를 옮기는 명령입니다. 템플릿 연결용 읽기 전용 속성이며 일반 코드에서는 `Focus()`를 사용합니다. |

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

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Focusable` | `False` | DefaultUiAutoSuggestBoxStyle |
| `MaxSuggestionListHeight` | `240` | DefaultUiAutoSuggestBoxStyle |
| `HorizontalAlignment` | `Stretch` | DefaultUiAutoSuggestBoxStyle |
| `VerticalAlignment` | `Center` | DefaultUiAutoSuggestBoxStyle |
| `HorizontalContentAlignment` | `Stretch` | DefaultUiAutoSuggestBoxStyle |
| `VerticalContentAlignment` | `Top` | DefaultUiAutoSuggestBoxStyle |
| `Padding` | `{DynamicResource TextControlThemePadding}` | DefaultUiAutoSuggestBoxStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultUiAutoSuggestBoxStyle |
| `BorderThickness` | `{StaticResource AutoSuggestBoxBorderThemeThickness}` | DefaultUiAutoSuggestBoxStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiAutoSuggestBoxStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiAutoSuggestBoxStyle |
| `ItemContainerStyle` | `{StaticResource DefaultAutoSuggestBoxItemContainerStyle}` | DefaultUiAutoSuggestBoxStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiAutoSuggestBoxStyle |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `QuerySubmitted` | Enter 등 검색 제출 시 발생합니다. `e.QueryText`가 제출 문자열입니다. |
| `SuggestionChosen` | 후보 선택 시 발생합니다. `e.SelectedItem`을 확인하고 `e.Handled=true`로 기본 텍스트 복사를 막을 수 있습니다. |
| `TextChanged` | 입력·프로그램 변경·후보 선택에 따른 문자열 변경입니다. AutoSuggestBox에서는 `e.Reason`을 구분합니다. |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `bool Focus()` | 내부 입력 요소로 키보드 포커스를 옮깁니다. |

## 동작과 주의 사항

기본 필터는 `OriginalItemsSource`를 공백으로 나눈 검색어로 대소문자 구분 없이 포함 검색합니다. 결과는 `ItemsSource`에 넣습니다. 사용자 필터를 구현하려면 `TextChanged`에서 `Reason == UserInput`을 확인하고 `e.Handled=true`로 기본 필터를 막습니다. 후보 선택은 `SuggestionChosen`, Enter 검색은 `QuerySubmitted`로 구별합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [AutoSuggestBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.cs)
- [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml)
- [Gallery: AutoSuggestBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/AutoSuggestBoxPage.xaml)
