# Image

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

비율 조정과 둥근 모서리를 지원하는 이미지 컨트롤입니다.

**타입:** `Wpf.Ui.Controls.Image` · **기반:** `Control`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Image x:Name="Demo" Width="160" Height="100" Source="Assets/photo.png" Stretch="UniformToFill" CornerRadius="8" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Stretch = System.Windows.Media.Stretch.Uniform;
Demo.CornerRadius = new System.Windows.CornerRadius(16);
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Source` | `ImageSource?` | 읽기·쓰기 | `null` | 표시할 이미지 소스입니다. 기본 WPF 이미지 소스 형식을 사용합니다. |
| `Stretch` | `Stretch` | 읽기·쓰기 | `Stretch.Uniform` | 가용 영역에 이미지를 맞추는 방식입니다. `Uniform`은 비율 유지, `UniformToFill`은 비율을 유지하며 일부 잘림, `Fill`은 비율을 무시합니다. |
| `StretchDirection` | `StretchDirection` | 읽기·쓰기 | `StretchDirection.Both` | 확대·축소를 어느 방향까지 허용할지 정합니다. `UpOnly`는 확대만, `DownOnly`는 축소만, `Both`는 둘 다 허용합니다. |
| `CornerRadius` | `CornerRadius` | 읽기·쓰기 | `new CornerRadius(0)` | 모서리 반지름(DIP)입니다. `0`은 직각이며 값을 키우면 더 둥글어집니다. 기본 스타일이 별도 값을 설정할 수 있습니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

예제의 `Assets/photo.png`는 앱에 준비해야 하는 리소스입니다. 네트워크 이미지의 다운로드·오류 처리와 리소스 URI 구성은 WPF ImageSource 규칙을 따릅니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Image.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Image/Image.cs)
- [Gallery: ImagePage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Media/ImagePage.xaml)
