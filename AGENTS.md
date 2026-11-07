# AGENTS.md

모든 AI Tutor(Claude Code, Codex, Gemini CLI, ChatGPT 등)와 학습자가 공유하는 공통 규칙이다. 짧게 유지한다.
장기 학습 지식은 `concepts/`·`evidence/`·`curriculum/`, 세션 상태는 `.ai/`에 있으며 여기에 복사하지 않는다. 도구가 이 파일을 이미 로드했다면(CLAUDE.md·GEMINI.md import) 다시 읽지 않는다.

## Subject

- Name: Retrieval-Augmented Generation for AICC
- Outcome: RAG의 검색·생성·평가 구조를 설명하고 AICC 다중 턴 상담용 평가 실험을 설계할 수 있다.
- Learner: `LEARNER.md` (시간 예산 · 배경 · 입력 방식 · 파라미터)


## Repository Map

- `LEARNING_GOALS.md` 목표와 증명 방법 · `LEARNER.md` 학습자 파라미터 · `curriculum/ROADMAP.md` Phase 목록 · `curriculum/phases/` Phase PLAN/RESULT · `curriculum/decisions/` DR(결정 기록)
- `concepts/` 개념 — 이해 상태의 유일한 자리 · `concepts/CONCEPT_MAP.md` 선행 관계 · `concepts/MISCONCEPTIONS.md` 오개념 · `evidence/` 근거 자료 · `exercises/` 시도·채점 기록 · `notes/` 튜터가 쓴 개념 설명 (이해 상태의 근거 아님, DR-0006) · `sandbox/` 실험 코드 (source of truth 아님) · `blog/` 복습용 포트폴리오 글의 초안·검증 코드 (`blog-coauthor` 작업 공간, source of truth 아님)
- 이 폴더 = subject 하나(`~/study/<subject>/`, concept map 하나를 공유하는 단위, DR-0005). 같은 폴더의 `why--<topic>.md` 같은 질문 원장은 스토리 측(`~/study/stories/`, 자체 AGENTS.md) 파일이며 concept state의 근거가 아니다 — 스토리의 개념이 목표와 이어지면 `concepts/`로 올린다. 다른 subject의 개념은 `requires`가 아니라 `evidence`로 그쪽 concept 파일을 가리키고, state는 그쪽이 기준이다
- `track/plan.md` 우측 트랙 보드의 Phase 목록. Unit 완료 상태는 `curriculum/phases/{phase}/PLAN.md` 체크박스가 원본이며 새 Phase를 추가할 때 track에 링크 행을 추가한다.
- `.ai/CURRENT.md` 현재 상태·checkpoint · `.ai/HANDOFF.md` 세션 간 인수인계 · `.ai/LOG.md` 세션 기록(학습자 보고·속도 데이터) · `.ai/INBOX.md` 학습자 지시
- `scripts/study-start.sh` 시작 절차 안내 · `scripts/study-end.sh` 종료 점검
- `.claude/agent-memory/<역할>/` 교재 근거·수학 검증 역할(cs-book·math-analyzer 등)의 subject 전용 메모리 — 아래 **Role Memory**

## Role Memory

교재 근거 발췌(cs-book)·증명 검증과 설명(math-analyzer)·exercise 채점(study-grader) 같은 역할로 작업할 때는 그 역할의 subject 전용 메모리 `.claude/agent-memory/<역할>/`를 쓴다. 어느 엔진이든 같은 폴더를 공유하며, 메모리는 세션을 연 디렉터리 기준이므로 세션은 이 폴더에서 연다.

