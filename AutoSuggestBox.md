# AutoSuggestBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

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

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

바깥 입력 영역은 ControlCornerRadius·TextControlThemePadding 등에 연결되고 후보 팝업은 FlyoutBackground·FlyoutBorderBrush 등 별도 키를 사용합니다. 입력란과 후보 목록을 한 종류의 Background로 조정한다고 가정하지 않습니다. ItemTemplate·DisplayMemberPath로 후보 표시를 바꾸고 팝업 높이는 MaxSuggestionListHeight를 사용합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example AutoSuggestBox_Resources -->
```xml
<ui:AutoSuggestBox Width="280" PlaceholderText="도시 검색" MaxSuggestionListHeight="240" ClearButtonEnabled="True"  x:Name="ResourceDemo">
    <ui:AutoSuggestBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:AutoSuggestBox.Resources>
</ui:AutoSuggestBox>
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
| `TextControlThemePadding` | Thickness | 컨트롤.Padding |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `FlyoutBackground` | SolidColorBrush | Border Background |
| `FlyoutBorderBrush` | SolidColorBrush | Border BorderBrush |
| `ListViewItemBackgroundPointerOver` | SolidColorBrush | ContentBorder.Background〔IsSelected=True〕 / ContentBorder.Background〔IsSelected=False; IsMouseOver=True〕 |
| `ListViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ListViewItemPillFillBrush` | SolidColorBrush | Rectangle#ActiveRectangle Fill |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `AutoSuggestBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `DefaultAutoSuggestBoxItemContainerStyle` | Style | 컨트롤.ItemContainerStyle |
| `DefaultUiAutoSuggestBoxStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiAutoSuggestBoxStyle` | `controls:AutoSuggestBox` | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

C# 구현이 이름으로 찾는 부분: `PART_SuggestionsList`, `PART_SuggestionsPopup`, `PART_TextBox`. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.

원본 템플릿에 정의된 PART: `PART_SuggestionsList` (ListView), `PART_SuggestionsPopup` (Popup), `PART_TextBox` (TextBox). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `ClearButtonEnabled` | `TextBox#PART_TextBox.ClearButtonEnabled` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Icon` | `TextBox#PART_TextBox.Icon` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `IsTabStop` | `TextBox#PART_TextBox.IsTabStop` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `PlaceholderText` | `TextBox#PART_TextBox.PlaceholderText` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `TabIndex` | `TextBox#PART_TextBox.TabIndex` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Text` | `TextBox#PART_TextBox.Text` | Binding to TemplatedParent | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ActualWidth` | `Popup#PART_SuggestionsPopup.MinWidth` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `IsSuggestionListOpen` | `Popup#PART_SuggestionsPopup.IsOpen` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `MaxSuggestionListHeight` | `ListView#PART_SuggestionsList.MaxHeight` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `DisplayMemberPath` | `ListView#PART_SuggestionsList.DisplayMemberPath` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ItemContainerStyle` | `ListView#PART_SuggestionsList.ItemContainerStyle` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ItemTemplate` | `ListView#PART_SuggestionsList.ItemTemplate` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ItemTemplateSelector` | `ListView#PART_SuggestionsList.ItemTemplateSelector` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ItemsSource` | `ListView#PART_SuggestionsList.ItemsSource` | TemplateBinding | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Popup#PART_SuggestionsPopup.Margin` | `0` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Border.Margin` | `0` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Border.Padding` | `0,6,0,6` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Border.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Border.CornerRadius` | `8` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

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
