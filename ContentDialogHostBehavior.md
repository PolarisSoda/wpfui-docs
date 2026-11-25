# ContentDialogHostBehavior

[전체 목차](README.md) · [대화상자 구성](DialogGuide.md)

기존 ContentPresenter를 ContentDialog 호스트로 쓰는 앱에 수명 관리·형제 요소 격리를 연결하는 **정적 붙임 동작**입니다. 인스턴스 컨트롤이 아니므로 `<ui:ContentDialogHostBehavior />`로 만들지 않습니다. 새 앱에서는 [ContentDialogHost](ContentDialogHost.md)를 먼저 검토합니다.

```xml
<ContentPresenter x:Name="LegacyHost"
    ui:ContentDialogHostBehavior.IsEnabled="True"
    ui:ContentDialogHostBehavior.IsDisableSiblingsEnabled="True" />
```

```csharp
using ui = Wpf.Ui.Controls;
ui.ContentDialogHostBehavior.SetIsEnabled(LegacyHost, true);
ui.ContentDialogHostBehavior.SetIsDisableSiblingsEnabled(LegacyHost, true);
```

| 붙임 속성 | 타입 | 등록 기본값 | 효과 |
| --- | --- | --- | --- |
| IsEnabled | bool | false | ContentPresenter의 콘텐츠 변경을 감시하고 내부 호스트 컨트롤러를 연결합니다. 끄면 감시·활성 상태를 정리합니다. |
| IsDisableSiblingsEnabled | bool | false | 다이얼로그 활성 중 호스트 형제 요소를 비활성화하도록 내부 컨트롤러에 전달합니다. |

`GetIsEnabled`·`GetIsDisableSiblingsEnabled`로 값을 읽고 `Set...`으로 변경합니다. 내부 `State` 붙임 속성은 앱용 API가 아닙니다. 이 동작을 켜는 것만으로 대화상자를 생성·표시하지는 않습니다. 대화상자에는 실제 호스트를 연결하고 ShowAsync를 호출해야 합니다.

기준: [4.3.0 구현](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialogHostBehavior.cs).