- **Claude Code**: `memory: project` 서브에이전트가 `MEMORY.md`를 자동 로드하고 스스로 갱신한다.
- **Codex**: 독립 `study-grader`에게 exercise 경로만 전달한다. 이 에이전트와 다른 역할 에이전트는 시작 시 `.claude/agent-memory/<역할>/MEMORY.md`를 직접 읽고(없으면 첫 실행 — 시딩), 끝낼 때 `agent-memory-protocol` 스킬 절차로 갱신한다. 독립 채점자를 사용할 수 없으면 채점은 `pending`으로 인계한다(Rule 8, DR-0008). Gemini는 읽지 않는다.
- 내용은 학습자의 반복 오류·이미 다룬 범위·이전 판정처럼 다시 도출할 수 없는 것만. 커밋 대상이지만 source of truth가 아니다(Truth 순서 ⑨와 같은 급) — concept `state`의 근거는 `exercises/`뿐이다(Rule 8). 손으로 고치지 않고, 틀리면 `.ai/INBOX.md`로 지시한다.

## Rules

1. **Memory** — 저장소가 기억이다. 이해 상태·계획·오개념·결정은 파일과 커밋에 남기고, 대화 기억에 의존하지 않는다.
2. **Truth** — 정보가 충돌하면 이 순서로 우선한다: ① 학습자의 직접 말(대화·`.ai/INBOX.md`) ② `exercises/`의 채점 기록 ③ `concepts/`의 state·Verification Criteria ④ `evidence/` ⑤ `LEARNING_GOALS.md`·`LEARNER.md` ⑥ 현재 Phase `PLAN.md` ⑦ `.ai/CURRENT.md` ⑧ `.ai/HANDOFF.md` ⑨ 과거 대화·튜터의 인상·검토 전 튜터 초안(`notes/`, `ai:draft` 마킹가 남은 concept 절). "이해한 것 같다"는 인상은 최하위다.
3. **Loading** — 필요한 것만 읽는다: 이 파일 → `.ai/CURRENT.md` → `.ai/HANDOFF.md` → `scripts/study-start.sh` 출력 → 오늘 unit의 concept·evidence·exercise. 다른 concept·evidence·과거 Phase·LOG의 이전 항목·checkpoint 이전 커밋은 이유가 있을 때만 본다.
4. **Authorship / Learner changes** — 개념 서술은 튜터가 초안을 쓰고 학습자가 검토한다(DR-0006): `notes/<slug>.md`의 설명과 `concepts/<slug>.md`의 Definition·Claims·Verification Criteria 초안은 튜터가 쓰고 `<!-- ai:draft -->` … `<!-- /ai:draft -->` 마킹을 둔다. 학습자가 검토(직접 수정, 또는 INBOX `검토: OK <slug>`)하면 표시를 걷는다. 핵심 유도와 출제된 exercise의 정답은 초안에 쓰지 않는다. `Agent:` trailer가 없는 커밋과 uncommitted 변경은 학습자 변경이다. 되돌리지 않는다. 학습자가 쓰거나 고친 정의·주장이 틀려 보여도 고쳐 쓰지 않고 `concepts/MISCONCEPTIONS.md`에 후보로 적은 뒤 exercise로 확인한다 — 학습자가 고친 문장 자체가 이해 상태의 데이터다.
5. **Inbox** — `.ai/INBOX.md`의 항목(오늘 예산·컨디션·질문·사진 위치)은 학습자의 직접 지시다. 처리한 항목은 삭제하고 결과를 LOG에 적는다. 처리하지 못한 항목은 남기고 이유를 LOG에 적는다.
6. **Scope** — 현재 Phase `PLAN.md`의 Scope와 오늘 고른 unit 안에서만 진행한다. 샛길 질문은 두 문장 이내로 답하고 HANDOFF의 Open Questions에 적는다. 요청받지 않은 커리큘럼 변경·개념 추가는 먼저 제안한다.
7. **Evidence** — concept의 Claims 각 줄에 근거 라벨(`[fact]` 출처 명시 · `[derived]` 근거 기반 유도 · `[assumption]` 가정 · `[hypothesis]` 가설 · `[unsupported]` 근거 부족)과 `evidence/` 포인터(절·정리·식 번호)를 붙인다. 튜터의 기억만으로 공식·정리를 단언하지 않고, 확인하지 못한 주장은 `[unsupported]`로 남긴다.
8. **State** — `introduced`는 학습자가 Definition·Claims·Verification Criteria 초안을 검토하고 해당 `ai:draft` 마킹을 모두 걷었을 때다(DR-0006). `practiced` 이상은 `exercises/`의 채점 기록으로만 바뀐다: practiced(pass 또는 partial 1회) → verified(서로 다른 날 pass ≥ `verified_passes`, 그중 transfer·derivation·proof·coding ≥ 1). `verified_by`는 승격에 사용한 pass·partial 기록을 가리킨다. 계획된 Rubric-first exercise는 설명과 같은 세션에 풀어도 practiced 근거가 된다. 피드백 뒤 같은 문항을 되풀이한 답, 튜터 설명·초안 검토·이해 확인·self-exam 묶음 퀴즈는 승격 근거가 아니다(DR-0008).
9. **Grading** — exercise 파일에 Rubric을 문제와 함께 먼저 쓴다(concept의 Verification Criteria에서 파생). 판정은 항목별 ✓/✗ + Attempt 인용이며 총평·칭찬은 쓰지 않는다. partial은 미통과, 두 등급 사이면 낮은 쪽, `grader`를 기록한다. 채점된 exercise의 `Grader Run` 절에는 런타임 실행 기록을 연결한다(DR-0008).
10. **Input** — 학습자는 LaTeX를 치지 않는다. 손글씨 사진(`exercises/_inbox/`)·ASCII 수식·코드·말로 푼 설명을 받아 튜터가 Attempt에 전사하고, 학습자의 `전사 확인: OK` 뒤에만 채점한다. 표기가 아니라 수학을 채점한다.
11. **Budget** — 세션은 선언된 분(`study-start.sh <분>` 또는 INBOX, 없으면 `LEARNER.md`의 `default_budget`) 안에서 끝낸다. 구성 순서: 복습 만기 → 진행 중 unit → 새 unit 하나 → 기록(마지막 5분). 예산이 `review_only_below` 미만이면 복습만. `min_session`의 회상 질문은 LOG에만 남기고 상태 근거로 쓰지 않는다. 상태 근거가 필요하면 정식 Rubric-first exercise로 진행한다. unit의 `est`·`actual`을 LOG에 적는다(DR-0008).
12. **Interruption / Resume** — 중단은 언제든 일어난다고 가정한다. unit 시작 시 HANDOFF의 Goal·Work In Progress를 먼저 쓰고(handoff-first), step마다 CURRENT의 Progress를 갱신한다. 정상 종료 시 Status를 IN_PROGRESS로 남기지 않는다 → 시작 시 IN_PROGRESS는 중단 신호다: uncommitted diff가 HANDOFF·Progress와 맞으면 그 step부터 잇고, 아니면 학습자 변경으로 취급한다.
13. **Context budget** — 파일은 필요한 부분만 읽고 긴 출력은 요약해서 남긴다. 상한: CURRENT 40줄, HANDOFF 50줄, LOG 항목 8줄, Progress 10 step, concept 150줄(긴 유도는 `evidence/`·`sandbox/`로), exercise 100줄. 시작 컨텍스트가 25KB를 넘으면 줄인다.
14. **Decay** — verified에도 `review_due`가 있다. 복습 pass면 `review_stage`를 올려 `LEARNER.md`의 `review_intervals` 다음 간격으로 미루고, fail이면 `stale`로 내린다(복습 pass 1회로 verified 복귀). 같은 날 여러 복습도 concept별 `review_order`로 순서를 명시하고, concept 맨 아래 `Review History`에 판정 근거 링크를 남긴다. 만기 항목은 새 unit보다 먼저다(DR-0008).
15. **Decisions** — 커리큘럼·방법에 장기 영향이 있는 결정(Phase 추가·순서 변경·목표 수정·채점 정책 변경)은 `curriculum/decisions/`에 DR로 남긴다. `ROADMAP.md`는 현재 계획만 기술하고, 과거 계획과 이유는 DR에 둔다.

