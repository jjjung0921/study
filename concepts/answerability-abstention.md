---
name: answerability-abstention
title: Answerability and Abstention
state: unseen
requires: [conversational-query-context]
evidence: [evidence/katsis-2025-mtrag.md, evidence/rosenthal-2026-mtrag-un.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Answerability and Abstention

## Definition

## Why It Matters

- G3 — 근거가 부족한 상담에서 추측 대신 확인·보류·전환을 선택하는 기준이 필요하다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. unanswerable, underspecified, unclear 상황을 구분할 수 있다.
- [ ] C2. 답변·추가 질문·abstention 중 적절한 행동을 판별할 수 있다.
- [ ] C3. coverage와 error risk의 trade-off를 혼동행렬로 계산할 수 있다.
- [ ] C4. 상담사 전환 기준과 전달할 evidence package를 설계할 수 있다.

## Connections

- requires: conversational-query-context
- used by: aicc-rag-experiment-design
- contrasts with: 낮은 retrieval score 하나만으로 답변 불가능성을 확정하지 않는다.
