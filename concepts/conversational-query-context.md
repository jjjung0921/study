---
name: conversational-query-context
title: Conversational Query Context
state: unseen
requires: [rag-evaluation, adaptive-retrieval]
evidence: [evidence/katsis-2025-mtrag.md, evidence/rosenthal-2026-mtrag-un.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Conversational Query Context

## Definition

## Why It Matters

- G3 — 후속 질문의 생략·지시어·의도 변화를 검색 질의로 복원해야 한다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. standalone·non-standalone 질문과 대화 이력의 역할을 설명할 수 있다.
- [ ] C2. 이력 전체 사용, 선택, query rewriting이 필요한 사례를 판별할 수 있다.
- [ ] C3. 대화 턴별 retrieval 지표의 변화를 계산할 수 있다.
- [ ] C4. AICC 후속 질문을 독립 질의로 재구성하고 보존해야 할 조건을 적을 수 있다.

## Connections

- requires: rag-evaluation, adaptive-retrieval
- used by: answerability-abstention
- contrasts with: 대화 이력을 전부 붙이는 것과 필요한 맥락을 선택하는 것은 다르다.
