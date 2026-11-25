# Resources·Style·Template 조정 예제

[문서 목차](../../README.md) · [조정 방법 안내](../../CustomizationGuide.md)

Windows와 .NET 10 SDK, WPF-UI 4.3.0에서 실행합니다.

```powershell
dotnet run --project examples/CustomizationLab/CustomizationLab.csproj
```

저장소 루트에서 실행합니다. 화면은 다음 차이를 나란히 보여 줍니다.

- Footer 없는 Card: Card.Resources의 ControlCornerRadius로 12 DIP 적용
- 기본 Footer가 있는 Card: 같은 리소스를 넣어도 원본 고정 반지름 4 유지
- 수정한 전체 Card 템플릿: 본문 위·Footer 아래를 12 DIP로 분리
- Button: Normal·PointerOver·Pressed 강조색과 반지름
- TextBox: 입력 여백·반지름·포커스 배경
- InfoBadge: 기본 숫자·점·아이콘 스타일
- ProgressRing: 진행 호와 뒤쪽 링의 별도 색

[CardWithFooter.xaml](CardWithFooter.xaml)을 App.xaml의 ControlsDictionary 다음에 병합하고 RoundedFooterCardStyle을 선택하면 Footer 템플릿을 재사용할 수 있습니다. `CustomCardTopRadius`·`CustomCardBottomRadius`는 이 예제의 사용자 정의 키이며, 원본 WPF UI 내장 키가 아닙니다. 비표준 BorderThickness를 사용하는 앱은 내부 테두리 분할 값도 함께 맞춥니다.

예제 템플릿은 원본 4.3.0 Card.xaml을 참고해 수정했습니다. [출처·MIT 고지](../../THIRD_PARTY_NOTICES.md)를 유지합니다. 소스 업데이트 후에는 원본 템플릿의 변경점도 함께 대조해야 합니다.
