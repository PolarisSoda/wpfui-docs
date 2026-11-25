using System;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using System.Windows;

internal static class SnippetSmoke
{
    [STAThread]
    public static int Main(string[] args)
    {
        var app = new Application { ShutdownMode = ShutdownMode.OnExplicitShutdown };
        app.Resources.MergedDictionaries.Add(new Wpf.Ui.Markup.ThemesDictionary
        {
            Theme = Wpf.Ui.Appearance.ApplicationTheme.Light
        });
        app.Resources.MergedDictionaries.Add(new Wpf.Ui.Markup.ControlsDictionary());
        using var manifest = JsonDocument.Parse(System.IO.File.ReadAllText(args[0]));
        int count = 0, properties = 0, failures = 0;
        foreach (var page in manifest.RootElement.GetProperty("pages").EnumerateArray())
        {
            string name = page.GetProperty("name").GetString()!;
            try
            {
                if (page.GetProperty("kind").GetString() == "custom")
                {
                    var type = typeof(Wpf.Ui.Controls.Button).Assembly.GetType("Wpf.Ui.Controls." + name)!;
                    var declared = type.GetProperties(BindingFlags.DeclaredOnly | BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static);
                    var listed = page.GetProperty("properties").EnumerateArray().Select(p => p.GetProperty("name").GetString()).ToArray();
                    var extra = declared.Select(p => p.Name).Except(listed).ToArray();
                    if (extra.Length > 0) throw new Exception("Undocumented properties: " + string.Join(", ", extra));
                    foreach (var prop in page.GetProperty("properties").EnumerateArray())
                    {
                        string propName = prop.GetProperty("name").GetString()!;
                        var actual = declared.SingleOrDefault(p => p.Name == propName);
                        if (actual is null) throw new Exception("Unknown property: " + propName);
                        bool writable = actual.SetMethod?.IsPublic == true;
                        if (writable != prop.GetProperty("writable").GetBoolean()) throw new Exception("Setter access mismatch: " + propName);
                        if (actual.GetMethod!.IsStatic != prop.GetProperty("static").GetBoolean()) throw new Exception("Static mismatch: " + propName);
                        properties++;
                    }
                }
                var wrapper = Assembly.GetExecutingAssembly().GetType("DocChecks.Check_" + name)!;
                var view = (FrameworkElement)Activator.CreateInstance(wrapper)!;
                // XAML is loaded but no window is shown and example methods are not executed.
                // This detects resource/construction issues without performing sample actions.
                count++;
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(name + ": " + e.GetBaseException().Message);
                failures++;
            }
        }
        Console.WriteLine($"Constructed {count} XAML examples; reflected {properties} declared properties; failures: {failures}.");
        app.Shutdown();
        return failures == 0 ? 0 : 1;
    }
}
