# RatingControl

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

별 아이콘으로 평점을 표시하고 입력받습니다.

**타입:** `Wpf.Ui.Controls.RatingControl` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:RatingControl x:Name="Demo" MaxRating="5" Value="3.5" HalfStarEnabled="True" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Value = 4;
Demo.HalfStarEnabled = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Value` | `double` | 읽기·쓰기 | `0.0D` | 별점 값입니다. `HalfStarEnabled`와 `MaxRating`을 함께 설정합니다. 기본 구현의 클릭 처리와 사용자 코드의 범위 검증을 구별합니다. |
| `MaxRating` | `int` | 읽기·쓰기 | `5` | 표시할 별 개수입니다. 양수로 설정하며 별 개수가 늘면 가로 공간도 더 필요합니다. |
| `HalfStarEnabled` | `bool` | 읽기·쓰기 | `true` | 반 개 단위 별점 입력을 허용할지 정합니다. `false`이면 사용자의 별 선택은 정수 단위가 됩니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 이 컨트롤의 Resources에서 바꾸기

`TextFillColorPrimaryBrush`는 `SolidColorBrush` 타입의 DynamicResource 참조입니다. 아래는 해당 키가 참조되는 기본 템플릿·상태에 적용하는 예제입니다. 기존 로컬 속성값·사용자 Style이 이 경로를 대체했다면 해당 설정도 확인합니다.

<!-- customization:example RatingControl_Resources -->
```xml
<ui:RatingControl MaxRating="5" Value="3.5" HalfStarEnabled="True"  x:Name="ResourceDemo">
    <ui:RatingControl.Resources>
        <SolidColorBrush x:Key="TextFillColorPrimaryBrush" Color="#2563EB" />
    </ui:RatingControl.Resources>
</ui:RatingControl>
```

```csharp
ResourceDemo.Resources["TextFillColorPrimaryBrush"] = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(37, 99, 235));
```

<!-- customization:example-end -->

C# 조각은 위 XAML과 같은 창·뷰에서 실행합니다. Resources에 넣는 값의 **타입**을 유지해야 합니다. 자식 컨트롤도 같은 키를 조회하면 영향을 받을 수 있습니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `DefaultControlFocusVisualStyle` | Style | 컨트롤.FocusVisualStyle |
| `RatingControlSelectedForeground` | SolidColorBrush | 컨트롤.Foreground |
| `TextFillColorPrimaryBrush` | SolidColorBrush | ContentPresenter TextElement.Foreground |

### 템플릿을 바꿀 때 유지할 연결

C# 구현이 이름으로 찾는 부분: `PART_Star1`, `PART_Star2`, `PART_Star3`, `PART_Star4`, `PART_Star5`. 이름과 요소 타입·명령·이벤트 연결을 함께 유지합니다.

원본 템플릿에 정의된 PART: `PART_Star1` (SymbolIcon), `PART_Star2` (SymbolIcon), `PART_Star3` (SymbolIcon), `PART_Star4` (SymbolIcon), `PART_Star5` (SymbolIcon). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `HorizontalContentAlignment` | `Grid#StarsContainer.HorizontalAlignment` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `VerticalContentAlignment` | `Grid#StarsContainer.VerticalAlignment` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `FontSize` | `SymbolIcon#PART_Star1.FontSize` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Foreground` | `SymbolIcon#PART_Star1.Foreground` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `FontSize` | `SymbolIcon#PART_Star2.FontSize` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Foreground` | `SymbolIcon#PART_Star2.Foreground` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `FontSize` | `SymbolIcon#PART_Star3.FontSize` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Foreground` | `SymbolIcon#PART_Star3.Foreground` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `FontSize` | `SymbolIcon#PART_Star4.FontSize` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Foreground` | `SymbolIcon#PART_Star4.Foreground` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `FontSize` | `SymbolIcon#PART_Star5.FontSize` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Foreground` | `SymbolIcon#PART_Star5.Foreground` | TemplateBinding | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.FontSize` | `20` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `Grid#ContentGrid.Margin` | `8,0,0,0` | 직접 지정 / 현재 템플릿 | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |
| `ContentGrid.Margin` | `0` | Content={x:Null} | [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{DynamicResource DefaultControlFocusVisualStyle}` | 암시적 스타일 |
| `Foreground` | `{DynamicResource RatingControlSelectedForeground}` | 암시적 스타일 |
| `FontSize` | `20` | 암시적 스타일 |
| `HorizontalAlignment` | `Left` | 암시적 스타일 |
| `VerticalAlignment` | `Center` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Center` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |
| `Margin` | `0` | 암시적 스타일 |
| `Padding` | `0` | 암시적 스타일 |

## 이벤트

| 이벤트 | 동작 |
| --- | --- |
| `ValueChanged` | 숫자·별점 값 변경을 알립니다. 현재 값은 컨트롤의 `Value`를 읽습니다. |

## 동작과 주의 사항

표시할 별 개수와 값 범위를 앱에서 일관되게 관리합니다. 값 변경은 `ValueChanged`로 관찰합니다. `Content`를 일반 본문 슬롯처럼 사용하기보다 기본 별점 템플릿을 유지합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [RatingControl.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.cs)
- [RatingControl.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RatingControl/RatingControl.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
