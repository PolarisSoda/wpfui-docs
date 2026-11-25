# MessageBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

별도 Window로 표시하는 비동기 메시지 창입니다. ContentDialog와 달리 화면 안 호스트를 요구하지 않습니다.

**타입:** `Wpf.Ui.Controls.MessageBox` · **기반:** `System.Windows.Window`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:MessageBox xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml"
    Title="안내" Content="작업을 마쳤습니다." CloseButtonText="확인" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var box = new ui.MessageBox
{
    Owner = this, Title = "삭제 확인", Content = "이 항목을 삭제할까요?",
    PrimaryButtonText = "삭제", CloseButtonText = "취소",
    PrimaryButtonAppearance = ui.ControlAppearance.Danger
};
ui.MessageBoxResult result = await box.ShowDialogAsync();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `ShowTitle` | `bool` | 읽기·쓰기 | `true` | 창 안 메시지 템플릿의 제목 표시 여부입니다. `Title` 값 자체를 지우거나 소유 창을 변경하는 설정은 아닙니다. |
| `PrimaryButtonText` | `string` | 읽기·쓰기 | `string.Empty` | 기본 동작 버튼의 글자입니다. 빈 문자열이면 기본 템플릿이 해당 버튼을 숨깁니다. |
| `SecondaryButtonText` | `string` | 읽기·쓰기 | `string.Empty` | 보조 동작 버튼의 글자입니다. 빈 문자열이면 기본 템플릿이 해당 버튼을 숨깁니다. |
| `CloseButtonText` | `string` | 읽기·쓰기 | `"Close"` | 닫기 버튼의 글자입니다. 기본값은 `Close`이며, 빈 문자열이면 기본 템플릿에서 버튼이 숨겨집니다. |
| `PrimaryButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 기본 동작 버튼 앞에 표시할 아이콘입니다. |
| `SecondaryButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 보조 동작 버튼 앞에 표시할 아이콘입니다. |
| `CloseButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 닫기 버튼 앞에 표시할 아이콘입니다. |
| `PrimaryButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Primary` | 기본 동작 버튼의 의미별 색입니다. 버튼 표시 여부는 `PrimaryButtonText`로 결정합니다. |
| `SecondaryButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Secondary` | 보조 동작 버튼의 의미별 색입니다. |
| `CloseButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Secondary` | 닫기 버튼의 의미별 색입니다. |
| `IsCloseButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 닫기 버튼 활성 여부입니다. 소유 창과 비동기 표시 방식도 함께 확인합니다. |
| `IsSecondaryButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 보조 동작 버튼의 활성 여부입니다. |
| `IsPrimaryButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 기본 동작 버튼의 활성 여부입니다. 유효하지 않은 입력 상태에서 `false`로 설정하면 실행을 막을 수 있습니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Title` | `string` | 창 제목입니다. |
| `Owner` | `Window` | 소유 창입니다. 메시지 창의 활성·표시 관계에 중요합니다. |
| `WindowState` | `WindowState` | Normal·Minimized·Maximized 창 상태입니다. |
| `ResizeMode` | `ResizeMode` | 창 크기 조절·최소화·최대화 허용 범위입니다. |
| `WindowStartupLocation` | `WindowStartupLocation` | 수동·화면 중앙·소유 창 중앙의 초기 배치입니다. |
| `SizeToContent` | `SizeToContent` | 내용에 맞춰 창 크기를 정할지 선택합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ControlAppearance`: `Primary`, `Secondary`, `Info`, `Dark`, `Light`, `Danger`, `Success`, `Caution`, `Transparent`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

별도 Window이므로 MessageBox.Resources에서 MessageBoxBackground·MessageBoxForeground·MessageBoxTopOverlay 등의 DynamicResource를 재정의할 수 있습니다. 내부 버튼·구분선·오버레이의 고정 레이아웃 값은 외부 Width·Padding만으로 모두 바뀌지 않습니다. 크기·소유 창을 지정한 뒤 ShowDialogAsync를 호출합니다.

### 이 컨트롤의 Resources에서 바꾸기

`MessageBoxBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example MessageBox_Resources -->
```xml
<ui:MessageBox xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:ui="http://schemas.lepo.co/wpfui/2022/xaml"
    Title="안내" Content="작업을 마쳤습니다." CloseButtonText="확인"  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" x:Name="ResourceDemo">
    <ui:MessageBox.Resources>
        <SolidColorBrush x:Key="MessageBoxBackground" Color="#2563EB" />
    </ui:MessageBox.Resources>
