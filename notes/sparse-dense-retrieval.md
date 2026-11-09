# Phase 02 U2: Sparse와 Dense Retrieval

<!-- ai:draft -->
고객은 "핸드폰 잃어버렸는데 잠깐 막을 수 있나요?"라고 묻고 문서는 "단말기 분실 시 회선 일시정지"라고 쓸 수 있다. 이 가상 사례는 같은 의도라도 어휘가 다를 수 있음을 보여준다. 실제 검색 순위는 실험하지 않았다.

BM25 같은 sparse 방식은 단어 일치에 가중치를 부여한다. Dense 방식은 질문과 문서를 학습된 벡터로 표현하여 관련성을 점수화한다. 전자는 정확한 용어 일치를 활용하고 후자는 학습을 통해 표현이 다른 관련 문서를 찾을 수 있다. Dense가 의미를 완벽히 이해하거나 항상 더 좋은 결과를 내는 것은 아니다.

두 방식 모두 질문과 문서 집합에서 상위 k개 후보를 선택한다. 정책 적용 조건, 부정 표현, 상품 코드 등 세부 구분은 결과에서 확인해야 한다. 이 차이가 검색된 근거를 평가하는 다음 연습으로 이어진다.

근거: [DPR evidence](../evidence/karpukhin-2020-dpr.md), Introduction과 Sections 3.1-3.2. 다음 읽기: 원문 p.6769 Introduction, pp.6770-6771 Section 3.1. Eq. (2)의 상세 유도는 첫 읽기에 요구하지 않는다.
<!-- /ai:draft -->

## 진행

- 2026-11-09 U2 시작. 초안 검토와 학습자 원문 읽기는 미확인. concept state는 unseen 유지.

## Section 3.2 질문

## U3 피드백 후 보충 설명

- 학습자: "DPR에 대한 내용을 Passage의 유사성으로 바꾸면 될 거 같고", "baseline을 삼는 건 Naive RAG로 삼아서 두 방식이 기존의 RAG 방식 대비 어떤 점에서 강점을 보이는지 비교".
- 튜터 피드백: DPR의 점수는 passage끼리의 유사성이 아니라 학습된 질문 벡터와 passage 벡터의 내적이다. Naive RAG는 처리 흐름의 범주이고 BM25와 DPR은 그 안에 사용할 수 있는 검색 방법이므로 서로 배타적인 대안이 아니다. 검색 방법만 비교하려면 같은 Naive 흐름 안에서 BM25를 쓰는 구성과 DPR을 쓰는 구성을 비교하고, 문서 집합, 질문, top-k, 생성기, prompt 구성 방식을 동일하게 유지한다. 검색 성능과 최종 답변 성능은 구분한다. 어느 쪽이 우수한지는 결과를 확인해야 한다.
- 이는 학습 피드백과 보충 설명이다. 보호된 원래 Attempt, Rubric, partial 판정을 변경하지 않으며 소급 재채점이나 state 승격 근거로 쓰지 않는다.

### 검토 후 보완 정리

학습자가 "응. 그렇게 보완해줘"라고 요청해 다음 보충 정리를 반영했다. 이는 피드백 후 설명이며 원래 제출 답안이 아니다.

1. BM25는 질문과 passage의 어휘 일치에 가중치를 부여한다. DPR은 학습된 encoder로 질문과 passage를 각각 벡터화하고 두 벡터의 내적으로 관련성을 계산한다. 따라서 "잃어버리다"와 "분실" 같은 표현 차이를 포괄할 수 있지만, 단어끼리의 유사성만 비교하는 방식은 아니다.
2. 첫 비교에서는 Naive RAG를 공통 처리 흐름으로 두고, BM25를 사용하는 구성을 baseline, DPR을 사용하는 구성을 비교 대상으로 삼는다. 상품 코드 구분을 명시적으로 점검할 기준선을 마련하고, DPR이 어휘 불일치를 보완하는지 함께 확인하려는 설계다. BM25가 반드시 코드를 구별하거나 DPR이 반드시 의미를 잘 매칭한다고 가정하지 않는다.
3. 문서 집합, 평가 질문, top-k, 생성기와 prompt 구성 방식은 동일하게 유지하고 검색 방식만 교체한다. 검색된 근거의 관련성 및 상품 코드 일치와 최종 답변 품질을 구분해 평가한다. 성능 우위는 실험 전 확정하지 않는다.