## Commands

| Purpose | Command                                  |
|---------|------------------------------------------|
| Start   | `scripts/study-start.sh [minutes]`       |
| End     | `scripts/study-end.sh --set-checkpoint`  |
| Sandbox | `N/A (실험 스크립트 작성 전)`      |

<!-- 초기화 시 Sandbox 줄을 채운다 (예: `uv run python sandbox/<file>.py`). -->

## Skills

<!-- 절차의 세부는 스킬에 위임한다. 계정에 없는 스킬은 건너뛴다. Codex를 쓰면 `.codex/skills/`에 같은 사본을 둔다. -->

메인 튜터는 학습 스킬(problem-framing·learning-coach·concept-tutor·self-exam·debug-to-concept)을 직접 적용한다. 독립 채점은 study-grader가 맡고, 교재·수학 근거 역할(cs-book·math-analyzer)은 필요할 때만 메인이 호출한다. paper-analysis·research-claim-check·research-survey·blog-coauthor는 자료 탐색·사후 정리에 쓴다. 역할별 메모리는 위 Role Memory 절의 agent-memory-protocol을 따른다.

| 상황 | 스킬 (있으면) |
|---|---|
| 목표를 "할 수 있다" 문장과 증명 방법으로 바꿀 때 | `problem-framing` |
| 학습 조율 프레임 — 당위성(기존 방식 → 한계 → 새 방식)·L0→L2 점진 심화·개념 연결(`~/study/concept-links.md`)·개념 서술 초안·이해 확인 | `learning-coach` (이 워크스페이스의 Rules·Session Procedure와 충돌하면 이 파일이 우선) |
| 개념 설명·질문 답변 — 한계→직관→정식화→경계→연결 5층(`notes/`에 기록), 핵심 유도만 힌트 사다리. 확인 질문은 학습자가 요청할 때만 | `concept-tutor` |
| 학습자가 "내가 이해한 게 맞아?"라고 물을 때 | `learning-coach`의 이해 확인 — 한 번 검토(정확한 부분 → 어긋난 부분과 이유 → 교정된 이해)하고 끝낸다. 재질문하지 않으며 튜터가 먼저 요구하지 않는다. 어긋남은 `MISCONCEPTIONS.md` 후보와 다음 exercise 소재로 |
| Phase·목표를 마친 뒤 복습용 블로그 글 → `blog/`에 초안 | `blog-coauthor` (이월 스토리의 시리즈는 `study-series`) |
| 계획된 단일 exercise 출제 | 메인 튜터가 concept의 Verification Criteria에서 Rubric을 파생해 문제와 함께 `exercises/`에 먼저 기록한다(Rule 9). 설명 뒤 자동 미니 체크는 없다 |
| 학습자가 요청한 묶음 퀴즈 | `self-exam` — 퀴즈 자체와 그 자체 채점은 concept state의 근거가 아니다 |
| exercise 채점 — Rubric과 `전사 확인: OK`가 갖춰진 뒤 | `study-grader` 에이전트 (튜터와 다른 컨텍스트에서 Rubric·Attempt만으로 판정. 호출 프롬프트에 설명·기대 정답을 넣지 않는다. 사용할 수 없으면 `pending`으로 인계한다. 튜터의 직접 평가는 학습 피드백으로 줄 수 있지만 `exercises/`의 채점·상태 승격 근거로 기록하지 않는다) |
| 교재 근거·수학 검증이 필요할 때 | 메인 튜터가 `cs-qa` 경유 `cs-book` 또는 `math-analyzer`를 호출한다. 받은 결과의 원출처를 확인한 뒤 `evidence/`와 concept Claims에 근거 라벨·위치를 기록한다 |
| 오개념을 원인 → 잘못된 가정 → 개념 갭으로 좁힐 때 | `debug-to-concept` |
| 논문·자료를 evidence로 정리할 때 | `paper-analysis`, `research-claim-check` |
| 분야 지도·자료 탐색 | `research-survey` |

