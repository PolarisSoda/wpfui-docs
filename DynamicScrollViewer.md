# DynamicScrollViewer

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

스크롤 활동에 따라 스크롤바 상태를 바꾸는 PassiveScrollViewer 파생형입니다.

**타입:** `Wpf.Ui.Controls.DynamicScrollViewer` · **기반:** `PassiveScrollViewer`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:DynamicScrollViewer x:Name="Demo" Height="180" Timeout="1200" VerticalScrollBarVisibility="Auto"><TextBlock Height="600" Text="스크롤할 콘텐츠" /></ui:DynamicScrollViewer>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Timeout = 1500;
Demo.ScrollToVerticalOffset(100);
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsScrollingVertically` | `bool` | 읽기·쓰기 | `false` | 세로 스크롤 활동 상태입니다. 자동 스크롤바 표시를 위해 컨트롤이 갱신합니다. |
| `IsScrollingHorizontally` | `bool` | 읽기·쓰기 | `false` | 가로 스크롤 활동 상태입니다. |
| `MinimalChange` | `double` | 읽기·쓰기 | `40d` | 스크롤 변화량의 활동 감지 기준입니다. 작게 하면 작은 변화도 활동으로 처리합니다. 컨텐츠의 최소 이동 단위를 설정하는 속성은 아닙니다. |
| `Timeout` | `int` | 읽기·쓰기 | `1200` | 스크롤 활동 상태를 유지하는 시간(밀리초)입니다. |

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `IsScrollSpillEnabled` | [PassiveScrollViewer](PassiveScrollViewer.md) | 내부 스크롤이 끝에 도달했을 때 마우스 휠을 상위 스크롤 뷰어로 전달할지 정합니다. 중첩 스크롤의 휠 막힘을 조정합니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `VerticalScrollBarVisibility / HorizontalScrollBarVisibility` | `ScrollBarVisibility` | Disabled·Auto·Hidden·Visible 중 방향별 스크롤바 정책입니다. |
| `CanContentScroll` | `bool` | IScrollInfo를 구현하는 콘텐츠에 논리적 스크롤을 위임할지 정합니다. 가상화 패널 구성에서 중요합니다. |
| `VerticalOffset / HorizontalOffset` | `double (읽기)` | 현재 위치입니다. ScrollToVerticalOffset·ScrollToHorizontalOffset으로 이동을 요청합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `UiDynamicScrollViewer` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `UiDynamicScrollViewer` | `controls:DynamicScrollViewer` | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_HorizontalScrollBar` (DynamicScrollBar), `PART_VerticalScrollBar` (DynamicScrollBar). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| (Style 내부 템플릿) | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) · 내부 정의 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `Border.Padding` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `CanContentScroll` | `ScrollContentPresenter.CanContentScroll` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `IsScrollingVertically` | `DynamicScrollBar#PART_VerticalScrollBar.IsScrolling` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ScrollableHeight` | `DynamicScrollBar#PART_VerticalScrollBar.Maximum` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ViewportHeight` | `DynamicScrollBar#PART_VerticalScrollBar.ViewportSize` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ComputedVerticalScrollBarVisibility` | `DynamicScrollBar#PART_VerticalScrollBar.Visibility` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `VerticalOffset` | `DynamicScrollBar#PART_VerticalScrollBar.Value` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `IsScrollingHorizontally` | `DynamicScrollBar#PART_HorizontalScrollBar.IsScrolling` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ScrollableWidth` | `DynamicScrollBar#PART_HorizontalScrollBar.Maximum` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ViewportWidth` | `DynamicScrollBar#PART_HorizontalScrollBar.ViewportSize` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ComputedHorizontalScrollBarVisibility` | `DynamicScrollBar#PART_HorizontalScrollBar.Visibility` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `HorizontalOffset` | `DynamicScrollBar#PART_HorizontalScrollBar.Value` | TemplateBinding | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |

</details>

<details>
<summary>템플릿·상태 트리거의 고정값 — 리소스 변경으로 바뀌지 않는 부분</summary>

| 위치 | 고정값 | 적용 조건 | 정의 |
| --- | --- | --- | --- |
| `컨트롤.Margin` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `컨트롤.Padding` | `0` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ColumnDefinition.Width` | `*` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `ColumnDefinition.Width` | `Auto` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `RowDefinition.Height` | `*` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |
| `RowDefinition.Height` | `Auto` | 직접 지정 / 현재 템플릿 | [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml) |

표는 고정값이 있다는 근거입니다. 컨트롤 자체의 로컬 속성으로 덮을 수 있는 최상위 Setter와 내부 요소·트리거의 값을 구분합니다. `RadiusX`·`RadiusY`는 Rectangle의 반지름이며 Border.CornerRadius와 다른 속성입니다.

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Margin` | `0` | UiDynamicScrollViewer |
| `Padding` | `0` | UiDynamicScrollViewer |
| `VerticalScrollBarVisibility` | `Auto` | UiDynamicScrollViewer |
| `HorizontalScrollBarVisibility` | `Disabled` | UiDynamicScrollViewer |
| `PanningMode` | `Both` | UiDynamicScrollViewer |
| `SnapsToDevicePixels` | `True` | UiDynamicScrollViewer |
| `OverridesDefaultStyle` | `True` | UiDynamicScrollViewer |

## 동작과 주의 사항

Timeout은 밀리초이며 0 이상 10000 미만의 실용적인 값을 사용합니다. 소스는 지나치게 큰 값을 1000ms 경로로 처리합니다. 가상화 목록을 외부 ScrollViewer로 다시 감싸지 않습니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [DynamicScrollViewer.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.cs)
- [DynamicScrollViewer.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DynamicScrollViewer/DynamicScrollViewer.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
