# 공통 속성 읽기

[전체 목차](README.md) · [시작하기](GettingStarted.md)

여기서는 컨트롤별 문서에서 반복하지 않는 기본 WPF 규칙을 설명합니다. 모든 타입이 아래 속성을 전부 갖는 것은 아닙니다. 예를 들어 GridViewColumn·IconSource는 FrameworkElement가 아니므로 Margin·Width·DataContext가 같은 방식으로 제공되지 않습니다.

## 크기와 배치

WPF 크기의 기본 단위는 DIP입니다. 96 DPI에서 1 DIP가 1 물리 픽셀에 대응하며, 화면 배율에 따라 실제 픽셀 수가 달라집니다.

| 속성 | 타입 | 변경 효과 |
| --- | --- | --- |
| Width / Height | double | 명시 크기입니다. 기본 NaN은 부모와 콘텐츠에 따른 자동 크기입니다. |
| MinWidth / MinHeight | double | 너무 작아지지 않게 하한을 정합니다. |
| MaxWidth / MaxHeight | double | 커질 수 있는 상한입니다. |
| ActualWidth / ActualHeight | double, 읽기 | 레이아웃 계산 결과입니다. 초기화 직후에는 0일 수 있습니다. |
| Margin | Thickness | 컨트롤 바깥의 여백입니다. |
| Padding | Thickness | 템플릿이 사용하는 안쪽 여백입니다. Control 파생형이어도 템플릿이 소비해야 반영됩니다. |
| HorizontalAlignment | HorizontalAlignment | 부모 안에서 Left·Center·Right·Stretch로 배치합니다. |
| VerticalAlignment | VerticalAlignment | 부모 안에서 Top·Center·Bottom·Stretch로 배치합니다. |
| HorizontalContentAlignment / VerticalContentAlignment | 정렬 열거형 | 컨트롤 내부 콘텐츠의 정렬입니다. 템플릿이 연결해야 합니다. |
| Grid.Row / Grid.Column | int, 붙임 | 부모 Grid의 행·열 인덱스입니다. |
| Grid.RowSpan / Grid.ColumnSpan | int, 붙임 | 차지할 행·열 개수입니다. |
| Panel.ZIndex | int, 붙임 | 같은 Panel 자식 사이의 겹침 순서를 지정합니다. |

Thickness의 XAML 값 `16`은 네 방향 모두, `16,8`은 좌우 16·상하 8, `4,8,12,16`은 왼쪽·위·오른쪽·아래 순서입니다. CornerRadius의 네 값은 왼쪽 위·오른쪽 위·오른쪽 아래·왼쪽 아래 순서입니다.

```xml
<ui:Button Width="160" Padding="16,8" Margin="0,0,0,12"
           HorizontalAlignment="Left" Content="저장" />
```

## 표시·입력·외형

| 속성 | 타입 | 변경 효과 |
| --- | --- | --- |
| Visibility | Visibility | Visible=표시, Hidden=숨기고 공간 유지, Collapsed=공간도 제거합니다. |
| IsEnabled | bool | false이면 상호작용을 막고 기본 템플릿은 비활성 색을 적용합니다. |
| IsHitTestVisible | bool | false이면 포인터 히트 테스트 대상에서 제외합니다. 표시 여부와는 별개입니다. |
| Focusable / IsTabStop | bool | 키보드 포커스·Tab 순서 참여 여부입니다. 타입별 지원이 다릅니다. |
| Opacity | double | 0~1 불투명도입니다. 0이어도 공간·입력 대상은 남을 수 있습니다. |
| Background / Foreground | Brush | 배경·글자·아이콘 등에 쓸 브러시입니다. 템플릿별 적용 영역을 확인합니다. |
| BorderBrush / BorderThickness | Brush / Thickness | 테두리 색과 두께입니다. 두께가 0이면 색을 바꿔도 보이지 않습니다. |
| FontFamily / FontSize / FontWeight / FontStyle | 글꼴 속성 | 텍스트·글꼴 아이콘을 조정합니다. 이미지 픽셀은 바뀌지 않습니다. |
| ToolTip | object | 짧은 도움말입니다. 문자열 또는 ToolTip 콘텐츠를 넣습니다. |
| ContextMenu | ContextMenu | 우클릭 메뉴입니다. 팝업의 DataContext 연결에 주의합니다. |
| FlowDirection | FlowDirection | LeftToRight·RightToLeft 배치 방향입니다. |
| AutomationProperties.Name | string, 붙임 | 스크린리더 등 접근성 도구에 이름을 제공합니다. 아이콘 전용 버튼에 특히 유용합니다. |

