# ToolTip

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

포인터가 머무를 때 표시하는 짧은 도움말입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Button x:Name="Demo" Content="저장"><Button.ToolTip><ToolTip Content="변경한 내용을 저장합니다." /></Button.ToolTip></Button>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.ToolTip = "Ctrl+S로도 저장할 수 있습니다.";
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Placement` | `PlacementMode` | 도움말 위치입니다. |
| `IsOpen` | `bool` | 도움말 표시 여부입니다. |
| `StaysOpen` | `bool` | 열림 상태 유지 정책입니다. 호스트의 ToolTipService 속성으로 지연·표시 시간을 구성할 수 있습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

ToolTipBackground·ToolTipBorderBrush·ToolTipForeground는 팝업 도움말의 색입니다. 버튼 Resources 범위와 팝업 범위에 의존하기보다 ToolTip 객체의 Resources에 조정 키를 두는 방법을 사용합니다. 표시 지연·지속 시간은 ToolTipService의 붙임 속성입니다.

### 이 컨트롤의 Resources에서 바꾸기

`ToolTipBackground`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example ToolTip_Resources -->
```xml
<Button x:Name="Demo" Content="저장"><Button.ToolTip><ToolTip Content="변경한 내용을 저장합니다."  x:Name="ResourceDemo">
    <ToolTip.Resources>
        <SolidColorBrush x:Key="ToolTipBackground" Color="#2563EB" />
    </ToolTip.Resources>
</ToolTip></Button.ToolTip></Button>
```

```csharp
ResourceDemo.Resources["ToolTipBackground"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ToolTipBackground` | SolidColorBrush | 컨트롤.Background |
| `ToolTipBorderBrush` | SolidColorBrush | 컨트롤.BorderBrush |
| `ToolTipForeground` | SolidColorBrush | 컨트롤.TextElement.Foreground / 컨트롤.Foreground |

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultToolTipStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultToolTipStyle` | `ToolTip` | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Width` | `Border.Width` | TemplateBinding | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `Height` | `Border.Height` | TemplateBinding | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `MaxWidth` | `Border.MaxWidth` | TemplateBinding | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `Background` | `Border.Background` | TemplateBinding | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.MaxWidth` | `260` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `컨트롤.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `컨트롤.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `Border.Padding` | `8` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `Border.BorderThickness` | `1` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `Border.CornerRadius` | `4` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |
| `ContentPresenter.Margin` | `4` | 직접 지정 / 현재 템플릿 | [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `MaxWidth` | `260` | DefaultToolTipStyle |
| `Height` | `Auto` | DefaultToolTipStyle |
| `Width` | `Auto` | DefaultToolTipStyle |
| `TextElement.FontSize` | `12` | DefaultToolTipStyle |
| `TextElement.FontWeight` | `Normal` | DefaultToolTipStyle |
| `TextBlock.LineHeight` | `16` | DefaultToolTipStyle |
| `TextBlock.TextAlignment` | `Justify` | DefaultToolTipStyle |
| `TextElement.Foreground` | `{DynamicResource ToolTipForeground}` | DefaultToolTipStyle |
| `Foreground` | `{DynamicResource ToolTipForeground}` | DefaultToolTipStyle |
| `Background` | `{DynamicResource ToolTipBackground}` | DefaultToolTipStyle |
| `BorderBrush` | `{DynamicResource ToolTipBorderBrush}` | DefaultToolTipStyle |
| `SnapsToDevicePixels` | `True` | DefaultToolTipStyle |
| `OverridesDefaultStyle` | `True` | DefaultToolTipStyle |

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [ToolTip.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ToolTip/ToolTip.xaml)
- [Gallery: ToolTipPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/StatusAndInfo/ToolTipPage.xaml)
