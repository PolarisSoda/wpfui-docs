using System.Windows;
using System.Windows.Controls;

namespace QuickStart;

public partial class HomePage : Page
{
    public HomePage() => InitializeComponent();

    private void OpenSettings(object sender, RoutedEventArgs e)
    {
        if (Window.GetWindow(this) is MainWindow window)
            window.Navigation.Navigate(typeof(SettingsPage));
    }
}
