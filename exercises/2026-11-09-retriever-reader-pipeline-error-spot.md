---
date: 2026-11-09
concept: retriever-reader-pipeline
type: error-spot
purpose: practice
input: text
cost: low
est: 15
actual:
grader: study-grader
review_order:
result: partial
---

# U5: 실패 위치 판별

## Problem

아래는 실제 통신사 규정이나 측정 결과가 아닌 가상 사례다. 문서 집합은 아래 세 passage가 전부이고 내용은 정확하다. Reader는 질문과 전달된 passage만 입력받아 그 안의 답 구간을 선택한다. 검색 결과는 누락이나 잘림 없이 그대로 reader에 전달됐다. 이 연습에서는 답변 유보 기능의 유무는 평가하지 않는다.

| Passage | 내용 |
|---|---|
| P1 | 2026년 X2 요금제의 온라인 신청 철회 가능 기간은 7일이다. |
| P2 | 2026년 X3 요금제의 온라인 신청 철회 가능 기간은 14일이다. |
| P3 | 2025년 X2 요금제의 온라인 신청 철회 가능 기간은 30일이었다. |

질문: "2026년 X2 요금제를 온라인으로 신청했어요. 철회할 수 있는 기간은 며칠인가요?"

| 실행 | 검색 결과이자 reader 입력 | Reader가 선택한 답 |
|---|---|---|
| A | P2만 전달 | P2의 "14일" |
| B | P1, P2 전달 | P2의 "14일" |

1. A와 B에서 각각 확인할 수 있는 실패 위치를 설명하고, passage를 근거로 적어라. 검색과 reading 양쪽을 점검하되 관찰만으로 확정할 수 없는 부분은 구분하라.
2. "두 실행 모두 최종 답이 틀렸으니 reader 자체의 실패가 입증됐다"는 진단이 타당한지 설명하라.

각 항목은 짧게 답해도 된다. 모델 내부의 구체적인 고장 원인을 추정하는 문제는 아니다.

## Rubric

<details>
<summary>답변 후에 연다</summary>

- R1. (필수) A에서는 질문의 상품과 연도에 맞는 P1이 누락됐으므로 검색 실패가 확인된다고 판별한다. — C1, C2
- R2. (필수) A만으로 충분한 근거를 제공했을 때의 reader 능력 실패를 별도로 입증할 수 없음을 설명한다. 답변 유보 기능을 임의로 필수 조건에 추가하지 않는다. — C2
- R3. (필수) B에서는 필요한 P1이 실제 입력에 있으므로 이 질문의 근거 확보는 성공했으며, P2의 값을 고른 reading/선택 단계의 실패가 확인된다고 판별한다. P2가 함께 있다는 이유만으로 검색 실패를 추가하지 않는다. — C1, C2
- R4. (필수) 최종 답의 오류만으로 reader 자체의 실패를 두 경우 모두 확정한다는 진단을 반박하고, 입력 근거 유무를 이유로 구분한다. — C2
- 판정: 필수 항목 모두 충족이면 pass, 일부 충족이나 핵심 구조가 맞으면 partial, 핵심 구조가 틀리거나 답이 없으면 fail. 두 등급 사이면 낮은 쪽.

</details>

## Attempt

1. A는 reader 입력에서 문제 reader가 답을 생성하는 부분에서의 문제는 확정할 수 없다., B는 reader가 답을 선택하는 과정에서 문제, reader에게 입력을 전달하는 부분에서의 문제는 확정할 수 없다.

2. 타당하지 않다. B에서는 가능하나 A에서는 reader의 입력 자체에 문제가 있었기에 진단 불가하다.

전사 확인: OK

## Grading

