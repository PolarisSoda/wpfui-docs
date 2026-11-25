# ToggleSwitch

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

설정을 켜고 끄는 스위치입니다. 상태별 라벨을 지원합니다.

**타입:** `Wpf.Ui.Controls.ToggleSwitch` · **기반:** `System.Windows.Controls.Primitives.ToggleButton`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:ToggleSwitch x:Name="Demo" IsChecked="True" OnContent="알림 켜짐" OffContent="알림 꺼짐" LabelPosition="Right" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.IsChecked = false;
Demo.OffContent = "알림 받지 않음";
Demo.LabelPosition = ui.ElementPlacement.Left;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `OffContent` | `object?` | 읽기·쓰기 | `null` | 꺼짐(`IsChecked=false`) 상태의 라벨입니다. `Content`가 비어 있을 때 기본 템플릿이 사용합니다. |
| `OnContent` | `object?` | 읽기·쓰기 | `null` | 켜짐(`IsChecked=true`) 상태의 라벨입니다. 고정 `Content`를 지정하면 상태별 라벨보다 우선합니다. |
| `LabelPosition` | `ElementPlacement` | 읽기·쓰기 | `ElementPlacement.Right` | 라벨을 스위치 왼쪽(`Left`) 또는 오른쪽(`Right`)에 둡니다. 기본 템플릿은 두 위치에 따라 열과 라벨 여백을 바꿉니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `IsChecked` | `bool?` | true=선택, false=해제, null=미정 상태입니다. 바인딩 시 Mode=TwoWay를 명시할 수 있습니다. |
| `IsThreeState` | `bool` | 사용자 조작으로 미정 상태까지 순환할지 정합니다. |
| `Command / CommandParameter` | `ICommand / object` | 토글 시 실행할 명령과 전달 값입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

### 선택 가능한 값

- `ElementPlacement`: `Left`, `Right`.

열거형 이름이 비슷해도 다른 타입일 수 있습니다. [열거형 안내](Enums.md)에서 의미를 비교할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

켜짐·꺼짐·포인터·눌림·비활성 상태마다 Fill·KnobFill 리소스가 다릅니다. 색 변경은 이 상태 키를 사용하고, 라벨 위치는 LabelPosition으로 설정합니다. 스위치 트랙·손잡이 크기와 모서리는 템플릿의 고정값이므로 ControlCornerRadius를 재정의하는 방식으로 스위치 형태가 바뀌는 것은 아닙니다.

### 이 컨트롤의 Resources에서 바꾸기

`ControlContentThemeFontSize`는 `Double` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ToggleSwitch_Resources -->
```xml
<ui:ToggleSwitch IsChecked="True" OnContent="알림 켜짐" OffContent="알림 꺼짐" LabelPosition="Right"  x:Name="ResourceDemo" xmlns:system="clr-namespace:System;assembly=System.Runtime">
    <ui:ToggleSwitch.Resources>
        <system:Double x:Key="ControlContentThemeFontSize">18</system:Double>
    </ui:ToggleSwitch.Resources>
</ui:ToggleSwitch>
```

```csharp
ResourceDemo.Resources["ControlContentThemeFontSize"] = 18d;
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 켜짐·꺼짐 트랙 색 조정

<!-- customization:example ToggleSwitch_Recipe1 -->
```xml
<ui:ToggleSwitch IsChecked="True" OnContent="켜짐" OffContent="꺼짐">
    <ui:ToggleSwitch.Resources>
        <SolidColorBrush x:Key="ToggleSwitchFillOn" Color="#2563EB" />
        <SolidColorBrush x:Key="ToggleSwitchFillOff" Color="#CBD5E1" />
    </ui:ToggleSwitch.Resources>