각 컨트롤의 기본 템플릿이 모두 같은 영역에 Background를 칠하지는 않습니다. CornerRadius 또한 모든 WPF 타입의 공통 인스턴스 속성이 아닙니다. WPF-UI가 제공하는 고유 속성인지, Border 같은 내부 요소의 속성인지 정확한 소유자와 템플릿 연결을 확인해야 합니다.

## 기본값을 두 종류로 나누는 이유

DP 등록 코드의 기본값은 스타일이 적용되기 전 기준값입니다. 예를 들어 NavigationView.OpenPaneLength의 등록값은 `0`, 기본 스타일의 Setter는 `320`입니다. Button.Appearance도 등록값과 스타일의 Setter가 다를 수 있습니다.

값의 출처는 대체로 로컬 값·바인딩, 스타일 트리거, 스타일 Setter, 상속값, 등록 메타데이터 등으로 나뉩니다. 애니메이션·강제 변환 등은 별도의 우선순위를 가집니다. 따라서 문서의 **등록 기본값**을 최종 화면값으로 읽지 않습니다.

```csharp
// 현재 적용값입니다. 등록 기본값과 다를 수 있습니다.
double width = navigation.OpenPaneLength;

// 로컬 값을 지워 스타일/기본값 경로로 돌립니다.
navigation.ClearValue(Wpf.Ui.Controls.NavigationView.OpenPaneLengthProperty);
```

## 바인딩·컬렉션·코드 변경

| 속성·개념 | 동작 |
| --- | --- |
| DataContext | 기본 Binding의 데이터 공급원입니다. 시각·논리 트리에서 상속되지만 팝업 등 경계에서는 별도 연결이 필요할 수 있습니다. |
| Binding.Mode | OneWay=모델→화면, TwoWay=양방향, OneTime=초기 읽기입니다. 기본값은 DP 메타데이터마다 다릅니다. |
| UpdateSourceTrigger | TextBox.Text는 기본적으로 포커스 이탈 때 모델을 갱신합니다. 실시간 입력은 PropertyChanged를 명시합니다. |
| ItemsSource | 외부 데이터 목록입니다. 같은 컨트롤의 Items에 동시에 직접 추가하지 않습니다. |
| ItemTemplate | 각 데이터 항목의 화면 구조입니다. |
| ItemContainerStyle | ListBoxItem·TreeViewItem 등 데이터 바깥 컨테이너의 스타일입니다. |
| SelectedItem | 보통 선택 데이터 객체입니다. 데이터와 생성된 UI 컨테이너를 구별합니다. |

```xml
<ui:TextBox Text="{Binding UserName, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
<ui:NumberBox Value="{Binding Quantity, Mode=TwoWay}" />
```

CLR 속성 대입·SetValue는 기존 바인딩을 대체할 수 있습니다. ViewModel을 바꾸는 방법을 먼저 사용하고 컨트롤 내부 협력 코드에서는 SetCurrentValue가 바인딩 유지에 도움이 됩니다. UI 변경은 UI Dispatcher 스레드에서 수행합니다.

## 읽기 전용이라는 말

문서의 `외부 읽기 전용`은 일반 C# 호출자가 속성에 대입할 수 없다는 뜻입니다. `get`만 있거나 setter가 protected·internal인 경우가 포함됩니다. `DependencyProperty.RegisterReadOnly` 등록과 항상 같은 뜻은 아닙니다.

NavigationView.MenuItems는 참조를 대입할 수 없지만 컬렉션이므로 `MenuItems.Add(...)`는 가능합니다. SelectedItem처럼 상태를 나타내는 값은 Navigate·클릭 등으로 바꿉니다. 내부 DP 필드를 강제로 설정해서 읽기 전용 CLR 계약을 우회하는 방식은 예제로 사용하지 않습니다.

## 참고

- [WPF 속성값 우선순위](https://learn.microsoft.com/dotnet/desktop/wpf/properties/dependency-property-value-precedence)
- [WPF 데이터 바인딩](https://learn.microsoft.com/dotnet/desktop/wpf/data/)
- [4.3.0 NavigationView 스타일](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationView.xaml)