| Rubric | 판정 | 근거 (Attempt 인용) |
|--------|------|---------------------|
| R1 | ✗ | A의 실패 위치를 입력 쪽으로 짚었다: "A는 reader 입력에서 문제". 그러나 문제가 요구한 passage 근거가 없다. 질문의 상품·연도(2026년 X2)에 맞는 P1이 누락됐다는 이유를 적지 않았다. Rubric은 "P1이 누락됐으므로 검색 실패"라는 근거까지 요구한다. |
| R2 | ✓ | "reader가 답을 생성하는 부분에서의 문제는 확정할 수 없다". A만으로는 reader 능력 실패를 입증할 수 없다고 구분했다. 답변 유보를 조건으로 추가하지 않았다. |
| R3 | ✗ | reading 단계의 실패는 맞게 짚었다: "B는 reader가 답을 선택하는 과정에서 문제". 그런데 검색 쪽은 "reader에게 입력을 전달하는 부분에서의 문제는 확정할 수 없다"고 판단을 미뤘다. Rubric은 필요한 P1이 입력에 있으므로 이 질문의 근거 확보는 성공했다고 판별하기를 요구한다. P1이 입력에 있다는 passage 근거도 없다. |
| R4 | ✓ | "타당하지 않다. B에서는 가능하나 A에서는 reader의 입력 자체에 문제가 있었기에 진단 불가하다". 진단을 반박했고, 입력 근거가 있었는지를 이유로 두 경우를 구분했다. |

- Result: partial
- Misconception: 새 후보(미확정). B에서 필요한 passage가 입력에 있는데도 검색 단계를 "확정할 수 없다"로 남겼다: "reader에게 입력을 전달하는 부분에서의 문제는 확정할 수 없다". 정답 passage가 입력에 있는지를 보고 근거 확보 성공을 판별하는 기준이 서지 않았을 수 있다. 답안을 짧게 쓰다 생략했을 가능성도 있어 단정하지 않는다. MISCONCEPTIONS.md active 표에 일치 항목 없음.

## Grader Run

- [독립 채점 실행 기록](../.ai/grading/runs/2026-11-09-retriever-reader-pipeline-error-spot-run.md)

## Next

- 이후 결정: 학습자가 피드백 반영과 U5 종료를 요청해 [DR-0011](../curriculum/decisions/DR-0011-u5-completion-after-feedback.md)을 적용했다. [보완 정리](../notes/retriever-reader-pipeline.md)의 P1 누락 및 포함에 따른 진단을 검토하고 U5는 완료 처리했다. 아래의 미완료 안내는 변경 전 PLAN 기준의 기록이다. 최초 Attempt와 partial, concept state는 유지하며 다음은 U6 대기다.
- 별도 리뷰: [Codex 채점 리뷰](cross/2026-11-09-retriever-reader-pipeline-error-spot-grading-codex.md)가 항목별 판정과 partial에 모두 동의했다. 호출자의 check도 통과했다. U5는 현재 PLAN의 pass 조건에 미달한다. 답안의 근거 생략과 실제 개념 혼동은 구분하고, R3의 판단 유보를 검색 실패 주장으로 해석하지 않는다.
- State 제안: partial 1회는 Rule 8상 practiced 근거가 될 수 있다. 다만 `concepts/retriever-reader-pipeline.md`는 `state: unseen`이고 Verification Criteria에 `ai:draft` 표시가 남아 있다. 승격 여부는 튜터가 초안 검토를 확인한 뒤 판단한다.
- Review 제안: 없음. verified가 아니므로 review_due가 없다.
- Next exercise: condition(C2). 정답 passage가 입력에 있는 경우와 없는 경우를 섞은 사례를 낸다. 각 실행마다 "정답 근거가 입력에 있는가"를 passage 번호로 먼저 쓰게 하고, 그 다음에 retrieval 성공·실패와 reading 성공·실패를 각각 판별하게 한다(R1·R3 ✗ 보완).
- 채점 실행 메모: 호출 시점에 `.ai/grading/` snapshot(d77a3310…)이 있었다. Grader Run 실행 기록은 호출자가 런타임 출력으로 작성한다. 채점자는 이 절을 채우지 않았다.
- 엄격도: 01-u2·U3와 같은 기준이다. Rubric이 판별의 근거(passage)나 성공 판정을 명시적으로 요구할 때, 위치만 짚거나 판단을 미룬 답은 ✗로 했다.
