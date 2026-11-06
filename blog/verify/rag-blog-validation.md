# RAG 학습 → 블로그 작성 검증

날짜: 2026-10-30. 대상: [RAG의 합과 곱은 무엇을 계산하는가](../drafts/rag-sequence-token-marginalization.md).

후속 개정: 사용자가 지정한 포스트 3편의 문체 분석·규칙화·재적용은 맨 아래 「세 포스트 기반 문체 재적용」에 기록했다. 아래 최초 작성의 검사 해시는 재적용 전 백업에 해당한다.

추가 표기 수정: 사용자의 특수 기호 금지 요청에 따라 현재 초안의 절 표시는 `2.1절` 형식으로 바꾸고 문장용 화살표와 가운뎃점을 일반 문장으로 풀었다. 따옴표도 일반 표기로 통일했다. 수정 전 파일은 `drafts/rag-sequence-token-marginalization.pre-plain-notation.md`에 보존했다. 아래 문체 검증 해시는 이 표기 수정 직전 버전이다. 수식 47개와 AI 초안 표시 10쌍은 동일함을 확인했다. 표기와 summary가 의도적으로 바뀌었으므로 과거 전체 문자열 동일성 검사를 현재 파일에 그대로 적용하지 않는다.

## 실행 범위

사용자가 고른 수식 중심 구성으로 QA와 원문에서 초안을 작성했다. 원문 대조 → 한국어 윤문 → 기존 글 문체 편집 → 보존·규격 점검을 완료했다. 사용자 검토와 게시 단계는 별개다. QA에서 확인된 질문은 글의 흐름에 사용하되 숙련도·재현 성공을 만들어 쓰지 않았다.

재료와 주장 대응은 [source map](rag-blog-source-map.md), 독립 원문 대조는 [fact review](fact-review.md)에 있다.

## 실행 주체·모델

| 작업 | 실행 주체 | 호출에서 선택한 모델·추론 수준 |
|---|---|---|
| 원문·QA 종합, 초안 작성, 최종 내용 수정 | 이 대화의 Codex 메인 | 현재 모델 유지. 세부 배포 ID를 별도로 확인한 것으로 기록하지 않음 |
| humanize 진단 | 별도 Codex 컨텍스트 `rag_blog_diagnosis` | `gpt-6.1-sol`, medium |
| humanize 윤문 | 별도 Codex 컨텍스트 `rag_blog_humanize` | `gpt-6.1-sol`, high |
| humanize finalize·의미 보존 및 필요시 국소 수정 | 별도 Codex 컨텍스트 `rag_blog_finalize` | `gpt-6.1-sol`, medium |
| 원문·QA 사실 검증 | 읽기 전용 Codex 검증자 `rag_blog_fact_check` | `gpt-6-luna`, high |
| 문체 편집 | Codex `blog-stylist`, `rag_blog_style` | `gpt-6.1-sol`, medium |

표의 모델은 도구 호출에서 선택하여 수락된 값이다. 내부 서비스의 배포 라우팅을 별도로 측정했다는 뜻은 아니다. 작성 작업을 경량 검증 모델로 보내지 않았다.

## 설정 반영

