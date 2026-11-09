---
date: 2026-11-09
concept: sparse-dense-retrieval
type: condition
purpose: practice
input: text
cost: low
est: 15
actual:
grader: study-grader
review_order:
result: partial
---

# U3: 상담 정책 검색 방식 선택

## Problem

아래는 설명용 가상 상황이다. 실제 검색 순위나 성능을 측정한 결과는 주어지지 않았다.

통신사 정책 문서에는 상품 코드가 ZP-X2와 ZP-X3로 구분되어 있다. X2의 정책을 X3에 적용하면 안 된다. 문서는 "분실 시 회선 일시정지"라는 표현을 쓴다.

고객 질문: "ZP-X2 쓰는데 폰을 잃어버렸어요. 찾을 때까지 잠깐 막아둘 수 있나요?"

1. BM25와 DPR이 이 질문에 관련된 문서를 찾을 때 각각 어떤 신호를 사용하는지 설명하라. 각 방식에서 주의할 실패 가능성을 이 사례와 연결해 하나씩 적어라.
2. 첫 비교 실험에서 BM25와 DPR 중 어느 것을 baseline으로 먼저 사용할지 선택하고 이유를 설명하라. 선택하지 않은 방식도 어떤 이유로 비교할 가치가 있는지 적어라. 실제 결과를 보지 않고 성능 우위를 확정하지 말라.

각 항목은 짧은 문장으로 답해도 된다. 한 가지 고정된 모델 선택을 정답으로 요구하지 않는다.

## Rubric

<details>
<summary>답변 후에 연다</summary>

- R1. (필수) BM25의 어휘 일치 신호와 DPR의 학습된 질문-passage 벡터 관련성을 구분한다. — C1
- R2. (필수) 어휘 불일치와 상품 코드 혼동이라는 서로 다른 위험을 두 방식의 한계와 타당하게 연결한다. Dense가 항상 코드 차이를 무시하거나 BM25가 반드시 실패한다고 단정하지 않는다. — C2
- R3. (필수) baseline 선택을 과제의 요구와 연결하고, 다른 방식의 비교 가치를 설명한다. 실험하지 않은 우위를 확정하지 않는다. — C4
- 판정: 필수 항목 모두 충족 시 pass. 일부 충족은 partial, 전부 미충족은 fail. partial은 unit 통과가 아니다.
- 주의: 앞선 ICT 및 점수 행렬 문답은 이 문제의 채점 대상이 아니다. 현재 질문에 대한 관련성만 평가한다.

</details>

## Attempt

1. BM25는 ZP-X2는 찾고 나머지 일치하는 단어를 가지는 passage를 찾을 거고 DPR은 "폰을 잃어버렸다"에서 "잃어버리다"와 "분실"이라는 단어의 유사성을 판단해서 찾을 것이다. BM25는 "분실"이라는 단어를 못 찾을 가능성이 있다. 반대로 DPR은 BM25보다 ZP-X3의 정책을 ZP-X2의 정책으로 혼동할 가능성이 높다.

2. 생성 모델은 고정하고 어떤 대상을 검색하는지를 먼저 비교할 거 같다. 1번에서 설명한 내용의 연장선으로 BM25는 맥락성을 고려해서 문장을 찾는지, 그리고 DPR은 정책의 대상을 혼동하지 않는지를 먼저 검사한다.

전사 확인: OK

## Grading

| Rubric | 판정 | 근거 (Attempt 인용) |
|--------|------|---------------------|
| R1 | ✗ | BM25 쪽은 어휘 일치다: "BM25는 ZP-X2는 찾고 나머지 일치하는 단어를 가지는 passage를 찾을 거고". 그런데 DPR 쪽은 단어끼리의 유사성으로만 적었다: “"잃어버리다"와 "분실"이라는 단어의 유사성을 판단해서 찾을 것이다”. 학습된 encoder가 질문과 passage를 각각 벡터로 바꾸고 그 벡터로 관련성을 매긴다는 신호가 없다. Rubric이 요구한 "학습된 질문-passage 벡터 관련성"과 구분되지 않는다. |
| R2 | ✓ | 어휘 불일치는 BM25에 연결했다: “BM25는 "분실"이라는 단어를 못 찾을 가능성이 있다”. 상품 코드 혼동은 DPR에 연결했다: "DPR은 BM25보다 ZP-X3의 정책을 ZP-X2의 정책으로 혼동할 가능성이 높다". 둘 다 "가능성"으로 적었고 반드시 실패한다고 단정하지 않았다. |
| R3 | ✗ | BM25와 DPR 중 무엇을 baseline으로 먼저 쓸지 고르지 않았다: "생성 모델은 고정하고 어떤 대상을 검색하는지를 먼저 비교할 거 같다". 두 방식을 각각 점검하는 계획만 있다: "BM25는 맥락성을 고려해서 문장을 찾는지, 그리고 DPR은 정책의 대상을 혼동하지 않는지를 먼저 검사한다". 선택을 과제 요구(상품 코드 구분)와 연결한 이유가 없다. |

