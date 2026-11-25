# ListViewItem

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

ListView가 선택·포커스·콘텐츠 표시를 위해 생성하는 항목 컨테이너입니다.

**타입:** `Wpf.Ui.Controls.ListViewItem` · **기반:** `System.Windows.Controls.ListViewItem`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ListViewItem x:Name="Demo" Content="문서 A" IsSelected="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Content = "문서 B";
Demo.IsSelected = false;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `IsSelected` | `bool` | 소유 목록에서 이 항목의 선택 여부입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

선택·포인터 강조 색과 왼쪽 선택 표시 막대는 ListViewItem 계열 리소스에 연결됩니다. ControlCornerRadius는 이 항목 컨테이너에 적용하는 것이며 소유 ListView 자체의 반지름과 다릅니다. 데이터 목록에서는 ItemContainerStyle을 사용합니다. GridView 모드와 일반 목록 모드의 템플릿도 구분합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlCornerRadius`는 `CornerRadius` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ListViewItem_Resources -->
```xml
<ui:ListViewItem Content="문서 A" IsSelected="True"  x:Name="ResourceDemo">
    <ui:ListViewItem.Resources>
        <CornerRadius x:Key="ControlCornerRadius">12</CornerRadius>
    </ui:ListViewItem.Resources>
</ui:ListViewItem>
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
| `TextControlThemePadding` | Thickness | 컨트롤.Padding |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `FlyoutBackground` | SolidColorBrush | Border Background |
| `FlyoutBorderBrush` | SolidColorBrush | Border BorderBrush |
| `GridViewItemTemplate` | ControlTemplate | 컨트롤.Template〔{Binding Path=ViewState, RelativeSource={RelativeSource AncestorType={x:Type ListView}}}=GridView〕 |
| `ListViewItemBackgroundPointerOver` | SolidColorBrush | Border.Background〔IsEnabled=True; IsMouseOver=True〕 / Border.Background〔IsSelected=True〕 / ContentBorder.Background〔IsSelected=True〕 / ContentBorder.Background〔IsSelected=False; IsMouseOver=True〕 |
| `ListViewItemForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ListViewItemPillFillBrush` | SolidColorBrush | Rectangle#ActiveRectangle Fill |
| `NullViewItemTemplate` | ControlTemplate | 컨트롤.Template〔{Binding Path=ViewState, RelativeSource={RelativeSource AncestorType={x:Type ListView}}}=Default〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `AutoSuggestBoxBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `DefaultAutoSuggestBoxItemContainerStyle` | Style | 컨트롤.ItemContainerStyle |
| `DefaultUiAutoSuggestBoxStyle` | Style | Style BasedOn |
| `ListViewItemStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultAutoSuggestBoxItemContainerStyle` | `controls:ListViewItem` | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `ListViewItemStyle` | `controls:ListViewItem` | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `NullViewItemTemplate` | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) · 사전 루트 |
| `GridViewItemTemplate` | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Border#Border.Background` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Border.CornerRadius` | `Border#Border.CornerRadius` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Padding` | `ContentPresenter.Margin` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Border.BorderBrush` | `Border#Border.BorderBrush` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Border.BorderThickness` | `Border#Border.BorderThickness` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Padding` | `GridViewRowPresenter.Margin` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Control.VerticalContentAlignment` | `GridViewRowPresenter.VerticalAlignment` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `GridView.ColumnCollection` | `GridViewRowPresenter.Columns` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `ContentControl.Content` | `GridViewRowPresenter.Content` | TemplateBinding | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `컨트롤.Margin` | `0,0,0,2` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `컨트롤.Padding` | `4` | 직접 지정 / 현재 템플릿 | [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml) |
| `Border#Border.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Border#Border.Padding` | `0` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Border#Border.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Rectangle#ActiveRectangle.Width` | `3` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Rectangle#ActiveRectangle.Height` | `18` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Rectangle#ActiveRectangle.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Rectangle#ActiveRectangle.RadiusX` | `2` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `Rectangle#ActiveRectangle.RadiusY` | `2` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `컨트롤.Margin` | `0,0,0,2` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |
| `컨트롤.Padding` | `4` | 직접 지정 / 현재 템플릿 | [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Foreground` | `{DynamicResource ListViewItemForeground}` | DefaultAutoSuggestBoxItemContainerStyle |
| `Background` | `Transparent` | DefaultAutoSuggestBoxItemContainerStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | DefaultAutoSuggestBoxItemContainerStyle |
| `Margin` | `0,0,0,2` | DefaultAutoSuggestBoxItemContainerStyle |
| `Padding` | `4` | DefaultAutoSuggestBoxItemContainerStyle |
| `OverridesDefaultStyle` | `True` | DefaultAutoSuggestBoxItemContainerStyle |
| `Foreground` | `{DynamicResource ListViewItemForeground}` | ListViewItemStyle |
| `Background` | `Transparent` | ListViewItemStyle |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | ListViewItemStyle |
| `Margin` | `0,0,0,2` | ListViewItemStyle |
| `Padding` | `4` | ListViewItemStyle |

## 동작과 주의 사항

ItemsSource를 사용하는 목록에서는 항목 객체와 컨테이너를 구별합니다. 대부분 ItemContainerStyle로 외형을 설정합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ListViewItem.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.cs)
- [AutoSuggestBox.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/AutoSuggestBox/AutoSuggestBox.xaml)
- [ListViewItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ListView/ListViewItem.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
