# DR-0009: 두 시간 세션에 맞춘 RAG 전체 학습 경로

- Status: Accepted
- Date: 2026-11-07
- Deciders: 학습자 요청과 Codex 커리큘럼 작성

## Context

Phase 02만 상세 unit이 있고 Phase 03과 04는 목표와 예상 시간만 있었다. 학습자는 기본 세션을 120분으로 바꾸고, 월요일과 화요일을 제외해 주 2회 학습하기로 했다. 개념 verified는 서로 다른 날의 pass 두 번과 high-cost 유형을 요구한다.

## Decision

기존 G1에서 G3까지의 순서와 10개 concept 선행 관계를 유지한다. Phase 02는 295분, Phase 03은 360분, Phase 04는 300분의 unit으로 계획한다. 각 concept의 첫 practice와 다른 날의 새로운 transfer 또는 coding 검증을 Phase PLAN에 명시한다. 통합 capstone은 개념별 채점 기록과 별도로 둔다.

주 2회, 회당 120분의 다섯 주 계획을 [track/plan.md](../../track/plan.md)에 둔다. 학습자가 밝힌 월요일과 화요일 근무, 맥북 Calendar에 이미 있는 수요일 저녁 일정을 피한다. 목요일 19시와 토요일 14시는 캘린더 배치를 위한 시간 가정이며 학습자가 바꿀 수 있다. 복습 만기는 새 unit보다 우선하고, 실제 pass와 속도가 계획보다 늦으면 다음 Phase 진입과 캘린더 일정을 조정한다.

## Rationale

기존 Phase 02의 25분 capstone은 네 개 concept의 서로 다른 날 검증과 여섯 사례 통합 진단을 모두 담기 어려웠다. Phase 03과 04에 상세 unit이 없으면 캘린더 시간이 학습 산출물과 연결되지 않는다.

## Consequences

- Phase 01에서 확인한 120분 기본값과 별개로, 개별 unit은 20분에서 85분 단위로 유지해 학습 속도에 따라 한 세션 안에서 조합한다.
- Phase 03과 04의 논문 접근과 실험 데이터 계약은 각 unit을 시작할 때 확인한다. 현재 PLAN의 논문 목록은 읽기 경로이며 원문 검증 완료를 뜻하지 않는다.
- 캘린더에는 10개 세션을 넣되, 통과 여부와 복습 만기에 따라 일정을 다시 잡을 수 있다.
