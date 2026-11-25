# 대화상자와 호스트

[전체 목차](README.md) · [ContentDialog](ContentDialog.md) · [MessageBox](MessageBox.md)

ContentDialog는 현재 창 안의 호스트를 덮고, MessageBox는 별도 Window로 표시합니다. 짧은 작업 결과만 알리려면 Snackbar·InfoBar도 검토합니다.

## 전용 ContentDialogHost

```xml
<Grid>
    <Grid x:Name="ApplicationContent">
        <TextBlock Text="일반 앱 화면" />
    </Grid>
    <ui:ContentDialogHost x:Name="DialogHost" IsDisableSiblingsEnabled="True" />
</Grid>
```

호스트는 최상위 Grid의 마지막 자식으로 두어 전체 화면을 덮게 합니다. `IsDisableSiblingsEnabled=True`이면 형제 요소의 기존 활성 상태를 관리하면서 배경 상호작용을 막습니다. 창당 한 호스트만 등록할 수 있습니다.

```csharp
using ui = Wpf.Ui.Controls;

// async 메서드 본문
var dialog = new ui.ContentDialog(DialogHost)
{
    Title = "계속할까요?",
    Content = "변경한 내용을 저장합니다.",
    PrimaryButtonText = "저장",
    CloseButtonText = "취소",
    DefaultButton = ui.ContentDialogButton.Primary
};
var result = await dialog.ShowAsync();
if (result == ui.ContentDialogResult.Primary)
{
    // 저장합니다.
}
```

Primary·Secondary 버튼은 텍스트가 비어 있으면 기본 템플릿에서 숨겨집니다. Close 버튼의 기본 텍스트는 `Close`입니다. 닫기·취소는 `ContentDialogResult.None`이며 별도의 Close 결과는 없습니다. `DefaultButton`에는 Primary·Secondary·Close만 있으며 None은 없습니다.

## 입력 검증으로 닫기 막기

```csharp
var input = new ui.TextBox { PlaceholderText = "이름" };
var dialog = new ui.ContentDialog(DialogHost)
{
    Title = "이름 입력", Content = input,
    PrimaryButtonText = "확인", CloseButtonText = "취소"
};
dialog.Closing += (_, e) =>
{
    if (e.Result == ui.ContentDialogResult.Primary && string.IsNullOrWhiteSpace(input.Text))
        e.Cancel = true;
};
await dialog.ShowAsync();
```

`ButtonClicked`는 클릭 알림입니다. 실제 닫기를 취소하는 경로는 `Closing`의 Cancel입니다. 이 이벤트 안에서 오래 걸리는 저장 작업을 무조건 실행하기보다 확인·검증과 결과 이후 작업을 나눕니다.

## 기존 ContentPresenter 호스트

기존 앱은 ContentPresenter를 호스트로 사용할 수 있으나 관련 생성자·DialogHost는 Obsolete입니다. 신규 예제는 ContentDialogHost를 사용합니다.

```xml
<ContentPresenter x:Name="LegacyHost"
    ui:ContentDialogHostBehavior.IsEnabled="True"
    ui:ContentDialogHostBehavior.IsDisableSiblingsEnabled="True" />
```

[ContentDialogHostBehavior](ContentDialogHostBehavior.md)는 기존 호스트의 수명·형제 격리를 보완합니다. ContentDialog.DialogHost와 DialogHostEx를 동시에 지정하면 예외가 발생합니다. 호스트 없는 기본 생성자만 만든 뒤 ShowAsync를 호출하는 구성은 피합니다. `ContentPresenter`라는 오래된 자동 속성만 설정하는 것은 실제 호스트 연결이 아닙니다.

## 별도 창 MessageBox

```csharp
var box = new ui.MessageBox
{
    Owner = this, // this는 Window
    Title = "안내", Content = "작업을 완료했습니다.",
    CloseButtonText = "확인"
};
ui.MessageBoxResult result = await box.ShowDialogAsync();
```

기본 `System.Windows.MessageBox.Show(...)`와 API가 다릅니다. `ui.MessageBox.Show()`·`ShowDialog()`·`Close()`를 호출하면 4.3.0 구현은 예외를 던집니다. ShowDialogAsync를 사용하며 소유 창을 지정합니다.

## 기준 소스

- [ContentDialog](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialog.cs)
- [ContentDialogHost](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/ContentDialog/ContentDialogHost.cs)
- [MessageBox](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/MessageBox/MessageBox.cs)
