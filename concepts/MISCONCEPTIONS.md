# Misconceptions

<!--
관찰된 오개념의 목록. 장기 학습 지식이다 — 해결돼도 지우지 않는다 (같은 오개념은 재발한다).
- Status: active(아직 관찰됨) | resolved(이후 exercise에서 재발 없음) | recurred(resolved 후 다시 관찰 → 원인 재조사, `debug-to-concept` 스킬)
- 학습자 표현을 그대로 적는다. 튜터가 "틀렸다"고 판단한 것뿐 아니라 학습자가 스스로 "헷갈린다"고 말한 것도 후보다 (Rule 4).
- 튜터는 active 항목을 새 exercise의 Rubric(흔한 오답)에 반영한다. 세션 시작 시 활성 목록은 scripts/study-start.sh가 보여준다.
-->

| Date       | Concept | Misconception (학습자 표현)               | Correct                          | Evidence (exercise)          | Status | Resolved by |
|------------|---------|-------------------------------------------|----------------------------------|------------------------------|--------|-------------|
| <YYYY-MM-DD> | <slug> | "<…라고 생각했다>"                        | <바로잡은 내용 한 줄>            | `exercises/<file>.md`        | active | —           |

## 미확인 후보

- 2026-11-09 U3 독립 채점과 별도 리뷰: "\"잃어버리다\"와 \"분실\"이라는 단어의 유사성을 판단해서 찾을 것이다". DPR을 단어끼리 비교하는 방식으로 한정했을 가능성이다. 질문-passage 벡터 관련성 설명이 부족해 R1 ✗이나 실제 이해를 단정하지 않는다. 근거: `exercises/2026-11-09-sparse-dense-retrieval-condition.md`, R1. R3의 baseline 선택 누락은 답안 누락이며 개념 오해로 단정하지 않는다.

- 2026-11-09 U2: "같은 공간으로 정사영시킬 수 있는 matrix를 만들기 위해서" QP^T를 만든 것인지 질문했다. 점수 행렬과 표현 변환 행렬을 혼동할 수 있는 후보다. QP^T의 각 원소는 이미 인코딩된 질문과 passage의 내적이며 정사영이 아니라고 설명했다. 질문을 확정된 오개념으로 취급하지 않으며 exercise 근거 없음.

- 2026-11-09 U2: "ICT는 문서의 다음 단어를 예측". DPR Introduction의 ICT는 가린 문장이 속한 문서 블록을 찾는 과제다. 다음 토큰 학습과 혼동한 후보이며, 문장이 실제 질문을 얼마나 잘 대리하는지가 원문의 문제 제기다. 대화 피드백 제공, exercise 확인 없음.
- 2026-11-09 U2: "문서 벡터는 추론 단계에서 생성". Inference 절에 기술된 오프라인 passage 벡터 준비와 질문마다 실행되는 question 인코딩을 구분해야 한다. 절 제목 기준의 표현인지 시점 혼동인지 미확인이므로 확정 오개념으로 취급하지 않는다. exercise 확인 없음.

- U1 II.D: "unsupervised learning을 통한 FT에서 새로운 지식을 학습하는데 outperform했다면서". 원문은 RAG가 unsupervised FT보다 우수했다는 비교다. 비교 주체를 반대로 읽은 후보로 기록하고 원문을 대조해 설명했다. exercise 근거 없음.

- 2026-11-08 U1, passage-fusion 관련: "rerank한 뒤에 희석된 내용을 제거하기 위해서 compressing을 진행". 필수 순서로 생각한 것인지, 핵심이 묻히는 원인인 불필요한 내용을 제거한다는 뜻인지 미확인이다. 튜터는 순위 재조정과 문맥 압축의 목적을 구분해 설명했다. 정식 exercise 근거 없음. 확정 오개념 및 concept state 변경 없음.
