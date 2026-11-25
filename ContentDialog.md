# ContentDialog

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

현재 창 위에 겹쳐 표시하는 비동기 대화상자입니다. 별도 최상위 Window를 만들지 않습니다.

**타입:** `Wpf.Ui.Controls.ContentDialog` · **기반:** `ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Grid>
    <StackPanel><TextBlock Text="앱 콘텐츠" /></StackPanel>
    <ui:ContentDialogHost x:Name="DialogHost" IsDisableSiblingsEnabled="True" />
</Grid>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var dialog = new ui.ContentDialog(DialogHost)
{
    Title = "저장할까요?", Content = "변경한 내용을 저장합니다.",
    PrimaryButtonText = "저장", CloseButtonText = "취소"
};
ui.ContentDialogResult result = await dialog.ShowAsync();
if (result == ui.ContentDialogResult.Primary)
{
    // 저장 작업을 수행합니다.
}
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Title` | `object?` | 읽기·쓰기 | `null` | 제목 영역에 표시할 값입니다. 본문과 구별되는 제목으로 사용합니다. |
| `TitleTemplate` | `DataTemplate?` | 읽기·쓰기 | `null` | 객체형 `Title`의 표시 방법을 정하는 `DataTemplate`입니다. 제목 데이터와 화면 구성을 분리할 때 사용합니다. |
| `DialogWidth` | `double` | 읽기·쓰기 | `double.PositiveInfinity` | 측정 과정에서 계산·갱신되는 다이얼로그 폭입니다. 일반 `Width`와 달리 전체 오버레이 내부의 대화상자 크기에 사용됩니다. |
| `DialogHeight` | `double` | 읽기·쓰기 | `double.PositiveInfinity` | 측정 과정에서 계산·갱신되는 대화상자 높이입니다. |
| `DialogMaxWidth` | `double` | 읽기·쓰기 | `double.PositiveInfinity` | 대화상자 본체 폭의 상한입니다. 호스트 크기와 함께 배치를 제한합니다. |
| `DialogMaxHeight` | `double` | 읽기·쓰기 | `double.PositiveInfinity` | 대화상자 본체 높이의 상한입니다. |
| `DialogMargin` | `Thickness` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 대화상자 본체 주위의 여백입니다. 전체 호스트를 덮는 컨트롤의 `Margin`과 구별합니다. |
| `PrimaryButtonText` | `string` | 읽기·쓰기 | `string.Empty` | 기본 동작 버튼의 글자입니다. 빈 문자열이면 기본 템플릿이 해당 버튼을 숨깁니다. |
| `SecondaryButtonText` | `string` | 읽기·쓰기 | `string.Empty` | 보조 동작 버튼의 글자입니다. 빈 문자열이면 기본 템플릿이 해당 버튼을 숨깁니다. |
| `CloseButtonText` | `string` | 읽기·쓰기 | `"Close"` | 닫기 버튼의 글자입니다. 기본값은 `Close`이며, 빈 문자열이면 기본 템플릿에서 버튼이 숨겨집니다. |
| `PrimaryButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 기본 동작 버튼 앞에 표시할 아이콘입니다. |
| `SecondaryButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 보조 동작 버튼 앞에 표시할 아이콘입니다. |
| `CloseButtonIcon` | `IconElement?` | 읽기·쓰기 | `null` | 닫기 버튼 앞에 표시할 아이콘입니다. |
| `IsPrimaryButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 기본 동작 버튼의 활성 여부입니다. 유효하지 않은 입력 상태에서 `false`로 설정하면 실행을 막을 수 있습니다. |
| `IsSecondaryButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 보조 동작 버튼의 활성 여부입니다. |
| `PrimaryButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Primary` | 기본 동작 버튼의 의미별 색입니다. 버튼 표시 여부는 `PrimaryButtonText`로 결정합니다. |
| `SecondaryButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Secondary` | 보조 동작 버튼의 의미별 색입니다. |
| `CloseButtonAppearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Secondary` | 닫기 버튼의 의미별 색입니다. |
| `DefaultButton` | `ContentDialogButton` | 읽기·쓰기 | `ContentDialogButton.Primary` | 초기 기본 버튼·키보드 동작에 사용할 버튼입니다. 4.3.0의 값은 `Primary`, `Secondary`, `Close`이며 `None`은 없습니다. 실제 표시·활성 버튼에 맞춰 선택합니다. |
| `IsFooterVisible` | `bool` | 읽기·쓰기 | `true` | 아래 버튼 영역 전체를 표시할지 정합니다. 개별 버튼의 글자 설정과 별개입니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |
| `IsLegacyHost` | `bool` | 외부 읽기 전용 | `true` | 현재 `ContentPresenter` 기반 구형 호스트를 쓰는지 나타냅니다. 생성자·호스트 속성에 의해 갱신됩니다. |
| `DialogHost` | `ContentPresenter?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 구형 `ContentPresenter` 호스트입니다. 표시 전에 지정해야 하며 `DialogHostEx`와 동시에 설정하지 않습니다. |
| `DialogHostEx` | `ContentDialogHost?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | 전용 `ContentDialogHost` 호스트입니다. 4.3.0에서는 이 경로를 사용해 형제 요소 비활성화와 포커스 관리를 구성할 수 있습니다. |
| `ContentPresenter` | `ContentPresenter?` | 읽기·쓰기 | `기존 DP 메타데이터 / CLR 계산값` | Obsolete로 표시된 호환 속성입니다. 4.3.0에서는 별도 자동 속성이며 ShowAsync의 호스트 조회 경로에 연결되어 있지 않습니다. 실제 호스트는 DialogHostEx 또는 구형 DialogHost에 지정합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ControlAppearance`: `Primary`, `Secondary`, `Info`, `Dark`, `Light`, `Danger`, `Success`, `Caution`, `Transparent`.
- `ContentDialogButton`: `Primary`, `Secondary`, `Close`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

대화상자는 PopupCornerRadius, 하단 영역은 DynamicResource DialogFooterCornerRadius, 상단 오버레이는 StaticResource DialogOverlayCornerRadius를 사용합니다. 따라서 PopupCornerRadius 하나를 바꿨다고 모든 내부 레이어가 같은 반지름으로 바뀌지는 않습니다. SmokeFill·본문 배경·하단 배경도 서로 다른 키입니다. 전용 ContentDialogHost 경로에서는 호스트가 배경 격리를 관리하므로 ContentDialogHost 문서도 확인합니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `PopupCornerRadius` | CornerRadius | 컨트롤.Border.CornerRadius |
| `ContentDialogBackground` | SolidColorBrush | 컨트롤.Background |
| `ContentDialogBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `ContentDialogForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ContentDialogSeparatorBorderBrush` | SolidColorBrush | Border BorderBrush |
| `ContentDialogSmokeFill` | SolidColorBrush | DialogRootGrid.Background〔IsLegacyHost=True〕 |
| `ContentDialogTopOverlay` | SolidColorBrush | Border Background |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `DialogFooterCornerRadius` | CornerRadius | Border CornerRadius |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `BoolToVisibilityConverter` | BoolToVisibilityConverter | Border Visibility / Button#PrimaryButton Visibility / Button#SecondaryButton Visibility |
| `DialogOverlayCornerRadius` | CornerRadius | Border CornerRadius |
| `EnumToBoolConverter` | ContentDialogButtonEnumToBoolConverter | Button#PrimaryButton IsDefault / Button#SecondaryButton IsDefault / Button#CloseButton IsDefault |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ContentScroll` (PassiveScrollViewer). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `DialogWidth` | `Border.MaxWidth` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `DialogHeight` | `Border.MaxHeight` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `DialogMargin` | `Border.Margin` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Background` | `Border.Background` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `BorderThickness` | `Border.BorderThickness` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Border.CornerRadius` | `Border.CornerRadius` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Title` | `ContentPresenter.Content` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `TitleTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ScrollViewer.CanContentScroll` | `PassiveScrollViewer#PART_ContentScroll.CanContentScroll` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ScrollViewer.HorizontalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentScroll.HorizontalScrollBarVisibility` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ScrollViewer.IsDeferredScrollingEnabled` | `PassiveScrollViewer#PART_ContentScroll.IsDeferredScrollingEnabled` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ScrollViewer.VerticalScrollBarVisibility` | `PassiveScrollViewer#PART_ContentScroll.VerticalScrollBarVisibility` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter.HorizontalAlignment` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `VerticalContentAlignment` | `ContentPresenter.VerticalAlignment` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Content` | `ContentPresenter.Content` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ContentTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ContentTemplateSelector` | `ContentPresenter.ContentTemplateSelector` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Padding` | `Border.Padding` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `IsFooterVisible` | `Border.Visibility` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PrimaryButtonAppearance` | `Button#PrimaryButton.Appearance` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PrimaryButtonText` | `Button#PrimaryButton.Content` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PrimaryButtonIcon` | `Button#PrimaryButton.Icon` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `DefaultButton` | `Button#PrimaryButton.IsDefault` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `IsPrimaryButtonEnabled` | `Button#PrimaryButton.IsEnabled` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `IsPrimaryButtonEnabled` | `Button#PrimaryButton.Visibility` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `SecondaryButtonAppearance` | `Button#SecondaryButton.Appearance` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `SecondaryButtonText` | `Button#SecondaryButton.Content` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `SecondaryButtonIcon` | `Button#SecondaryButton.Icon` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `DefaultButton` | `Button#SecondaryButton.IsDefault` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `IsSecondaryButtonEnabled` | `Button#SecondaryButton.IsEnabled` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `IsSecondaryButtonEnabled` | `Button#SecondaryButton.Visibility` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `CloseButtonAppearance` | `Button#CloseButton.Appearance` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `CloseButtonText` | `Button#CloseButton.Content` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `CloseButtonIcon` | `Button#CloseButton.Icon` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `DefaultButton` | `Button#CloseButton.IsDefault` | TemplateBinding | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Padding` | `24` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `컨트롤.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Grid.Margin` | `24,10` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ContentPresenter.Margin` | `0,12,0,0` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PassiveScrollViewer#PART_ContentScroll.Margin` | `0,20` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PassiveScrollViewer#PART_ContentScroll.Padding` | `0,0,12,0` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `Border.BorderThickness` | `0,1,0,0` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ColumnDefinition#PrimaryColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ColumnDefinition#FirstSpacer.Width` | `8` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ColumnDefinition#SecondaryColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ColumnDefinition#SecondSpacer.Width` | `8` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `ColumnDefinition#CloseColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `PrimaryColumn.Width` | `0` | IsPrimaryButtonEnabled=False | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `FirstSpacer.Width` | `0` | IsSecondaryButtonEnabled=False | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `SecondaryColumn.Width` | `0` | IsSecondaryButtonEnabled=False | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |
| `SecondSpacer.Width` | `0` | IsPrimaryButtonEnabled=False; IsSecondaryButtonEnabled=False | [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `ScrollViewer.CanContentScroll` | `True` | 암시적 스타일 |
| `ScrollViewer.HorizontalScrollBarVisibility` | `Disabled` | 암시적 스타일 |
| `ScrollViewer.VerticalScrollBarVisibility` | `Auto` | 암시적 스타일 |
| `ScrollViewer.IsDeferredScrollingEnabled` | `False` | 암시적 스타일 |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | 암시적 스타일 |
| `Border.CornerRadius` | `{DynamicResource PopupCornerRadius}` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `DialogMaxHeight` | `850` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |
| `Padding` | `24` | 암시적 스타일 |
| `DialogMaxWidth` | `1000` | 암시적 스타일 |
| `VerticalContentAlignment` | `Stretch` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Stretch` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.TabNavigation` | `Cycle` | 암시적 스타일 |
| `KeyboardNavigation.DirectionalNavigation` | `Cycle` | 암시적 스타일 |
| `KeyboardNavigation.ControlTabNavigation` | `Cycle` | 암시적 스타일 |
| `DialogMargin` | `35` | 암시적 스타일 |
| `BorderThickness` | `1` | 암시적 스타일 |
| `Foreground` | `{DynamicResource ContentDialogForeground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource ContentDialogBorderBrush}` | 암시적 스타일 |
| `Background` | `{DynamicResource ContentDialogBackground}` | 암시적 스타일 |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `Opened` | 열림 상태 또는 표시 완료 경로에서 발생합니다. 컨트롤별 실제 팝업·상태 변경 시점은 구현을 확인합니다. |
| `Closing` | 닫기 직전에 발생합니다. ContentDialog에서 `e.Cancel=true`로 닫기를 취소할 수 있습니다. |
| `Closed` | 닫힌 후 발생합니다. ContentDialog는 결과가 이벤트 인자에 들어갑니다. |
| `ButtonClicked` | ContentDialog 버튼 클릭 알림입니다. `e.Button`으로 Primary·Secondary·Close를 구분합니다. |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `Task<ContentDialogResult> ShowAsync(CancellationToken cancellationToken = default)` | ContentDialog는 닫힘 결과까지 기다립니다. Snackbar의 기본 경로는 큐 등록만 하고 반환합니다. |
| `void Hide(ContentDialogResult result = ContentDialogResult.None)` | ContentDialog를 지정 결과로 닫도록 요청합니다. Closing에서 취소될 수 있습니다. Flyout은 팝업을 닫습니다. |
| `bool IsFocusInsideDialog()` | 현재 키보드 포커스가 이 대화상자 안에 있는지 확인합니다. |

## 동작과 주의 사항

C#은 `async` 메서드 본문입니다. 버튼 닫기를 막으려면 `Closing`에서 `e.Cancel=true`를 설정합니다. `ButtonClicked`는 클릭 알림이며 결과는 Primary·Secondary·None입니다. 제목·본문 크기는 내부 측정 과정에서 갱신되므로 크기 제한은 `DialogMaxWidth`·`DialogMaxHeight`를 우선 검토합니다. [호스트 구성](DialogGuide.md)을 참고합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ContentDialog.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.cs)
- [ContentDialog.FocusBehavior.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.FocusBehavior.cs)
- [ContentDialog.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.xaml)
- [Gallery: ContentDialogPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DialogsAndFlyouts/ContentDialogPage.xaml)