</ui:MessageBox>
```

```csharp
ResourceDemo.Resources["MessageBoxBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `MessageBoxBackground` | SolidColorBrush | 컨트롤.Background |
| `MessageBoxForeground` | SolidColorBrush | 컨트롤.Foreground |
| `MessageBoxSeparatorBorderBrush` | SolidColorBrush | Border BorderBrush |
| `MessageBoxTopOverlay` | SolidColorBrush | Border Background |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `BoolToVisibilityConverter` | BoolToVisibilityConverter | Button Visibility |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Grid.Background` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Foreground` | `TextBlock#Title.Foreground` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Title` | `TextBlock#Title.Text` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ContentTemplate` | `ContentPresenter#ContentPresenter.ContentTemplate` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ContentTemplateSelector` | `ContentPresenter#ContentPresenter.ContentTemplateSelector` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Padding` | `Border.Padding` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `PrimaryButtonAppearance` | `Button.Appearance` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `PrimaryButtonText` | `Button.Content` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `PrimaryButtonIcon` | `Button.Icon` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `IsPrimaryButtonEnabled` | `Button.IsEnabled` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `IsPrimaryButtonEnabled` | `Button.Visibility` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondaryButtonAppearance` | `Button.Appearance` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondaryButtonText` | `Button.Content` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondaryButtonIcon` | `Button.Icon` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `IsSecondaryButtonEnabled` | `Button.IsEnabled` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `IsSecondaryButtonEnabled` | `Button.Visibility` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `CloseButtonAppearance` | `Button.Appearance` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `CloseButtonText` | `Button.Content` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `CloseButtonIcon` | `Button.Icon` | TemplateBinding | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.MaxWidth` | `450` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `컨트롤.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `컨트롤.FontSize` | `14` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `컨트롤.Padding` | `12` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `WindowChrome.CornerRadius` | `0` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `TextBlock#Title.Margin` | `12,12,35,0` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ContentPresenter#ContentPresenter.Margin` | `12,10,12,12` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Border.BorderThickness` | `0,1,0,0` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `Border.CornerRadius` | `0` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ColumnDefinition#PrimaryColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ColumnDefinition#FirstSpacer.Width` | `8` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ColumnDefinition#SecondaryColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ColumnDefinition#SecondSpacer.Width` | `8` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ColumnDefinition#CloseColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `ContentPresenter.Margin` | `8` | WindowState=Maximized | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `PrimaryColumn.Width` | `0` | IsPrimaryButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `FirstSpacer.Width` | `0` | IsPrimaryButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondSpacer.Width` | `0` | IsPrimaryButtonEnabled=False; IsSecondaryButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `FirstSpacer.Width` | `0` | IsSecondaryButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondaryColumn.Width` | `0` | IsSecondaryButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `CloseColumn.Width` | `0` | IsCloseButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `SecondSpacer.Width` | `0` | IsCloseButtonEnabled=False | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |
| `컨트롤.BorderThickness` | `6,6,6,0` | WindowState=Maximized | [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `MaxWidth` | `450` | 암시적 스타일 |
| `BorderThickness` | `0` | 암시적 스타일 |
| `Background` | `{DynamicResource MessageBoxBackground}` | 암시적 스타일 |
| `FontSize` | `14` | 암시적 스타일 |
| `Padding` | `12` | 암시적 스타일 |
| `Foreground` | `{DynamicResource MessageBoxForeground}` | 암시적 스타일 |
| `TextElement.FontWeight` | `Regular` | 암시적 스타일 |
| `WindowStyle` | `ToolWindow` | 암시적 스타일 |
| `ShowInTaskbar` | `False` | 암시적 스타일 |
| `RenderOptions.BitmapScalingMode` | `Fant` | 암시적 스타일 |
| `ResizeMode` | `NoResize` | 암시적 스타일 |
| `WindowState` | `Normal` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void Show()` | Flyout은 팝업을 열고 Snackbar는 Presenter 큐에 추가합니다. MessageBox의 이 메서드는 예외를 던집니다. |
| `bool? ShowDialog()` | WPF-UI MessageBox에서 사용하면 예외를 던집니다. ShowDialogAsync를 사용합니다. |
| `void Close()` | WPF-UI MessageBox의 숨겨진 기본 종료 메서드입니다. 해당 타입은 내부 버튼·비동기 표시 수명으로 닫습니다. |
| `Task<MessageBoxResult> ShowDialogAsync( bool showAsDialog = true, CancellationToken cancellationToken = default )` | 메시지 창을 표시하고 MessageBoxResult를 돌려줍니다. await로 호출합니다. |

## 동작과 주의 사항

XAML은 독립 창 선언 형태를 보여 주는 예시입니다. 일반적인 사용은 C#에서 인스턴스를 만들고 `ShowDialogAsync()`를 호출합니다. 4.3.0의 `Show()`·`ShowDialog()`·`Close()`는 대체 API 사용을 요구하며 예외를 던지므로 기본 Window처럼 호출하지 않습니다. 코드의 `this`는 소유 Window입니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [MessageBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.cs)
- [MessageBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.xaml)
- [Gallery: MessageBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DialogsAndFlyouts/MessageBoxPage.xaml)
