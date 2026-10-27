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

## Why It Matters

- G1 — RAG가 답변 전에 어떤 근거 후보를 선택하는지 이해하는 출발점이다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. lexical matching과 learned dense representation의 입력·출력을 말할 수 있다.
- [ ] C2. 어휘 불일치와 의미적 모호성이 있는 사례에서 두 검색 방식의 실패 가능성을 판별할 수 있다.
- [ ] C3. 작은 검색 결과에서 Recall@k를 계산할 수 있다.
- [ ] C4. AICC 정책 질문에 적합한 검색 baseline을 선택하고 이유를 설명할 수 있다.

## Connections

- requires: 없음
- used by: retriever-reader-pipeline
- contrasts with: sparse retrieval은 토큰 일치 신호, dense retrieval은 학습된 표현 유사도를 주로 사용한다.
