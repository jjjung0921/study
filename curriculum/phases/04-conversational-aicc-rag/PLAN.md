# Phase 04 — conversational-aicc-rag

- Status: PLANNED
- Start: 미정 · End: 미정
- Goals: G3

## Goal

공개 다중 턴 사례를 합성 AICC 상담 시나리오로 바꾸고, 맥락 의존, 답변 불가, 정책 충돌을 포함하는 평가 프로토콜을 설계한다. 세 concept의 verified와 G3 capstone pass가 완료 조건이다.

## Motivation

단일 질문에서 맞는 답을 내는 파이프라인도 이전 턴의 제약을 놓치거나 근거가 없는 질문에 단정할 수 있다. 상담에서는 답변 보류와 사람 상담사 인계까지 평가 계약에 포함해야 한다.

## Scope

- Concepts: conversational-query-context, answerability-abstention, aicc-rag-experiment-design
- Evidence: mtRAG, MTRAG-UN, τ-bench의 평가 설정과 적용 한계
- 자료: 공개 벤치마크와 합성 상담 시나리오만 사용
- 결과: 사례 변환 규칙, baseline, 평가 항목, annotation 지침, 반증 조건을 담은 프로토콜

## Out of Scope

- 실제 고객 상담 기록, 개인정보, 기관 정책 문서 수집
- 음성 인식, 합성 및 실시간 음성 대화
- τ-bench의 도구 사용 과제를 RAG 검색 과제와 동일하게 취급하는 성능 비교

## Dependencies

- Phase 03의 G2 capstone과 평가 지표의 분리
- 공개 벤치마크 사례의 원문 및 사용 조건 확인

## Units

- [ ] U1. mtRAG로 턴 간 질의 맥락과 근거 연결 읽기 — learn · est 30m · requires — · Done when: 독립 질문과 이전 턴 의존 질문의 필요한 상태를 구분
- [ ] U2. 대화 맥락 연습 — practice · est 20m · requires U1 · Done when: 새 대화에서 누락된 제약과 필요한 검색 질의를 Rubric-first exercise로 판정
- [ ] U3. MTRAG-UN의 답변 불가 사례 읽기 — learn · est 30m · requires U1 · Done when: 근거 부재와 정책 충돌의 사례 유형 및 원문 위치를 기록
- [ ] U4. 기권과 사람 인계의 판단 기준 설계 — design · est 20m · requires U3 · Done when: 보류 조건, 추가 질문, 인계에 전달할 맥락을 구분
- [ ] U5. 답변 가능성 연습 — practice · est 20m · requires U4 · Done when: 새 사례의 답변, 기권, 인계 판단을 Rubric-first exercise로 판정
- [ ] U6. τ-bench에서 가져올 평가 구조와 적용 한계 확인 — learn · est 20m · requires U4 · Done when: 도구 상호작용과 RAG 근거 평가가 다른 지점을 명시
- [ ] U7. AICC 평가 프로토콜 초안 — design · est 40m · requires U5,U6 · Done when: 합성 시나리오 변환 규칙, 최소 두 baseline, 평가 항목, annotation 지침, 반증 조건을 작성
- [ ] U8. 프로토콜 설계 연습 — practice · est 20m · requires U7 · Done when: 누락된 통제군과 관찰 불가능한 지표를 Rubric-first exercise로 찾아 수정
- [ ] U9. 맥락과 답변 가능성의 다른 날 검증 — verify · est 40m · requires U2,U5 · Done when: 두 concept 각각의 초기 practice와 다른 날 새 transfer exercise pass
- [ ] U10. 설계 검증과 G3 capstone — capstone · est 60m · requires U8,U9 · Done when: 설계 concept의 다른 날 transfer exercise와 공개 사례를 AICC 시나리오로 바꾼 평가 프로토콜 capstone이 pass

## Relevant Documents

- `LEARNING_GOALS.md` — G3
- `concepts/CONCEPT_MAP.md` — Phase 04 subgraph
- `evidence/INDEX.md` — mtRAG, MTRAG-UN, τ-bench
- `curriculum/decisions/DR-0007-rag-scope-and-reading-path.md`

## Acceptance Criteria

- [ ] AC1. 세 concept가 서로 다른 날의 독립 pass 2회 이상과 transfer 유형을 포함해 verified다.
- [ ] AC2. G3 capstone이 공개 사례와 합성 AICC 시나리오의 변환 근거를 추적할 수 있다.
- [ ] AC3. 맥락 의존, 답변 불가, 정책 충돌 각각에 판단 기준과 실패 사례가 있다.
- [ ] AC4. baseline, annotation, 지표, 반증 조건, 데이터 제한이 프로토콜에 명시됐다.

## Validation Plan

- U2, U5, U8을 정식 practice로 채점하고 다른 날 U9, U10에서 새로운 transfer 문제를 독립 채점한다.
- 합성 시나리오가 공개 원문의 정답과 모순되지 않는지 대조한다. 벤치마크의 라이선스와 사용 조건을 확인한다.
- 프로토콜 설계의 pass와 실제 상담 성능의 검증을 구분한다. 이 Phase는 실제 고객 데이터를 사용하지 않는다.
