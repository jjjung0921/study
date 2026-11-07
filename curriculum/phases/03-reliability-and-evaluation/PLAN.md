# Phase 03 — reliability-and-evaluation

- Status: PLANNED
- Start: 미정 · End: 미정
- Goals: G2

## Goal

검색 품질, 근거 충실성, 답변 정확성을 분리해 측정하고 두 RAG 파이프라인의 오류 표를 재현 가능한 작은 실험으로 만든다. 세 concept의 verified와 G2 capstone pass가 완료 조건이다.

## Motivation

검색 결과가 맞아도 생성기가 근거를 사용하지 않을 수 있다. 답변 하나의 점수만 보면 어느 단계가 실패했는지 알 수 없으므로 측정 대상과 오류 분류를 먼저 고정한다.

## Scope

- Concepts: retrieval-generation-failures, rag-evaluation, adaptive-retrieval
- Evidence: Lost in the Middle, Self-RAG, RAGAs, ARES
- Sandbox: 같은 질문, corpus, 정답 및 top-k 조건으로 두 파이프라인을 비교하는 작은 실험
- 결과: 질문별 검색 근거, 답변, 지표, 오류 유형을 연결한 표

## Out of Scope

- 논문 성능 수치 재현과 새로운 state of the art 주장
- 대규모 자동 judge 학습과 사람 평가 없는 주관적 품질 단정
- 실제 상담 데이터 및 개인정보 사용

## Dependencies

- Phase 02의 G1 capstone과 네 기초 concept 검증
- 비교에 사용할 공개 질문 집합과 원문 접근 확인

## Units

- [ ] U1. 검색 실패와 생성 실패의 관찰 기준 세우기 — learn · est 25m · requires — · Done when: 정답 문서 누락, 근거 사용 실패, 근거 없는 생성 사례를 관측값으로 구분
- [ ] U2. Lost in the Middle와 Self-RAG에서 실패와 개입 위치 읽기 — learn · est 25m · requires U1 · Done when: context utilization과 retrieval 결정의 근거 절을 concept 초안에 연결
- [ ] U3. 실패 위치 진단 연습 — practice · est 20m · requires U2 · Done when: 처음 보는 사례의 실패 단계와 필요한 로그를 Rubric-first exercise로 판정
- [ ] U4. RAGAs와 ARES의 평가 대상과 한계 읽기 — learn · est 30m · requires U1 · Done when: retrieval, faithfulness, answer correctness의 입력과 측정 대상을 분리
- [ ] U5. 질문 집합, 정답, annotation 규칙 설계 — design · est 20m · requires U4 · Done when: 공개 사례의 포함 기준과 오류 표 스키마를 기록
- [ ] U6. 지표 해석 연습 — practice · est 20m · requires U4,U5 · Done when: 지표가 좋은데 답변이 틀린 사례를 Rubric-first exercise로 설명
- [ ] U7. Self-RAG의 적응적 검색과 critique 읽기 — learn · est 30m · requires U2,U4 · Done when: 고정 검색과 적응적 검색의 결정 지점을 concept 초안에 기록
- [ ] U8. 검색 결정 연습 — practice · est 20m · requires U7 · Done when: 검색, 재검색, 기권 후보의 선택 근거를 Rubric-first exercise로 판정
- [ ] U9. 두 파이프라인의 비교 계약 고정 — design · est 25m · requires U5,U7 · Done when: 공통 corpus, 질문, top-k, 생성 조건, 오류 분류와 반증 조건을 기록
- [ ] U10. 작은 비교 실험 실행 — coding · est 55m · requires U9 · Done when: 두 파이프라인의 질문별 retrieval 결과, 답변, 지표와 실행 명령을 남김
- [ ] U11. 세 concept의 다른 날 검증 — verify · est 45m · requires U3,U6,U8 · Done when: 각 concept에 대해 초기 practice와 다른 날의 별도 high-cost transfer 또는 coding exercise pass
- [ ] U12. G2 capstone: 측정 결과와 오류 표 해석 — capstone · est 45m · requires U10,U11 · Done when: 같은 질문 집합의 두 실행 결과에서 검색과 생성 지표, 사례별 오류, 불확실성을 제시한 coding 및 transfer exercise pass

## Relevant Documents

- `LEARNING_GOALS.md` — G2
- `concepts/CONCEPT_MAP.md` — Phase 03 subgraph
- `evidence/INDEX.md` — Lost in the Middle, Self-RAG, RAGAs, ARES
- `curriculum/decisions/DR-0008-learning-evidence-boundaries.md`

## Acceptance Criteria

- [ ] AC1. 세 concept가 서로 다른 날의 독립 pass 2회 이상과 high-cost 유형을 포함해 verified다.
- [ ] AC2. G2 capstone에서 두 파이프라인이 같은 공개 질문 집합과 통제된 조건으로 실행됐다.
- [ ] AC3. 검색 품질, 근거 충실성, 답변 정확성이 별도 열과 오류 사례로 보고됐다.
- [ ] AC4. 각 concept Claims의 논문 근거 위치가 확인됐고 미검증 수치는 저자 보고값으로 표시됐다.

## Validation Plan

- U3, U6, U8의 정식 practice를 먼저 채점하고 U11의 새로운 문제를 다른 날 채점한다. 미통과는 다음 세션에 새 문제로 재시도한다.
- U9에서 비교 조건을 먼저 기록하고 U10에서 실행 로그를 남긴다. U12에서 지표 계산과 사례 분류를 원자료에 대조한다.
- judge 기반 지표는 적용 범위와 한계를 명시하며, 작은 표본에서 일반적 우월성을 주장하지 않는다.
