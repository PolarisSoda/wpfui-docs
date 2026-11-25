using System;
using System.Linq;
using System.Reflection;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using ui = Wpf.Ui.Controls;

internal static class CustomizationSmoke
{
    static int assertions;
    static void Assert(bool ok, string message)
    {
        if (!ok) throw new Exception(message);
        assertions++;
    }
    static void Layout(FrameworkElement view)
    {
        if (!view.IsInitialized) { view.BeginInit(); view.EndInit(); }
        view.ApplyTemplate();
        view.Measure(new Size(600, 400));
        view.Arrange(new Rect(0, 0, 600, 400));
        view.UpdateLayout();
        System.Windows.Threading.Dispatcher.CurrentDispatcher.Invoke(
            System.Windows.Threading.DispatcherPriority.DataBind, new Action(() => {}));
    }
    static Border BorderOf(Control view, string name = "ContentBorder")
    {
        Layout(view);
        return (Border)(view.Template.FindName(name, view) ?? throw new Exception("Missing template part: " + name));
    }
    [STAThread]
    public static int Main()
    {
        var app = new Application { ShutdownMode = ShutdownMode.OnExplicitShutdown };
        app.Resources.MergedDictionaries.Add(new Wpf.Ui.Markup.ThemesDictionary { Theme = Wpf.Ui.Appearance.ApplicationTheme.Light });
        app.Resources.MergedDictionaries.Add(new Wpf.Ui.Markup.ControlsDictionary());
        app.Resources.MergedDictionaries.Add(new ResourceDictionary
        {
            Source = new Uri("/CustomizationChecks;component/Fixtures/CardWithFooter.xaml", UriKind.Relative)
        });
        int count = 0;
        foreach (var t in Assembly.GetExecutingAssembly().GetTypes().Where(t => t.Namespace == "DocCustom" && t.Name.StartsWith("Customize_")))
        {
            try { _ = Activator.CreateInstance(t); count++; }
            catch (Exception e) { Console.Error.WriteLine(t.Name + ": " + e.GetBaseException().Message); return 1; }
        }
        try
        {
            var card = new ui.Card { Content = "plain" };
            card.Resources["ControlCornerRadius"] = new CornerRadius(12);
            var content = BorderOf(card);
            Assert(content.CornerRadius == new CornerRadius(12), "Card.Resources must reach ContentBorder.");
            card.Resources["ControlCornerRadius"] = new CornerRadius(18);
            Layout(card);
            Assert(content.CornerRadius == new CornerRadius(18), "DynamicResource replacement must update Card.");
            card.SetValue(Border.CornerRadiusProperty, new CornerRadius(6));
            Layout(card);
            Assert(content.CornerRadius == new CornerRadius(6), "Local DP value must override resource setter.");
            card.ClearValue(Border.CornerRadiusProperty);
            Layout(card);
            Assert(content.CornerRadius == new CornerRadius(18), "ClearValue must restore resource path.");

            var footer = new ui.Card { Content = "body", Footer = "footer" };
            footer.Resources["ControlCornerRadius"] = new CornerRadius(12);
            Assert(BorderOf(footer).CornerRadius == new CornerRadius(4,4,0,0), "Default Card Footer top remains fixed at 4.");
            Assert(BorderOf(footer,"FooterBorder").CornerRadius == new CornerRadius(0,0,4,4), "Default Card Footer bottom remains fixed at 4.");

            var custom = new ui.Card { Content = "body", Footer = "footer", Style = (Style)app.FindResource("RoundedFooterCardStyle") };
            Assert(BorderOf(custom).CornerRadius == new CornerRadius(12,12,0,0), "Custom Card Footer top must be 12.");
            Assert(BorderOf(custom,"FooterBorder").CornerRadius == new CornerRadius(0,0,12,12), "Custom Card Footer bottom must be 12.");

            var button = new ui.Button { Content = "button" };
            button.Resources["ControlCornerRadius"] = new CornerRadius(11);
            Layout(button);
            Assert(button.CornerRadius == new CornerRadius(11), "Button resources must supply CornerRadius.");
            var action = new ui.CardAction { Content = "action" };
            action.Resources["ControlCornerRadius"] = new CornerRadius(9);
            Assert(BorderOf(action).CornerRadius == new CornerRadius(9), "CardAction must consume Border.CornerRadius.");

            var expander = new ui.CardExpander { Header = "settings", Content = "body" };
            expander.Resources["ControlCornerRadius"] = new CornerRadius(13);
            Assert(BorderOf(expander,"ToggleButtonBorder").CornerRadius == new CornerRadius(13), "Collapsed CardExpander retains all corners.");
            expander.IsExpanded = true;
            Assert(BorderOf(expander,"ToggleButtonBorder").CornerRadius == new CornerRadius(13,13,0,0), "Expanded CardExpander splits top corners using converter.");
            Assert(BorderOf(expander,"ContentPresenterBorder").CornerRadius == new CornerRadius(0,0,13,13), "Expanded CardExpander splits bottom corners using converter.");

            var scope = new StackPanel();
            scope.Resources["ControlCornerRadius"] = new CornerRadius(7);
            var scopedCard = new ui.Card { Content = "parent scope" };
            var localCard = new ui.Card { Content = "local scope" };
            localCard.Resources["ControlCornerRadius"] = new CornerRadius(15);
            scope.Children.Add(scopedCard); scope.Children.Add(localCard);
            Layout(scope);
            Assert(BorderOf(scopedCard).CornerRadius == new CornerRadius(7), "Parent Resources scope must reach card.");
            Assert(BorderOf(localCard).CornerRadius == new CornerRadius(15), "Local Resources must override parent scope.");

            var box = new ui.TextBox();
            box.Resources["TextControlThemePadding"] = new Thickness(16,10,16,10);
            box.Resources["ControlCornerRadius"] = new CornerRadius(10);
            Layout(box);
            Assert(box.Padding == new Thickness(16,10,16,10), "TextBox dynamic padding must be applied. Actual="+box.Padding+"; lookup="+box.FindResource("TextControlThemePadding")+"; source="+DependencyPropertyHelper.GetValueSource(box,Control.PaddingProperty).BaseValueSource+"; selection="+box.IsTextSelectionEnabled+"; style="+box.Style?.TargetType);
            Assert((CornerRadius)box.GetValue(Border.CornerRadiusProperty) == new CornerRadius(10), "TextBox dynamic radius DP must be applied.");

            var valueBadge = new ui.InfoBadge { Value = "3", CornerRadius = new CornerRadius(12) };
            valueBadge.Resources["ValueInfoBadgeStyleCornerRadius"] = new CornerRadius(19);
            Assert(BorderOf(valueBadge).CornerRadius == new CornerRadius(8), "Value InfoBadge uses static radius, not local Resources or CornerRadius.");
            var iconBadge = new ui.InfoBadge
            {
                Style = (Style)app.FindResource("IconInfoBadgeStyle"),
                Icon = new ui.SymbolIcon(ui.SymbolRegular.Checkmark24),
                CornerRadius = new CornerRadius(12)
            };
            Assert(BorderOf(iconBadge).CornerRadius == new CornerRadius(12), "Icon InfoBadge must bind CornerRadius.");

            var ring = new ui.ProgressRing();
            ring.Resources["ProgressRingForegroundThemeBrush"] = Brushes.CornflowerBlue;
            ring.Resources["ProgressRingBackgroundThemeBrush"] = Brushes.LightBlue;
            Layout(ring);
            Assert(ring.Foreground == Brushes.CornflowerBlue, "ProgressRing foreground resource.");
            Assert(ring.CoverRingStroke == Brushes.LightBlue, "ProgressRing background ring resource.");

            app.Resources["DefaultIconFontSize"] = 23d;
            var icon = new ui.FontIcon();
            icon.Resources["DefaultIconFontSize"] = 41d;
            Assert(icon.FontSize == 23d, "FontIcon constructor reads Application.Resources, not local Resources.");
        }
        catch (Exception e) { Console.Error.WriteLine(e.ToString()); return 1; }
        Console.WriteLine($"PASS: {count} customization XAML examples constructed; {assertions} behavior assertions passed.");
        app.Shutdown();
        return 0;
    }
}