- `~/.agents/skills/blog-coauthor/SKILL.md`: Codex 작성·윤문·검증 역할, 가용 모델 선택, 기존 글 검색, QA 발화 근거, 로컬 초안 위임·게시 경계, 윤문 보존 검사 및 백업 보존.
- `~/.agents/agents/blog-stylist.md`: Codex 실행 역할 명시, Claude 전용 `model: sonnet` 제거. 고정 모델을 만들지 않고 호출 시 적합한 모델 선택.
- 원본으로부터 `~/.agents/skills/blog-stylist/SKILL.md`와 `~/.codex/agents/blog-stylist.toml` 동기화. 원본 본문과 파생물 일치 및 TOML 파싱 확인.
- `~/.agents/rules/model-routing.md`: 학습 블로그 작성·문체 편집은 Codex. `sync-rules.sh`로 도구별 미러 반영.
- 사용자가 제공한 [im-not-ai](https://github.com/epoko77-ai/im-not-ai)의 Codex용 `humanize-korean` 설치. 고정 커밋 `b37e0206d31fffd9149bf57168d4d62eb2086bee`, 공식 `install.sh --codex-only --copy` 사용. LICENSE·설치 출처 보관. 런타임 스크립트와 룰북은 수정하지 않았다.
- 초기 자동 승인 검토는 사용량 제한으로 실행 전에 실패했다. 2026-10-30 재개 후 정상 승인·동기화·설치를 완료했다.

## 이번 실행에서 발견한 허점

### 1. QA를 내적 믿음으로 확대하는 문장

첫 초안의 “처음에는 … 생각했다”는 진술을 독립 검증자가 지적했다. QA는 문서별 벡터·행렬에 대한 질문을 뒷받침하지만, 내적 믿음의 서술까지 직접 보장하지 않는다. 최종본은 “RAG 논문의 §2.1을 읽으며 합과 곱의 계산 대상을 여러 번 질문했다.”로 바꿨다. 질문·가설·확인된 이해를 나누는 규칙이 실제 검토에서 작동한 사례다.

### 2. 윤문 도구의 각주 오탐

`humanize-korean`은 standard 경로로 진단·윤문을 실행했다. 문자 변경률은 **0.74%**, sentence touch는 **4.9%**, 서법 소실은 **0건**이다. `footnote_anchor` 경고 3건 때문에 finalize를 추가했다.

벡터 `(0.3,0.5,0.2)`, `(0.05,0.05,0.9)`, `(0.4,0.4,0.2)`의 끝부분을 각주 `2)`, `9)`, `2)`로 해석했다. 원문을 자기 자신과 비교하는 대조에서도 같은 3건이 나왔다. 직접 대조와 보존 검사에서 해당 표·수식은 동일했다. **원시 게이트 결과는 WARN으로 유지**하고, 이 3건은 이번 윤문으로 발생한 각주 이동의 근거가 아니라고 판정했다. 외부 도구의 오탐 자체를 고친 것은 아니다.

- [원시 게이트](humanize-gates-initial.txt)
- [동일입력 대조](humanize-gates-identity.txt)
- [finalize 판정](../_workspace/2026-10-30-001-8ce6/09_finalize.json)

윤문 finalize는 본문 수정 0건으로 accept했다. 등급은 **잠정 C**, 자체검증 **5/6**이며 S1 잔존 0건을 확정하지 않았다. `blog`용 기준값이 없어 `essay` 기준으로 대체한 한계도 있다. 이 값들은 블로그 내용의 정확성 점수나 인간 작성 여부 판정이 아니다. 추가 heavy 윤문은 수행하지 않았다.

### 3. 경량 검증자의 출처 줄 번호 오류

검증자가 대화 인용에 잘못된 JSON 줄 번호를 붙였다. 메인이 실제 파일과 대조해 발견했고, 검증자가 안정적인 E ID로 정정했다. 판정뿐 아니라 출처 위치 자체도 확인해야 한다. 교정 이력은 [fact review](fact-review.md) 끝에 남겼다.

### 4. 기존 스킬의 초안 삭제 규칙 충돌

`blog-coauthor`의 “이동 후 초안 삭제”가 RAG blog README의 보존 규칙과 충돌했다. 초안·윤문 전 백업·검증 기록을 다음 개정 자료로 보존하도록 공통 규칙을 고쳤다. 이번 실행에서 파일을 삭제하지 않았다.

## 검증 한계

원문과 QA에 근거한 글 작성 흐름 한 건의 검증이다. 모델 성능 비교·학습자의 이해도 검사·공식 구현 재현·latency 실험·포트폴리오 빌드·브라우저 시각 검증은 수행하지 않았다. 최종 사용자 검토 전이므로 `ai:draft` 표시를 유지한다. 커밋·푸시·게시 없음.

## 최종 파일 검사

검토용 초안 작성과 검사 완료. 사용자 검토·게시 완료를 뜻하지 않는다.

| 검사 | 결과·범위 |
|---|---|
| 수식 렌더링 | 설치된 KaTeX로 인라인·블록 수식 47개 렌더링 통과(`throwOnError`, strict error). |
| 포트폴리오 규격 | 실제 `src/content/config.ts`의 `noteSchema`를 설치된 Zod로 적용해 통과. 필수 frontmatter 충족, 한국어 글 폴더 내 동일 `translationKey` 없음. |
| 윤문 전후 보존 | frontmatter·수식·표·수치·링크·출처 라벨·직접 인용·draft 마킹 동일. |
| AI 작성 표시 | 시작·끝이 짝을 이룬 `ai:draft` 블록 10개, 본문 전체 포함. |
| 설명용 계산 | Sequence 0.456, Token 0.372 및 문서별 확률의 가중합 확인. 논문 실험값과 구분. |
| 문체 편집 | 정의 어미·목록 예고·연결 표현 3곳 수정. [문체 기록](style-review.md)에 전후 문장과 범위 기록. |
| 내용 교정 | 메인이 QA에 근거 없는 내적 믿음 진술을 질문 기록으로 교정하고, 토큰 위치 기호 i의 정의를 추가. 문체 편집자의 변경과 구분. |
| 정적 표기 검사 | 미정의 기호 경고 8건을 검토했다. 한국어 설명·표 안의 정의를 인식하지 못하는 한계를 확인했고 i의 정의를 명시했다. lint 경고 0건을 주장하지 않는다. |
| 윤문 게이트 | 각주 오탐 3건의 원시 WARN 유지. 동일입력 대조·직접 대조를 근거로 해석했으며 외부 도구 수정은 하지 않음. |

기계 검사 결과: [보존·마킹·메타데이터](final-checks.json), [KaTeX·실제 스키마](render-schema-checks.json).

백업: [윤문 전](../drafts/rag-sequence-token-marginalization.pre-humanize.md), [문체 편집 전](../drafts/rag-sequence-token-marginalization.md.pre-style.md). 윤문 자체 보고는 실행 기록에 보관하고 블로그 본문에서는 분리했다.

최초 검사를 마친 초안의 SHA-256: `b9362a0e447501eabbf75f190b9d9079c1846bab10c658e076057035b123bfe5`.

## 세 포스트 기반 문체 재적용

사용자가 `ts-type-check`, `performative-prediction`, `ts-generics` 3편을 지정했다. 초기 탐색에서 본 다른 글은 최종 문체 규칙의 근거에서 제외했다. 기존 글은 수정하지 않았다.

### 분석과 규칙

- 규칙 원본: `~/.agents/skills/blog-coauthor/references/portfolio-writing-style.md`. 세 글의 개별 분석, 실제 문장·행 번호를 근거로 한 S1–S8, 적용 예외와 한계를 담았다.
- `ts-type-check`: 질문을 검사 단계로 나누고 코드·결과·해석을 잇는다.
- `performative-prediction`: 기존 설명의 한계에서 다음 개념으로 넘어가고, 수식 뒤에 변수 역할과 조건을 푼다.
- `ts-generics`: 작은 예시의 차이에서 정의와 일반 원리로 나아간다.
- 근거: [선정 세 편의 발췌](style-corpus-20261030/selected-excerpts.md), [원본 해시·범위](style-corpus-20261030/selected-manifest.json). TypeScript 두 편은 같은 시리즈이며, 세 편을 저자의 모든 글로 일반화하지 않았다.

im-not-ai는 복사본의 지표 산출과 룰북을 이용한 읽기 전용 진단에 사용했다. 원문 포스트를 다시 쓰는 standard/heavy 파이프라인이나 개인 모델 학습을 수행한 것은 아니다. 세 편 모두 `blog->essay` 기준값 대체 경고가 있었으므로 점수를 문체 유사도나 저작 판별로 사용하지 않았다. 식 예고·영어 기술 용어·개념을 구분하는 부정문 등을 일반 윤문 규칙으로 일괄 제거하지 않도록 사례별 예외를 적었다. upstream 스크립트·룰북 변경 없음.

규칙 작성과 판단은 Codex 메인, 독립 검증은 `portfolio_profile_check`(`gpt-6-luna`, high)가 맡았다. 검증에서 I-3 예외 근거 부족과 문서 단위 지표를 문장 위치로 표현한 오류를 찾아 수정했고 재검토에서 해소를 확인했다. [프로필 검증 기록](portfolio-profile-review.md).

### 초안 적용과 연결

Codex `blog-stylist`를 `gpt-6.1-sol`, high로 호출해 검증된 규칙을 적용했다. 0·2·3·4·6·7절에서 9개 편집 단위(문단 분리 3개 포함)를 바꿨다. 변경별 규칙·원문 근거와 전후 문장은 [적용 기록](style-review-three-post.md)에 있다. 메인은 이 기록의 P1 인용 위치 1곳을 39행에서 실제 41행으로 정정했다.

`blog-coauthor`와 원본 `blog-stylist`가 같은 프로필을 읽도록 연결했다. 오래된 6편 기반 고정 문체 목록을 교체하고, `우리` 사용·문단 길이·제목 형식을 강제하지 않도록 했다. 원본 에이전트 → 파생 스킬 → Codex native TOML 일치와 파싱을 확인했다. 이번 native 동기화에서는 `blog-stylist.toml`만 선택해 반영했다.

### 재적용 검증

- [재적용 전 백업](../drafts/rag-sequence-token-marginalization.pre-three-post-style.md) 보존. 이전 윤문·문체 백업도 유지했다.
- [보존 검사](style-three-post-checks.json): 수식 47개, 표 41행, 수치 130개, 직접 인용 10개, 출처 11개, 메타데이터·코드·링크·제목 동일. `ai:draft` 10쌍과 마킹 밖 문자열 동일. 기준 포스트 3편의 해시도 동일.
- 수식 문자열과 frontmatter가 이전 검사를 통과한 값과 같으므로 기존 KaTeX·실제 스키마 검사 근거가 유지된다. 사이트 전체 빌드·브라우저 검증은 추가하지 않았다.
- im-not-ai의 변경률 검사: **0.6%, exit 0**. [원시 결과](style-three-post-change-rate.txt). 변경률 검사만 수행한 결과이며 전체 윤문 게이트 PASS로 확대하지 않는다. 앞서 기록한 각주 오탐의 원시 WARN을 덮어쓰지 않았다.
- 최종 변경 문장의 독립 의미 검토: [검토 기록](style-three-post-semantic-review.md).

재적용 초안 SHA-256: `cd1fa5057ad6fe7738dece27f2b6458427fa4a9b6791b09433100a19e6cb5ca2`. 사용자 검토 전이며 `ai:draft` 유지. 커밋·푸시·게시 없음.
