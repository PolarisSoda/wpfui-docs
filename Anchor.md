# Anchor

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

HyperlinkButton을 그대로 상속한 호환 이름입니다. 별도 고유 속성이나 새 탐색 기능은 없습니다.

**타입:** `Wpf.Ui.Controls.Anchor` · **기반:** `Wpf.Ui.Controls.HyperlinkButton`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Anchor x:Name="Demo" Content="프로젝트 열기" NavigateUri="https://github.com/lepoco/wpfui" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.NavigateUri = "https://wpfui.lepo.co/";
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### WPF-UI 기반 클래스에서 상속한 속성

| 속성 | 선언 타입 | 효과 |
| --- | --- | --- |
| `NavigateUri` | [HyperlinkButton](HyperlinkButton.md) | 클릭 시 외부 프로세스 실행으로 여는 주소 문자열입니다. `https://...` 같은 검증된 주소를 사용합니다. 앱 내부 페이지 탐색은 `NavigationView.Navigate()`로 구현합니다. |
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

상속 이벤트: `Click`. 업무 동작은 `Command` 바인딩으로도 연결할 수 있습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

화면의 데이터 내용은 공개 속성·ContentTemplate·ItemTemplate로, 여러 속성의 공통 설정은 Style로 바꿉니다. 아래에서 DynamicResource로 연결된 키는 해당 요소의 Resources 재정의 후보이고, StaticResource·고정 템플릿 값은 별도 수정 경로입니다. 상태별 트리거가 있으면 그 상태에서 쓰이는 값을 조정해야 합니다.

<details>
<summary>정적 리소스 참조 — 인스턴스 Resources 재정의 보장 대상 아님</summary>

| 키 | 타입 | 쓰이는 위치 |
| --- | --- | --- |
| `DefaultUiAnchorStyle` | Style | Style BasedOn |
| `DefaultUiButtonStyle` | Style | Style BasedOn |

StaticResource는 라이브러리 사전·템플릿을 읽는 시점에 값이 정해질 수 있습니다. 같은 이름을 Control.Resources에 넣으면 반드시 바뀐다고 해석하지 않습니다. 공개 속성·Style.Setter로 바꾸거나 원본 템플릿을 복제해 해당 참조를 DynamicResource·TemplateBinding으로 바꿉니다.

</details>

### 선택·확장할 수 있는 스타일 키

| 키 | 대상 | 정의 |
| --- | --- | --- |
| `DefaultUiAnchorStyle` | `controls:Anchor` | [Anchor.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Anchor/Anchor.xaml) |

`Style="{StaticResource 키}"`로 선택하거나 새 Style의 BasedOn에 연결합니다. TargetType이 맞아야 하며 정의 파일이 실제 리소스 범위에 로드되어 있어야 합니다. 접두사 Default가 붙은 키도 앱에서 선택할 수 있지만 내부 구현 변경에 영향을 받을 수 있습니다.

<!-- customization:end -->

## 동작과 주의 사항

새 코드에서는 목적이 분명한 [HyperlinkButton](HyperlinkButton.md)도 검토합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Anchor.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Anchor/Anchor.cs)
- [Gallery: AnchorPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/BasicInput/AnchorPage.xaml)
