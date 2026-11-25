# GridViewColumnHeader

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

GridView 열의 헤더를 표시하고 크기 조절·클릭을 제공하는 기본 WPF 컨테이너입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<GridViewColumnHeader x:Name="Demo" Content="이름" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Content = "파일 이름";
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

### 재정의할 수 있는 동적 리소스

참조 위치가 보조 스타일·다른 상태에만 있으면 그 스타일·상태를 선택해야 효과가 납니다. 타입은 원본 정의에서 읽었으며 미정의 키는 정상 조정 키로 권장하지 않습니다.

| 키 | 타입 | 쓰이는 영역·조건 |
| --- | --- | --- |
| `ControlCornerRadius` | CornerRadius | Border CornerRadius |
| `ListViewItemBackgroundPointerOver` | SolidColorBrush | HeaderBorder.Background〔IsMouseOver=True〕 |
| `TextFillColorPrimaryBrush` | SolidColorBrush | 컨트롤.Foreground |

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `UiGridViewColumnHeaderStyle` | `GridViewColumnHeader` | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) · 내부 정의 |
| (Style 내부 템플릿) | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `ActualWidth` | `Rectangle.Width` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `ActualHeight` | `Rectangle.Height` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Background` | `Border.Background` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Border.BorderBrush` | `Border.BorderBrush` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `BorderBrush` | `Border.BorderBrush` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Padding` | `Border.Padding` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `HorizontalContentAlignment` | `ContentPresenter.HorizontalAlignment` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `VerticalContentAlignment` | `ContentPresenter.VerticalAlignment` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Content` | `ContentPresenter.Content` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `ContentStringFormat` | `ContentPresenter.ContentStringFormat` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `ContentTemplate` | `ContentPresenter.ContentTemplate` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `SnapsToDevicePixels` | `ContentPresenter.SnapsToDevicePixels` | TemplateBinding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `Rectangle.Fill` | `#FF000000` | GridViewColumnHeader.Role=Floating | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Border.BorderThickness` | `0,0,0,0` | GridViewColumnHeader.Role=Padding | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `컨트롤.Background` | `Transparent` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `컨트롤.BorderThickness` | `0,0,0,0` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `컨트롤.Margin` | `0,0,0,0` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `컨트롤.Padding` | `0,2` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Border.BorderThickness` | `0,0,0,0` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `Border.Margin` | `6,0,0,0` | 직접 지정 / 현재 템플릿 | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `PART_HeaderGripper.Background` | `Transparent` | IsMouseOver=True | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |
| `HeaderBorder.Background` | `Transparent` | IsPressed=True | [GridViewColumnHeader.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/GridView/GridViewColumnHeader.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
