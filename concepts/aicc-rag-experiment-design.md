---
name: aicc-rag-experiment-design
title: AICC RAG Experiment Design
state: unseen
requires: [rag-evaluation, answerability-abstention]
evidence: [evidence/yao-2024-tau-bench.md, evidence/katsis-2025-mtrag.md, evidence/rosenthal-2026-mtrag-un.md]
verified_by: []
verified_on:
review_stage: 0
review_due:
last_reviewed:
---

# AICC RAG Experiment Design

## Definition

## Why It Matters

- G3 — RAG 구성 요소의 개선을 실제 상담 행동과 연결해 검증한다.

## Claims

- 해당 학습 unit에서 원 논문 위치와 함께 작성한다.

## Verification Criteria

- [ ] C1. 연구 질문, baseline, 변경 요소, 고정 조건, 반증 조건을 명시할 수 있다.
- [ ] C2. retrieval·generation·대화 결과 지표의 역할을 구분할 수 있다.
- [ ] C3. 작은 합성 상담 세트의 결과표와 신뢰 구간 또는 반복 변동을 계산할 수 있다.
- [ ] C4. 처음 보는 AICC 정책 시나리오에 재현 가능한 비교 프로토콜을 작성할 수 있다.

## Connections

- requires: rag-evaluation, answerability-abstention
- used by: G3 capstone
- contrasts with: 공개 QA 정확도만으로 실제 상담 업무 완료를 대신 측정하지 않는다.
