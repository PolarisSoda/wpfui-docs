# RichTextBox

[전체 목차](README.md) · [시작하기](GettingStarted.md) · [공통 속성](CommonProperties.md)

FlowDocument 문단·서식을 표시하거나 편집하는 WPF RichTextBox에 선택용 표시 스타일을 더합니다.

**타입:** `Wpf.Ui.Controls.RichTextBox` · **기반:** `System.Windows.Controls.RichTextBox`

## 사용 예제

XAML 조각은 [시작하기](GettingStarted.md)의 `xmlns:ui`·`xmlns:x` 선언을 전제로 합니다. `local:`은 앱의 화면 클래스 네임스페이스입니다.

```xml
<ui:RichTextBox x:Name="Demo" Height="140" IsTextSelectionEnabled="True">
    <FlowDocument><Paragraph><Bold>안내</Bold> 문서를 선택해 복사할 수 있습니다.</Paragraph></FlowDocument>
</ui:RichTextBox>
```

### C#에서 변경하기

`using ui = Wpf.Ui.Controls;`를 추가합니다. 별도 설명이 없으면 위 XAML과 같은 창·뷰의 메서드 본문이며, `await`가 있으면 `async Task` 또는 이벤트 처리기 안에서 호출합니다.

```csharp
Demo.Document.Blocks.Add(new System.Windows.Documents.Paragraph(
    new System.Windows.Documents.Run("추가 문단")));
Demo.IsTextSelectionEnabled = false;
Demo.IsReadOnly = false;
```

## 속성과 화면 변화

아래 기본값은 **DP 등록 코드의 값**입니다. 생성자·상속 메타데이터·테마 스타일이 실제 값을 바꿀 수 있으므로 뒤의 스타일 설정도 확인합니다. `외부 읽기 전용`은 CLR setter가 없거나 public이 아니라는 뜻이며 DP 자체의 읽기 전용 등록과는 구별합니다. `정적` 속성은 인스턴스 대신 타입 이름으로 읽습니다.

| 속성 | 타입 | 접근 | 등록 기본값 / 계산 방식 | 변경 효과와 사용 조건 |
| --- | --- | --- | --- | --- |
| `IsTextSelectionEnabled` | `bool` | 읽기·쓰기 | `false` | `true`이면 기본 스타일이 `IsReadOnly=True`, 투명 배경, 여백·테두리 제거를 적용합니다. 편집기에서 읽기 전용 문서 표시로 전환하는 용도입니다. |

### 자주 쓰는 기본 WPF 속성

| 속성 | 타입 | 효과 |
| --- | --- | --- |
| `Document` | `FlowDocument` | 표시·편집할 문서입니다. 문단은 Document.Blocks에 넣습니다. |
| `IsReadOnly` | `bool` | 문서 편집을 허용할지 정합니다. |
| `AcceptsTab` | `bool` | Tab 키를 문서 입력으로 처리할지 정합니다. |

크기·여백·표시 여부·활성화·바인딩의 공통 규칙은 [CommonProperties.md](CommonProperties.md)를 참고합니다. 기본 WPF 전체 상속 API를 재수록하지는 않습니다.

## 동작과 주의 사항

문서는 `Text` 문자열 속성이 아니라 `Document`와 `FlowDocument.Blocks`로 다룹니다. 기본 스타일에서 `IsTextSelectionEnabled=True`는 읽기 전용 표시를 적용합니다.

## 확인한 소스

기준: WPF UI **4.3.0**, 커밋 `153baadeaf475875a81a4605881ca5c2dbe53972`.

- [RichTextBox.cs](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui/Controls/RichTextBox/RichTextBox.cs)
- [Gallery: RichTextBoxPage](https://github.com/lepoco/wpfui/blob/153baadeaf475875a81a4605881ca5c2dbe53972/src/Wpf.Ui.Gallery/Views/Pages/Text/RichTextBoxPage.xaml)
