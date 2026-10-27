---
name: parametric-nonparametric-memory
title: Parametric and Non-parametric Memory
state: unseen
requires: [retriever-reader-pipeline]
evidence: [evidence/lewis-2020-rag.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Parametric and Non-parametric Memory

## Definition

## Why It Matters

- G1 — 모델 내부 지식과 갱신 가능한 외부 지식의 책임을 구분한다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. 두 memory의 저장 위치와 갱신 방식을 말할 수 있다.
- [ ] C2. 최신 정책 변경을 모델 재학습과 인덱스 갱신 중 어디에 반영할지 판단할 수 있다.
- [ ] C3. RAG의 latent document marginalization이 무엇을 합산하는지 식의 항으로 식별할 수 있다.
- [ ] C4. 답변의 provenance를 추적하기 위한 최소 기록을 설계할 수 있다.

## Connections

- requires: retriever-reader-pipeline
- used by: passage-fusion
- contrasts with: 외부 문서를 제공했다고 생성 결과가 자동으로 grounded되는 것은 아니다.