위 비교는 개념 설명을 위한 설계 예시이며 실험 실행 결과가 아니다. 이 보충 정리만으로 U3 pass나 concept state 승격을 기록하지 않는다.

- 2026-11-09: 학습자가 종료 기준 변경을 요청해 [DR-0010](../curriculum/decisions/DR-0010-u3-completion-after-feedback.md)에 따라 U3 학습 절차는 완료 처리했다. exercise는 partial 유지, concept state는 변경 없음이다.

## Section 3.2 추가 기록

- 후속 질문: positive를 하나만 설정한 별도 이유가 있는가?
- [fact] 원문 Sections 3.2와 4.2는 단일 positive 학습 구성과 positive 선정 절차를 설명한다. 확인한 해당 절에서 단일 positive가 다중 positive보다 우수하다는 비교 근거는 찾지 못했다.
- [derived] 질문별로 선택한 근거 하나를 사용하면 모든 관련 passage를 주석할 필요 없이 기존 QA 자료에서 학습 항목을 구성할 수 있고, 기본 in-batch 점수표에서 행마다 대각 positive 하나를 지정하는 구성이 단순해진다. 이는 데이터 및 목적함수 구성에 대한 해석이며 저자가 명시한 단일 positive 선택 동기나 최적성 결론으로 취급하지 않는다. 다중 positive도 가능하나 표시된 positive 집합과 그에 맞는 목적함수 또는 sampling 처리가 필요하다.

- 후속 질문: false negative를 굳이 넣는 장점이 있는가? positive 하나는 식의 표기에만 해당하는가?
- 튜터 설명 보완: 의도한 것은 다른 질문의 positive를 현재 질문의 negative로 재사용하는 것이며, 실제 관련 passage가 섞이는 false negative를 의도적으로 만드는 것이 아니다. Hard negative는 표면적으로 비슷하지만 실제로 무관한 비교 대상인 반면 false negative는 관련 문서를 잘못 negative로 취급한 것이다. 두 개념은 구분한다.
- 원문 Section 3.2는 학습 데이터의 각 instance에 relevant passage 하나를 두고, in-batch에서도 질문마다 relevant passage 하나를 연결한다고 명시한다. Section 4.2는 정답만 주어진 데이터에서 정답 문자열을 포함하는 BM25 최고 순위 passage 하나를 positive로 선택한다고 설명한다. 따라서 positive 하나는 수식만의 단순화가 아니라 이 논문의 학습 구성이다. 실제 corpus나 원래 QA 자료에 관련 근거가 하나뿐이라는 뜻은 아니다.

- 학습자 질문: positive와 negative의 선정 주체, gold passage의 의미, positive가 하나인 이유, QP^T가 공통 공간으로 정사영시키는 행렬인지.

