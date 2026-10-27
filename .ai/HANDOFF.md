# Handoff

- From: codex — RAG 워크스페이스 초기화
- Date: 2026-10-27
- Phase / Unit: 01-orientation / U1 완료

## Goal

RAG의 발전 과정을 학습하고 AICC 다중 턴 평가 연구로 이어지는 검증 가능한 학습 경로를 만든다.

## Work Completed

- G1–G3와 capstone, Non-Goals, 공개 자료 제약을 정의했다.
- 10개 concept의 DAG와 Verification Criteria를 만들었다.
- survey·DPR·RAG·FiD·Self-RAG·RAGAs·mtRAG 등 11편을 등록했다.
- Phase 02의 12개 unit과 scope를 작성했다. 작업 커밋: `d3eaddc`.

## Work In Progress

- 없음

## Decisions Made

- 기초 검색·생성 → reliability·evaluation → conversational AICC 순서로 진행한다 — DR-0007.
- Graph·multimodal·serving·음성 모델은 초기 범위에서 제외한다.

## Exercises Graded

- 없음

## Misconceptions Observed

- 없음

## Open Questions

- AICC의 우선 도메인(통신·금융·공공 등)은 Phase 04 전에 정한다.

## Unverified Assumptions

- 한 세션 30분, 입문 수준, 한국어 설명, 말·ASCII·Python 입력을 선호한다고 임시 가정했다.
- LLM·embedding·Python 배경은 U2 diagnostic 전에는 concept state에 반영하지 않았다.
- 실제 고객 데이터 없이 공개 벤치마크와 합성 상담 시나리오로 시작한다고 가정했다.

## Exact Next Action

U2 diagnostic을 만들고 학습자의 시간 예산·입력 선호를 확인한다. 그다음 U3에서 Phase 02 원문 접근과 evidence 파일을 준비한다.
