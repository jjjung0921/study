---
name: karpukhin-2020-dpr
title: "Dense Passage Retrieval for Open-Domain Question Answering"
type: paper
ref: "Karpukhin et al. (2020), EMNLP, DOI:10.18653/v1/2020.emnlp-main.550, https://aclanthology.org/2020.emnlp-main.550/"
concepts: [sparse-dense-retrieval, retriever-reader-pipeline]
status: unread
---

# Dense Passage Retrieval for Open-Domain Question Answering

## Access and Bibliography

- 공식 기록: https://aclanthology.org/2020.emnlp-main.550/ — 제목, 저자 Vladimir Karpukhin 외, EMNLP 2020, DOI 확인.
- 원문 PDF: https://aclanthology.org/2020.emnlp-main.550.pdf — 2026-11-02 접근 및 첫 페이지 텍스트 추출 성공(13쪽).

## What It Supports

- Phase 02 U2의 sparse·dense retrieval 읽기 자료. 아래는 튜터가 원문 관련 절에서 확인한 범위다.

## Key Statements

- [fact] DPR의 end-to-end QA reader는 BERT-base uncased 기반이다. 검색된 passage마다 선택 점수와 정답 span의 시작 및 끝 확률을 계산하고, 선택 점수가 가장 높은 passage의 최상위 span을 최종 답으로 고른다. 생성형 decoder가 새 답변 문장을 쓰는 방식이 아니다. Section 6.1, p.6775 (PDF 7쪽), Eqs. (3)-(5).
- [fact] DPR 논문은 검색기가 작은 passage 집합을 고른 뒤 reader가 정답을 추출하는 두 단계 구조를 설명한다. 논문 과제의 답은 passage 내 span으로 제한된다. Section 1, p.6769 및 Section 2, p.6770.
- [fact] 이 논문의 top-k retrieval accuracy는 검색 집합에 정답 span을 포함한 passage가 있는 질문의 비율이다. 모든 관련 passage 중 회수한 비율인 일반적인 Recall@k와 구분한다. Section 2, p.6770.
- [fact] TF-IDF와 BM25는 단어 일치를 사용하는 가중 sparse 표현으로 설명되며, 어휘가 다른 동의어와 바꿔 쓴 표현이 검색의 어려움이 될 수 있다. Section 1, p.6769.
- [fact] DPR은 질문과 passage를 각각 encoder로 벡터화하고 내적으로 관련성 점수를 계산한다. Section 3.1, pp.6770-6771, Eq. (1).
- [fact] DPR은 관련 passage와 무관 passage를 비교해 관련 passage의 점수가 높아지도록 encoder를 학습한다. Section 3.2, p.6771, Eq. (2).
- [fact] DPR의 passage 벡터는 미리 계산해 FAISS로 색인하고, 실행 시 질문을 벡터화해 상위 passage를 검색한다. Section 3.1, p.6771, Inference.

## Reading Notes

- 2026-11-09 U4 후속 질문으로 Section 6.1 및 Appendix D를 확인했다. 튜터가 읽기 안내에서 reader의 구체적 모델을 누락한 점을 보완했다. 생성형 RAG 일반론과 DPR의 추출형 reader를 구분한다.
- 2026-11-02: 공식 페이지의 서지와 PDF 첫 페이지만 확인. 본문 미독.
- 2026-11-09: 튜터가 공식 ACL PDF의 Introduction과 Sections 3.1-3.2를 확인했다. 학습자의 해당 절 읽기는 아직 미확인이다. AICC에서의 우위나 실험 재현을 주장하지 않는다.
