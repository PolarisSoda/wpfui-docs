# Separator

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

인접 영역을 구분하는 시각적 선입니다.

**타입:** 기본 WPF 타입 (`System.Windows.Controls` 또는 `System.Windows`) · **선언:** 기본 XAML 네임스페이스

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<Separator x:Name="Demo" Margin="0,8" />
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Visibility = System.Windows.Visibility.Collapsed;
```

## 속성과 화면 변화

이 타입이 새로 추가하는 공개 인스턴스 속성은 없습니다. 아래 상속 속성으로 구성합니다.

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Margin` | `Thickness` | 주변 요소와의 간격입니다. |
| `Visibility` | `Visibility` | 표시·공간 유지 숨김·공간 제거를 선택합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Width` | `3` | DefaultDropLocationIndicatorStyle |
| `Template` | `{StaticResource  GridViewHeaderRowIndicatorTemplate}` | DefaultDropLocationIndicatorStyle |
| `BorderBrush` | `{DynamicResource MenuBarItemBorderBrush}` | {x:Static MenuItem.SeparatorStyleKey} |
| `Background` | `Transparent` | {x:Static MenuItem.SeparatorStyleKey} |
| `Margin` | `0,1,0,1` | {x:Static MenuItem.SeparatorStyleKey} |
| `BorderThickness` | `1,1,0,0` | {x:Static MenuItem.SeparatorStyleKey} |
| `SnapsToDevicePixels` | `True` | {x:Static MenuItem.SeparatorStyleKey} |
| `OverridesDefaultStyle` | `True` | {x:Static MenuItem.SeparatorStyleKey} |
| `BorderBrush` | `{DynamicResource SeparatorBorderBrush}` | 암시적 스타일 |
| `Background` | `Transparent` | 암시적 스타일 |
| `Margin` | `0` | 암시적 스타일 |
| `BorderThickness` | `1,1,0,0` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource ControlElevationBorderBrush}` | {x:Static StatusBar.SeparatorStyleKey} |
| `Background` | `Transparent` | {x:Static StatusBar.SeparatorStyleKey} |
| `Margin` | `6,0` | {x:Static StatusBar.SeparatorStyleKey} |
| `BorderThickness` | `1,1,0,0` | {x:Static StatusBar.SeparatorStyleKey} |
| `SnapsToDevicePixels` | `True` | {x:Static StatusBar.SeparatorStyleKey} |
| `OverridesDefaultStyle` | `True` | {x:Static StatusBar.SeparatorStyleKey} |

## 동작과 주의 사항

WPF-UI 전용 클래스가 아닙니다. `xmlns:ui` 접두사 대신 기본 WPF 태그를 사용합니다. WPF UI의 ControlsDictionary를 병합하면 제공되는 스타일이 적용됩니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [DataGrid.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/DataGrid/DataGrid.xaml)
- [MenuItem.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Menu/MenuItem.xaml)
- [Separator.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Separator/Separator.xaml)
- [StatusBar.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/StatusBar/StatusBar.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
