using System.Windows;
using System.Windows.Controls;

namespace QuickStart;

public partial class SettingsPage : UserControl
{
    public SettingsPage()
    {
        InitializeComponent();
        City.OriginalItemsSource = new[] { "서울", "부산", "대전", "광주", "인천" };
    }

    private async void SaveClicked(object sender, RoutedEventArgs e)
    {
        if (Window.GetWindow(this) is MainWindow window)
            await window.ShowSaveDialogAsync();
    }
}
