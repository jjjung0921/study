---
name: learner-feedback
description: RAG 학습자의 U2 후속 설명과 채점 메모리 교정
metadata:
  type: user
---

## U2 오개념 추정 철회 (2026-11-02)
학습자는 부적절한 검색 문서가 오류를 낳을 수 있다는 뜻이었고, softmax는 학습에서 흔히 사용된다는 뜻이었다고 후속 설명했다. 독립 리뷰도 원래 Attempt만으로 두 오개념을 확정할 수 없다고 판정했다. `exercises/01-u2-prior-knowledge.md`에는 두 후보가 철회되어 있다.
Why: 원래 Attempt의 Rubric 판정과 학습자의 실제 개념 이해를 혼동해 다음 채점에 잘못된 선입견을 남기지 않기 위해.
How to apply: U2의 fail은 원래 Attempt에서 요구 사항을 명시하지 못한 결과로만 참고한다. 철회된 두 추정을 학습자의 오개념이나 반복 패턴으로 취급하지 않는다.