## Session Procedure

- **시작**: `scripts/study-start.sh [분]`을 실행하고 출력의 next steps를 따른다 — Resume 판단 → 학습자 변경·INBOX 반영 → pending exercise와 HANDOFF의 대기 이유·다음 행동 확인 → 복습 만기 → unit 선택(PLAN의 Units·Acceptance Criteria 확인) → CURRENT의 Status=IN_PROGRESS·Progress 작성과 HANDOFF 초안 → 진행.
- **확인**: 이해 확인·확인 질문은 학습자가 요청할 때만 한다 — 종료 조건이 아니다. unit에 계획된 exercise는 그대로 진행한다.
- **종료**: exercise 기록 정리(채점 가능한 시도는 result 확정, 미수신·전사 확인 대기 등으로 채점할 수 없는 시도는 pending으로 두고 HANDOFF에 인계) → concept의 state·review_due 갱신 → 작업 커밋과 PLAN의 unit SHA 갱신 → CURRENT(Status≠IN_PROGRESS)·HANDOFF·LOG(planned·actual) 갱신 → 필요 시 DR, Phase 완료 시 `RESULT.md`·`ROADMAP.md`·`phase/NN` 태그 → `scripts/study-end.sh --set-checkpoint` → close commit.

## Commit Format

- `<type>(<scope>): <summary>` — type: learn(concept·evidence), exercise, curriculum, docs, chore, wip. scope는 concept slug 또는 phase. 본문에 무엇을·왜. WIP는 미완료 사항.
- trailer: `git commit --trailer "Agent: claude-code" --trailer "Unit: 02/U3"` — Agent 이름은 소문자 kebab-case, unit 밖 작업은 `02/-`.
- unit 완료 커밋의 SHA를 PLAN에 적는다: `- [x] U3. ... (commit abc1234)`. 특정 unit 조회: `git log --grep='Unit: 02/U3'`.
- close commit: `docs(ai): close session — <요약>` (`.ai/`·`curriculum/`만 포함).

