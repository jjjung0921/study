# Blog — 복습용 포트폴리오 글 작업 공간

학습 완료 후 `blog-coauthor` 스킬이 쓰는 작업 공간이다. 완성된 글은 포트폴리오 저장소(`src/content/notes/ko/<field>/<slug>.md`)로 옮기고, 이 폴더에는 그 전까지의 초안·검증 코드만 둔다 — source of truth가 아니다(`concepts/`·`exercises/`가 근거).

- `drafts/<slug>.md` — 절마다 `<!-- ai:draft -->` … `<!-- /ai:draft -->`로 감싼 초안. 윤문 단계의 백업(`<slug>.pre-humanize.md`)도 여기에 둔다.
- `verify/` — 글의 코드 블록이 실제로 동작함을 확인하는 스크립트. 글에 싣는 실행 결과는 이 폴더에서 돌린 것만 쓴다(blog-coauthor 금지 목록 — "실행하지 않은 코드·결과"). 컴파일·빌드 산출물은 커밋하지 않는다 — 도구에 맞게 `.gitignore`에 추가한다.
- 핸드오프 체크리스트(마킹 잔존 여부·TODO·frontmatter 규격)는 `blog-coauthor` 스킬이 소유한다. 포트폴리오로 옮긴 뒤에도 초안·검증 코드는 지우지 않는다(다음 개정의 재료).
