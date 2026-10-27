# RAG 학습 워크스페이스

Retrieval-Augmented Generation(RAG)의 발전 과정을 원 논문으로 따라가고, 검색과 생성의 실패를 분리해 진단한 뒤 AICC의 다중 턴 상담에 맞는 평가 실험을 설계하기 위한 학습 저장소다.

## 학습 흐름

1. BM25와 dense retrieval의 차이를 통해 검색 단계의 역할을 익힌다.
2. DPR, RAG, FiD를 읽으며 검색 결과가 생성 모델에 결합되는 방식을 비교한다.
3. Self-RAG, Lost in the Middle, RAGAs를 통해 검색 필요성, 문맥 사용, 근거 충실성 평가를 다룬다.
4. mtRAG와 MTRAG-UN을 바탕으로 맥락 의존 질문, 답변 불가 질문, 상담사 전환을 포함한 AICC 평가를 설계한다.

## 시작 방법

```sh
scripts/study-start.sh 30
```

현재 계획은 [curriculum/ROADMAP.md](curriculum/ROADMAP.md), 논문 목록은 [evidence/INDEX.md](evidence/INDEX.md), 개념 선행 관계는 [concepts/CONCEPT_MAP.md](concepts/CONCEPT_MAP.md)에 있다.

## 완료 산출물

- RAG 발전 계보를 검색·결합·평가·대화의 관점에서 설명한 개념 지도
- 동일 질문 집합에서 검색과 생성을 따로 측정하는 재현 가능한 비교 실험
- AICC 다중 턴 상담용 RAG 평가 프로토콜 초안
