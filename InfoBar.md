# InfoBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

페이지 안에 유지되는 정보·성공·경고·오류 메시지입니다.

**타입:** `Wpf.Ui.Controls.InfoBar` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:InfoBar x:Name="Demo" IsOpen="True" Severity="Warning" Title="연결 끊김" Message="네트워크를 확인하세요." IsClosable="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Severity = ui.InfoBarSeverity.Success;
Demo.Title = "다시 연결됨";
Demo.Message = "정상적으로 사용할 수 있습니다.";
Demo.IsOpen = true;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsClosable` | `bool` | 읽기·쓰기 | `true` | 닫기 버튼 표시 여부입니다. `false`이면 사용자가 닫기 버튼으로 숨길 수 없습니다. |
| `IsOpen` | `bool` | 읽기·쓰기 | `false` | 알림 표시 여부입니다. 닫기 동작은 컨트롤을 삭제하지 않고 이 값을 `false`로 바꿉니다. |
| `Title` | `string` | 읽기·쓰기 | `string.Empty` | 짧은 제목 문자열입니다. |
| `Message` | `string` | 읽기·쓰기 | `string.Empty` | 제목 옆·아래에 표시할 설명 문자열입니다. 줄바꿈은 템플릿과 할당 폭에 영향을 받습니다. |
| `Severity` | `InfoBarSeverity` | 읽기·쓰기 | `InfoBarSeverity.Informational` | `Informational`, `Success`, `Warning`, `Error`에 따라 배경·아이콘·전경 리소스를 바꿉니다. |
| `TemplateButtonCommand` | `IRelayCommand` | 외부 읽기 전용 | `null` | 기본 템플릿 내부 버튼이 호출하는 명령입니다. 외부에서 교체하는 업무용 `Command`가 아니며 사용자 코드는 해당 공개 이벤트·메서드를 사용합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `InfoBarSeverity`: `Informational`, `Success`, `Warning`, `Error`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

ControlCornerRadius는 기본 테두리로 연결됩니다. Severity별 배경·테두리·아이콘 색은 InfoBarInformational/Success/Warning/Error 계열 키로 나뉘며 ContentBorder에 직접 적용되는 트리거도 있습니다. 컨트롤 Background 하나만 바꾸면 모든 Severity 상태가 바뀌는 구조는 아닙니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example InfoBar_Resources -->
```xml
<ui:InfoBar IsOpen="True" Severity="Warning" Title="연결 끊김" Message="네트워크를 확인하세요." IsClosable="True"  x:Name="ResourceDemo">
    <ui:InfoBar.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:InfoBar.Resources>
</ui:InfoBar>
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
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `ControlFillColorDefault` | Color | SolidColorBrush Color |
| `InfoBarBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `InfoBarErrorSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Error〕 |
| `InfoBarErrorSeverityBorderBrush` | SolidColorBrush | ContentBorder.BorderBrush〔Severity=Error〕 |
| `InfoBarErrorSeverityIconBackground` | SolidColorBrush | SymbolIcon.Foreground〔Severity=Error〕 |
| `InfoBarInformationalSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Informational〕 |
| `InfoBarInformationalSeverityBorderBrush` | SolidColorBrush | ContentBorder.BorderBrush〔Severity=Informational〕 |
| `InfoBarSuccessSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Success〕 |
| `InfoBarSuccessSeverityBorderBrush` | SolidColorBrush | ContentBorder.BorderBrush〔Severity=Success〕 |
| `InfoBarSuccessSeverityIconBackground` | SolidColorBrush | SymbolIcon.Foreground〔Severity=Success〕 |
| `InfoBarTitleForeground` | SolidColorBrush | 컨트롤.Foreground |
| `InfoBarWarningSeverityBackgroundBrush` | SolidColorBrush | ContentBorder.Background〔Severity=Warning〕 |
| `InfoBarWarningSeverityBorderBrush` | SolidColorBrush | ContentBorder.BorderBrush〔Severity=Warning〕 |
| `InfoBarWarningSeverityIconBackground` | SolidColorBrush | SymbolIcon.Foreground〔Severity=Warning〕 |
| `SystemAccentColorSecondary` | Color | SolidColorBrush Color〔Severity=Informational〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `InfoBarBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `InfoBarPadding` | Thickness | 컨트롤.Padding |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `BorderBrush` | `Border#ContentBorder.BorderBrush` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `BorderThickness` | `Border#ContentBorder.BorderThickness` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Border.CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Title` | `TextBlock#TitleText.Text` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `FontSize` | `TextBlock#TitleText.TextElement.FontSize` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Message` | `TextBlock.Text` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `FontSize` | `TextBlock.TextElement.FontSize` | TemplateBinding | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `TemplateButtonCommand` | `Button#CloseButton.Command` | Binding to TemplatedParent | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Border#ContentBorder.Padding` | `16,12` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Border.Margin` | `0,2,14,0` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `SymbolIcon#SymbolIcon.FontSize` | `16` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `TextBlock#TitleText.Margin` | `0,0,14,0` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `TextBlock.Margin` | `0` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Border.Margin` | `12,-2,0,0` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Button#CloseButton.Padding` | `4` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Button#CloseButton.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |
| `Button#CloseButton.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource InfoBarTitleForeground}` | 암시적 스타일 |
| `Padding` | `{StaticResource InfoBarPadding}` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalAlignment` | `Center` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource InfoBarBorderBrush}` | 암시적 스타일 |
| `BorderThickness` | `{StaticResource InfoBarBorderThemeThickness}` | 암시적 스타일 |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `False` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

Snackbar처럼 자동 숨김 타이머를 제공하지 않습니다. `IsOpen=False`면 숨김 상태로 남아 있으므로 다시 표시할 수 있습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [InfoBar.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.cs)
- [InfoBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/InfoBar/InfoBar.xaml)
- [Gallery: InfoBarPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/InfoBarPage.xaml)
