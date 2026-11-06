# Handoff

- From: codex — U3 근거 자료 접근 확인
- Date: 2026-11-02
- Phase / Unit: 01-orientation / U3 완료

## Goal

RAG의 발전 과정을 학습하고 AICC 다중 턴 평가 연구로 이어지는 검증 가능한 학습 경로를 만든다.

## Work Completed

- G1–G3와 capstone, Non-Goals, 공개 자료 제약을 정의했다.
- survey·DPR·RAG·FiD·Self-RAG·RAGAs·mtRAG 등 11편을 등록했다.
- Phase 02의 12개 unit과 scope를 작성했다. 작업 커밋: `d3eaddc`.
- U3의 네 편 공식 서지·PDF 접근을 확인하고 evidence 파일을 만들었다. 작업 커밋: `0210e0e`.

## Work In Progress

- U4에서 시작·종료 스크립트와 임시 학습 파라미터를 확인한다.
- U2 진단 Attempt 전사를 학습자가 확인했고, `study-grader`가 원래 Attempt를 세 항목 ✗, 종합 fail로 채점했다. 별도 Codex 리뷰도 항목 판정과 등급에 동의했다. 학습자가 후속 설명으로 의도를 명확히 했으며 원래 Attempt의 점수와 구분해 exercise에 기록했다.
- 기존 RAG 블로그 초안과 검증 기록은 미커밋 학습자 변경으로 보존한다. 지정 대화 직접 읽기는 실패했다.

## Decisions Made

- 기초 검색·생성 → reliability·evaluation → conversational AICC 순서로 진행한다 — DR-0007.
- Graph·multimodal·serving·음성 모델은 초기 범위에서 제외한다.

## Exercises Graded

- `exercises/01-u2-prior-knowledge.md` — 진단 fail, concept state 변경 없음

## Misconceptions Observed

- 처음 채점 파일에 적힌 두 오개념 후보는 독립 리뷰와 학습자 후속 설명에 따라 철회했다. 확정된 오개념은 없다.
- `study-grader` 역할 메모리도 학습자 후속 설명과 독립 리뷰에 맞게 정정했다.

## Open Questions

- AICC의 우선 도메인(통신·금융·공공 등)은 Phase 04 전에 정한다.

## Unverified Assumptions

- 한 세션 30분, 입문 수준, 한국어 설명, 말·ASCII·Python 입력을 선호한다고 임시 가정했다.
- LLM·embedding·Python 배경은 U2 diagnostic 전에는 concept state에 반영하지 않았다.
- 실제 고객 데이터 없이 공개 벤치마크와 합성 상담 시나리오로 시작한다고 가정했다.

## Exact Next Action

U4에서 시작·종료 스크립트와 임시 시간 예산·입력 선호를 확인한다.
