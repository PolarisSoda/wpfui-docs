# TreeViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

기본 TreeViewItem에 아이콘 슬롯을 더한 트리 항목입니다.

**타입:** `Wpf.Ui.Controls.TreeViewItem` · **기반:** `System.Windows.Controls.TreeViewItem`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TreeViewItem x:Name="Demo" Header="문서" IsExpanded="True" Icon="{ui:SymbolIcon Folder24}">
    <ui:TreeViewItem Header="보고서" />
</ui:TreeViewItem>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Header = "내 문서";
Demo.IsExpanded = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Header` | `object` | 트리 노드에 표시할 헤더입니다. |
| `Items / ItemsSource` | `ItemCollection / IEnumerable` | 하위 노드 목록입니다. |
| `IsExpanded` | `bool` | 하위 노드를 펼칠지 정합니다. |
| `IsSelected` | `bool` | 현재 노드 선택 여부입니다. |
| `ItemTemplate` | `DataTemplate` | 하위 데이터의 표시 템플릿입니다. 계층 데이터에는 HierarchicalDataTemplate을 사용합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource TreeViewItemForeground}` | DefaultUiTreeViewItemStyle |
| `Background` | `{DynamicResource TreeViewItemBackground}` | DefaultUiTreeViewItemStyle |
| `Padding` | `4` | DefaultUiTreeViewItemStyle |
| `FocusVisualStyle` | `{StaticResource TreeViewItemFocusVisual}` | DefaultUiTreeViewItemStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiTreeViewItemStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiTreeViewItemStyle |

## 동작과 주의 사항

이 항목은 기본 `<TreeView>` 안에 배치합니다. 데이터 바인딩 트리에는 HierarchicalDataTemplate와 ItemContainerStyle을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TreeViewItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.cs)
- [TreeViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TreeView/TreeViewItem.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