## Repository boundary

Before project writes or commits, run `python3 scripts/check-workspace.py`. The default expected Git root is this project directory. For an intentionally nested workspace, explicitly set `AI_EXPECTED_GIT_ROOT` to the agreed containing repository; never infer consent from Git's upward search. A new project must be initialized independently before its first commit. Hooks are supplementary checks and can be bypassed; always validate the staged path list before committing.

완료 후 독립 검증은 `bash scripts/study-end.sh --post-close`를 사용한다. 기본 검사는 close commit 전용이다. checkpoint는 마지막 작업 커밋이며, 완료 검사는 이후 커밋의 실제 변경 경로와 깨끗한 작업 상태를 검사한다. 완료 검사에서 checkpoint를 자동 갱신하지 않는다.

채점 전에는 실제 전사 확인 후 `check-exercise.py prepare`, 채점 후에는 `check-exercise.py check`를 실행한다. 도구는 사용자 확인을 대신하지 않는다. `.ai/grading/` snapshot은 exercise와 함께 작업 커밋에 포함한다.

## Claude hook checks

`.claude/settings.json` calls repository-owned read-only checkers at SessionStart and Stop. Stop checks only explicit DONE/REVIEW/BLOCKED states; ordinary working turns are not session closure. Dirty bookkeeping uses pre-close checks; clean Git history uses post-close checks. A repeated stop skips automatic retry to avoid a loop; failures still require resolution. Hooks never confirm learner input, prepare grading snapshots, update checkpoints, commit, or execute experiments. Codex must call the same checkers explicitly; this configuration is Claude-specific.
SubagentStop for study-grader validates all exercise records, including previously graded records. Legacy grades without snapshots require review; never fabricate a retrospective snapshot.