<!-- ai:draft -->
- Positive는 데이터셋의 정답 근거 passage를 사용하거나, 질문과 정답만 있으면 BM25 상위 결과 중 정답 문자열이 포함된 passage를 택해 구성한다. DPR Section 4.2는 후자의 경우 최고 순위의 해당 passage를 택하고 top 100에 없으면 질문을 제외한다고 설명한다. 데이터셋의 사람 주석과 학습 전처리 절차를 구분한다.
- Negative는 학습 구성 절차가 고른다. Section 3.2의 Random은 무작위 문서, BM25는 단어는 맞지만 정답을 포함하지 않는 상위 문서, Gold는 다른 질문의 positive passage다. 휴리스틱이므로 실제로 관련된 문서가 negative가 되는 가능성은 있다.
- Gold는 참조 정답 또는 정답 근거를 뜻한다. 이 논문의 gold negatives에서는 다른 질문의 정답 근거 문서를 현재 질문의 negative로 재사용한다. 모든 질문에 대한 좋은 문서라는 뜻이 아니다.
- Eq. (2)는 한 학습 항목에 positive 하나를 두고, 기본 in-batch 구성은 B개 질문과 각 질문의 positive 하나로 이뤄진다. 실제 세상에서 관련 passage가 하나뿐이라는 뜻은 아니다. 별도 BM25 negative를 추가하는 최종 구성은 기본 B×B 설명보다 후보가 많다.
- Q와 P는 각 B×d 행렬로, 이미 encoder를 통과한 질문과 passage 벡터를 행에 담는다. S=QP^T는 B×B 점수표이며 S_ij는 질문 i와 passage j의 내적이라는 스칼라다. 대각 원소는 지정 positive, 비대각은 이 학습 구성에서 negative다. d차원 벡터의 외적이나 공통 공간으로 보내는 정사영 행렬이 아니다. Encoder들이 학습되어 질문과 passage가 내적으로 비교 가능한 표현을 갖게 되며, S 자체가 그런 표현 변환을 수행하지 않는다.

근거: [DPR evidence](../evidence/karpukhin-2020-dpr.md), Section 3.2와 Eq. (2), pp.6771-6772, Section 4.2 p.6772. 행렬 차원과 각 원소 해석은 원문에 따른 기본 선형대수 해석이다.
<!-- /ai:draft -->

## 학습자 설명 검토

- 학습자 설명: "ICT는 문서의 다음 단어를 예측"하고 "BERT를 사용해 pre-train으로 인한 계산량을 줄이고 question-answer pair로 학습"한다. "문서 벡터는 추론 단계에서 생성"하고 질문과 내적으로 비교한다.
- 정확한 부분: 표현이 달라도 관련 문서를 찾으려는 동기, DPR의 질문과 passage 벡터 간 내적 계산.

<!-- ai:draft -->
- ICT는 next-token prediction이 아니다. ORQA에서 사용한 inverse cloze task는 가려 둔 문장을 질의처럼 사용해 그 문장이 속한 문서 블록을 찾는 추가 사전학습이다. DPR Introduction은 이런 일반 문장이 실제 질문의 좋은 대리인지 분명하지 않다고 지적한다. 문서에서 온 정답 블록을 모른다는 뜻이 아니다.
- DPR은 이미 사전학습된 BERT를 출발점으로 삼고, ORQA의 ICT 같은 추가 사전학습 없이 관련 질문-passage 쌍으로 encoder를 fine-tuning한다. BERT 사전학습 자체를 없앴다는 뜻이 아니다. 질문-정답 자료만 있을 때는 답 문자열을 이용해 positive passage를 구성할 수 있다.
- 서비스용 passage 벡터는 질문이 들어오기 전에 passage encoder로 일괄 계산하고 오프라인 색인한다. 질문이 들어오면 question encoder로 질문 벡터를 계산하고 내적으로 상위 passage를 검색한다. 원문의 Inference 절이 오프라인 준비와 온라인 실행을 함께 기술하므로, 절 제목만으로 passage 인코딩이 질문마다 일어난다고 해석하지 않는다. encoder가 변경되면 기존 passage 벡터와의 일관성을 점검하고 필요하면 다시 인코딩해야 한다.
- Dense 벡터의 점수는 질문과 passage의 학습된 관련성이지 단어들의 동일한 의미 여부만을 판정하는 것은 아니다. BM25 또한 단어 일치뿐 아니라 단어별 가중치 등을 사용한다.

근거: [DPR evidence](../evidence/karpukhin-2020-dpr.md), Introduction pp.6769-6770, Section 3.1 Inference p.6771, Section 4.2 Selection of positive passages p.6772. 벡터 갱신 시 일관성 설명은 고정된 encoder로 문서와 질의를 표현하는 설계에서의 해석이다.
<!-- /ai:draft -->

- 정식 exercise의 Attempt나 채점이 아닌 학습 피드백이다. 추가 설명 재현을 요구하지 않으며 concept state는 변경하지 않는다.
