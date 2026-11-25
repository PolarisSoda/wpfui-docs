# DropDownButton

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

버튼을 눌러 선택 메뉴를 여는 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.DropDownButton` · **기반:** `Button`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:DropDownButton x:Name="Demo" Content="내보내기">
    <ui:DropDownButton.Flyout>
        <ContextMenu>
            <MenuItem Header="PDF" />
            <MenuItem Header="이미지" />
        </ContextMenu>
    </ui:DropDownButton.Flyout>
</ui:DropDownButton>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
var menu = (System.Windows.Controls.ContextMenu)Demo.Flyout!;
menu.PlacementTarget = Demo;
menu.IsOpen = true;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Flyout` | `object?` | 읽기·쓰기 | `null` | 4.3.0의 버튼 구현은 이 객체가 WPF `ContextMenu`일 때만 메뉴를 연결합니다. 이름이 Flyout이지만 `ui:Flyout`을 넣는 경로는 구현되어 있지 않습니다. |
| `IsDropDownOpen` | `bool` | 읽기·쓰기 | `false` | ContextMenu의 열림·닫힘 이벤트에 따라 갱신되는 상태입니다. 4.3.0에서는 이 값을 설정해도 메뉴를 여는 콜백이 없습니다. 코드로 열 때는 `(ContextMenu)Flyout`의 `IsOpen`과 `PlacementTarget`을 설정합니다. |

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

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

바깥 버튼은 Button 계열 스타일을 기반으로 하므로 상속된 CornerRadius·Appearance를 우선 사용하고 공통 키는 Button 문서도 확인합니다. Flyout에 연결하는 ContextMenu는 별도 팝업이므로 메뉴 색은 ContextMenu.Resources에서 조정합니다. 메뉴 위치를 바꾸려면 버튼 코드의 Placement.Bottom 설정과도 충돌하는지 확인합니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlStrokeColorDefaultBrush`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example DropDownButton_Resources -->
```xml
<ui:DropDownButton Content="내보내기" x:Name="ResourceDemo">
    <ui:DropDownButton.Resources>
        <SolidColorBrush x:Key="ControlStrokeColorDefaultBrush" Color="#2563EB" />
    </ui:DropDownButton.Resources>
    <ui:DropDownButton.Flyout>
        <ContextMenu>
            <MenuItem Header="PDF" />
            <MenuItem Header="이미지" />
        </ContextMenu>
    </ui:DropDownButton.Flyout>
</ui:DropDownButton>
```

```csharp
ResourceDemo.Resources["ControlStrokeColorDefaultBrush"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlFillColorDisabledBrush` | SolidColorBrush | ContentBorder.Background〔IsEnabled=False〕 |
| `ControlStrokeColorDefaultBrush` | SolidColorBrush | ContentBorder.BorderBrush〔IsEnabled=False〕 |
| `TextFillColorDisabledBrush` | SolidColorBrush | ContentPresenter.TextElement.Foreground〔IsEnabled=False〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ButtonChevronIconMargin` | Thickness | Grid Margin |
| `ButtonIconMargin` | Thickness | ContentPresenter#ControlIcon Margin |
| `DefaultUiButtonStyle` | Style | Style BasedOn |
| `DefaultUiDropDownButtonStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiDropDownButtonStyle` | `controls:DropDownButton` | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Width` | `Border#ContentBorder.Width` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Height` | `Border#ContentBorder.Height` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `MinWidth` | `Border#ContentBorder.MinWidth` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `MinHeight` | `Border#ContentBorder.MinHeight` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `HorizontalAlignment` | `Border#ContentBorder.HorizontalAlignment` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `VerticalAlignment` | `Border#ContentBorder.VerticalAlignment` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Background` | `Border#ContentBorder.Background` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `CornerRadius` | `Border#ContentBorder.CornerRadius` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Padding` | `Border.Padding` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `BorderThickness` | `Border.BorderThickness` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `CornerRadius` | `Border.CornerRadius` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `HorizontalContentAlignment` | `Grid.HorizontalAlignment` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `VerticalContentAlignment` | `Grid.VerticalAlignment` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Icon` | `ContentPresenter#ControlIcon.Content` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `ContentTemplate` | `ContentPresenter#ControlIcon.ContentTemplate` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `FontSize` | `ContentPresenter#ControlIcon.TextElement.FontSize` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Foreground` | `ContentPresenter#ControlIcon.TextElement.Foreground` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `Foreground` | `ContentPresenter#ContentPresenter.TextElement.Foreground` | TemplateBinding | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `SymbolIcon.FontSize` | `10` | 직접 지정 / 현재 템플릿 | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `ControlIcon.Margin` | `0` | Content={x:Null} | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `ControlIcon.Margin` | `0` | Content= | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |
| `ControlIcon.Margin` | `0` | Icon={x:Null} | [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `IsDropDownOpen` | `False` | DefaultUiDropDownButtonStyle |

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

4.3.0의 `Flyout` 처리 코드는 `ContextMenu`만 연결합니다. `ui:Flyout` 객체를 넣어도 같은 동작을 하지 않습니다. `IsDropDownOpen=true`만 지정해서 메뉴를 여는 구현도 없습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [DropDownButton.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.cs)
- [DropDownButton.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DropDownButton/DropDownButton.xaml)
- [Gallery: DropDownButtonPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/DropDownButtonPage.xaml)
