---
name: rag-evaluation
title: RAG Evaluation
state: unseen
requires: [retrieval-generation-failures]
evidence: [evidence/es-2024-ragas.md, evidence/saxton-2024-ares.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# RAG Evaluation

## Definition

## Why It Matters

- G2 — retrieval과 generation을 별도 지표로 검증하는 실험 계약의 핵심이다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. context relevance, faithfulness, answer correctness의 평가 대상을 구분할 수 있다.
- [ ] C2. reference-free judge가 필요한 상황과 사람 검증이 필요한 상황을 판단할 수 있다.
- [ ] C3. Recall@k, precision, faithfulness 표본 점수를 계산할 수 있다.
- [ ] C4. 한 지표가 좋아졌지만 사용자 결과가 나빠지는 반례를 설계할 수 있다.

## Connections

- requires: retrieval-generation-failures
- used by: adaptive-retrieval, conversational-query-context, aicc-rag-experiment-design
- contrasts with: 자동 평가 점수는 사람 평가와의 일치가 확인되어야 한다.
