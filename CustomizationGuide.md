# Resources·Style·Template로 조정하기

[전체 목차](README.md) · [컨트롤별 조사 결과](CustomizationIndex.md) · [리소스 키 전체 사전](ResourceCatalog.md)

공개 속성 목록에 없는 모양도 바꿀 수 있습니다. WPF UI는 크기·색·반지름을 리소스로 공급하고, Style·ControlTemplate에서 이를 연결합니다. **무엇을 바꾸려는지와 실제 연결 경로**를 함께 확인해야 합니다. 키 이름이 존재하는 것만으로 모든 컨트롤·상태에서 동작하는 것은 아닙니다.

## 먼저 선택할 방법

| 바꾸려는 것 | 먼저 사용할 방법 | 예 |
| --- | --- | --- |
| 한 컨트롤의 공개 설정 | XAML 속성 또는 C# 속성 | CardControl.CornerRadius, NumberBox.Minimum |
| 기본 스타일이 동적으로 읽는 크기·색 | 해당 컨트롤의 Resources | Card의 ControlCornerRadius |
| 한 영역의 여러 자식에 같은 설정 | 부모 Grid·Window.Resources | 폼 영역의 TextControlThemePadding |
| 같은 종류의 여러 컨트롤에 공통 속성 | Style + Setter + BasedOn | 버튼의 Padding·MinWidth |
| 라이브러리의 별도 모양 선택 | 명명된 Style 키 | IconInfoBadgeStyle, DotInfoBadgeStyle |
| 데이터 본문·목록 항목 구조 | ContentTemplate·ItemTemplate·CellTemplate | 아이콘+제목+설명 목록 |
| 항목의 선택 테두리·간격 | ItemContainerStyle | ListViewItem.Margin |
| 템플릿의 고정 크기·모서리 분할·구조 | 원본 ControlTemplate 복제·수정 | Footer가 있는 Card의 위·아래 반지름 |

## Card 반지름: Resources를 사용하는 간단한 예

```xml
<ui:Card Padding="16">
    <ui:Card.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:Card.Resources>
    <TextBlock Text="둥근 카드" />
</ui:Card>
```

원본 연결은 `DynamicResource ControlCornerRadius` → Card의 `Border.CornerRadius` DP → 내부 ContentBorder의 CornerRadius입니다. `Card.CornerRadius`라는 공개 CLR 속성을 새로 만든 것은 아닙니다.

```csharp
MyCard.Resources["ControlCornerRadius"] = new System.Windows.CornerRadius(12);
```

이 예제는 **Footer가 없는 기본 템플릿**에 해당합니다. Footer가 있으면 HasFooter 트리거와 FooterBorder의 고정값이 개입합니다. [Card](Card.md)와 [Footer용 전체 템플릿](examples/CustomizationLab/CardWithFooter.xaml)을 참고합니다.

## Resources를 어디에 둘까

```xml
<StackPanel>
    <StackPanel.Resources>
        <CornerRadius x:Key="ControlCornerRadius">8</CornerRadius>
    </StackPanel.Resources>
    <ui:Card Content="부모 영역의 반지름 8" />
    <ui:Card Content="이 카드만 반지름 16">
        <ui:Card.Resources>
            <CornerRadius x:Key="ControlCornerRadius">16</CornerRadius>
        </ui:Card.Resources>
    </ui:Card>
</StackPanel>
```

개별 컨트롤 → 부모 영역 → 앱·테마 범위 등의 조회 규칙으로 값을 찾습니다. 실제로는 Style.Resources·Template.Resources도 조회에 참여합니다. 따라서 컨트롤 안에 같은 키를 쓰는 자식이 있다면 그 자식도 영향을 받을 수 있습니다. 앱 전체 테마를 바꾸려는 경우가 아니면 가장 좁은 범위부터 시작합니다.

팝업 메뉴·ToolTip은 호출 컨트롤과 별도의 시각 트리를 사용합니다. 버튼 Resources에 둔 키가 모든 팝업까지 전달된다고 가정하지 말고 ContextMenu·ToolTip 객체 자체의 Resources나 명시적인 공통 사전을 사용합니다.

