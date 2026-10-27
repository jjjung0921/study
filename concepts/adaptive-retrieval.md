---
name: adaptive-retrieval
title: Adaptive Retrieval
state: unseen
requires: [retrieval-generation-failures, rag-evaluation]
evidence: [evidence/asai-2024-self-rag.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Adaptive Retrieval

## Definition

## Why It Matters

- G2·G3 — 모든 질문에 같은 방식으로 검색하는 고정 파이프라인의 한계를 다룬다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. retrieve 여부·시점·횟수를 적응적으로 결정한다는 뜻을 설명할 수 있다.
- [ ] C2. 검색이 도움이 되거나 해가 될 수 있는 질문을 판별할 수 있다.
- [ ] C3. 검색 비용과 품질을 함께 보는 간단한 목적함수를 구성할 수 있다.
- [ ] C4. AICC 질문 유형별 retrieval policy를 제안하고 반증 조건을 적을 수 있다.

## Connections

- requires: retrieval-generation-failures, rag-evaluation
- used by: conversational-query-context
- contrasts with: adaptive retrieval은 생성 후 자기검증 전체와 같은 개념이 아니다.
