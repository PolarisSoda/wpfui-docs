# DataGrid

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

기본 WPF 표에 자동·추가 열의 표시·편집 스타일 연결을 더한 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.DataGrid` · **기반:** `System.Windows.Controls.DataGrid`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:DataGrid x:Name="Demo" AutoGenerateColumns="False" IsReadOnly="True">
    <DataGrid.Columns><DataGridTextColumn Header="이름" Binding="{Binding Name}" /></DataGrid.Columns>
</ui:DataGrid>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ItemsSource = new[] { new { Name = "문서 A" }, new { Name = "문서 B" } };
Demo.IsReadOnly = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `CheckBoxColumnElementStyle` | `Style?` | 읽기·쓰기 | `null` | 자동 생성하거나 컬렉션에 추가하는 CheckBox 형식 열의 표시 상태 요소 스타일입니다. 편집 상태 스타일과 구분하며 열별 사용자 스타일이 있으면 그 설정을 우선합니다. |
| `CheckBoxColumnEditingElementStyle` | `Style?` | 읽기·쓰기 | `null` | CheckBox 형식 열을 편집할 때 생성되는 요소의 스타일입니다. 화면 표시용 스타일과 별도로 지정합니다. |
| `ComboBoxColumnElementStyle` | `Style?` | 읽기·쓰기 | `null` | 자동 생성하거나 컬렉션에 추가하는 ComboBox 형식 열의 표시 상태 요소 스타일입니다. 편집 상태 스타일과 구분하며 열별 사용자 스타일이 있으면 그 설정을 우선합니다. |
| `ComboBoxColumnEditingElementStyle` | `Style?` | 읽기·쓰기 | `null` | ComboBox 형식 열을 편집할 때 생성되는 요소의 스타일입니다. 화면 표시용 스타일과 별도로 지정합니다. |
| `TextColumnElementStyle` | `Style?` | 읽기·쓰기 | `null` | 자동 생성하거나 컬렉션에 추가하는 Text 형식 열의 표시 상태 요소 스타일입니다. 편집 상태 스타일과 구분하며 열별 사용자 스타일이 있으면 그 설정을 우선합니다. |
| `TextColumnEditingElementStyle` | `Style?` | 읽기·쓰기 | `null` | Text 형식 열을 편집할 때 생성되는 요소의 스타일입니다. 화면 표시용 스타일과 별도로 지정합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |
| `AutoGenerateColumns` | `bool` | 데이터 멤버로 열을 자동 생성할지 정합니다. |
| `Columns` | `ObservableCollection<DataGridColumn>` | 명시적으로 정의한 열입니다. |
| `IsReadOnly` | `bool` | 표 편집을 막습니다. 개별 열도 읽기 전용 설정이 가능합니다. |
| `SelectedItem` | `object` | 현재 선택한 행 데이터입니다. |
| `SelectionUnit` | `DataGridSelectionUnit` | 행·셀 단위 선택 정책입니다. |
| `CanUserAddRows` | `bool` | 새 행 입력 UI를 허용할지 정합니다. 데이터 원본의 추가 지원도 필요합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `CellStyle` | `{StaticResource DefaultUiDataGridCellStyle}` | DefaultUiDataGridStyle |
| `ColumnHeaderStyle` | `{StaticResource DefaultUiDataGridColumnHeaderStyle}` | DefaultUiDataGridStyle |
| `CheckBoxColumnEditingElementStyle` | `{StaticResource DefaultDataGridCheckBoxEditingElementStyle}` | DefaultUiDataGridStyle |
| `CheckBoxColumnElementStyle` | `{StaticResource DefaultDataGridCheckBoxElementStyle}` | DefaultUiDataGridStyle |
| `ComboBoxColumnEditingElementStyle` | `{StaticResource DefaultDataGridComboBoxEditingElementStyle}` | DefaultUiDataGridStyle |
| `ComboBoxColumnElementStyle` | `{StaticResource DefaultDataGridComboBoxElementStyle}` | DefaultUiDataGridStyle |
| `TextColumnEditingElementStyle` | `{StaticResource DefaultDataGridTextEditingElementStyle}` | DefaultUiDataGridStyle |
| `TextColumnElementStyle` | `{StaticResource DefaultDataGridTextElementStyle}` | DefaultUiDataGridStyle |

## 동작과 주의 사항

열 타입은 기본 WPF의 DataGridTextColumn·DataGridCheckBoxColumn·DataGridComboBoxColumn입니다. `ui:DataGrid.Columns`도 가능하지만 기본 소유자 표기와 혼동하지 않습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [DataGrid.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.cs)
- [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml)
- [Gallery: DataGridPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Collections/DataGridPage.xaml)
