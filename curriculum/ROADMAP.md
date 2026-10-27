# RAG for AICC Roadmap

| # | Phase | Goal | Concepts | Est (m) | Status | Result |
|---|---|---|---|---:|---|---|
| 01 | [orientation](phases/01-orientation/PLAN.md) | 목표·진단·근거 접근·실행 파라미터를 확정한다 | — | 80 | IN_PROGRESS | — |
| 02 | [rag-foundations](phases/02-rag-foundations/PLAN.md) | 검색부터 passage fusion까지 기본 정보 흐름을 설명하고 실패를 진단한다 | sparse-dense-retrieval, retriever-reader-pipeline, parametric-nonparametric-memory, passage-fusion | 235 | PLANNED | — |
| 03 | reliability-and-evaluation | 검색·생성 실패를 분리하고 평가 실험을 구현한다 | retrieval-generation-failures, rag-evaluation, adaptive-retrieval | 240 | PLANNED | — |
| 04 | conversational-aicc-rag | 다중 턴·답변 불가 상황을 포함한 AICC 평가 프로토콜을 설계한다 | conversational-query-context, answerability-abstention, aicc-rag-experiment-design | 245 | PLANNED | — |

## Phase Rules

- Phase 02는 G1, Phase 03은 G2, Phase 04는 G3의 capstone을 통과해야 완료된다.
- 개념의 state는 채점된 exercise 기록으로만 바뀐다.
- verified 뒤 복습은 Phase와 무관하게 3·7·21·60일 간격으로 우선 수행한다.
- Phase 03·04의 상세 PLAN은 직전 Phase 결과와 실제 속도를 반영해 시작 전에 작성한다.
