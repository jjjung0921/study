# DR-0008: 학습 피드백과 상태 근거의 경계를 분명히 한다

- Status: Accepted
- Date: 2026-11-06
- Deciders: 학습자의 RAG 재초기화 요청에 따른 Codex 적용

## Context

RAG의 기존 DR-0007은 주제 범위와 읽기 경로의 결정이다. 이 결정은 그 경로를 유지하며 템플릿의 학습 근거 계약을 이 워크스페이스에 적용한다.


DR-0002는 상태를 채점 기록에서 도출하고, DR-0006은 강제 이해 확인을 없앴다. 현재 종료 검사는 concept의 `verified_by`에 적힌 pass·partial만 읽는다. 복습 fail은 이 목록에 들어가지 않으므로 `verified → stale`과 이후 복귀를 검사하지 못한다. 또한 DR-0002의 "설명 직후 확인 질문은 practiced 근거" 문장과 Rule 8의 "같은 세션의 되풀이 제외"가 다른 범위를 가리키는지 불분명하다.

## Decision

1. **상태 근거**: `introduced`는 학습자가 초안 세 절을 검토한 기록과 남은 `ai:draft` 표시로 판단한다. `practiced`와 `verified`는 `purpose: practice | verify`인 정식 Rubric-first exercise의 독립 채점으로만 승격한다. `purpose: diagnostic`과 요청에 따른 묶음 `self-exam`은 승격 근거가 아니다. `review`는 verified 유지·stale 강등·복귀에만 쓴다. `verified_by`는 승격에 쓰인 pass·partial 목록으로 유지한다.
2. **같은 세션**: 문제와 Rubric을 학습자 답변보다 먼저 쓴 정식 exercise는 설명과 같은 세션에 풀어도 practiced 근거다. 채점 피드백을 본 뒤 같은 문항을 다시 푼 답은 새 근거로 세지 않는다. `verified`의 서로 다른 날 조건은 유지한다. DR-0002의 설명 직후 *확인 질문*을 practiced 근거로 인정한 문장은 이 결정으로 대체한다.
3. **채점 대기**: 답변 미수신, 전사 확인 대기, 독립 채점자 부재는 `pending`으로 남기고 HANDOFF에 인계한다. 튜터가 학습 피드백을 줄 수는 있지만 자기 채점을 상태 근거로 삼지 않는다. `prepare → 독립 채점 → check` 순서를 지킨다.
4. **짧은 세션**: `min_session`의 회상 질문과 요청한 `self-exam`은 학습 피드백이며 상태 근거가 아니다. 정식 상태 근거가 필요하면 별도의 Rubric-first exercise를 만든다.
5. **복습 이력**: concept별로 모든 채점 완료 exercise의 `concept`, `purpose`, `date`, `result`, `review_order`를 대조한다. `review_order`는 concept별 복습 완료 순서인 양의 정수로, 같은 날에도 중복 없이 1씩 증가한다. 중복되거나 빠진 순서는 검사 실패로 남긴다. `verified_by`에 없는 review fail도 무시하지 않는다. 가장 높은 `review_order`의 fail 또는 partial은 stale의 근거이고, 이후 pass는 verified 복귀의 근거다. concept 파일 맨 아래 `Review History`에 순서, 결과, 상태 영향, 해당 exercise의 상대 링크와 판정 근거를 기록한다. 기존 기록에는 소급 snapshot이나 확인 표시를 만들지 않는다.
6. **다음 검증 기회**: practiced 개념의 다음 verify 기회는 Phase PLAN의 unit이나 capstone에 배치한다. practiced 상태에 자동 만기를 도입하지 않는다.
7. **동일 문제**: 같은 concept에서 Problem 해시가 같은 채점 기록이 발견되면 경고만 낸다. 이 사실만으로 피드백 열람이나 부정행위를 추정하지 않고, 기록을 상태 계산에서 자동 제외하지 않는다. 튜터가 실제 재시도를 확인한 경우 Rule 8에 따라 근거로 세지 않는다.
8. **채점 실행 기록**: 채점된 exercise의 `Grader Run` 절에서 `.ai/grading/runs/`의 실행 기록에 상대 링크를 둔다. 실행 기록에는 exercise 경로와 입력 snapshot 해시, 튜터와 채점자의 역할, 사용한 공식 CLI 또는 서브에이전트 호출, 런타임이 반환한 세션 또는 호출 식별자, 완료 결과와 출력 위치를 남긴다. 튜터의 자기신고만으로 실행 기록을 만들지 않는다. 검사기는 링크된 기록의 존재와 exercise·입력 해시·채점 결과의 일치를 확인한다. 기록은 독립 실행을 감사할 단서이며 런타임 자체가 위조 불가능하다는 증명은 아니다. 실행 식별자나 원출력을 확보하지 못하면 채점은 `pending`으로 인계한다.
9. **시작 전 알림**: 세션 시작 출력에서 pending exercise를 새 학습보다 먼저 상기시킨다. 각 항목의 대기 이유와 다음 행동은 HANDOFF에 적는다. `study-start.sh`의 현재 `next steps`는 이미 pending 파일을 표시하므로 그 경로를 사용한다. 시간 경과만으로 자동 채점하거나 폐기하지 않는다.