## DynamicResource와 StaticResource의 차이

| 연결 방식 | Resources 재정의의 의미 | 주의 |
| --- | --- | --- |
| DynamicResource | 런타임 조회·재평가 경로가 남습니다. 컨트롤 범위의 키로 조정하는 대표 방법입니다. | 더 높은 우선순위의 로컬 값·애니메이션·상태 트리거 또는 다른 내부 값이 실제 표시를 결정할 수 있습니다. |
| StaticResource | 사전·Style·Template를 로드할 때 값이 결정될 수 있습니다. | 라이브러리 내부에서 이미 해석한 값을 인스턴스 Resources로 반드시 덮어쓸 수 있다고 안내하지 않습니다. |
| TemplateBinding | 템플릿 내부 요소가 부모 컨트롤 DP 값을 읽습니다. | 컨트롤 속성 자체에 올바른 값을 공급해야 합니다. |
| TemplatedParent Binding·MultiBinding | 부모 속성과 변환기를 사용합니다. | CardExpander처럼 반지름을 위·아래로 분리하는 처리가 있을 수 있습니다. |
| 고정값 | 해당 위치에 숫자·색이 직접 지정되어 있습니다. | 동일한 이름의 리소스를 추가해도 자동으로 연결되지 않습니다. |
| C#의 Application.Resources 조회 | 구현 코드가 앱 사전에서 직접 값을 읽습니다. | 개별 컨트롤 Resources 재정의와 다릅니다. 생성자에서 읽으면 이후 자동 갱신도 보장되지 않습니다. |

InfoBadge의 기본 숫자 스타일은 ValueInfoBadgeStyleCornerRadius를 StaticResource로 읽습니다. 반면 아이콘·점 스타일은 CornerRadius 속성에 TemplateBinding합니다. 같은 컨트롤이라도 **선택한 Style에 따라 조정 방법이 다릅니다.**

## 리소스 값의 타입을 지키기

```xml
<ui:TextBox xmlns:system="clr-namespace:System;assembly=System.Runtime">
    <ui:TextBox.Resources>
        <CornerRadius x:Key="ControlCornerRadius">10</CornerRadius>
        <Thickness x:Key="TextControlThemePadding">16,10</Thickness>
        <system:Double x:Key="TextControlThemeMinHeight">40</system:Double>
        <SolidColorBrush x:Key="TextControlBackgroundFocused" Color="#EFF6FF" />
    </ui:TextBox.Resources>
</ui:TextBox>
```

Color와 Brush는 다른 타입입니다. 이름에 Brush가 들어 있어도 이름만 믿지 말고 정의와 사용하는 속성의 타입을 확인합니다. 예를 들어 Snackbar의 PaletteRedColor는 Color, SnackBarBackground는 Brush입니다. 이 문서의 리소스 표에는 원본 정의 타입을 함께 실었습니다. 정의가 없는 참조 키도 표시하지만 정상 사용 키로 권장하지 않습니다.

## 상태별 키와 직접 속성의 우선순위

버튼은 Normal·PointerOver·Pressed·Disabled, 토글은 Checked·Unchecked, InfoBar는 Severity마다 다른 리소스·트리거를 사용할 수 있습니다. 일반 배경 하나를 바꾸면 눌렀을 때 원래 색이 다시 나오는 이유입니다.

직접 `Background="Red"`를 지정한 뒤 Resources의 기본 배경 키만 바꾸면 로컬 값이 우선할 수 있습니다. 반대로 템플릿 내부 Border에 트리거가 직접 적용되면 바깥 컨트롤 Background를 설정해도 내부 상태 색이 남을 수 있습니다. 각 문서의 **입력 속성 → 내부 반영 위치**, **고정값·적용 조건** 표를 함께 확인합니다.

```csharp
// 이전에 직접 지정한 로컬 값을 제거하고 스타일 경로로 되돌리는 예입니다.
MyCard.ClearValue(System.Windows.Controls.Border.CornerRadiusProperty);
```

