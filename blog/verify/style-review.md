# 문체 편집 기록

- 원본 역할: `~/.agents/agents/blog-stylist.md`
- 대상: [초안](../drafts/rag-sequence-token-marginalization.md)
- 윤문 전 대조본: [pre-humanize](../drafts/rag-sequence-token-marginalization.pre-humanize.md)
- 기준 글: `~/projects/portfolio/src/content/notes/ko/typescript/ts-generics.md`
- 백업: [pre-style](../drafts/rag-sequence-token-marginalization.md.pre-style.md)

## 바꾼 절

- `## 2. Sequence: 문서별 전체 출력 확률을 더한다`: 정의 어미와 목록 예고 문장 2곳.
- `## 6. 확률을 정의하는 것과 답변을 찾는 것`: 앞 내용을 가리키는 연결과 주어 1곳.

## 대표 변경

1. “**주변화(marginalization)**는 직접 관측하거나 확정하지 않은 문서 $z$를 합으로 없애는 계산이다.” → “직접 관측하거나 확정하지 않은 문서 $z$를 합으로 없애는 계산을 **주변화(marginalization)**라고 한다.”
2. “계산 순서를 적으면 다음과 같다.” → “계산 순서를 정리하면 아래와 같다.”
3. “앞에서는 후보 $y$를 알고 그 확률을 계산했다.” → “앞서 우리는 후보 $y$를 알고 그 확률을 계산했다.”

## 보존 검사

- 작업 경계 검사 통과: `python3 ~/.agents/scripts/check-workspace.py --workspace ~/study/RAG/blog --git-root ~/study/RAG`
- pre-humanize, pre-style, 편집 후 초안을 Python 정규식 추출로 대조했다. frontmatter 1개, 인라인 코드 8개, 수식 47개, 표 행 41개, 링크·이미지 2개, 주석 20개, 원문 인용 표기 11개, 숫자 토큰 130개, 따옴표 인용 10개, 제목 16개가 모두 동일했다. fenced code와 details 태그는 세 파일 모두 없었다.
- `ai:draft` 시작·끝 마킹은 내용과 줄 위치까지 동일했다.
- `diff -u`로 pre-style과 편집 후 초안의 변경 3줄을 확인했다. 주장과 논리 순서, 고유명사, 참고 문헌을 보존했다. 문체 수정은 모두 draft 마킹 안에 있다.
- 윤문 중 깨진 보존 대상 및 복원한 곳: 없음.
- 자체 점검 후 되돌린 곳: 없음.

## 유지한 표현과 한계

- 도입의 개인 생각과 문답 경험 진술은 호출자의 별도 사실 검토 대상이므로 유지했다.
- 확률·학습·decoding의 구분을 설명하는 부정형과 반복은 내용상 필요한 경계 설명으로 유지했다.
- 기존 본문은 평서형, 질문, 번호 절, 영어 기술 용어, 굵은 강조, 짧은 문단, 정리·연결 구성이 이미 프로필에 맞아 추가 수정하지 않았다.
- 논문의 사실 관계와 수학적 타당성은 이번 문체 편집의 검증 범위에 포함하지 않았다.
