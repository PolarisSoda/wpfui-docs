# TabView

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md) · [Resources·스타일](#속성-외에-모양을-바꾸는-방법)

기본 WPF TabControl·TabItem을 감싼 탭 컨테이너입니다. 4.3.0에는 추가 고유 속성이 없습니다.

**타입:** `Wpf.Ui.Controls.TabView` · **기반:** `System.Windows.Controls.TabControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:TabView x:Name="Demo" SelectedIndex="0">
    <ui:TabViewItem Header="문서"><TextBlock Text="첫 문서" /></ui:TabViewItem>
    <ui:TabViewItem Header="설정"><TextBlock Text="설정 화면" /></ui:TabViewItem>
</ui:TabView>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.SelectedIndex = 1;
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
| `SelectedIndex / SelectedItem` | `int / object` | 현재 표시하는 탭입니다. |
| `TabStripPlacement` | `Dock` | 탭 헤더를 Top·Bottom·Left·Right에 배치합니다. |
| `ContentTemplate` | `DataTemplate` | 선택된 탭 본문 데이터의 표시 방식입니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

<!-- customization:start -->
## 속성 외에 모양을 바꾸는 방법

[리소스·스타일·템플릿 사용법](CustomizationGuide.md) · [전체 리소스 사전](ResourceCatalog.md)

4.3.0의 TabView는 TabControl 파생 빈 클래스이며 독립 WPF UI ControlTemplate을 제공하지 않습니다. 기본 WPF 타입용 암시적 Style은 파생 타입과 정확히 일치하지 않을 수 있으므로 테마 TabControl 스타일을 쓰려면 TabView용 Style을 만들고 BasedOn="{StaticResource {x:Type TabControl}}"으로 명시적으로 연결합니다. TabItem·TabViewItem도 별도로 고려합니다.

### 기본 TabControl 테마 스타일을 명시적으로 연결

<!-- customization:example TabView_Recipe1 -->
```xml
<ui:TabView>
    <ui:TabView.Style>
        <Style TargetType="{x:Type ui:TabView}" BasedOn="{StaticResource {x:Type TabControl}}" />
    </ui:TabView.Style>
    <TabItem Header="일반"><TextBlock Text="일반 설정" /></TabItem>
    <TabItem Header="고급"><TextBlock Text="고급 설정" /></TabItem>
</ui:TabView>
```

<!-- customization:example-end -->

<!-- customization:end -->

## 동작과 주의 사항

WinUI TabView의 탭 닫기·추가·드래그 재정렬 API를 이 클래스에 그대로 적용할 수 없습니다. 해당 동작은 직접 구현해야 합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [TabView.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/TabView/TabView.cs)
- [Gallery: TabViewPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Navigation/TabViewPage.xaml)