- Result: partial
- Misconception: 새 후보(미확정). DPR의 관련성 신호를 단어끼리의 유사성으로 서술했다: “"잃어버리다"와 "분실"이라는 단어의 유사성을 판단해서 찾을 것이다”. 질문 전체와 passage 전체를 벡터로 비교한다는 점과 혼동했을 수 있다. MISCONCEPTIONS.md active 항목과 일치하는 것은 없다.

## Grader Run

- [독립 채점 실행 기록](../.ai/grading/runs/2026-11-09-sparse-dense-retrieval-condition-run.md)

## Next

- 이후 결정: 학습자 요청으로 [DR-0010](../curriculum/decisions/DR-0010-u3-completion-after-feedback.md)의 U3 종료 기준을 적용했다. 피드백 보완과 학습자 검토를 마쳐 U3는 완료다. 아래의 "U3 미통과"와 최초 Rubric은 변경 전 기준의 기록이며, 이 exercise의 partial 및 concept state는 유지한다. 다음 unit은 U4 대기다.
- 학습자 요청에 따라 피드백 후 보완 정리를 [학습 노트](../notes/sparse-dense-retrieval.md)의 "검토 후 보완 정리"에 반영했다. DPR의 질문-passage 벡터 관련성과 동일한 Naive RAG 안에서 BM25 baseline 대 DPR 비교라는 구성을 명시했다. 원래 Attempt와 partial 판정은 유지한다.
- 피드백 후 학습자 보충: DPR을 "Passage의 유사성"으로 표현하고 Naive RAG를 baseline으로 제안했다. 튜터는 질문-passage 벡터의 비교와 처리 흐름/검색 방법의 층위를 구분해 설명했다. 자세한 기록은 `notes/sparse-dense-retrieval.md`의 U3 피드백 후 보충 설명에 있다. 원래 Attempt와 partial은 유지하며 재채점하지 않는다.
- 채점 리뷰: [별도 Codex 리뷰](cross/2026-11-09-sparse-dense-retrieval-condition-grading-codex.md)가 세 항목과 partial에 모두 동의했다. 호출자의 check도 통과했다. 초안 검토는 아직 미확인이므로 concept state는 unseen 유지, U3는 미통과다.
- State 제안: partial 1회는 Rule 8에 따라 practiced 근거가 될 수 있다. 다만 `concepts/sparse-dense-retrieval.md`는 `state: unseen`이고 `ai:draft` 표시가 남아 있다. 승격 여부는 튜터가 초안 검토를 확인한 뒤 판단한다.
- Review 제안: 없음. verified가 아니므로 review_due도 없다.
- Next exercise: recall(C1). R1 ✗ 때문에 DPR이 무엇을 입력받아 무엇을 출력하는지 다시 확인한다. encoder 두 개, 질문 벡터와 passage 벡터, 그 둘의 내적 점수를 말하게 한다. 이어서 condition(C4)을 낸다. R3 ✗ 때문에 baseline을 하나 명시적으로 고르고 과제 요구와 연결하라는 요구를 문제에 분명히 넣는다.
- 채점 실행 메모: 채점자 런타임에서 Python과 awk 실행 권한이 거부되었다. 그래서 snapshot 해시 대조와 `check-exercise.py check`를 실행하지 못했다. Grader Run 실행 기록은 호출자가 작성한 뒤 check를 실행한다.
- 엄격도: 이전 판정(01-u2)과 같은 기준으로 판정했다. Rubric이 요구한 구분을 명시하지 않고 막연하게 말한 부분은 ✗로 했다.
