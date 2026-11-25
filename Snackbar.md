# Snackbar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

작업 결과를 잠시 보여 주고 자동으로 숨기는 알림입니다. SnackbarPresenter가 표시 순서를 관리합니다.

**타입:** `Wpf.Ui.Controls.Snackbar` · **기반:** `ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Grid>
    <TextBlock Text="앱 화면" />
    <ui:SnackbarPresenter x:Name="Presenter" VerticalAlignment="Bottom" Margin="16" />
</Grid>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var snackbar = new ui.Snackbar(Presenter)
{
    Title = "저장 완료", Content = "문서를 저장했습니다.",
    Appearance = ui.ControlAppearance.Success,
    Timeout = System.TimeSpan.FromSeconds(3)
};
snackbar.Show();
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsCloseButtonEnabled` | `bool` | 읽기·쓰기 | `true` | 사용자가 스낵바를 닫는 버튼의 활성 여부입니다. |
| `SlideTransform` | `TranslateTransform?` | 읽기·쓰기 | `null` | 슬라이드 표시·숨김 애니메이션에 쓰는 이동 변환입니다. 보통 기본 템플릿이 관리합니다. |
| `IsShown` | `bool` | 읽기·쓰기 | `false` | 표시 애니메이션 상태입니다. 이 값만 바꾸어도 Presenter에 자동 삽입되지는 않습니다. 실제 표시는 `Show()` 계열로 요청합니다. |
| `Timeout` | `TimeSpan` | 읽기·쓰기 | `TimeSpan.FromSeconds(2)` | 표시 후 자동 숨김까지의 `TimeSpan`입니다. 단위 없는 정수가 아니라 `TimeSpan.FromSeconds(3)`처럼 지정합니다. |
| `Title` | `object?` | 읽기·쓰기 | `null` | 제목 영역에 표시할 값입니다. 본문과 구별되는 제목으로 사용합니다. |
| `TitleTemplate` | `DataTemplate?` | 읽기·쓰기 | `null` | 객체형 `Title`의 표시 방법을 정하는 `DataTemplate`입니다. 제목 데이터와 화면 구성을 분리할 때 사용합니다. |
| `Icon` | `IconElement?` | 읽기·쓰기 | `null` | 텍스트 옆에 표시할 아이콘입니다. `SymbolIcon`, `FontIcon`, `ImageIcon` 등을 넣습니다. 아이콘을 다른 부모와 공유하지 말고 각각 생성합니다. |
| `Appearance` | `ControlAppearance` | 읽기·쓰기 | `ControlAppearance.Secondary` | 테마의 의미별 색을 선택합니다. `Primary`는 강조, `Secondary`는 일반 보조 동작, `Danger`는 위험 동작에 적합합니다. 실제 색은 테마 리소스가 결정합니다. |
| `ContentForeground` | `Brush` | 읽기·쓰기 | `SystemColors.ControlTextBrush` | 스낵바 본문에 적용할 별도 전경 브러시입니다. 제목·아이콘 색과 본문 색을 나눌 때 사용합니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ControlAppearance`: `Primary`, `Secondary`, `Info`, `Dark`, `Light`, `Danger`, `Success`, `Caution`, `Transparent`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

생성자에 Presenter가 필요하므로 Snackbar.Resources는 C#에서 채운 뒤 Show를 호출하는 방식이 간단합니다. 키의 실제 대소문자는 `SnackBarBackground`·`SnackBarBorderBrush`·`SnackBarForeground`입니다. Appearance별 트리거는 Palette 계열 Color도 사용하므로 Brush와 Color의 타입을 구별합니다. 스낵바 자체와 Presenter의 위치·Margin을 나눠 조정합니다.

### C#에서 알림별 리소스를 지정

<!-- customization:csharp-only Snackbar_Resources -->
```csharp
var notice = new ui.Snackbar(Presenter)
{
    Title = "완료", Content = "저장했습니다.",
    Appearance = ui.ControlAppearance.Secondary
};
notice.Resources["SnackBarBackground"] = System.Windows.Media.Brushes.MidnightBlue;
notice.Show();
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `PaletteGreenColor` | Color | SolidColorBrush Color〔Appearance=Success〕 |
| `PaletteLightBlueColor` | Color | SolidColorBrush Color〔Appearance=Info〕 |
| `PaletteOrangeColor` | Color | SolidColorBrush Color〔Appearance=Caution〕 |
| `PaletteRedColor` | Color | SolidColorBrush Color〔Appearance=Danger〕 |
| `SnackBarBackground` | SolidColorBrush | 컨트롤.Background |
| `SnackBarBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `SnackBarForeground` | SolidColorBrush | 컨트롤.Foreground / 컨트롤.ContentForeground |
| `SystemAccentColorSecondary` | Color | SolidColorBrush Color〔Appearance=Primary〕 |
| `TextOnAccentFillColorPrimary` | Color | SolidColorBrush Color〔Appearance=Primary〕 |
| `TextOnAccentFillColorSecondary` | Color | SolidColorBrush Color〔Appearance=Primary〕 |

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `MinHeight` | `Border#CardBorder.MinHeight` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Background` | `Border#CardBorder.Background` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `BorderBrush` | `Border#CardBorder.BorderBrush` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `SlideTransform` | `Border#CardBorder.RenderTransform` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Visibility` | `Border#CardBorder.Visibility` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Icon` | `ContentPresenter#CardIcon.Content` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Foreground` | `ContentPresenter#CardIcon.TextElement.Foreground` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Title` | `ContentPresenter#TitleContentPresenter.Content` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `TitleTemplate` | `ContentPresenter#TitleContentPresenter.ContentTemplate` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Foreground` | `ContentPresenter#TitleContentPresenter.TextElement.Foreground` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Content` | `ContentPresenter.Content` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentStringFormat` | `ContentPresenter.ContentStringFormat` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentTemplateSelector` | `ContentPresenter.ContentTemplateSelector` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentForeground` | `ContentPresenter.TextElement.Foreground` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Appearance` | `Button#CloseButton.Appearance` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `TemplateButtonCommand` | `Button#CloseButton.Command` | Binding to TemplatedParent | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Foreground` | `Button#CloseButton.Foreground` | TemplateBinding | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Margin` | `24` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `컨트롤.MinHeight` | `68` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Grid#CardBorderContainer.Margin` | `0,0,0,-200` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Border#CardBorder.Padding` | `12` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Border#CardBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Border#CardBorder.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ColumnDefinition#ChevronColumn.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentPresenter#CardIcon.Margin` | `0,0,12,0` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `ContentPresenter#TitleContentPresenter.Margin` | `0` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Button#CloseButton.Margin` | `12,0,0,0` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `Button#CloseButton.Padding` | `6` | 직접 지정 / 현재 템플릿 | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `CardIcon.Margin` | `0` | Icon={x:Null} | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `CloseButton.Margin` | `0` | IsCloseButtonEnabled=False | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |
| `컨트롤.Background` | `Transparent` | Appearance=Transparent | [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource SnackBarForeground}` | 암시적 스타일 |
| `ContentForeground` | `{DynamicResource SnackBarForeground}` | 암시적 스타일 |
| `Background` | `{DynamicResource SnackBarBackground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource SnackBarBorderBrush}` | 암시적 스타일 |
| `Margin` | `24` | 암시적 스타일 |
| `MinHeight` | `68` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `False` | 암시적 스타일 |
| `VerticalAlignment` | `Bottom` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `Opened` | 열림 상태 또는 표시 완료 경로에서 발생합니다. 컨트롤별 실제 팝업·상태 변경 시점은 구현을 확인합니다. |
| `Closed` | 닫힌 후 발생합니다. ContentDialog는 결과가 이벤트 인자에 들어갑니다. |

## 주요 메서드

| 시그니처 | 용도 |
| --- | --- |
| `void Show()` | Flyout은 팝업을 열고 Snackbar는 Presenter 큐에 추가합니다. MessageBox의 이 메서드는 예외를 던집니다. |
| `void Show(bool immediately)` | Flyout은 팝업을 열고 Snackbar는 Presenter 큐에 추가합니다. MessageBox의 이 메서드는 예외를 던집니다. |
| `Task ShowAsync()` | ContentDialog는 닫힘 결과까지 기다립니다. Snackbar의 기본 경로는 큐 등록만 하고 반환합니다. |
| `Task ShowAsync(bool immediately)` | ContentDialog는 닫힘 결과까지 기다립니다. Snackbar의 기본 경로는 큐 등록만 하고 반환합니다. |

## 동작과 주의 사항

Snackbar는 Presenter를 받는 생성자를 사용하므로 일반 `<ui:Snackbar />` 선언으로 만들지 않습니다. `ShowAsync(false)`는 큐에 넣은 뒤 곧바로 반환하는 경로이며 표시 종료까지 기다리는 API로 해석하지 않습니다. 즉시 표시·교체는 `ShowAsync(true)`를 검토합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Snackbar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.cs)
- [Snackbar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Snackbar/Snackbar.xaml)
- [Gallery: SnackbarPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/DialogsAndFlyouts/SnackbarPage.xaml)
