# Handoff

- From: codex — Phase 01 완료와 전체 커리큘럼 작성
- Date: 2026-11-07
- Phase / Unit: 02-rag-foundations / U1 대기

## Goal

RAG의 발전 과정을 학습하고 AICC 다중 턴 평가 연구로 이어지는 검증 가능한 학습 경로를 만든다.

## Work Completed

- G1–G3와 capstone, Non-Goals, 공개 자료 제약을 정의했다.
- survey·DPR·RAG·FiD·Self-RAG·RAGAs·mtRAG 등 11편을 등록했다.
- Phase 02의 12개 unit과 scope를 작성했다. 작업 커밋: `d3eaddc`.
- U3의 네 편 공식 서지·PDF 접근을 확인하고 evidence 파일을 만들었다. 작업 커밋: `0210e0e`. U4의 120분 설정과 Phase 02부터 04까지의 상세 계획을 기록했다. 작업 커밋: `205b0b7`.

## Work In Progress

- Phase 02 U1의 survey 분류와 정보 흐름 읽기가 다음 작업이다. pending exercise는 없다. 학습 일정은 목요일 19시와 토요일 14시로 잡았으며 시간은 학습자 확인 전의 운영 가정이다.
- U2 진단 Attempt 전사를 학습자가 확인했고, `study-grader`가 원래 Attempt를 세 항목 ✗, 종합 fail로 채점했다. 별도 Codex 리뷰도 항목 판정과 등급에 동의했다. 학습자가 후속 설명으로 의도를 명확히 했으며 원래 Attempt의 점수와 구분해 exercise에 기록했다.
- 기존 RAG 블로그 초안과 검증 기록은 `c9c2eeb`에 기록됐다. 지정 대화 직접 읽기는 실패했다.

## Decisions Made

- 기초 검색과 생성에서 평가, 대화형 AICC 순서로 진행한다 — DR-0007. 120분 주 2회 계획은 DR-0009.
- Graph·multimodal·serving·음성 모델은 초기 범위에서 제외한다.

## Exercises Graded

- `exercises/01-u2-prior-knowledge.md` — 진단 fail, concept state 변경 없음

## Misconceptions Observed

- 처음 채점 파일에 적힌 두 오개념 후보는 독립 리뷰와 학습자 후속 설명에 따라 철회했다. 확정된 오개념은 없다.
- `study-grader` 역할 메모리도 학습자 후속 설명과 독립 리뷰에 맞게 정정했다.

## Open Questions

- AICC의 우선 도메인(통신·금융·공공 등)은 Phase 04 전에 정한다.

## Unverified Assumptions

- 한국어 설명과 RAG 입문 수준은 현재 학습 설정이다. 목요일과 토요일의 시작 시각은 학습자 확인 전의 운영 가정이다.
- LLM·embedding·Python 배경은 U2 diagnostic 전에는 concept state에 반영하지 않았다.
- 실제 고객 데이터 없이 공개 벤치마크와 합성 상담 시나리오로 시작한다고 가정했다.

## Exact Next Action

Phase 02 U1에서 survey 원문을 읽고 검색, 결합, 평가, 대화의 전체 흐름을 기록한다.
