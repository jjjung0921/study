---
name: retrieval-generation-failures
title: Retrieval and Generation Failures
state: unseen
requires: [retriever-reader-pipeline, passage-fusion]
evidence: [evidence/asai-2024-self-rag.md, evidence/liu-2024-lost-middle.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Retrieval and Generation Failures

## Definition

## Why It Matters

- G1·G2 — 개선안을 고르기 전에 실패가 발생한 단계를 식별해야 한다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. missing evidence, noisy evidence, conflicting evidence, unsupported generation을 구분할 수 있다.
- [ ] C2. 검색 결과와 답변이 주어진 사례를 실패 유형으로 분류할 수 있다.
- [ ] C3. 오류 유형별 빈도표를 계산할 수 있다.
- [ ] C4. 새로운 상담 로그에 적용 가능한 오류 taxonomy를 만들 수 있다.

## Connections

- requires: retriever-reader-pipeline, passage-fusion
- used by: rag-evaluation, adaptive-retrieval
- contrasts with: hallucination이라는 한 단어로 모든 실패 원인을 합치지 않는다.
