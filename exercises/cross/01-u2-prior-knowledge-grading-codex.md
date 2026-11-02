| 항목 | 채점 표시와의 비교 | 확정 Attempt 근거 |
|---|---|---|
| LLM | **✗ 동의.** 앞선 토큰을 다음 토큰 예측의 *조건*으로 설명하지 않았다. 다만 부적절한 검색 문서도 사실과 다른 답의 가능한 원인이므로, 그 이유 자체를 틀렸다고 본 채점 근거에는 동의하지 않는다. | “앞서 나온 토큰은 자연스러운 문장이 될 수 있도록 돕는다”, “부적절한 문서라면 실제와 다른 답이 산출될 수도 있다” ([Attempt](/Users/leejungjin/study/RAG/exercises/01-u2-prior-knowledge.md:22)) |
| Embedding | **✗ 동의.** 유사도가 무엇을 뜻하는지 설명하지 못했고, 정답성이나 근거 충실성이 보장되지 않는다는 구분도 분명히 하지 않았다. | “무엇을 의미하는 지는 명쾌하게 설명할 수 없으나”, “근거가 되는 문서가 될 확률이 높을 것” ([Attempt](/Users/leejungjin/study/RAG/exercises/01-u2-prior-knowledge.md:24)) |
| Python | **✗ 동의.** 점수와 문서의 인덱스를 대응시켜 B를 찾지 않았다. 다만 이 답만으로 softmax가 *필수*라고 생각한다고 단정할 수는 없다. | “softmax를 수행한 뒤 확률이 높은 k개의 문서를 선정한다” ([Attempt](/Users/leejungjin/study/RAG/exercises/01-u2-prior-knowledge.md:26)) |

**종합 `fail`에 동의한다.** Rubric은 충족 항목이 없으면 `fail`로 정한다([Rubric](/Users/leejungjin/study/RAG/exercises/01-u2-prior-knowledge.md:13)). 전사 확인은 `OK`이고([확인](/Users/leejungjin/study/RAG/exercises/01-u2-prior-knowledge.md:28)), [MISCONCEPTIONS.md](/Users/leejungjin/study/RAG/concepts/MISCONCEPTIONS.md:10)에는 기존 active 항목이 없다. 판정과 별개로, 위 두 오개념 추정은 Attempt만으로 확정하기 어렵다.
