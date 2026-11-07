# Exercises

exercise 기록은 이해 상태의 근거다 (Rule 8, DR-0002). 파일 하나 = 시도 하나. 유형별 디렉터리를 두지 않고 frontmatter로 거른다.

- 파일명: `YYYY-MM-DD-<concept>-<type>.md`. 같은 날 같은 개념·유형이 둘이면 `-2`를 붙인다. 양식은 `_template.md`.
- 문제와 Rubric을 먼저 쓰고, 답을 받아 전사·확인한 뒤, 항목별로 판정한다. `result`가 `pending`인 파일은 다음 세션에 이어서 채점한다(시차 채점).
- 손글씨 사진은 `_inbox/YYYY-MM-DD-<concept>.jpg`에 넣고 `.ai/INBOX.md`에 파일명을 적는다. `_inbox/`는 gitignore이며, 전사만 커밋한다 (Rule 10).
- 상태 근거로 쓰는 기록은 계획된 Rubric-first exercise다. 학습자가 요청한 `self-exam` 묶음 퀴즈와 `min_session`의 회상 질문은 이 폴더에 넣지 않는다. 진단(`purpose: diagnostic`) 결과는 개념 상태 승격에 사용하지 않는다(DR-0008).

## Types

<!-- cost는 학습자의 입력 비용. 일상 검증(practice·review)은 low, verified 승격·capstone은 high 1회 이상 (DR-0003). C1–C4는 concept의 Verification Criteria 유형. -->

| type       | cost | input        | 무엇을 보는가                                        | 판정 재량 |
|------------|------|--------------|------------------------------------------------------|-----------|
| recall     | low  | text, speech | 정의·성립 조건을 말할 수 있는가 (C1)                 | 중        |
| condition  | low  | choice, text | 주어진 상황에서 적용 가능 여부와 이유 (C2)           | 중        |
| error-spot | low  | text         | 튜터가 쓴 유도·코드에서 틀린 단계 지목               | 없음      |
| fill-step  | low  | text, photo  | 빈 단계 채우기                                       | 낮음      |
| choice     | low  | choice       | 다음 단계·옳은 식 고르기                             | 없음      |
| numeric    | low  | text, code   | 구체적 예에서 값 계산 (C3)                           | 없음      |
| skeleton   | low  | photo, text  | 유도의 뼈대(어떤 정리를 어디에)만 — 계산은 튜터·sympy | 중        |
| derivation | high | photo, code  | 전체 유도                                            | 중        |
| proof      | high | photo        | 증명                                                 | 중        |
| coding     | high | code         | sandbox 구현 + 테스트·출력                           | 없음      |
| transfer   | high | any          | 처음 보는 조건·문제에 적용 (C4) — verified에 필수    | 중        |

## Frontmatter

| key       | 값                                                   |
|-----------|------------------------------------------------------|
| date      | YYYY-MM-DD                                           |
| concept   | concept slug                                         |
| type      | 위 표                                                |
| purpose   | diagnostic · practice · verify · review              |
| input     | text · photo · code · speech · choice                |
| cost      | low · high                                           |
| est / actual | 분                                                |
| grader    | 채점한 Agent 이름 (커밋 trailer와 같은 값)           |
| review_order | `purpose: review` 완료 순서. concept별 1부터 증가하며 그 밖에는 비움 |
| result    | pending · pass · partial · fail                      |

## Grading Scale

- **pass** — Rubric의 필수 항목 전부 ✓.
- **partial** — 필수 항목 일부 ✗이지만 핵심 구조는 맞음. 미통과이며 practiced의 근거만 된다.
- **fail** — 핵심 구조가 틀렸거나 답이 없음.
- 두 등급 사이면 낮은 쪽. 판정마다 Attempt 인용. 총평·칭찬 없음 (Rule 9).

## After Grading

1. concept 파일: 승격에 쓴 pass·partial은 `verified_by`에 추가한다. review는 `review_order` 순서대로 맨 아래 `Review History`에 exercise 상대 링크와 Rubric·Attempt 근거, 상태 영향을 기록한다. state 승격 조건(Rule 8)을 확인한 뒤 verified면 `verified_on`·`review_due`, 복습이면 `review_stage`·`last_reviewed`·`review_due`를 갱신한다(Rule 14, DR-0008). `check-exercise.py ledger`가 전체 채점 이력과 복습 순서를 검사한다.
2. 오개념이 보이면 `concepts/MISCONCEPTIONS.md`에 한 줄 + concept의 Misconceptions
3. PLAN의 unit이 완료되면 `[x]`와 근거 파일명
4. `.ai/LOG.md`의 Exercises·State changes 줄

## Executable grading boundary

Before invoking the independent grader, the tutor runs `python3 scripts/check-exercise.py prepare exercises/{attempt}.md` after obtaining the learner's actual transcript confirmation. This saves hashes of Problem/Rubric/Attempt under `.ai/grading/`; it never creates the confirmation itself. Include the snapshot with the exercise in the content commit. A changed answer or rubric requires a new attempt file, not overwriting the snapshot.

After grading, run `python3 scripts/check-exercise.py check exercises/{attempt}.md`. `pending` remains valid without a response. Graded results require the snapshot, a grader, one row per numbered Rubric item, ✓/✗, an exact double-quoted Attempt excerpt, matching Result, Next, and the Grader Run link. `study-end.sh` reuses this validator and runs `ledger`. The checks verify record structure and provenance links, not mathematical correctness or authentic human confirmation. A historical diagnostic without a snapshot can be marked `legacy_unverified: true`; it remains history only and never becomes state evidence. Never fabricate a retrospective snapshot or reclassify it as verified automatically.

채점 완료 파일의 `Grader Run` 절은 `.ai/grading/runs/`의 실행 기록을 상대 링크로 가리킨다. 그 기록에는 exercise 경로, `prepare` snapshot 해시, 튜터·채점자 역할, 실제 CLI 또는 서브에이전트 호출과 런타임 식별자, 완료 결과와 원출력 위치를 담는다. `check`가 링크의 존재와 snapshot·결과 일치를 확인한다. 기존 기록에 실행 증거를 소급해서 만들지 않는다(DR-0008).
