# CalendarDatePicker

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

버튼을 누르면 달력을 열어 날짜를 고르는 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.CalendarDatePicker` · **기반:** `Wpf.Ui.Controls.Button`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:CalendarDatePicker x:Name="Demo" Content="날짜 선택" IsTodayHighlighted="True" FirstDayOfWeek="Monday" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Date = System.DateTime.Today;
Demo.FirstDayOfWeek = System.DayOfWeek.Sunday;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsTodayHighlighted` | `bool` | 읽기·쓰기 | `false` | 내부 달력에서 오늘 날짜를 강조할지 정합니다. |
| `IsCalendarOpen` | `bool` | 읽기·쓰기 | `false` | 달력 팝업의 열림 상태입니다. 내부 팝업은 첫 클릭에서 생성되므로 첫 클릭 전 코드로 `true`만 지정해도 팝업이 생성되는 구조는 아닙니다. |
| `FirstDayOfWeek` | `DayOfWeek` | 읽기·쓰기 | `DateTimeHelper.GetCurrentDateFormat().FirstDayOfWeek` | 달력 열의 시작 요일입니다. 등록 기본값은 현재 문화권의 요일 설정입니다. |
| `Date` | `DateTime?` | 읽기·쓰기 | `null` | 선택 날짜입니다. `null`은 미선택이며, 달력에서 날짜를 고르면 이 값이 바뀌고 팝업이 닫힙니다. 바인딩에는 명시적으로 `Mode=TwoWay`를 지정합니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `Icon` | [Button](Button.md) | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `Appearance` | [Button](Button.md) | 테마의 의미별 색을 선택합니다. `Primary`는 강조, `Secondary`는 일반 보조 동작, `Danger`는 위험 동작에 적합합니다. 실제 색은 테마 리소스가 결정합니다. |
| `MouseOverBackground` | [Button](Button.md) | 마우스가 올라간 동안 사용할 배경 브러시입니다. 일반 상태의 `Background`와 구분됩니다. |
| `MouseOverBorderBrush` | [Button](Button.md) | 마우스가 올라간 동안 사용할 테두리 브러시입니다. `BorderThickness`가 0이면 테두리는 보이지 않습니다. |
| `PressedForeground` | [Button](Button.md) | 누르는 동안의 텍스트·아이콘 전경색입니다. |
| `PressedBackground` | [Button](Button.md) | 누르는 동안의 배경 브러시입니다. |
| `PressedBorderBrush` | [Button](Button.md) | 누르는 동안의 테두리 브러시입니다. |
| `CornerRadius` | [Button](Button.md) | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Command` | `ICommand` | 실행할 ViewModel 명령입니다. CanExecute=false이면 버튼이 비활성화될 수 있습니다. |
| `CommandParameter` | `object` | 명령에 전달할 데이터입니다. |
| `ClickMode` | `ClickMode` | Release·Press·Hover 중 클릭을 발생시킬 시점을 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Icon` | `{StaticResource CalendarPickerIcon}` | DefaultUiCalendarDatePickerStyle |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

내부 팝업은 첫 클릭 때 생성됩니다. 날짜 선택 시 `Date`가 바뀌고 팝업이 닫힙니다. 기본 DatePicker의 `SelectedDate` 대신 `Date`를 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [CalendarDatePicker.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CalendarDatePicker/CalendarDatePicker.cs)
- [CalendarDatePicker.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/CalendarDatePicker/CalendarDatePicker.xaml)
- [Gallery: CalendarDatePickerPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DateAndTime/CalendarDatePickerPage.xaml)
