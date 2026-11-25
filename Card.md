# Card

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

본문과 선택적 하단 영역을 담는 카드 컨테이너입니다.

**타입:** `Wpf.Ui.Controls.Card` · **기반:** `System.Windows.Controls.ContentControl`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:Card x:Name="Demo" Padding="16">
    <TextBlock Text="최근 프로젝트" />
    <ui:Card.Footer><TextBlock Text="마지막 수정: 오늘" /></ui:Card.Footer>
</ui:Card>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Footer = "파일 3개";
Demo.Content = new System.Windows.Controls.TextBlock { Text = "프로젝트 목록" };
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `Footer` | `object?` | 읽기·쓰기 | `null` | 카드 아래쪽 별도 영역의 콘텐츠입니다. 본문과 구분된 상태·보조 설명을 넣습니다. |
| `HasFooter` | `bool` | 외부 읽기 전용 | `false` | `Footer`가 `null`이 아닌지에 따라 계산되는 상태입니다. 외부에서 직접 설정하지 않습니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Content` | `object` | 본문 문자열 또는 단일 UI 요소입니다. 여러 요소는 Grid·StackPanel로 묶습니다. |
| `ContentTemplate` | `DataTemplate` | 본문 데이터의 표시 방식을 지정합니다. |
| `HorizontalContentAlignment / VerticalContentAlignment` | `HorizontalAlignment / VerticalAlignment` | 컨트롤 안에서 본문을 정렬합니다. 컨트롤 자체 위치를 정하는 Alignment와 구분합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 기본 스타일에서 설정하는 값

4.3.0 스타일 파일의 최상위 Setter 선언입니다. 리소스 참조는 현재 테마에서 해석되며, `BasedOn`·스타일 트리거·로컬 값·애니메이션을 모두 계산한 최종값 표는 아닙니다. 템플릿 내부 요소 Setter는 포함하지 않습니다.

| 속성 | 스타일의 값 | 스타일 키 |
| --- | --- | --- |
| `Background` | `{DynamicResource CardBackground}` | 암시적 스타일 |
| `Foreground` | `{DynamicResource CardForeground}` | 암시적 스타일 |
| `BorderBrush` | `{DynamicResource CardBorderBrush}` | 암시적 스타일 |
| `BorderThickness` | `{StaticResource CardBorderThemeThickness}` | 암시적 스타일 |
| `Padding` | `{StaticResource CardPadding}` | 암시적 스타일 |
| `HorizontalAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalAlignment` | `Center` | 암시적 스타일 |
| `HorizontalContentAlignment` | `Stretch` | 암시적 스타일 |
| `VerticalContentAlignment` | `Center` | 암시적 스타일 |
| `FontSize` | `{DynamicResource ControlContentThemeFontSize}` | 암시적 스타일 |
| `FontWeight` | `Normal` | 암시적 스타일 |
| `Border.CornerRadius` | `{DynamicResource ControlCornerRadius}` | 암시적 스타일 |
| `Focusable` | `False` | 암시적 스타일 |
| `KeyboardNavigation.IsTabStop` | `False` | 암시적 스타일 |
| `SnapsToDevicePixels` | `True` | 암시적 스타일 |
| `OverridesDefaultStyle` | `True` | 암시적 스타일 |

## 동작과 주의 사항

카드 자체는 실행 버튼이 아닙니다. 클릭 동작이 필요하면 CardAction·CardControl을 사용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [Card.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.cs)
- [Card.xaml](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/Card/Card.xaml)
- 이 이름의 독립 Gallery 페이지는 없습니다. 위 구현·스타일을 기준으로 작성했습니다.
