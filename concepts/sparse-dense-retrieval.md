---
name: sparse-dense-retrieval
title: Sparse and Dense Retrieval
state: unseen
requires: []
evidence: [evidence/karpukhin-2020-dpr.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Sparse and Dense Retrieval

## Definition

<!-- ai:draft -->
검색기는 질문과 문서 집합을 입력받아 관련성 점수에 따라 일부 문서를 반환한다. BM25 같은 전통적인 sparse 검색은 단어 일치와 단어별 가중치를 사용한다. Dense 검색은 학습된 encoder로 질문과 문서를 비교적 낮은 차원의 밀집 벡터로 표현하여 관련성을 계산한다. DPR은 두 encoder의 출력 벡터 간 내적을 사용한다. Sparse와 dense라는 이름은 표현의 형태를 가리키며, 모든 sparse 방법이 비학습 방식인 것은 아니다.
<!-- /ai:draft -->

## Why It Matters

- G1 — RAG가 답변 전에 어떤 근거 후보를 선택하는지 이해하는 출발점이다.

## Claims

<!-- ai:draft -->
- [fact] BM25 같은 단어 기반 검색은 어휘가 다른 동의어와 바꿔 쓴 표현을 매칭하는 데 어려움이 있을 수 있다. 근거: `evidence/karpukhin-2020-dpr.md`, Section 1, p.6769.
- [fact] DPR은 질문과 passage를 별도 encoder로 벡터화하고 내적 점수로 검색한다. 근거: 같은 evidence, Section 3.1, Eq. (1), pp.6770-6771.
- [fact] 관련 및 무관 passage를 비교하는 목적함수로 DPR의 encoder를 학습한다. 근거: 같은 evidence, Section 3.2, Eq. (2), p.6771.
- [derived] Dense 점수는 학습된 관련성 신호이며 사실의 정확성이나 정책 적용 여부를 보장하지 않는다. 근거: 같은 evidence, Sections 3.1-3.2의 점수 정의와 학습 목표. AICC의 실패 예시는 설명용 가설이며 별도 검증이 필요하다.
<!-- /ai:draft -->

## Verification Criteria

<!-- ai:draft -->

- [ ] C1. lexical matching과 learned dense representation의 입력·출력을 말할 수 있다.
- [ ] C2. 어휘 불일치와 의미적 모호성이 있는 사례에서 두 검색 방식의 실패 가능성을 판별할 수 있다.
- [ ] C3. 작은 검색 결과에서 Recall@k를 계산할 수 있다.
- [ ] C4. AICC 정책 질문에 적합한 검색 baseline을 선택하고 이유를 설명할 수 있다.
<!-- /ai:draft -->

## Connections

- requires: 없음
- used by: retriever-reader-pipeline
- contrasts with: sparse retrieval은 토큰 일치 신호, dense retrieval은 학습된 표현 유사도를 주로 사용한다.