</ui:ToggleSwitch>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlContentThemeFontSize` | Double | 컨트롤.FontSize |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `ToggleSwitchContentForeground` | SolidColorBrush | 컨트롤.Foreground |
| `ToggleSwitchContentForegroundDisabled` | SolidColorBrush | 컨트롤.Foreground〔IsChecked=False; IsEnabled=False〕 / 컨트롤.Foreground〔IsChecked=True; IsEnabled=False〕 |
| `ToggleSwitchFillOff` | SolidColorBrush | Rectangle#ToggleRectangle Fill |
| `ToggleSwitchFillOffDisabled` | SolidColorBrush | ToggleRectangle.Fill〔IsChecked=False; IsEnabled=False〕 |
| `ToggleSwitchFillOffPointerOver` | SolidColorBrush | ToggleRectangle.Fill〔IsMouseOver=True; IsPressed=False; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchFillOffPressed` | SolidColorBrush | ToggleRectangle.Fill〔IsMouseOver=True; IsPressed=True; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchFillOn` | SolidColorBrush | 컨트롤.Background |
| `ToggleSwitchFillOnDisabled` | SolidColorBrush | ActiveToggleRectangle.Fill〔IsChecked=True; IsEnabled=False〕 |
| `ToggleSwitchFillOnPointerOver` | SolidColorBrush | 컨트롤.Background〔IsMouseOver=True; IsPressed=False; IsChecked=True; IsEnabled=True〕 |
| `ToggleSwitchFillOnPressed` | SolidColorBrush | 컨트롤.Background〔IsMouseOver=True; IsPressed=True; IsChecked=True; IsEnabled=True〕 |
| `ToggleSwitchKnobFillOff` | SolidColorBrush | Rectangle#ToggleEllipse Fill |
| `ToggleSwitchKnobFillOffDisabled` | SolidColorBrush | ToggleEllipse.Fill〔IsChecked=False; IsEnabled=False〕 |
| `ToggleSwitchKnobFillOffPointerOver` | SolidColorBrush | ToggleEllipse.Fill〔IsMouseOver=True; IsPressed=False; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchKnobFillOffPressed` | SolidColorBrush | ToggleEllipse.Fill〔IsMouseOver=True; IsPressed=True; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchKnobFillOn` | SolidColorBrush | Rectangle#ActiveToggleEllipse Fill |
| `ToggleSwitchKnobFillOnDisabled` | SolidColorBrush | ActiveToggleEllipse.Fill〔IsChecked=True; IsEnabled=False〕 |
| `ToggleSwitchKnobFillOnPointerOver` | SolidColorBrush | ActiveToggleEllipse.Fill〔IsMouseOver=True; IsPressed=False; IsChecked=True; IsEnabled=True〕 |
| `ToggleSwitchKnobFillOnPressed` | SolidColorBrush | ActiveToggleEllipse.Fill〔IsMouseOver=True; IsPressed=True; IsChecked=True; IsEnabled=True〕 |
| `ToggleSwitchStrokeOff` | SolidColorBrush | Rectangle#ToggleRectangle Stroke |
| `ToggleSwitchStrokeOffDisabled` | SolidColorBrush | ToggleRectangle.Stroke〔IsChecked=False; IsEnabled=False〕 |
| `ToggleSwitchStrokeOffPointerOver` | SolidColorBrush | ToggleRectangle.Stroke〔IsMouseOver=True; IsPressed=False; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchStrokeOffPressed` | SolidColorBrush | ToggleRectangle.Stroke〔IsMouseOver=True; IsPressed=True; IsChecked=False; IsEnabled=True〕 |
| `ToggleSwitchStrokeOnPointerOver` | SolidColorBrush | ToggleRectangle.Stroke〔IsMouseOver=True; IsPressed=False; IsChecked=True; IsEnabled=True〕 |
| `ToggleSwitchStrokeOnPressed` | SolidColorBrush | ToggleRectangle.Stroke〔IsMouseOver=True; IsPressed=True; IsChecked=True; IsEnabled=True〕 |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultUiToggleSwitchStyle` | Style | Style BasedOn |
| `ToggleButtonHeight` | Double | Grid#ToggleGrid Height / Rectangle#ToggleRectangle Height / Rectangle#ActiveToggleRectangle Height |
| `ToggleButtonWidth` | Double | Grid#ToggleGrid Width / Rectangle#ToggleRectangle Width / Rectangle#ActiveToggleRectangle Width |
| `ToggleSwitchBorderThemeThickness` | Thickness | 컨트롤.BorderThickness |
| `ToggleSwitchContentMargin` | Thickness | ContentPresenter#ContentPresenter Margin |
| `ToggleSwitchPadding` | Thickness | 컨트롤.Padding |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiToggleSwitchStyle` | `controls:ToggleSwitch` | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `Grid.Margin` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Background` | `Rectangle#ActiveToggleRectangle.Fill` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter#ContentPresenter.HorizontalAlignment` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `VerticalContentAlignment` | `ContentPresenter#ContentPresenter.VerticalAlignment` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Content` | `ContentPresenter#ContentPresenter.Content` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ContentTemplate` | `ContentPresenter#ContentPresenter.ContentTemplate` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Foreground` | `ContentPresenter#ContentPresenter.TextElement.Foreground` | TemplateBinding | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Grid.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ColumnDefinition#ToggleColumn.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ColumnDefinition#ContentColumn.Width` | `*` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleRectangle.RadiusX` | `10` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleRectangle.RadiusY` | `10` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleRectangle.StrokeThickness` | `1` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleRectangle.RadiusX` | `10` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleRectangle.RadiusY` | `10` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleRectangle.StrokeThickness` | `0` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleEllipse.Width` | `12` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleEllipse.Height` | `12` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleEllipse.RadiusX` | `7` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleEllipse.RadiusY` | `7` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ToggleEllipse.StrokeThickness` | `0` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleEllipse.Width` | `12` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleEllipse.Height` | `12` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleEllipse.RadiusX` | `7` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleEllipse.RadiusY` | `7` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `Rectangle#ActiveToggleEllipse.StrokeThickness` | `0` | 직접 지정 / 현재 템플릿 | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ContentPresenter.Margin` | `0,0,8,0` | LabelPosition=Left | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ContentPresenter.Margin` | `8,0,0,0` | LabelPosition=Right | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ContentPresenter.Margin` | `0` | Content={x:Null}; OnContent={x:Null}; OffContent={x:Null} | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ContentPresenter.Margin` | `0` | Content=; OnContent=; OffContent= | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ToggleEllipse.Height` | `14` | IsMouseOver=True | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ToggleEllipse.Width` | `14` | IsMouseOver=True | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ActiveToggleEllipse.Height` | `14` | IsMouseOver=True | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ActiveToggleEllipse.Width` | `14` | IsMouseOver=True | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ToggleEllipse.Width` | `17` | IsPressed=True; IsChecked=False | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |
| `ActiveToggleEllipse.Width` | `17` | IsPressed=True; IsChecked=True | [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | DefaultUiToggleSwitchStyle |
| `Background` | `{DynamicResource ToggleSwitchFillOn}` | DefaultUiToggleSwitchStyle |
| `Foreground` | `{DynamicResource ToggleSwitchContentForeground}` | DefaultUiToggleSwitchStyle |
| `BorderBrush` | `Transparent` | DefaultUiToggleSwitchStyle |
| `BorderThickness` | `{StaticResource ToggleSwitchBorderThemeThickness}` | DefaultUiToggleSwitchStyle |
| `Padding` | `{StaticResource ToggleSwitchPadding}` | DefaultUiToggleSwitchStyle |
| `HorizontalAlignment` | `Left` | DefaultUiToggleSwitchStyle |
| `VerticalAlignment` | `Center` | DefaultUiToggleSwitchStyle |
| `LabelPosition` | `Right` | DefaultUiToggleSwitchStyle |
| `HorizontalContentAlignment` | `Left` | DefaultUiToggleSwitchStyle |
| `VerticalContentAlignment` | `Center` | DefaultUiToggleSwitchStyle |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | DefaultUiToggleSwitchStyle |
| `FontWeight` | `Normal` | DefaultUiToggleSwitchStyle |
| `SnapsToDevicePixels` | `True` | DefaultUiToggleSwitchStyle |
| `OverridesDefaultStyle` | `True` | DefaultUiToggleSwitchStyle |

상속 이벤트: `Click` · `Checked` · `Unchecked` · `Indeterminate`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

## 동작과 주의 사항

`Content`에 고정 문자열을 넣으면 `OnContent`·`OffContent`보다 우선합니다. 상태를 ViewModel에 저장하려면 `IsChecked="{Binding NotificationsEnabled, Mode=TwoWay}"`를 사용합니다. 이벤트는 `Checked`, `Unchecked`, `Indeterminate`를 상속합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ToggleSwitch.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.cs)
- [ToggleSwitch.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToggleSwitch/ToggleSwitch.xaml)
- [Gallery: ToggleSwitchPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/ToggleSwitchPage.xaml)
