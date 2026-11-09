# DR-0011: U5도 피드백 보완과 학습자 검토로 종료한다

- Status: Accepted
- Date: 2026-11-09
- Deciders: 학습자, Codex

## Context

U5의 최초 error-spot 답안은 독립 채점과 별도 리뷰에서 partial이었다. 튜터는 A에서 P1이 누락되어 검색 실패이며 reader 자체의 실패는 확정할 수 없고, B에서는 P1이 있으므로 근거 확보는 성공했으나 reader 선택이 실패했다고 보완했다. 학습자는 "응 그렇게 보완하고 U5도 닫자"라고 요청했다.

## Decision

DR-0010의 학습 절차와 독립 검증을 구분하는 방식을 U5에도 적용한다. U5는 답안 제출과 전사 확인, 독립 채점 및 리뷰, 피드백 보완과 학습자 검토를 완료 조건으로 한다. 해당 절차를 마친 U5를 완료 처리하고 U6 대기로 인계한다.

- 최초 exercise의 Problem, Rubric, Attempt, partial과 보호 snapshot은 유지한다.
- 보완 설명은 학습 노트와 exercise의 Next에 기록하며 새 독립 pass로 세지 않는다.
- concept state 및 전체 초안 검토 여부는 변경하지 않는다.
- Phase의 독립 pass 횟수 및 transfer 요건은 유지한다. 부족한 근거는 후속 검증에서 확보한다.
- 이번 결정은 U5에 한정한다. 다른 unit, 스킬, 채점 에이전트는 바꾸지 않는다.

## Rationale and Consequences

학습자가 검토한 피드백의 반영을 unit 진척으로 인정하면서 최초 수행 기록을 보존한다. U5 완료는 exercise 통과나 독립 적용 능력 검증을 의미하지 않는다.
