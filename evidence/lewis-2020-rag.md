---
name: lewis-2020-rag
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
type: paper
ref: "Lewis et al. (2020), arXiv:2005.11401, https://arxiv.org/abs/2005.11401"
concepts: [parametric-nonparametric-memory, retriever-reader-pipeline]
status: unread
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Access and Bibliography

- 공식 기록: https://arxiv.org/abs/2005.11401 — 제목, 저자 Patrick Lewis 외, 최초 제출일 2020-05-22 확인.
- 원문 PDF: https://arxiv.org/pdf/2005.11401 — 2026-11-02 접근 및 첫 페이지 텍스트 추출 성공(19쪽, arXiv v4, 2021-04-12).
- 2020은 최초 제출 연도이며 확인한 PDF는 2021년 개정판이다.

## What It Supports

- Phase 02 U6의 원 RAG 읽기 자료. 아래는 튜터가 원문 v4에서 확인한 범위다.

## Key Statements

- [fact] 논문의 parametric memory는 BART generator의 가중치이며, non-parametric memory는 Wikipedia passage의 dense vector index다. Introduction p.2, Sections 2.2-2.3 p.3.
- [fact] 검색기는 사전학습된 DPR로 초기화하고, 생성기는 BART-large를 사용한다. Sections 2.2-2.3, p.3.
- [fact] RAG-Sequence는 출력 전체에 동일한 latent document를 조건으로 한 확률을 계산한 뒤 문서에 대해 합산한다. RAG-Token은 각 토큰의 조건부 확률을 문서에 대해 합산한다. 두 방식 모두 검색된 top-k 집합을 사용하며, 토큰마다 검색을 새로 수행한다고 설명하지 않는다. Section 2.1, p.3의 두 수식.
- [fact] 이 논문의 학습에서는 passage encoder와 index를 고정하고 query encoder와 BART generator를 fine-tuning한다. Section 2.4, pp.3-4.
- [fact] 외부 non-parametric memory를 교체해 지식을 갱신할 수 있음을 논문이 다룬다. Introduction p.2. 모든 출력이 갱신 문서를 정확히 따르거나 환각이 제거된다는 보장은 아니다.

## Reading Notes

- 2026-11-02: 공식 페이지의 서지와 PDF 첫 페이지만 확인. 본문 미독.
- 2026-11-09: 튜터가 v4 Introduction, Figure 1, Sections 2.1-2.4를 확인했다. 학습자의 해당 절 읽기는 미확인이며 성능 결과를 재현한 것은 아니다.
