# RAG 블로그 작성 검증 — 재료와 판정 기준

작성일: 2026-10-30. 대상: [초안](../drafts/rag-sequence-token-marginalization.md).

## 요청과 구성 선택

- 사용자는 RAG 학습 QA로 실제 블로그 작성 흐름을 검증하고, 작성·문체 편집은 적합한 Codex 모델로 실행하도록 요청했다.
- 사용자가 고른 구성: “수식 이해 중심: 메모리 → Sequence/Token 계산 → 학습·디코딩 → 실험의 한계”.
- 기존 글 확인: qmd에서 RAG·논문명을 검색한 뒤 지정 폴더를 직접 검색했다. `~/projects/portfolio/src/content/notes/ko/`의 Markdown에서 RAG 전용 글을 찾지 못했다. 새 글 초안으로 진행한다. 게시 승인은 받지 않았다.
- 스타일 참고: `~/projects/portfolio/src/content/notes/ko/typescript/ts-generics.md`. 기존 프로필의 `AI/performative-prediction.md` 경로는 존재하지 않아 사용하지 않았다.

## 재료

- 대화 원문: `~/.agents/audits/2026-10-28-rag-qa-agent-validation/source/conversation.json` (E001–E137).
- QA 복기: `~/.agents/audits/2026-10-28-rag-qa-agent-validation/review/qa-retrospective.md`.
- 논문 텍스트: `~/.agents/audits/2026-10-28-rag-qa-agent-validation/source/rag-paper.txt` (arXiv:2005.11401v4).
- 블로그 규격: `~/projects/portfolio/src/content/config.ts`.

## QA → 초안 → 원문

| QA 근거 | 반영 위치 | 논문 근거 | claim 유형 |
|---|---|---|---|
| 논문이 제시한 배경 | 문제 도입 | §1 | source-supported interpretation |
| E018, E020, E054–E061: 메모리와 외부 문서 | §0 | §2.2–2.3, §5 | source-supported interpretation |
| E030, E032, E044: 합·곱·행렬·전체 답변 | §1–4 | §2.1, §2.5 | source-supported interpretation |
| E040, E042, E049: N과 길이 1 | §1, §4 | §2.1 | source-supported interpretation |
| E032: 한 문서 확률 0 | §4 | §2.1의 합 | verified fact (예제 산술) |
| E072, E078: optimizer와 감독 | §5 | §2.4 | source-supported interpretation |
| E086, E088: 문서별 beam과 속도 | §6 | §2.5, Appendix A | source-supported interpretation; 속도 우열 미검증 |
| E088, E129, E131: 다양성 가설 | §7 | §4.5, Table 5 | 관측 수치는 source-supported interpretation; 원인은 hypothesis |
| E118: 근거 검색 평가 | §7 | §4.4, Appendix E | source-supported interpretation |

## 통과 기준

- 질문을 학습자의 확정 오답으로 집계하지 않는다. 확인되지 않은 숙련도·재현·실험을 주장하지 않는다.
- 문서별 같은 후보, 위치별 스칼라와 어휘 분포, EOS를 포함한 예제, N=1 경계가 일관된다.
- 예제 산술과 논문 Table 5·Appendix A 값을 대조한다.
- 전체 본문은 절별 `ai:draft` 마킹으로 남긴다. 필수 frontmatter와 translationKey 중복을 확인한다.
- 윤문 전후 수식·숫자·표·직접 인용·링크·frontmatter·마킹 보존을 확인한다.
- 정적 검증, 원문 대조, 문체 에이전트 실행, 사용자 검토를 별도로 기록한다.

## 범위 밖

학습자 이해도 채점, 공식 구현·latency 재현, 포트폴리오 게시, 커밋·푸시. 기존 RAG 학습 curriculum 및 concept state는 이 글의 생성으로 완료 처리하지 않는다.
