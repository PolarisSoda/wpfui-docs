# NavigationViewContentPresenter

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

NavigationView 내부에서 페이지와 전환 애니메이션을 표시하는 Frame 파생 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.NavigationViewContentPresenter` · **기반:** `Frame`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:NavigationViewContentPresenter x:Name="Demo" TransitionDuration="150" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Transition = Wpf.Ui.Animations.Transition.FadeIn;
Demo.Content = new System.Windows.Controls.TextBlock { Text = "본문" };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `TransitionDuration` | `int` | 읽기·쓰기 | `200` | 화면 전환 애니메이션의 시간(밀리초)입니다. 짧게 설정하면 더 빠르게 전환됩니다. |
| `Transition` | `Transition` | 읽기·쓰기 | `Transition.FadeInWithSlide` | 콘텐츠가 들어올 때 적용할 애니메이션 종류입니다. 열거형 `Wpf.Ui.Animations.Transition`을 사용합니다. |
| `IsDynamicScrollViewerEnabled` | `bool` | 외부 읽기 전용 | `true` | 기본 템플릿의 동적 스크롤 사용을 나타내는 상태입니다. CLR setter는 protected이므로 일반 설정 API로 취급하지 않습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |
| `Source` | `Uri` | 탐색할 페이지 URI입니다. |
| `NavigationUIVisibility` | `NavigationUIVisibility` | 기본 프레임 탐색 바 표시 정책입니다. |
| `CanGoBack / CanGoForward` | `bool (읽기)` | 프레임 자체의 탐색 저널 이동 가능 상태입니다. |
| `JournalOwnership` | `JournalOwnership` | 자체·부모 저널 사용 정책입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

IsDynamicScrollViewerEnabled에 따라 서로 다른 ControlTemplate을 선택합니다. 기본 Frame의 ContentTemplate을 바꾸는 것과 스크롤 컨테이너·전환 효과를 구성하는 ControlTemplate 교체를 구별합니다. 실제 앱에서는 상위 NavigationView 템플릿의 PART 연결을 유지합니다.

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultNavigationViewContentPresenterControlTemplate` | ControlTemplate | 컨트롤.Template〔IsDynamicScrollViewerEnabled=False〕 |
| `DefaultNavigationViewContentPresenterStyle` | Style | Style BasedOn |
| `DefaultNavigationViewContentPresenterWithDynamicScrollViewerControlTemplate` | ControlTemplate | 컨트롤.Template〔IsDynamicScrollViewerEnabled=True〕 |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultNavigationViewContentPresenterStyle` | `controls:NavigationViewContentPresenter` | [NavigationViewContentPresenter.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

### 템플릿을 바꿀 때 유지할 연결

원본 템플릿에 정의된 PART: `PART_FrameCP` (ContentPresenter). WPF 기반 클래스가 사용하는 연결도 보존합니다.

| 템플릿 키 | 소스·범위 |
| --- | --- |
| `DefaultNavigationViewContentPresenterControlTemplate` | [NavigationViewContentPresenter.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.xaml) · 사전 루트 |
| `DefaultNavigationViewContentPresenterWithDynamicScrollViewerControlTemplate` | [NavigationViewContentPresenter.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.xaml) · 사전 루트 |

리소스·속성으로 해결되지 않는 모서리 분할·고정 크기·구조 변경은 ControlTemplate 전체를 복제해 수정합니다. 기존 템플릿의 일부 시각 자식만 Style.Setter로 교체하는 기능은 없습니다.

<details>
<summary>공개 속성·붙임 DP가 내부 요소에 연결되는 위치</summary>

| 입력 속성 | 내부 반영 위치 | 연결 방식 | 정의 |
| --- | --- | --- | --- |
| `Padding` | `ContentPresenter#PART_FrameCP.Margin` | TemplateBinding | [NavigationViewContentPresenter.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.xaml) |

</details>

<!-- customization:end -->

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `FocusVisualStyle` | `{x:Null}` | DefaultNavigationViewContentPresenterStyle |
| `IsTabStop` | `False` | DefaultNavigationViewContentPresenterStyle |
| `SnapsToDevicePixels` | `True` | DefaultNavigationViewContentPresenterStyle |
| `OverridesDefaultStyle` | `True` | DefaultNavigationViewContentPresenterStyle |
| `JournalOwnership` | `OwnsJournal` | DefaultNavigationViewContentPresenterStyle |

## 동작과 주의 사항

일반 앱에서는 NavigationView가 이 요소를 템플릿 내부에서 생성합니다. 직접 사용할 때 메뉴·캐시·저널까지 자동 구성되는 것은 아닙니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [NavigationViewContentPresenter.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.cs)
- [NavigationViewContentPresenter.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/NavigationView/NavigationViewContentPresenter.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
