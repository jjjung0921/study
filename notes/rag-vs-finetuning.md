# Phase 02 U1: RAG와 Fine-tuning 비교 문답

## 학습자 질문

- FT의 환각 감소가 작은 데이터를 반복 학습하기 때문인가?
- 개인별 FT 파라미터를 JSON으로 저장하는가? 자원 비용이 크지 않은가?
- unsupervised FT의 학습 절차는 무엇인가?
- 새로운 지식에서 outperform했다는 말과 새로운 사실 학습이 어렵다는 말은 모순인가?

<!-- ai:draft -->
## 설명

- survey II.D는 FT가 환각을 줄일 수 있다고 서술한다. FT가 항상 환각을 줄이거나 RAG보다 환각이 적다는 비교 결과로 읽지 않는다. 올바른 도메인 지식이나 근거 사용, 답변 유보 행동을 학습하면 오류를 줄일 수 있다는 것은 일반적인 조건부 설명이다. 동일 데이터를 반복하는 것만으로 사실의 정확한 활용과 일반화가 보장되지 않는다.
- FT는 사용자별 모델을 필수로 요구하지 않는다. 전체 FT를 개인별로 하면 저장 부담이 크지만, LoRA 등 PEFT 방식은 공통 base model과 작은 개인별 adapter를 분리할 수 있다. Hugging Face PEFT에서는 adapter_model.safetensors 등에 가중치 텐서를, adapter_config.json에는 구성을 저장한다. 특정 에이전트 회사의 실제 저장 방식은 확인하지 않았다. 저장과 실행 메모리 비용은 구분한다.
- 인용 논문의 unsupervised FT는 원시 문서로 next-token prediction을 계속하는 continual pre-training이다. 문서의 토큰을 입력으로 삼고 앞선 토큰에서 다음 토큰을 예측하게 해 손실을 계산하고 가중치를 업데이트한다. 사람이 QA 정답을 붙이지 않지만 문서 자체에서 학습 목표가 나온다는 뜻에서 self-supervised라고도 한다. QA 평가와 문서 기반 학습을 구분한다.
- 해당 논문은 문서를 256-token 학습 단위로 구성하고 BOS/EOS로 원래 문서 조각 경계를 표시했다. 세 7B 모델을 최대 5 epochs, batch size 64로 학습했다. 이는 논문 설정이며 보편 절차의 필수값이 아니다.
- 원문 "RAG consistently outperforms it"에서 it은 unsupervised FT다. 기존 지식과 새 지식 모두에서 RAG가 FT보다 우수했다는 비교와, FT로 새 사실을 배우기 어려웠다는 결과는 양립한다. 별개의 지식 개념을 도입해 모순을 해소할 필요가 없다.
- 이 결과는 Llama2-7B, Mistral-7B, Orca2-7B와 해당 MMLU 및 시사 객관식 평가 설정의 결과다. 모든 FT나 모델에 대한 불가능성 정리가 아니다. 논문은 같은 사실의 여러 paraphrase가 FT 결과를 개선할 수 있음도 보고한다. 반복 노출과 다양한 표현의 노출을 구분한다.

## 원출처

- [Gao survey v5](https://arxiv.org/pdf/2312.10997v5), p.5 II.D와 reference [28].
- [Ovadia et al.](https://arxiv.org/pdf/2312.05934v3), p.1 abstract, p.4 Section 3.2, p.5 Table 2, p.6-8 Sections 5-6. 원문 관련 절과 표를 확인했으며 전체 논문 재현은 하지 않았다.
- [Hugging Face PEFT checkpoint format](https://huggingface.co/docs/peft/developer_guides/checkpoint), PEFT files: 가중치와 구성 파일 및 base model 분리.
<!-- /ai:draft -->

## 진행

- U1 II.D 관련 설명 초안. 개인화 저장의 세부 구현은 현재 unit에서 확장하지 않는다. exercise 채점이나 concept state 변경 없음.

## 후속 질문: 사용자 지침과 학습의 정답

- 학습자 질문: AI agent의 사용자 설정 지침은 FT인가? Unsupervised FT의 예측이 정답임을 확신할 수 있는가?

<!-- ai:draft -->
사용자 지침은 일반적으로 저장한 텍스트를 실행 시 모델의 입력 문맥에 제공해 동작을 유도하는 방식이다. 저장된 설정이 지속되는 것과 모델 가중치가 학습으로 변경되는 것은 별개다. 특정 제품의 별도 학습 절차나 대화 데이터 사용 정책은 확인하지 않았으며, 지침 저장 자체를 FT의 증거로 보지 않는다.

다음 토큰 예측에서는 모델의 예측을 정답이라고 가정하지 않는다. 학습 문서에 실제로 등장하는 다음 토큰이 비교할 target이며, 모델이 그 토큰에 부여한 확률에 따라 손실을 계산한다. 문서에 잘못된 사실이 있으면 그 문장을 잘 예측하도록 학습할 수도 있다. 따라서 관측 토큰이라는 학습 목표의 확정과 문장 내용의 사실성은 구분한다. 가능한 다음 표현이 여럿이어도 해당 예시에서는 관측된 토큰이 target이다. 학습 손실 감소만으로 factual QA의 정확성을 보장하지 않는다.

근거: 위 Ovadia et al. Section 3.2의 causal autoregressive next-token 학습 설명에 기반한 해석. 사용자 지침과 FT의 구분은 입력 문맥과 가중치 업데이트의 기술적 차이에 대한 설명이며 특정 서비스 내부 구현을 확인했다는 주장이 아니다.
<!-- /ai:draft -->
