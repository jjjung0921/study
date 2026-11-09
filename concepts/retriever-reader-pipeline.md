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

<!-- ai:draft -->
Retriever는 질문과 문서 집합에서 관련 passage 후보를 선택한다. Reader는 질문과 선택된 passage를 받아 답을 산출한다. DPR 논문의 reader는 passage 안의 정답 span을 추출한다. 생성형 RAG에서는 generator가 입력된 근거를 활용해 답변 텍스트를 생성하며, 추출형 reader와 동일한 출력 제약을 갖는다고 가정하지 않는다.
<!-- /ai:draft -->

## Why It Matters

- G1 — 검색 실패와 답변 생성 실패를 분리해 진단하는 시스템 경계다.

## Claims

<!-- ai:draft -->
- [fact] 검색으로 후보를 좁힌 뒤 reader가 정답을 추출하는 두 단계 구조를 사용한다. 근거: `evidence/karpukhin-2020-dpr.md`, Sections 1-2, pp.6769-6770.
- [fact] 생성형 RAG의 기본 흐름은 질문과 검색된 문서를 생성기에 제공해 답을 만드는 것이다. 근거: `evidence/gao-2023-rag-survey.md`, Section II.A와 Figure 2, p.3.
- [derived] 최종 답변 오류만으로 검색기와 reader 중 어느 쪽이 실패했는지 확정할 수 없다. 질문에 필요한 근거가 실제 reader 입력에 있었는지와 출력이 그 근거를 사용했는지를 함께 확인해야 한다. 근거: 위 두 단계 구조 및 survey Section II.A의 문제 구분.
- [derived] 상위 k개를 그대로 제공한다면 k 증가는 reader가 받는 passage 수를 늘린다. 입력 토큰과 처리 비용의 변화는 passage 길이, 압축, 모델 구조에 의존하며 답변 품질 향상은 보장되지 않는다. 근거: DPR Section 2의 후보 집합 정의 및 survey Section II.B의 정보 과부하 설명.
<!-- /ai:draft -->

## Verification Criteria

<!-- ai:draft -->

- [ ] C1. query, corpus, retrieved passages, reader output의 흐름을 그릴 수 있다.
- [ ] C2. 사례별 오류를 retrieval·reading·둘 다로 분류할 수 있다.
- [ ] C3. top-k 변화가 reader 입력과 계산량에 미치는 영향을 설명할 수 있다.
- [ ] C4. 상담 질문 하나를 재현 가능한 retriever–reader 입력과 출력으로 정의할 수 있다.
<!-- /ai:draft -->

## Connections

- requires: sparse-dense-retrieval
- used by: parametric-nonparametric-memory, retrieval-generation-failures
- contrasts with: end-to-end 정확도만 보면 어느 단계가 실패했는지 알 수 없다.
