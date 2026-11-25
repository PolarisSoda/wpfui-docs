# QuickStart

[문서 목차](../../README.md) · [시작하기](../../GettingStarted.md)

Windows와 .NET 10 SDK에서 실행하는 작은 WPF 앱입니다. WPF-UI 4.3.0을 사용합니다.

```powershell
dotnet restore
dotnet build
dotnet run
```

이 폴더에서 위 명령을 실행합니다. 외부 이미지·비밀번호·서비스 연결은 필요하지 않습니다.

홈에서 설정으로 이동하면 ToggleSwitch·TextBox·NumberBox·AutoSuggestBox를 시험할 수 있습니다. 저장 확인은 ContentDialogHost 위의 대화상자를 열며, 저장 버튼을 누르면 Snackbar를 표시합니다. 실제 디스크 저장 동작은 없는 UI 예제입니다.

| 파일 | 설명 |
| --- | --- |
| App.xaml | 테마와 ControlsDictionary 설정 |
| MainWindow.xaml | FluentWindow·TitleBar·NavigationView·두 호스트 배치 |
| MainWindow.xaml.cs | 최초 탐색과 대화상자·스낵바 수명 |
| HomePage.xaml | Page 기반 홈 화면 |
| SettingsPage.xaml | UserControl 기반 설정 화면 |

설정 페이지는 NavigationCacheMode=Enabled이므로 재방문 시 인스턴스 상태를 유지합니다. 이 예제는 이해를 위해 코드비하인드를 사용합니다. ViewModel 바인딩은 각 문서의 속성·바인딩 설명을 참고합니다.
