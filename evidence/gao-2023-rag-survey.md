---
name: gao-2023-rag-survey
title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
type: paper
ref: "Gao et al. (2023), arXiv:2312.10997, https://arxiv.org/abs/2312.10997"
concepts: []
status: unread
---

# Retrieval-Augmented Generation for Large Language Models: A Survey

## Access and Bibliography

- 공식 기록: https://arxiv.org/abs/2312.10997 — 제목, 저자 Yunfan Gao 외, 최초 제출일 2023-12-18 확인.
- 원문 PDF: https://arxiv.org/pdf/2312.10997 — 2026-11-02 접근 및 첫 페이지 텍스트 추출 성공(21쪽, arXiv v5, 2024-03-27).
- 2023은 최초 제출 연도이며 확인한 PDF는 2024년 개정판이다.

## What It Supports

- Phase 02 U1의 전체 지도 읽기 자료. 아래 근거는 원문에서 확인한 범위만 기록한다. 개별 concept Claim의 세부 근거는 해당 unit에서 다시 확인한다.

## Key Statements

- [fact] Naive RAG의 대표 흐름은 문서 분할과 색인, 질의에 맞는 상위 문서 검색, 질의와 검색 문서를 함께 넣은 답변 생성의 세 단계다. 근거: arXiv:2312.10997v5, p.2 Section II, p.3 Figure 2와 Section II.A.
- [fact] 논문은 Naive, Advanced, Modular RAG를 구분한다. Advanced는 검색 전과 검색 후 처리를 개선하고, Modular는 순차 흐름 외 반복 및 적응적 검색도 다룬다. 근거: p.2 Section II, p.3-4 Sections II.B-C와 Figure 3.
- [fact] Naive RAG의 문제로 관련 문서 누락, 검색 근거로 뒷받침되지 않는 생성, 중복 또는 부조화된 문맥 결합을 따로 설명한다. 근거: p.3 Section II.A의 Retrieval Challenges, Generation Difficulties, Augmentation Hurdles.
- [fact] 평가는 검색 품질과 생성 품질을 별도 대상으로 다룬다. 검색에는 Hit Rate, MRR, NDCG 등을, 생성에는 faithfulness와 relevance 등을 언급한다. 근거: p.12 Section VI.B, p.14 Table III.
- [fact] 대화 이력은 생성 prompt에 넣을 수 있다고 서술하지만, 이 문장만으로 다중 턴 평가 성능은 확인할 수 없다. 근거: p.3 Section II.A의 Generation 단락.

## U1 Learning Map

- [derived] 검색 축: 색인과 retrieval에서 필요한 문서를 찾는지 본다 (p.3 Figure 2, Section II.A).
- [derived] 결합과 생성 축: 검색 결과를 질의와 연결해 답을 만들고, 근거를 제대로 쓰는지 본다 (p.3 Section II.A, p.4 Section II.B).
- [derived] 평가 축: 검색 결과와 최종 답변을 서로 다른 대상으로 측정한다 (p.12 Section VI.B).
- [derived] 대화 축: 이전 턴의 맥락이 질의와 prompt에 어떤 영향을 주는지 후속 Phase에서 구체적으로 검증한다. 이 survey는 대화 이력을 prompt에 넣을 수 있다고 언급한다 (p.3 Section II.A). 이 네 축은 논문 자체의 분류가 아니라 현재 커리큘럼의 읽기 지도다.

## Reading Notes

- 2026-11-08: v5 p.4 II.B와 p.10 IV.A 확인. II.B는 post-retrieval의 주요 방법으로 reranking과 compression을 소개하고 관련 내용을 prompt 양 끝으로 재배치하는 전략을 언급한다. 두 방법을 필수 순서로 규정하지 않는다. 정보 과부하는 불필요한 내용이 핵심에 대한 집중을 희석하는 문제로 설명한다.

- 2026-11-08: 원문 v5 p.3 Section II.A의 Generation Difficulties를 재확인했다. hallucination을 "content not supported by the retrieved context"로 설명한다. 올바른 chunk가 검색되었다는 조건은 명시하지 않는다. 이는 생성 결과의 문맥 충실성에 관한 기술이며, 검색과 무관한 생성 모델만의 원인이라고 입증한 문장은 아니다.

- 2026-11-02: 공식 페이지의 서지와 PDF 첫 페이지만 확인. 본문 미독.
- 2026-11-07: 튜터가 원문 p.2-4와 p.12, p.14의 관련 대목을 확인해 U1 지도를 작성했다. 학습자의 원문 읽기 여부는 아직 확인하지 않았다.
