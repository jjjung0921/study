# DR-0007: RAG 기초에서 AICC 다중 턴 평가로 이어지는 읽기 경로

- Status: Accepted
- Date: 2026-10-27
- Deciders: 학습자 요청 / Codex 초안

## Context

사용자는 AICC 연구를 위해 RAG 발전 과정을 survey로 파악하고 읽을 논문을 추출한 뒤 학습 폴더로 만들 것을 요청했다.

## Problem

빠르게 확장되는 RAG 변형 전체를 다루지 않으면서 AICC 연구 질문에 필요한 검색·생성·평가·다중 턴 개념을 어떤 순서로 배울 것인가.

## Alternatives

1. 최신 RAG 변형을 폭넓게 조사한다 — 범위는 넓지만 기본 실패 원인과 평가 계약이 흐려진다.
2. DPR→RAG→FiD의 기초 뒤 reliability·evaluation, multi-turn AICC로 진행한다 — 핵심 관계와 검증 산출물이 명확하다.
3. AICC 응용 논문부터 읽는다 — 동기는 직접적이지만 방법의 기초와 지표 해석이 부족해질 수 있다.

## Decision

대안 2를 선택한다. Phase 02는 검색과 결합, Phase 03은 실패 진단과 평가, Phase 04는 다중 턴과 abstention을 다룬다.

## Rationale

최종 산출물이 논문 목록 자체가 아니라 AICC RAG 평가 실험이므로, 구성 요소별 실패와 지표를 먼저 분리할 수 있어야 한다.

## Consequences

- 긍정: 각 Phase가 관찰 가능한 capstone으로 끝나고 AICC 연구 질문으로 자연스럽게 연결된다.
- 부정 / 감수한 것: Graph RAG, multimodal RAG, 대규모 serving은 초기 범위에서 제외된다.
- 후속 작업: Phase 01 진단과 논문 접근 확인 뒤 Phase 02를 시작한다.
