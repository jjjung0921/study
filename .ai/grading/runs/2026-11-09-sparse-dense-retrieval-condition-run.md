# U3 독립 채점 실행 기록

- Exercise: exercises/2026-11-09-sparse-dense-retrieval-condition.md
- Input snapshot: .ai/grading/71252f23bf975136b2c9270bb4173e3b6cbe551efffa199042b7d3371283de28.json
- Snapshot SHA-256: 549c01b647e8d9e0fc8e8862475859183d64aa6976f485b3dbf81168f7726622
- Tutor: codex
- Grader: study-grader
- Invocation: claude -p --agent study-grader --permission-mode acceptEdits --output-format json 'exercise: exercises/2026-11-09-sparse-dense-retrieval-condition.md'
- Runtime reference: Claude session c127ea0e-b2f5-417f-82e1-9d0182f03ad2; exec session 47202
- Completed: 2026-11-08T16:08:54+00:00
- Exit status: 0
- Raw output: [Claude 실행 원출력](2026-11-09-sparse-dense-retrieval-condition-claude-retry-raw.json)
- Result: partial

사용자는 채점 전 "확인했어. 채점해줘"로 전사를 확인했다. 호출 전 prepare snapshot을 생성했고, 최초 인증 실패 뒤 로그인 완료 통보를 받아 같은 보호 입력으로 재호출했다. 위 완료 시각은 호출자가 종료를 관측하고 현재 시각을 확인한 시점이다.

채점자 런타임에서는 일부 읽기와 검사 명령의 권한이 거부되었다. 채점자는 Grading과 Next를 작성했으며, 호출자가 보호 입력 해시 및 기록 구조 검사와 별도 Codex 리뷰를 진행한다. 이 실행 기록 자체가 판정의 의미적 정확성을 인증하지는 않는다.

## 별도 채점 리뷰

- Invocation: codex exec --sandbox read-only --skip-git-repo-check --disable apps (원격 쓰기 도구 차단 옵션 포함)
- Runtime reference: Codex session 01a1bbeb-ee44-7e50-8e34-30e553c9ff59; exec session 38180
- Exit status: 0
- 원출력: [Codex 리뷰 실행 로그](2026-11-09-sparse-dense-retrieval-condition-review-retry-raw.log)
- 판정: R1 ✗, R2 ✓, R3 ✗, partial에 모두 동의.
- 결과: `exercises/cross/2026-11-09-sparse-dense-retrieval-condition-grading-codex.md`
- 출처 기록 보완: 리뷰어는 실행 기록 교체 전 exercise를 읽어 과거 인증 오류 문구를 지적했다. 호출자가 실제 성공 실행 원출력과 session ID에 근거해 Grader Run을 연결한 뒤 check를 통과했다. 판정 이견은 없으며 리뷰 원문은 보존했다.
