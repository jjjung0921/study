---
name: passage-fusion
title: Passage Fusion
state: unseen
requires: [parametric-nonparametric-memory]
evidence: [evidence/izacard-2021-fid.md, evidence/liu-2024-lost-middle.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Passage Fusion

## Definition

## Why It Matters

- G1 — 여러 문서에 흩어진 근거를 생성 모델이 결합하는 방식을 비교한다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. early concatenation과 Fusion-in-Decoder의 정보 결합 위치를 설명할 수 있다.
- [ ] C2. 근거 순서와 문맥 길이가 답변에 영향을 줄 수 있는 사례를 판별할 수 있다.
- [ ] C3. top-k와 입력 길이에 따른 계산량의 상대 변화를 설명할 수 있다.
- [ ] C4. 두 정책 문서를 함께 써야 하는 상담 질문에 fusion 전략을 선택할 수 있다.

## Connections

- requires: parametric-nonparametric-memory
- used by: retrieval-generation-failures
- contrasts with: 검색 recall이 높아도 생성 모델이 모든 passage를 고르게 사용하지는 않는다.