## Implementation boundary

`scripts/check-exercise.py ledger`가 concept별 채점 장부와 `verified_by`, 복습 순서·근거 링크를 대조한다. `study-end.sh`가 이를 호출한다. 선언된 state가 근거보다 높거나 review fail이 빠진 경우 실패로 보고하고, 근거가 더 높은 경우에는 제안만 출력한다. 같은 Problem 해시에는 경고만 낸다. `check`는 입력 snapshot과 실행 기록 링크를 대조하지만 사람의 확인과 런타임 자체의 진위를 증명하지 못한다. `study-start.sh`는 이미 pending 파일을 알린다. 대기 이유와 HANDOFF 내용의 자동 대조는 하지 않으며 튜터가 확인한다. 과거 diagnostic의 `legacy_unverified: true`는 스냅샷을 소급 생성하지 않고 진단 이력으로만 보존하는 이행 표시다.

위 7~9항과 `review_order`, `Review History`는 합의문에서 남긴 쟁점에 대한 템플릿 소유자의 후속 결정이다. 기존 채점 기록에 순서나 실행 기록을 소급 생성하지 않는다. 기존 상태 승격 기록은 자동 이행하지 않고 개별 근거를 검토한다.

## Rejected additions

- 전사 확인 경로를 새 frontmatter 키로 강제하지 않는다. `전사 확인: OK`는 사람의 실제 확인을 증명하지 못하며, 경로 태그만으로 그 신뢰 경계를 강화할 수 없다.
- 초안 검토 날짜와 출처를 concept frontmatter에 중복 저장하지 않는다. 마킹 해제, INBOX 처리 기록, LOG와 Git 이력으로 확인한다. 실제 추적 실패가 발견되면 다시 검토한다.
- 종료 스크립트가 state를 자동 수정하거나 커밋하지 않는다. 검사는 오류를 드러내고, 기록과 판단은 튜터가 맡는다.

## Verification needed

- practice의 당일 pass가 practiced 근거가 되는지, 다른 날 pass와 high 유형으로 verified가 되는지 확인한다.
- diagnostic pass와 self-exam 결과가 state를 올리지 않는지 확인한다.
- `verified_by`에 없는 review fail 뒤 verified 선언이 실패하고, 이후 review pass로 복귀하는지 확인한다.
- 같은 날짜의 상반된 review 결과가 `review_order` 순서대로 판정되고, 중복 순서는 실패하는지 확인한다.
- 동일 Problem 해시는 경고만 내고 상태 근거에서 자동 제외하지 않는지 확인한다.
- 채점 실행 기록의 누락·불일치, pending, 기존 snapshot 없는 기록을 안전하게 처리하는지 확인한다.
