# Phase 02 U6: 원 RAG의 두 memory

<!-- ai:draft -->
## 문제와 핵심 아이디어

모델 가중치에 담긴 지식은 수정과 출처 확인이 쉽지 않다. 원 RAG는 가중치에 담긴 지식과 검색으로 가져오는 외부 문서를 함께 활용해 답변을 생성한다. 외부 문서 제공이 정확한 답변을 보장하는 것은 아니다.

| 구분 | 원 RAG에서의 실체 | 갱신 방식 |
|---|---|---|
| Parametric memory | BART generator 가중치 | 학습으로 가중치 조정 |
| Non-parametric memory | Wikipedia passage와 dense vector index | 외부 자료와 그에 맞는 색인 갱신 |

Non-parametric은 검색기 전체가 학습되지 않는다는 뜻이 아니다. DPR encoder에도 가중치가 있다. 논문의 이름은 외부 문서 색인을 가리킨다.

## 실제 모델 구성

원 RAG는 DPR로 초기화한 검색기와 BART-large 생성기를 결합한다. DPR 논문의 추출형 BERT reader와 달리 답을 새 토큰 시퀀스로 생성한다. 질문에 대해 top-k 문서를 검색하고 각 문서를 질문과 함께 BART에 제공해 출력 확률을 계산한다.

## Sequence와 Token의 읽기 지도

- RAG-Sequence: 각 문서를 출력 전체의 근거로 가정해 확률을 계산하고, 그 문서별 확률을 검색 확률로 가중합한다. 가장 높은 순위 문서 하나만 고정해서 사용하는 방식으로 오해하지 않는다.
- RAG-Token: 각 토큰을 예측할 때 문서별 조건부 확률을 검색 확률로 가중합한다. 토큰마다 새로 검색하는 것은 아니다.
- 첫 읽기는 Introduction과 Figure 1, PDF p.1-2다. 이후 Section 2.1 p.3에서 합산과 곱의 순서를 비교한다. 수식의 기호는 해당 문답에서 정의한다.

근거: [원 RAG evidence](../evidence/lewis-2020-rag.md), v4 Introduction, Figure 1, Sections 2.1-2.4, pp.1-4. 생성기와 query encoder의 공동 학습은 가능하지만 논문의 document encoder와 index는 학습 중 고정한다.
<!-- /ai:draft -->

## 진행

- 2026-11-09 U6 시작. 학습자 읽기와 초안 검토 미확인. exercise 및 concept state 변경 없음.
