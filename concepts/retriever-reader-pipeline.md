---
name: retriever-reader-pipeline
title: Retriever–Reader Pipeline
state: unseen
requires: [sparse-dense-retrieval]
evidence: [evidence/karpukhin-2020-dpr.md, evidence/lewis-2020-rag.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# Retriever–Reader Pipeline

## Definition

## Why It Matters

- G1 — 검색 실패와 답변 생성 실패를 분리해 진단하는 시스템 경계다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. query, corpus, retrieved passages, reader output의 흐름을 그릴 수 있다.
- [ ] C2. 사례별 오류를 retrieval·reading·둘 다로 분류할 수 있다.
- [ ] C3. top-k 변화가 reader 입력과 계산량에 미치는 영향을 설명할 수 있다.
- [ ] C4. 상담 질문 하나를 재현 가능한 retriever–reader 입력과 출력으로 정의할 수 있다.

## Connections

- requires: sparse-dense-retrieval
- used by: parametric-nonparametric-memory, retrieval-generation-failures
- contrasts with: end-to-end 정확도만 보면 어느 단계가 실패했는지 알 수 없다.
