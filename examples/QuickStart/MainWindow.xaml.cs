using System.Windows;
using ui = Wpf.Ui.Controls;

namespace QuickStart;

public partial class MainWindow : ui.FluentWindow
{
    public MainWindow()
    {
        InitializeComponent();
        Loaded += (_, _) => Navigation.Navigate(typeof(HomePage));
    }

    public async Task ShowSaveDialogAsync()
    {
        var dialog = new ui.ContentDialog(DialogHost)
        {
            Title = "설정을 저장할까요?",
            Content = "변경한 설정을 적용합니다.",
            PrimaryButtonText = "저장",
            CloseButtonText = "취소"
        };
        if (await dialog.ShowAsync() == ui.ContentDialogResult.Primary)
        {
            new ui.Snackbar(SnackbarHost)
            {
                Title = "저장 완료",
                Content = "설정 적용 예제입니다.",
                Appearance = ui.ControlAppearance.Success,
                Timeout = TimeSpan.FromSeconds(3)
            }.Show();
        }
    }
}
