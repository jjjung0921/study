---
name: grading-history
description: study-grader가 RAG subject에서 내린 이전 판정 목록 — 엄격도를 일관되게 맞추는 기준
metadata:
  type: project
---

## 01-u2-prior-knowledge.md — fail (2026-11-02, 진단)
세 항목 모두 ✗. 이 문제의 Rubric은 "모두 충족 = pass, 일부 = partial, 없음 = fail"로 정해져 있다.
엄격도 기준: 개념을 막연히 다시 말한 것("자연스러운 문장이 되도록 돕는다")은 ✗로 했다. 비보장을 짐작으로만 내비친 것("확률이 높을 것")도 Rubric이 요구한 명시적 구분이 아니라서 ✗로 했다. 결과 값(문서 B)이 없는 Python 답도 ✗로 했다.
Why: 이후 채점이 이 엄격도와 어긋나는지 비교하기 위해.
How to apply: 같은 유형의 "막연한 다시 말하기"는 ✗로 유지한다.

## 2026-11-09-sparse-dense-retrieval-condition.md — partial (2026-11-09, practice)
R1 ✗ · R2 ✓ · R3 ✗.
엄격도 기준: DPR을 단어 대 단어 유사성으로만 서술하고 encoder·벡터·질문-passage 수준을 언급하지 않은 답은 R1 ✗로 했다. BM25와 DPR을 둘 다 점검하겠다고만 하고 baseline을 하나 고르지 않은 답은 R3 ✗로 했다. 실패 가능성을 "가능성"으로 표현한 것은 단정이 아니라서 ✓로 했다.
How to apply: 선택을 요구하는 문항에서 선택이 없으면 ✗로 한다. 방법의 신호는 Rubric이 지정한 수준(표현·입출력)까지 말해야 ✓로 한다.

## 2026-11-09-retriever-reader-pipeline-error-spot.md — partial (2026-11-09, practice)
R1 ✗ · R2 ✓ · R3 ✗ · R4 ✓.
엄격도 기준: 실패 위치만 짚고("reader 입력에서 문제") 문제가 요구한 passage 근거(P1 누락)를 대지 않은 답은 R1 ✗로 했다. 정답 passage가 입력에 있는데 검색을 "확정할 수 없다"로 남긴 답은 R3 ✗로 했다. Rubric은 근거 확보 성공이라는 판별을 요구한다. "확정할 수 없다"는 구분이 Rubric의 비입증 항목과 맞는 자리에서는 ✓로 했다(R2).
How to apply: "passage를 근거로" 같은 근거 요구가 문제에 있으면, 근거 없이 위치만 맞힌 답은 ✗로 한다. 학습자는 짧게 답하는 경향이 있다(U3, U5). 근거·선택 누락이 두 번 반복됐으며 개념 오해인지는 미확정이다.
