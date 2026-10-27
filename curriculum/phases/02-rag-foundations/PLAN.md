# Phase 02 — rag-foundations

- Status: PLANNED
- Start: 미정 · End: 미정
- Goals: G1

## Goal

네 개 기초 개념이 verified이고, 처음 보는 QA 실패를 retrieval 또는 generation 단계에 근거와 함께 귀속하는 capstone을 통과한다.

## Motivation

AICC용 RAG를 설계하기 전에 문서가 어떻게 선택되고 생성기에 결합되는지, 각 단계가 어떤 실패를 만들 수 있는지 알아야 한다.

## Scope

- Concepts: sparse-dense-retrieval, retriever-reader-pipeline, parametric-nonparametric-memory, passage-fusion
- Evidence: RAG survey, DPR, 원 RAG, FiD, Lost in the Middle
- Sandbox: 작은 문서 집합에서 BM25형 lexical baseline과 dense 결과를 비교하는 실험

## Out of Scope

- adaptive retrieval 학습과 자동 judge 구현
- 다중 턴 query rewriting
- 상용 벡터 데이터베이스 성능 비교

## Dependencies

- Phase 01의 Prior Knowledge 진단과 핵심 논문 접근 확인

## Units

- [ ] U1. RAG survey의 분류와 전체 정보 흐름 읽기 — learn · est 20m · requires — · Done when: 발전 흐름을 검색·결합·평가·대화 네 축으로 요약
- [ ] U2. sparse·dense retrieval 도입과 DPR 근거 읽기 — learn · est 25m · requires U1 · Done when: `concepts/sparse-dense-retrieval.md` 초안과 evidence 포인터 작성
- [ ] U3. sparse·dense retrieval 연습 — practice · est 15m · requires U2 · Done when: condition 또는 numeric exercise pass
- [ ] U4. retriever–reader pipeline 도입 — learn · est 20m · requires U2 · Done when: 단계 경계와 실패 위치를 concept 초안에 기록
- [ ] U5. retriever–reader 실패 진단 — practice · est 15m · requires U3,U4 · Done when: error-spot exercise pass
- [ ] U6. 원 RAG의 parametric·non-parametric memory 읽기 — learn · est 25m · requires U4 · Done when: RAG-Sequence와 RAG-Token의 차이를 근거 위치와 기록
- [ ] U7. memory 경계 연습 — practice · est 15m · requires U6 · Done when: 정책 갱신 사례 condition exercise pass
- [ ] U8. FiD와 passage fusion 읽기 — learn · est 25m · requires U6 · Done when: fusion 위치와 top-k 역할을 concept 초안에 기록
- [ ] U9. Lost in the Middle로 문맥 사용 한계 확인 — learn · est 20m · requires U8 · Done when: retrieval 성공과 context utilization 실패를 구분
- [ ] U10. passage fusion 연습 — practice · est 15m · requires U8,U9 · Done when: 처음 보는 다문서 사례 condition exercise pass
- [ ] U11. 기초 개념 통합 복습 — review · est 15m · requires U5,U7,U10 · Done when: 네 개 concept의 관계를 빈 흐름도에 복원
- [ ] U12. G1 실패 귀속 capstone — capstone · est 25m · requires U11 · Done when: 새로운 QA 사례 6개의 단계별 진단 transfer exercise pass

## Relevant Documents

- `LEARNING_GOALS.md` — G1
- `concepts/CONCEPT_MAP.md` — Phase 02 subgraph
- `evidence/INDEX.md` — survey, DPR, RAG, FiD, Lost in the Middle
- `curriculum/decisions/DR-0007-rag-scope-and-reading-path.md`

## Acceptance Criteria

- [ ] AC1. 네 concept가 verified이며 서로 다른 날 pass 2회와 high-cost 유형을 포함한다.
- [ ] AC2. G1 capstone transfer exercise가 pass다.
- [ ] AC3. 검색 성공·생성 실패를 혼동한 사례가 있으면 MISCONCEPTIONS에 기록된다.
- [ ] AC4. 각 Claims에 원 논문의 절·식·표 포인터가 있다.

## Validation Plan

- U3·U5·U7·U10의 low-cost exercise로 각 개념을 practiced까지 확인한다.
- U12 transfer와 이후 다른 날의 복습 pass로 verified 조건을 충족한다.
- verified 시 `review_due`를 3일 뒤로 설정하고 다음 Phase보다 복습을 우선한다.
- sandbox 비교는 같은 corpus·query·k를 사용하고 결과를 `evidence/`에 기록한다.
