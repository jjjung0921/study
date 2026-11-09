# Phase 02 U1: Section II.C.1 New Modules

## 학습자 질문과 해석

- 2026-11-08: New Modules까지만 읽고 검토를 요청했다. 역할 분리와 multi-query의 목적을 짚었다. Search를 자료구조 기반 효율화, Memory를 분포에 따른 텍스트 재정렬, Predict를 미래 문장의 중복 탐지로 해석했다. unbounded memory pool, zero-shot input, prompt retrieval, few-shot query generation의 의미를 질문했다. exercise Attempt나 채점 기록이 아니다.

<!-- ai:draft -->
## 설명

- 모듈화는 역할 분리와 더불어 기능의 추가, 교체, 조합을 포함한다. 모든 모듈이 새로 발명된 기능이거나 모든 시스템의 필수 구성요소인 것은 아니다.
- Search: II.C.1은 LLM이 생성한 코드와 질의 언어로 검색 엔진, 데이터베이스, 지식 그래프 등 다양한 출처에 접근하는 기능을 강조한다. 자료구조를 통한 색인 효율화가 이 문단의 핵심은 아니다.
- RAG-Fusion: 여러 관점의 query로 각각 검색한 결과를 통합하고 순위를 조정한다. 여러 답변을 단순히 이어 붙이는 것과 구분한다.
- Memory: 인용된 Selfmem은 생성한 후보 텍스트 중 하나를 선택해 다음 생성의 memory로 사용한다. unbounded는 고정된 검색 말뭉치에 후보가 제한되지 않는다는 의미이며 무한한 저장 공간이나 context window가 아니다. 데이터 분포에 가까워진다는 표현을 텍스트 순서 변경으로 해석하지 않는다. Selfmem의 동기는 모델 출력이 추론 시 목표 출력의 분포에 더 가까울 수 있다는 것이며 모든 과제에 대한 보장은 아니다. 일반적인 장기 대화 기억과도 구분한다.
- Predict: LLM이 최종 답변을 위한 context를 직접 생성하는 역할이다. 미래 답변의 중복을 미리 탐지하는 역할로 설명하지 않는다. survey가 제시한 노이즈 감소라는 목적이 생성 문맥의 사실성을 보장하지는 않는다.
- Task Adapter는 여러 방법을 묶은 범주다. UPRISE는 현재 입력에 유용한 prompt 예시를 검색한다. PROMPTAGATOR는 소수의 query-document 예시를 바탕으로 문서에 대응하는 query를 생성하고, 합성 query-document 쌍으로 과제별 검색기를 학습한다. 두 방법은 하나의 필수 순서가 아니다.
- Routing은 질문에 따라 데이터 출처나 처리 경로를 선택하는 역할로 원문에 함께 등장한다.

## 용어

- 일반적으로 zero-shot prompting은 예시 없이, few-shot prompting은 소수의 예시를 주는 방식이다. 다만 UPRISE의 zero-shot 평가에서는 검색기를 학습하지 않은 과제 유형으로의 전이를 뜻하며 최종 prompt에는 다른 과제에서 검색한 예시가 들어간다.
- UPRISE의 prompt pool은 입력과 정답 출력을 포함한 과제 시범 예시다. 검색 대상은 지식 문서뿐 아니라 이런 예시도 될 수 있다.
- PROMPTAGATOR의 query 생성은 검색기 학습 데이터를 만드는 과정이다. 사용자 질문을 받은 뒤 여러 query로 확장하는 RAG-Fusion의 역할과 구분한다.

## 근거

- [survey](../evidence/gao-2023-rag-survey.md): v5 p.4-5 II.C.1, p.9 III.D.2와 III.E, references [13], [17], [20], [21].
- [Selfmem](https://arxiv.org/abs/2305.02437): v3 p.1-2, Sections 3.2-3.4. 위 memory 설명은 이 인용 사례에 한정한다.
- [UPRISE](https://arxiv.org/abs/2303.08518): v4 Sections 2와 3.1, p.2-3.
- [PROMPTAGATOR](https://arxiv.org/abs/2209.11755): Sections 3, 5-6의 query 생성과 검색기 학습 설명.
<!-- /ai:draft -->

## 진행

- II.C.1에서 대기한다. New Patterns는 아직 진행하지 않았다. 초안 검토와 exercise 근거가 없으므로 concept state 변경 없음.

## 후속 문답: 모듈화와 학습 방법의 관계

- 학습자 설명: Search, Routing, Generation을 모듈화하고 다양한 순서로 재사용하면서 RAG 패턴과 모듈 학습 방법이 다양해졌다. 질문: 여러 평가 case를 만들 수 있기 때문인가?

<!-- ai:draft -->
모듈화는 역할별 입출력과 교체 경계를 분명하게 하므로, 다른 모듈을 고정한 채 특정 모듈만 학습하거나 여러 모듈을 공동으로 조정하기 쉽게 한다. 예를 들어 생성기를 고정하고 검색기를 학습하거나, 검색기를 고정하고 생성기를 fine-tuning하거나, 생성기의 피드백을 검색기 학습 신호로 사용할 수 있다. 핵심은 평가 사례 수의 증가보다 학습 대상과 피드백 연결을 선택하기 쉬워지는 것이다. 다양한 평가와 ablation은 이를 비교하는 데 도움이 되지만 모듈화만의 고유한 결과는 아니다.

근거: survey v5 p.4 II.C는 순차 처리 및 통합 end-to-end 학습을, p.5 II.C.2는 검색기 fine-tuning, 생성기 fine-tuning, 협력 fine-tuning의 결합을 언급한다. 위 인과 설명은 원문 기반 해석이며 모듈화가 이런 학습법을 최초로 가능하게 했다고 주장하지 않는다. 모든 모듈이 학습 가능한 것은 아니며, 공동 학습에는 적절한 학습 신호와 최적화 방법이 별도로 필요하다. 순서는 각 모듈의 입력 의존성을 만족해야 한다.
<!-- /ai:draft -->
