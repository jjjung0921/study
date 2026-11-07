# Learning Goals

## Why

AICC 연구를 시작하기 전에 RAG가 어떤 문제를 해결하며 발전했는지 원 논문으로 확인하고, 검색 성능과 답변 품질을 분리해 측정할 수 있는 기초를 만든다. 최종적으로는 다중 턴 상담에서 근거가 부족한 경우까지 다루는 작은 평가 실험을 설계한다.

## Goals

| # | Goal ("…를 할 수 있다") | Proof (capstone exercise) | Phase | Status |
|---|---|---|---|---|
| G1 | sparse·dense retrieval과 RAG·FiD의 정보 흐름을 비교하고 주어진 실패를 검색 또는 생성 단계에 귀속할 수 있다 | 처음 보는 QA 사례 6개를 단계별로 진단하고 근거를 설명한다 — transfer | 02 | PLANNED |
| G2 | RAG의 검색 품질·근거 충실성·답변 정확성을 분리해 측정하는 실험을 구현할 수 있다 | 같은 질문 집합에 두 파이프라인을 실행하고 retrieval·generation 지표와 오류 표를 산출한다 — coding + transfer | 03 | PLANNED |
| G3 | AICC 다중 턴 대화에서 맥락 의존·답변 불가·정책 충돌을 포함한 RAG 평가 프로토콜을 설계할 수 있다 | 공개 벤치마크 사례를 AICC 시나리오로 변환해 평가 항목·baseline·반증 조건을 작성한다 — transfer | 04 | PLANNED |

## Non-Goals

- 대규모 벡터 데이터베이스 운영과 분산 인프라 최적화
- 특정 상용 RAG 프레임워크 사용법 습득
- 음성 인식·합성 및 full-duplex 음성 대화 모델
- 실제 고객 개인정보나 기업 내부 상담 기록을 사용하는 실험
- 모든 Graph RAG·multimodal RAG·agentic RAG 변형의 포괄적 조사

## Prior Knowledge

- LLM과 임베딩의 기본 개념을 접해 보았다고 가정한다 — 근거: 이전 AI 연구·학습 프로젝트 경험, Phase 01 진단 전에는 상태에 반영하지 않음
- Python으로 작은 실험을 실행할 수 있다고 가정한다 — 근거: 기존 학습 저장소의 코드 기반 작업, Phase 01 진단 필요
- 정보 검색 지표와 다중 턴 RAG는 처음 배우는 것으로 가정한다

## Constraints

- 공개 논문·공개 벤치마크·합성 상담 시나리오만 사용한다.
- 논문의 성능 수치는 저자 보고값으로 취급하고 재현 전에는 검증된 개선으로 표현하지 않는다.
- 기본 세션은 학습자가 확인한 120분이다. 주 2회 일정의 원본은 [track/plan.md](track/plan.md)에 둔다. 개념의 verified 시점은 서로 다른 날의 독립 채점 결과에 따라 달라질 수 있다.
