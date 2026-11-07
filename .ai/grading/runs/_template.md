# 채점 실행 기록

<!-- 실제 CLI 또는 서브에이전트 호출을 실행한 쪽이 런타임 출력에서 채운다. 튜터의 기억이나 채점자 자기신고로 식별자를 만들지 않는다. exercise의 Grader Run 절에서 이 파일을 링크한다(DR-0008). -->

- Exercise: `exercises/{exercise-file}.md`
- Input snapshot: `.ai/grading/{snapshot-hash}.json`
- Snapshot SHA-256: `{실제 snapshot 파일의 해시}`
- Tutor: `{튜터 역할과 엔진}`
- Grader: `{독립 채점 역할과 엔진}`
- Invocation: `{사용한 공식 CLI 또는 서브에이전트 호출 방식}`
- Runtime reference: `{런타임이 반환한 세션 ID 또는 호출 ID}`
- Completed: `{시간대가 포함된 완료 시각}`
- Exit status: `{성공 또는 실패}`
- Raw output: `[원출력]({exercise-file}-output.txt)`
- Result: `{exercise의 result}`

실행 기록은 호출 경로와 출력을 추적하는 근거다. 사람의 전사 확인이나 답의 수학적 정확성을 증명하지 않는다.