UI 갱신은 UI Dispatcher 스레드에서 수행합니다. 바인딩된 속성은 ViewModel에서 변경하는 방법을 우선 사용하고, 로컬 DP 대입이 바인딩을 대체할 수 있다는 점도 고려합니다.

## Style을 확장하기

```xml
<ui:Button Content="넓은 버튼">
    <ui:Button.Style>
        <Style TargetType="{x:Type ui:Button}"
               BasedOn="{StaticResource {x:Type ui:Button}}">
            <Setter Property="MinWidth" Value="160" />
            <Setter Property="Padding" Value="24,12" />
        </Style>
    </ui:Button.Style>
</ui:Button>
```

기존 WPF UI 스타일을 BasedOn으로 연결하면 기본 템플릿·상태 설정을 유지하면서 속성을 추가할 수 있습니다. TargetType은 적용 대상과 맞아야 합니다. 한 번 적용되어 봉인된 Style 객체를 C#에서 직접 수정하는 대신 새 Style을 만듭니다.

기본 WPF 타입의 암시적 스타일과 `ui:` 파생 타입의 스타일은 정확한 타입 일치 조건이 다릅니다. TabView·TabViewItem은 독립 템플릿이 없는 빈 파생형이므로 [해당 문서](TabView.md)의 명시적 BasedOn 예제도 확인합니다.

자동 조사 표의 `controls:`는 원본 XAML이 사용하는 `Wpf.Ui.Controls` 접두사이며 이 가이드의 `ui:`와 같은 타입을 가리킵니다. 이를 앱에 복사할 때는 앱에서 선언한 네임스페이스 접두사를 사용합니다.

### 문자열이 아닌 리소스 키

ToolBar는 자식 버튼에 `ToolBar.ButtonStyleKey`라는 객체 키의 Style을 사용합니다. 이를 바꾸는 키는 문자열 `"ToolBar.ButtonStyleKey"`가 아니라 `{x:Static ToolBar.ButtonStyleKey}`입니다. [ToolBar](ToolBar.md)의 예제는 이 키로 자식 버튼의 스타일을 지정합니다. `x:Type`이나 `ComponentResourceKey`로 정의한 리소스도 해당 객체 키를 사용해야 합니다.

## 템플릿을 복제해야 할 때

Card Footer의 고정 반지름, 스위치 손잡이 지름, Slider의 트랙·Thumb 크기처럼 속성·동적 리소스에 연결되지 않은 부분은 원본 ControlTemplate을 복제합니다. 구조를 바꿀 때는 템플릿 전체를 지정해야 합니다.

ControlTemplate 안의 PART 이름은 장식용 이름이 아닐 수 있습니다. 예를 들어 SplitButton은 PART_Toggle·PART_ToggleButton을 이름으로 찾으며 필요한 요소가 없으면 동작하지 않거나 예외가 발생합니다. ScrollViewer·ItemsPresenter·VirtualizingPanel 연결을 제거하면 스크롤·가상화도 손상될 수 있습니다.

[CustomizationLab](examples/CustomizationLab/README.md)은 기본 카드, Footer용 수정 템플릿, 버튼·입력·배지·진행률의 실제 조정 예제를 제공합니다.

## 조사와 검증의 범위

105개 문서에 대해 고정 버전의 리소스 정의 881개(문자열 키 862개·복합 키 19개), 문자열 참조 방식, 명명된 Style, 템플릿 속성 연결과 고정 레이아웃·색상 값을 조사했습니다. 전체 정의와 위치는 customization-manifest.json·ResourceCatalog에 보관합니다. 목록에 있는 모든 내부 키가 버전 간 호환성을 보장하는 공식 API는 아닙니다. 모든 상태·운영체제의 시각 결과를 자동 검증했다는 뜻도 아닙니다. 자세한 재검사 방법은 [VALIDATION](VALIDATION.md)에 있습니다.

## 근거

- [WPF UI 4.3.0 Card 템플릿](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml)
- [Microsoft: XAML 리소스·조회 범위](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/systems/xaml-resources-overview)
- [Microsoft: Style·ControlTemplate](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/styles-templates-overview)
- [Microsoft: DP 값 우선순위](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/properties/dependency-property-value-precedence)
