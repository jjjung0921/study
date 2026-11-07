# Learner

## Time Budget

- Default session: 120분 · 최소 세션: 5분 (회상 질문 1개)
- Typical week: 미정. 한 세션 120분을 기본값으로 사용한다.
- Velocity: 손으로 적지 않는다 — `scripts/study-start.sh`가 `.ai/LOG.md`의 planned·actual에서 계산한다.

## Background

- AI·메타러닝 연구와 Python 기반 실험 경험이 있다.
- RAG의 체계적인 논문 계보와 평가 방법은 입문 수준으로 가정한다.
- 목표는 제품 사용법보다 연구 질문과 검증 가능한 실험 설계를 만드는 것이다.

## Input Preferences

- 입력: 말로 설명하고, 수식은 손글씨 사진을 우선 사용한다. ASCII 수식과 Python 코드도 받을 수 있다.
- 사진 위치: `exercises/_inbox/` (gitignore. 튜터가 전사한 뒤 `전사 확인: OK`를 받는다.)
- 설명: 한국어를 기본으로 하고 논문 용어는 영어를 병기한다.
- 피하고 싶은 유형: 긴 수식이나 증명을 직접 LaTeX로 입력하는 과제

## Grading Preferences

- Default grader: Claude `study-grader` (Codex 튜터와 독립 채점)
- 피드백 형식: Rubric 항목별 판정과 틀린 항목의 다음 힌트

## Parameters

- default_budget: 120
- min_session: 5
- review_only_below: 15
- review_est: 5
- record_est: 5
- verified_passes: 2
- review_intervals: 3 7 21 60
- context_warn_kb: 25
