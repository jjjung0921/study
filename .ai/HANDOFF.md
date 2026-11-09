# Handoff

- From: codex — U5 피드백 보완 및 종료
- Date: 2026-11-09
- Phase / Unit: 02-rag-foundations / U6 진행 중

## Goal

RAG의 검색과 생성 경계를 이해하고 AICC 다중 턴 평가 실험 설계로 이어간다.

## Work Completed

- Phase 01 완료. 작업 커밋 `205b0b7`, close commit `5260057`.
- Phase 02 U1: survey Section II 문답과 네 축 요약 완료. `notes/rag-overview.md`, `notes/rag-new-modules.md`, `notes/rag-vs-finetuning.md`.
- U2: DPR Introduction과 Sections 3.1-3.2 문답, concept 및 evidence 초안 작성. `notes/sparse-dense-retrieval.md`.
- U3: 사용자 전사 확인 뒤 prepare, Claude study-grader 채점과 별도 Codex 리뷰 완료. R1 ✗, R2 ✓, R3 ✗, partial에 일치. check 통과, ledger 오류 없음.

## Work In Progress

- 학습자가 "쉬었다가 핮"이라고 요청해 일시 중단했다. U6 두 memory와 DPR+BART 구성을 소개하고 Introduction 및 Figure 1을 읽을 범위로 안내한 지점이다. 학습자 읽기는 아직 미확인이며 exercise나 state 변경은 없다.
- 사용자가 다음 진행을 요청해 U6를 시작했다. 원 RAG v4의 Introduction, Figure 1, Sections 2.1-2.4를 확인하고 두 memory와 BART generator를 안내한다. 첫 읽기는 Introduction과 Figure 1이며, 다음은 Sequence/Token의 합산 단위 차이다. 학습자 원문 읽기와 초안 검토는 아직 미확인이다.
- U5 수정 답안 확인 뒤 독립 채점 및 별도 리뷰에서 R1 ✗, R2 ✓, R3 ✗, R4 ✓, partial에 일치했다. 사용자가 보완과 종료를 요청해 DR-0011로 완료 조건을 변경하고 학습 절차는 완료 처리했다. 최초 Attempt와 partial은 유지하며 concept state 변경 없음.
- U5의 주된 부족은 passage 근거 누락 및 B에서 근거 확보 성공을 명시하지 않은 점이다. R3의 판단 유보를 검색 실패 주장으로 확대하지 않는다. 개념 오해라고 확정하지 말고 피드백에서 A의 P1 누락과 B의 P1 포함을 연결해 설명한다.
- U4 후속 질문에서 실제 reader 모델 안내 누락을 보완했다. DPR Section 6.1의 BERT-base uncased 추출형 reader와 passage 선택 및 span 예측을 원문 확인 후 설명했다. 생성형 상담 예시는 DPR 실험 설정과 구분하며 `notes/retriever-reader-pipeline.md`에 튜터 누락으로 기록했다.
- U4의 단계 경계 및 실패 위치를 concept와 `notes/retriever-reader-pipeline.md` 초안에 기록하고 DPR Introduction 및 Section 2 읽기 범위를 안내했다. 학습자가 "알겠어. 이해했어"라고 말하고 진행 여부를 물어, 추가 이해 확인 없이 초안 작성 완료 조건으로 U4를 마무리했다. 이 말만으로 초안 전체 검토 완료나 concept state 승격을 기록하지 않는다. 다음은 U5의 계획된 error-spot exercise다.
- `exercises/2026-11-09-sparse-dense-retrieval-condition.md`: partial 유지. 학습자가 종료 기준 변경을 요청해 DR-0010을 작성했고 답안 제출, 독립 채점 및 리뷰, 피드백 보완과 학습자 검토를 마친 U3는 완료 처리했다. 원래 답안을 소급 수정하거나 재채점하지 않는다.
- DPR의 질문-passage 벡터 관련성 설명과 명시적인 baseline 선택 근거가 후속 학습 대상이다. concept 초안 검토는 미확인이므로 state는 unseen 유지한다.
- 학습자 요청으로 피드백 후 보완 정리를 `notes/sparse-dense-retrieval.md`에 반영했다. 동일한 Naive RAG에서 BM25 baseline과 DPR을 비교하는 예시다. 원래 답안과 partial은 유지하며, concept 전체 초안 검토로 확대 해석하지 않는다.
- 학습 문서와 채점 근거는 `2f04d9f`에 저장했다. GitHub push는 사용자 승인 대기다. 기존 시간 추적 코드와 설정 변경은 별도 작업이며 보존한다. 클라우드 재개 절차: `notes/cloud-study.md`.

## Verification

- Claude 최초 인증 실패 뒤 사용자 재로그인 통보를 받아 성공 재호출했다. runtime: `.ai/grading/runs/2026-11-09-sparse-dense-retrieval-condition-run.md`.
- 별도 리뷰: `exercises/cross/2026-11-09-sparse-dense-retrieval-condition-grading-codex.md`. 리뷰 도중 이전 인증 실패 기록을 읽은 데 따른 출처 지적은 실제 성공 실행 기록 연결과 check로 해소했다. 판정 이견 없음.
- ledger의 경고 1건은 과거 진단 `01-u2-prior-knowledge.md`의 legacy 실행 증거 부재이며 이번 채점 오류가 아니다.

## Decisions and Boundaries

- 기본 세션 120분, 말과 손글씨 수식 입력. DR-0007과 DR-0009의 경로를 유지한다.
- 이전 진단의 오개념 두 후보는 철회된 상태를 유지한다. 이번 DPR 단어 유사성 서술은 별도의 미확인 후보이며, baseline 선택 누락을 오개념으로 단정하지 않는다.
- `c9c2eeb`의 기존 블로그 기록과 학습자 변경을 보존한다.

## Open Questions

- AICC의 우선 도메인은 Phase 04 전에 정한다. 목요일과 토요일의 시작 시각은 확인 전 운영 가정이다.

## Exact Next Action

휴식 후 U6 원 RAG Introduction과 Figure 1부터 이어간다. 이후 Section 2.1의 Sequence/Token 차이를 다룬다.
