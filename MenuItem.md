# MenuItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

기본 메뉴 항목에 IconElement 타입 아이콘 슬롯을 적용한 파생형입니다.

**타입:** `Wpf.Ui.Controls.MenuItem` · **기반:** `System.Windows.Controls.MenuItem`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:MenuItem x:Name="Demo" Header="저장" InputGestureText="Ctrl+S" Icon="{ui:SymbolIcon Save24}" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Header = "다른 이름으로 저장";
Demo.IsEnabled = true;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Icon` | `IconElement` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Header` | `object` | 메뉴 표시 글자·요소입니다. 밑줄은 액세스 키로 사용할 수 있습니다. |
| `Items / ItemsSource` | `ItemCollection / IEnumerable` | 하위 메뉴 항목입니다. |
| `Command / CommandParameter` | `ICommand / object` | 실행할 명령과 인자입니다. |
| `InputGestureText` | `string` | 단축키 안내 문자열입니다. 이 값만으로 키 바인딩을 등록하지 않습니다. |
| `IsCheckable / IsChecked` | `bool` | 체크 가능한 메뉴와 체크 상태입니다. |
| `IsSubmenuOpen` | `bool` | 하위 메뉴 열림 상태입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `OverridesDefaultStyle` | `True` | WpfUiMenuItem |
| `KeyboardNavigation.IsTabStop` | `True` | WpfUiMenuItem |
| `Focusable` | `True` | WpfUiMenuItem |

## 동작과 주의 사항

Menu 또는 ContextMenu의 자식으로 배치합니다. InputGestureText는 표시 문자열이므로 실제 단축키는 InputBindings·Command로 별도 연결합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [MenuItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Menu/MenuItem.cs)
- [MenuItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Menu/MenuItem.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
