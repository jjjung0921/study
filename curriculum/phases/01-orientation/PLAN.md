# Phase 01 — orientation

- Status: DONE
- Start: 2026-10-27 · End: 2026-11-07
- Goals: 전체 목표의 학습 계약 확정

## Goal

RAG 학습 목표, 개념 지도, 검증된 논문 목록, 진단 계획과 세션 파라미터를 갖추고 첫 학습 Phase를 시작할 수 있다.

## Motivation

RAG는 검색·생성·평가·대화 연구가 섞여 있으므로, AICC 연구에 필요한 범위와 단계별 증명 방법을 먼저 고정한다.

## Scope

- 목표와 capstone 정의
- 10개 개념의 선행 관계와 검증 기준
- DPR·RAG·FiD부터 mtRAG·MTRAG-UN까지 읽기 자료 등록
- Prior Knowledge 진단과 자료 접근 확인
- Phase 02 상세 계획과 실행 스크립트 확인

## Out of Scope

- 개념 설명과 논문 정독
- 개념 state 승격
- 실제 AICC 데이터 수집

## Dependencies

- 사용자의 요청: RAG 발전 과정을 학습하고 AICC 연구로 연결
- 공개 논문 접근

## Units

- [x] U1. 학습 워크스페이스 초기화 — setup · est 30m · requires — · Done when: 목표·개념 지도·논문 목록·ROADMAP·Phase 02 PLAN이 주제에 맞게 작성됨 (commit d3eaddc)
- [x] U2. Prior Knowledge 진단 — practice · est 20m · requires U1 · Done when: LLM·embedding·Python 배경에 대한 low-cost exercise 기록이 있고 결과가 반영됨 (commit db8522f)
- [x] U3. Phase 02 근거 자료 접근 확인 — learn · est 15m · requires U1 · Done when: survey·DPR·RAG·FiD 원문 접근과 evidence 파일 생성이 완료됨 (commit 0210e0e)
- [x] U4. 스크립트와 파라미터 확인 — setup · est 15m · requires U1 · Done when: `scripts/study-start.sh 30`과 `scripts/study-end.sh`가 예상 정보를 출력하고 학습 파라미터가 확인됨 (commit 205b0b7)

## Relevant Documents

- `LEARNING_GOALS.md`
- `LEARNER.md`
- `concepts/CONCEPT_MAP.md`
- `evidence/INDEX.md`
- `curriculum/phases/02-rag-foundations/PLAN.md`
- `curriculum/decisions/DR-0007-rag-scope-and-reading-path.md`

## Acceptance Criteria

- [x] AC1. G1부터 G3까지 각기 다른 capstone과 Phase가 연결되어 있다.
- [x] AC2. 10개 concept의 `requires`와 CONCEPT_MAP이 일치한다.
- [x] AC3. 진단 exercise 결과 없이 concept state가 승격되지 않았다.
- [x] AC4. Phase 02 핵심 논문 네 편의 접근과 서지가 확인됐다.
- [x] AC5. 세션 예산과 입력 선호가 학습자에게 확인됐다 (2026-11-07: 기본 120분, 말과 손글씨 수식 사진 선호).
- [x] AC6. 시작과 종료 스크립트가 FAIL 없이 실행된다.

## Validation Plan

- concept frontmatter와 Mermaid DAG를 정적 대조한다.
- 논문 URL을 열어 제목·저자·연도를 확인한다.
- U2에서 low-cost diagnostic을 별도 기록한다.
- U4에서 스크립트 출력을 저장하지 않고 종료 코드와 FAIL 항목만 확인한다.
