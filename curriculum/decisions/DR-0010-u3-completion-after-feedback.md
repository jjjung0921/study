# DR-0010: U3의 학습 종료와 exercise 통과를 구분한다

- Status: Accepted
- Date: 2026-11-09
- Deciders: 학습자, Codex

## Context

Phase 02 U3의 최초 exercise는 독립 채점과 별도 리뷰에서 partial이었다. 학습자는 피드백 후 보완 설명을 검토하고 기록 반영을 요청했다. 기존 PLAN은 exercise pass만 U3 종료 조건으로 두어, 보완을 마친 뒤에도 같은 unit에 머물게 했다.

## Problem

연습의 학습 절차를 마친 것과 독립적인 적용 능력이 검증된 것을 구분하여 기록한다.

## Alternatives

1. 기존 pass 조건 유지: 통과 전 같은 unit에 머물러야 한다.
2. 최초 답안을 보완본으로 교체하고 pass로 변경: 피드백 전 수행과 보완 후 설명을 혼동하므로 채택하지 않는다.
3. U3는 답안 제출, 전사 확인, 독립 채점 및 별도 리뷰, 피드백 보완과 학습자 검토로 종료한다. exercise 등급과 concept 검증은 별도로 유지한다.

## Decision

학습자의 "기준을 바꿔주고 U3는 종료하면 되나?" 요청에 따라 3안을 U3에 적용한다. 다른 practice unit의 완료 기준은 이번 변경 범위에 포함하지 않는다.

- U3 완료 조건을 확인된 답안 제출, 독립 채점 및 별도 리뷰, 피드백 보완과 학습자 검토로 변경한다.
- U3는 이 절차를 마쳤으므로 완료 처리한다. 보완과 검토의 근거는 `notes/sparse-dense-retrieval.md`의 "검토 후 보완 정리"와 학습자의 보완 반영 및 종료 요청이다.
- 최초 exercise의 Problem, Rubric, Attempt, partial 판정과 보호 snapshot은 유지한다. exercise Rubric의 기존 "partial은 unit 통과가 아니다" 문구는 출제 당시 기준의 기록이며, 이후 U3 종료에는 이 결정과 변경된 PLAN을 적용한다.
- U3 종료는 exercise pass나 concept state 승격을 뜻하지 않는다. concept 전체 초안 검토도 확인된 것으로 간주하지 않는다.
- Phase Acceptance Criteria와 DR-0008의 상태 근거, 서로 다른 날 pass 횟수, transfer 요구는 유지한다. 부족한 독립 pass는 이후 검증 기회에서 확보하며 보완 설명을 pass로 세지 않는다.

## Rationale

연습 후 피드백을 반영한 학습 진척을 인정하면서 최초 수행 기록과 독립적인 검증 근거를 보존한다. 이미 제안된 기준을 학습자가 선택한 것이므로 새 정책 대안을 추가로 설계하지 않고 문서에 반영한다.

## Consequences

- PLAN에서 U3를 완료 처리하고 다음 작업은 U4 대기로 인계한다.
- U3의 최초 partial은 남으므로 Phase 완료 전 pass 횟수 부족 여부를 별도로 확인한다.
- 채점 에이전트, 스킬, 공통 규칙, 코드는 수정하지 않는다.
