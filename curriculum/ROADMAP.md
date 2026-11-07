# RAG for AICC Roadmap

| # | Phase | Goal | Concepts | Est (m) | Status | Result |
|---|---|---|---|---:|---|---|
| 01 | [orientation](phases/01-orientation/PLAN.md) | 목표, 진단, 근거 접근, 실행 파라미터를 확정한다 | — | 80 | DONE | [결과](phases/01-orientation/RESULT.md) |
| 02 | [rag-foundations](phases/02-rag-foundations/PLAN.md) | 검색부터 passage fusion까지 기본 정보 흐름을 설명하고 실패를 진단한다 | sparse-dense-retrieval, retriever-reader-pipeline, parametric-nonparametric-memory, passage-fusion | 295 | PLANNED | — |
| 03 | [reliability-and-evaluation](phases/03-reliability-and-evaluation/PLAN.md) | 검색과 생성의 실패를 분리하고 평가 실험을 구현한다 | retrieval-generation-failures, rag-evaluation, adaptive-retrieval | 360 | PLANNED | — |
| 04 | [conversational-aicc-rag](phases/04-conversational-aicc-rag/PLAN.md) | 다중 턴과 답변 불가 상황을 포함한 AICC 평가 프로토콜을 설계한다 | conversational-query-context, answerability-abstention, aicc-rag-experiment-design | 300 | PLANNED | — |

## Phase Rules

- Phase 02는 G1, Phase 03은 G2, Phase 04는 G3의 capstone을 통과해야 완료된다.
- 개념의 state는 채점된 exercise 기록으로만 바뀐다.
- verified 뒤 복습은 Phase와 무관하게 3·7·21·60일 간격으로 우선 수행한다.
- Phase 03과 04의 상세 PLAN은 현재 선행 관계와 검증 조건을 기준으로 작성했다. 각 Phase 시작 전에 직전 결과와 실제 속도를 확인하고 unit 시간만 조정한다. 주차 일정은 [track/plan.md](../track/plan.md)가 원본이다.
