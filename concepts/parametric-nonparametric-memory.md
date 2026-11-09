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

<!-- ai:draft -->
Parametric memory는 학습된 가중치에 분산되어 저장된 지식을 뜻한다. 원 RAG 논문은 BART generator의 가중치를 이렇게 부른다. Non-parametric memory는 검색으로 접근하는 외부 지식 저장소이며, 원 논문에서는 Wikipedia passage의 dense vector index다. 검색기의 encoder도 학습된 가중치를 가지므로 non-parametric이라는 이름이 전체 검색 모듈에 학습 파라미터가 없다는 뜻은 아니다.
<!-- /ai:draft -->

## Why It Matters

- G1 — 모델 내부 지식과 갱신 가능한 외부 지식의 책임을 구분한다.

## Claims

<!-- ai:draft -->
- [fact] 원 RAG는 DPR로 초기화한 검색기와 BART-large generator를 결합한다. 근거: `evidence/lewis-2020-rag.md`, Sections 2.2-2.3 p.3.
- [fact] BART generator 가중치와 Wikipedia 문서 색인은 각각 parametric 및 non-parametric memory다. 근거: 같은 evidence, Introduction 및 Sections 2.2-2.3, pp.2-3.
- [fact] RAG-Sequence는 출력 전체에 대한 문서별 확률을 합산하고, RAG-Token은 토큰별 조건부 확률을 문서에 대해 합산한다. 근거: 같은 evidence, Section 2.1, p.3.
- [fact] 원 논문의 학습은 document encoder와 index를 고정하고 query encoder와 generator를 조정한다. 근거: 같은 evidence, Section 2.4, pp.3-4.
- [derived] 최신 정책 반영을 위해 외부 문서와 일관된 색인을 갱신할 수 있지만, 생성기가 이를 정확히 활용했는지는 별도 평가해야 한다. 근거: 같은 evidence, Introduction p.2 및 두 memory를 결합하는 구조.
<!-- /ai:draft -->

## Verification Criteria

<!-- ai:draft -->

- [ ] C1. 두 memory의 저장 위치와 갱신 방식을 말할 수 있다.
- [ ] C2. 최신 정책 변경을 모델 재학습과 인덱스 갱신 중 어디에 반영할지 판단할 수 있다.
- [ ] C3. RAG의 latent document marginalization이 무엇을 합산하는지 식의 항으로 식별할 수 있다.
- [ ] C4. 답변의 provenance를 추적하기 위한 최소 기록을 설계할 수 있다.
<!-- /ai:draft -->

## Connections

- requires: retriever-reader-pipeline
- used by: passage-fusion
- contrasts with: 외부 문서를 제공했다고 생성 결과가 자동으로 grounded되는 것은 아니다.
