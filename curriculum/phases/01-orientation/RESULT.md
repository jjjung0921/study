# Phase 01 — orientation · Result

- Completed on: 2026-11-07
- Final Status: DONE
- Tag: `phase/01`
- Time: planned 80m · actual 최소 30m 기록됨 (U1 30m, U2부터 U4까지는 미측정)

## Completed

- U1. 목표, 개념 지도, 논문 목록, 후속 Phase 경로를 만들었다 (commit d3eaddc).
- U2. 선행지식 진단을 전사 확인 후 채점하고 결과를 기록했다. 진단 fail은 개념 상태 승격에 사용하지 않았다 (commit db8522f, `exercises/01-u2-prior-knowledge.md`).
- U3. survey, DPR, RAG, FiD 원문 접근과 서지를 대조하고 evidence 파일을 만들었다 (commit 0210e0e).
- U4. 시작 및 종료 스크립트 출력을 확인하고 기본 세션 120분, 말과 손글씨 수식 사진 입력 선호를 기록했다 (commit 205b0b7).
- G1부터 G3까지의 capstone 연결, 10개 concept 선행 관계, 진단과 상태 근거의 분리를 정적으로 대조했다.

## Not Completed

- 없음. 논문 정독과 개념 state 승격은 Phase 02 이후의 범위다.

## Deviations from Plan

- 처음 가정한 30분 대신 학습자가 120분 기본 세션과 주 2회 학습을 선택했다.
- Phase 03과 04의 상세 unit을 미리 작성했다. 주차별 일정은 [track/plan.md](../../../track/plan.md)에 둔다.
- U2의 과거 진단은 새 채점 실행 기록 도입 전의 이력이므로 `legacy_unverified`로 보존한다. 새 snapshot을 소급 생성하지 않았다.

## Important Decisions

- RAG 기초에서 평가, 다중 턴 AICC로 진행한다 ([DR-0007](../../decisions/DR-0007-rag-scope-and-reading-path.md)).
- 진단과 연습, 검증의 상태 근거를 분리한다 ([DR-0008](../../decisions/DR-0008-learning-evidence-boundaries.md)).
- 120분 세션과 서로 다른 날의 검증을 전체 계획에 반영한다 ([DR-0009](../../decisions/DR-0009-two-hour-rag-curriculum.md)).

## Understanding State

- 10개 concept 모두 `unseen`이다. Phase 01에서 state 승격 근거가 되는 exercise는 없다.

## Misconceptions

- 확정된 오개념은 없다. U2의 초기 후보는 학습자 후속 설명과 독립 리뷰 뒤 철회됐다.

## Follow-up Work

- [Phase 02 PLAN](../02-rag-foundations/PLAN.md)의 U1부터 시작한다.
- AICC 우선 도메인은 Phase 04 시작 전에 정한다.
