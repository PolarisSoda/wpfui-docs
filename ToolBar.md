# ToolBar

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

작업 버튼을 묶어 표시하는 도구 모음입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ToolBar x:Name="Demo"><Button Content="열기" /><Button Content="저장" /></ToolBar>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Items.Add(new ui.Button { Content = "내보내기" });
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Items` | `ItemCollection` | 직접 선언한 항목 컬렉션입니다. ItemsSource와 동시에 항목을 직접 추가하지 않습니다. |
| `ItemsSource` | `IEnumerable` | 목록의 데이터 공급원입니다. 변경 통지는 ObservableCollection을 사용합니다. |
| `ItemTemplate` | `DataTemplate` | 각 데이터 항목의 화면 구성을 정의합니다. |
| `ItemContainerStyle` | `Style` | 생성되는 항목 컨테이너의 스타일입니다. |
| `ItemsPanel` | `ItemsPanelTemplate` | 항목들을 배치하는 패널입니다. |
| `DisplayMemberPath` | `string` | 객체 중 문자열로 표시할 멤버 이름입니다. ItemTemplate와 용도를 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 문자열이 아닌 ToolBar.ButtonStyleKey로 자식 버튼 스타일 지정

<!-- customization:example ToolBar_Recipe1 -->
```xml
<ToolBar>
    <ToolBar.Resources>
        <Style x:Key="{x:Static ToolBar.ButtonStyleKey}"
               TargetType="{x:Type Button}"
               BasedOn="{StaticResource {x:Type Button}}">
            <Setter Property="MinWidth" Value="100" />
        </Style>
    </ToolBar.Resources>
    <Button Content="저장" />
</ToolBar>
```

<!-- customization:example-end -->

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlFillColorDefault` | Color | SolidColorBrush Color |
| `MenuBorderColorDefaultBrush` | **정의 없음** | Border#DropDownBorder BorderBrush |
| `SystemFillColorSolidNeutralBackground` | Color | SolidColorBrush Color |
| `TextFillColorTertiary` | Color | SolidColorBrush Color |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `ToolBarButtonBaseStyle` | Style | Style BasedOn |
| `ToolBarOverflowButtonStyle` | Style | ToggleButton Style |
| `ToolBarThumbStyle` | Style | Thumb#ToolBarThumb Style |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `{x:Type ToolBar}` | `ToolBar` | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

`{x:Static ...}`·`{x:Type ...}` 형태는 문자열 키가 아닌 객체 키입니다. 예를 들어 ToolBar.ButtonStyleKey를 읽을 때는 `Style="{StaticResource {x:Static ToolBar.ButtonStyleKey}}"`처럼 중첩 마크업을 사용합니다. 일반 문자열처럼 같은 이름을 추가하는 방식과 다릅니다. [복합 키 사용 예](CustomizationGuide.md)를 확인합니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_ToolBarOverflowPanel` (ToolBarOverflowPanel), `PART_ToolBarPanel` (ToolBarPanel). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Background` | `Border#Border.Background` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `BorderBrush` | `Border#Border.BorderBrush` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `BorderThickness` | `Border#Border.BorderThickness` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `HasOverflowItems` | `ToggleButton.IsEnabled` | TemplateBinding | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `컨트롤.BorderThickness` | `0` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#Border.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#DropDownBorder.Margin` | `12,0,12,18` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#DropDownBorder.Padding` | `0,3,0,3` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#DropDownBorder.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Border#DropDownBorder.CornerRadius` | `8` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `ToolBarOverflowPanel#PART_ToolBarOverflowPanel.Margin` | `0` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `Thumb#ToolBarThumb.Width` | `10` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |
| `ToolBarPanel#PART_ToolBarPanel.Margin` | `0,1,2,2` | 직접 지정 / 현재 템플릿 | [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `Transparent` | {x:Type ToolBar} |
| `BorderBrush` | `Transparent` | {x:Type ToolBar} |
| `BorderThickness` | `0` | {x:Type ToolBar} |
| `SnapsToDevicePixels` | `True` | {x:Type ToolBar} |
| `OverridesDefaultStyle` | `True` | {x:Type ToolBar} |

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ToolBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolBar/ToolBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
