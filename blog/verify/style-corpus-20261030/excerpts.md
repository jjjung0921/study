# 포트폴리오 문체 근거 발췌

현재 파일의 지정 범위만 문체 분석에 사용. 글의 기술 주장 정확성·단독 인간 저작 여부는 이 자료로 판정하지 않는다.


## ts-intro

원본: `~/projects/portfolio/src/content/notes/ko/typescript/ts-intro.md`


```text
22: # 문제
23: 
24: **14기 멋쟁이사자처럼 프론트엔드 멘토**를 진행하며 새롭게 TypeScript 세션을 추가하게 되었다. 해당 포스트는 아래 2가지 주제를 다룬다.
25: 1. 기존의 JavaScript에서는 어떤 문제가 발생할 수 있는가?
26: 2. TypeScript는 이 문제를 어떻게 해결했는지 간략하게 overview를 제공한다.
27: 
28: 2026/07/13인 현재 Javascript의 구체적인 포스트는 아직 작성하지 않았지만 추후 추가할 예정이기에 JS에 대해서는 알고 있다는 가정 하에 진행한다.
29: 
30: # 0. JS에는 무슨 문제가 있었는가?
31: 
32: > JS는 <strong>동적 타입 언어(Dynamically Typed Language)</strong>이다.
33: 
34: 큰 틀에서 JS의 동작 과정을 그려보면 아래와 같다.
35: 
36: ```
37: JavaScript Source Code
38: → Parse
39: → Scope / Binding Preparation
40: → Runtime Execution
41: → Expression Evaluation
42:    └─ actual value types에 따라
43:       property access / function call / operator / coercion 수행
44: → Result or Runtime Error
45: ```
46: 
47: 위 과정에서 **Binding은 특정 스코프에서 식별자와 그에 대응하는 변수·함수·매개변수의 관계를 구성**한다.
48: 
49: 이후 **Runtime Execution에서는 선언문, 할당문, 함수 호출 등이 실행되면서 binding이 초기화되거나 새로운 값으로 갱신**되며
50: 
51: **Expression Evalution에서는 실제 값을 대상으로 프로퍼티 접근, 함수 호출, 연산자 적용, 암묵적 타입 변환 등이 수행**된다. 해당 연산을 수행할 수 없으면 **예외가 발생**할 수 있다.
52: 
53: JavaScript에는 binding 이후, 실제 실행 전에 값의 사용 관계를 검사하는 정적 타입 검사 단계가 없다. 따라서 부적절한 값 사용은 표현식이 실제 런타임 값으로 평가될 때 드러날 수 있다.
54: 
55: 예를 들어, Number 타입의 원시값(primitive value)을 가지는 데이터에서 `toUpperCase` 같은 함수를 호출할 경우 해당 type에서는 호출할 수 없는 함수이기에 에러가 발생한다.
56: 
57: ```js
58: const a = 10;
59: a.toUpperCase() //TypeError: a.toUpperCase is not a function
60: ```
61: TypeScript는 가능한 런타임 값의 형태와 사용 관계를 **정적으로 모델링**하고 코드가 실행되기 전에 일부 오류 가능성을 진단하기 위해 등장했다.
62: 
63: # 1. TypeScript의 등장
64: 
65: TypeScript는 앞서 말했듯 런타임 값의 형태를 모델링해서 "Expression Evaluation"에서 발생할 수 있는 일부 문제를 미리 찾기 위해 등장한 언어이다.
66: 
67: 동작 과정은 아래와 같다.
68: ```
69: TypeScript Source Code
70: → Parse
71: → Bind
72: → Type Check
73: → Transform
74: → Emit
75: → JavaScript Source Code
76: ```
77: 
78: 위 과정에서 **Type Check**라는 정적 타입 검사 과정이 추가되어 실제 프로그램을 실행하지 않더라도 compile 과정에서 미리 일부 타입 관련 오류를 체크할 수 있다.
79: 
80: ```ts
81: a = 10;
82: a.toUpperCase() //Property 'toUpperCase' does not exist on type '10'.
83: ```
84: 
85: 일반적인 TypeScript 컴파일 과정에서는 타입 정보가 제거되고 **JavaScript 소스 코드가 출력**된다. 이후 생성된 JavaScript가 브라우저나 Node.js 등의 JavaScript 런타임에서 실행된다.
86: 
87: # 연결
88: 
```


## ts-type-check

원본: `~/projects/portfolio/src/content/notes/ko/typescript/ts-type-check.md`


```text
22: # 문제
23: 
24: 이전 글에서는 JavaScript에는 일반적으로 실행 전 정적 타입 검사 단계가 없으며 TypeScript가 다음과 같은 과정을 추가한다고 설명했다.
25: 
26: ```
27: TypeScript Source Code
28: → Parse
29: → Bind
30: → Type Check
31: → Transform
32: → Emit
33: → JavaScript Source Code
34: → Runtime Execution
35: ```
36: 
37: 하지만 여기에는 다음 질문이 남는다.
38: 
39: > TypeScript의 Type Check는 JavaScript 프로그램의 무엇을 검사하는가?
40: 
41: TS를 컴파일한 JS 파일에는 우리가 TS에서 선언한 type이 남지 않는 것을 알 수 있다.
42: 
43: 다시 말해 TS는 JS 런타임에 새로운 타입 객체를 추가하는 방식으로 동작하지 않는다. 대신, 프로그램이 실행될 때 각 표현식이 가질 수 있는 값을 정적으로 근사하고 그 값에 수행하려는 연산이 안전한지를 검사한다.
44: 
45: 위 과정을 이해하기 위해 총 6개의 단계로 나눠서 학습한다.
46: 
47: ```
48: Type erasure
49: → Structural typing
50: → Types as sets
51: → Type inference
52: → Control-flow analysis
53: → Soundness boundaries
54: ```
55: 
56: 위 6개의 단계를 아래 6개의 질문에 대한 답이다.
57: 
58: 1. 타입은 런타임에 남는가?
59: 2. 두 타입의 호환성은 무엇으로 결정되는가?
60: 3. 타입은 어떤 의미를 가지는가?
61: 4. 타입을 직접 쓰지 않으면 compiler는 어떻게 알아내는가?
62: 5. 조건문을 통과하면서 타입은 어떻게 달라지는가?
63: 6. TypeScript의 검사는 어디까지 신뢰할 수 있는가?
64: 
65: # 0. Overview
66: TypeScript에서 type의 탄생은 아래와 같은 과정을 거친다.
67: ```
68: JavaScript runtime values
69:         │
70:         │ static abstraction
71:         ▼
72: TypeScript types
73:         │
74:         │ type checking
75:         ▼
76: Potentially invalid operations
77: ```
78: 
79: TS의 type은 js runtime의 value 혹은 type 그 자체가 아니다.
80: 
81: 그보다는 특정 표현식이 런타임에 가질 가능성이 있는 값들을 **정적으로 추상화(static abstraction)** 한 대상으로 이해해야 한다. 이 추상화는 potentially invalid한 operation을 감지하기 위한 것이다.
82: 
83: 예를 들어, 다음 변수의 런타임 값은 number type인 숫자 10이다.
84: ```ts
85: const value:number = 10;
86: ```
87: 위 TS의 `number`는 별도의 런타임 객체가 아니다. `value`가 숫자 값 중 하나를 가진다는 정적 정보일 뿐이다.
88: 
89: # 1. Type Erasure: TS에서의 type은 런타임에 남지 않는다.
90: 다음 TS 코드를 살펴보자.
91: ```ts
92: function greet(name: string): string {
93:   return `Hello, ${name}`;
94: }
95: ```
96: 위 코드를 JS로 compile하면 아래가 된다.
97: 
98: ```js
99: function greet(name) {
100:   return `Hello, ${name}`;
101: }
102: ```
103: 우리가 TS에서 정의한 type, `string`은 JS에 남지 않았다. 우리가 TS에서 작성하는 type annotation은 다음 단계에서만 사용된다.
104: ```
105: TypeScript Source
106:         │
107:         ├─ name은 string인가?
108:         ├─ 반환값은 string인가?
109:         │
110:         ▼
111: Type Check
112: ```
113: TS의 공식 문서에서는 이러한 개념을 **Erased Types**로 정의하며 type annotation은 JS의 일부가 아니고 TS에서 *대부분의 고유 타입 정보*는 emit 과정에서 제거된다고 설명한다. 그러니 type annotation 자체는 프로그램의 runtime 동작에 영향을 주지 않는다.
114: 
115: <details>
116: <summary>필자의 생각</summary>
117: 위 특성을 알았다면, TS의 본질에 대해서 다시 고민해볼 필요가 있다. TS는 결국 컴파일 타임에서 타입에 의한 런타임 에러를 미리 감지하기 위해 등장한 언어이다. 만약 프로그래머가
118: 
119: 1. 타입에 대한 확신을 가지고 있거나
120: 2. JS가 가지고 있는 자유도를 활용
121: 
122: 하고 싶다면 .ts보다는 .js를 선택하는 것이 더욱 현명할 것이다.
```


```text
476: # 8. 결론
477: 가장 중요한 점은 대부분의 경우 TS의 타입 시스템은 JS Runtime에서 새로운 타입 객체를 추가하지 않는다는 점이다.
478: 
479: 대신, JavaScript 표현식이 가질 수 있는 값을 정적으로 추상화한다.
480: ```text
481: Type erasure
482: → 타입은 정적 분석 단계에만 존재한다.
483: 
484: Structural typing
485: → 타입 호환성은 주로 멤버 구조로 결정된다.
486: 
487: Types as sets
488: → 타입은 가능한 런타임 값의 집합으로 해석할 수 있다.
489: 
490: Type inference
491: → compiler는 값과 사용 문맥으로부터 타입을 계산한다.
492: 
493: Control-flow analysis
494: → 조건과 도달 가능성에 따라 program point별 타입을 좁힌다.
495: 
496: Soundness boundaries
497: → any, assertion, 외부 입력 등에서는 정적 보장이 약해질 수 있다.
498: ```
499: 
500: 지금까지의 내용을 한 문장으로 정리하자.
501: 
502: > TypeScript는 JavaScript 프로그램의 가능한 런타임 값을 정적으로 **근사**하고, 그 근사에 비추어 안전하지 않을 가능성이 있는 연산을 실행 전에 진단한다.
503: 
504: TS은 새로운 런타임 시스템을 제공하기보다 JS의 엔진 위에서 구성된 **erasable structural static type system**이다. 모든 Runtime 오류를 잡지는 못하지만 많은 부분의 오류를 컴파일 과정에서 찾아낼 수 있다.
505: 
506: # 연결
507: 
508: - 다음에 확인할 질문: TypeScript에서의 basic type
```


## ts-generics

원본: `~/projects/portfolio/src/content/notes/ko/typescript/ts-generics.md`


```text
22: # 문제
23: 
24: `any`는 정적 타입 검사를 비활성화한다. 이로 인해 발생하는 문제는 **두 종류**이며 이 둘을 구분하는 것이 이 글의 출발점이다.
25: 
26: ```ts
27: // (1) 아무도 모르는 값
28: const data: any = JSON.parse(input);
29: data.foo.bar(); // 검사 없이 통과
30: 
31: // (2) 호출하는 쪽은 알고 있던 값
32: function identity(x: any): any { return x; }
33: const s = identity("hello"); // s: any
34: ```
35: 
36: (1)은 **검사 실패**다. `data` 값의 형태를 아무도 모르는데 어떠한 연산이나 허용된다.
37: 
38: (2)는 (1)번 문제와는 성격이 다르다. `identity("hello")`를 호출한 쪽은 인자가 `string`임을 분명히 알고 있었다. 그런데 함수 경계를 지나자 그 정보가 사라졌다. 이것은 타입의 **운반 실패**다.
39: 
40: ```
41: 호출하는 쪽이 아는 것: "hello" 는 string
42:         │
43:         │ 함수 경계 통과
44:         ▼
45: 반환값에 대해 아는 것: any
46: ```
47: 
48: 두 문제는 원인이 다르므로 해법도 달라야 한다. (1)의 해법은 `unknown`이고 (2)의 해법이 **제네릭**이다.
49: 
50: > 호출 시점의 타입 정보를 어떻게 함수 경계 너머로 운반할 것인가?
51: 
52: # 0. Overview
53: 
54: 이 글은 다음 순서로 진행한다.
55: 
56: ```
57: Parametric polymorphism  → 제네릭은 무엇인가
58: Parametricity            → 왜 본문에서 아무것도 못 하는가
59: Bounded quantification   → 제약은 무엇을 사고 무엇을 파는가
60: Types as sets            → 그 거래의 메커니즘은 무엇인가
61: ```
62: 
63: # 1. Parametric polymorphism: 타입을 매개변수로 받는다
64: 
65: 제네릭의 핵심은 입력과 출력에 **같은 이름표**를 붙이는 것이다. 타입을 일종의 변수로 취급한다고 생각하면 된다.
66: 
67: ```ts
68: function identity<T>(x: T): T {
69:   return x;
70: }
71: 
72: const a = identity("hi"); // a: "hi"
73: const b = identity(10);   // b: 10
74: ```
75: 
76: `T`는 값 대신 **타입을 담는 변수**다. 값을 매개변수로 받듯 타입을 매개변수로 받으므로 이를 **매개변수 다형성(parametric polymorphism)** 이라고 한다.
77: 
78: 논리식으로 작성하면 아래와 같다.
79: 
80: $$
81: \texttt{identity} : \forall T.\ T \rightarrow T
82: $$
83: 
84: "모든 타입 $T$에 대하여, $T$를 받아 $T$를 반환한다." 함수 앞에 **전칭 정량자($\forall$)가** 붙은 형태다.
85: 
86: `any`와 비교하면 차이가 드러난다.
87: 
88: ```ts
89: function identityAny(x: any): any { return x; }
90: 
91: const c = identity("hi");    // "hi"  — 알던 타입이 살아 나온다
92: const d = identityAny("hi"); // any   — 경계에서 증발한다
93: ```
94: 
95: 제네릭은 검사를 강화하는 장치가 아니라 **정보를 잃지 않고 흘려보내는 장치**다.
96: 
97: # 2. Parametricity: 그 대가로 본문은 무력해진다
98: 
99: `T`가 모든 타입이 될 수 있다는 것은 곧 본문에서 `T`에 대해 **아무것도 가정할 수 없다**는 뜻이다. 임의로 `T`를 `number`나 `string`으로 취급할 수 없다.
```


```text
240: # 6. 연습
241: 
242: 다음 코드에서 각 위치의 타입이 어떻게 결정될지, 그리고 어느 줄이 에러가 될지 생각해 보자.
243: 
244: ```ts
245: function first<T extends { length: number }>(xs: T): T { return xs; }
246: 
247: const r1 = first("hello");
248: const r2 = first([1, 2, 3]);
249: const r3 = first({ length: 0, extra: true });
250: const r4 = first(42);
251: 
252: function g<T>(x: T) {
253:   if (typeof x === "string") {
254:     return x.toUpperCase();
255:   }
256:   return x;
257: }
258: ```
259: 
260: # 7. 결론
261: 
262: ```
263: Parametric polymorphism
264: → 제네릭은 타입을 매개변수로 받는다. ∀T. T → T
265: 
266: 운반이 목적이다
267: → any는 호출자가 알던 타입을 경계에서 잃는다.
268: → 제네릭은 입력과 출력을 같은 이름으로 묶어 그것을 보존한다.
269: 
270: Parametricity
271: → 그 대가로 T에 대해 아무것도 가정할 수 없다.
272: → 제약은 제네릭의 목적이 아니라 대가다.
273: 
274: Bounded quantification
275: → T extends X 는 T의 범위를 상한 아래로 자른다.
276: → 본문의 능력을 사고, 호출자의 자유를 판다. 안전성은 무관하다.
277: 
278: Types as sets
279: → 본문에서 가능한 연산 = T의 가능 범위에 속한 타입들의 교집합.
280: → 범위를 자르면 교집합이 커진다. 한 절단의 두 결과다.
281: ```
282: 
283: 한 문장으로 정리하면 다음과 같다.
```


```text
372: # 연결
373: 
374: - 다음에 확인할 질문: `identity("hi")`처럼 타입 인자를 생략했을 때 compiler는 T를 어떻게 결정하는가?
```


## ts-type-argument-inference

원본: `~/projects/portfolio/src/content/notes/ko/typescript/ts-type-argument-inference.md`


```text
22: # 문제
23: 
24: [앞선 글](/notes/ts-generics)에서 우리는 제네릭 함수를 정의했지만 정작 호출할 때는 타입 인자를 쓰지 않았다.
25: 
26: ```ts
27: function identity<T>(x: T): T { return x; }
28: 
29: const explicit = identity<string>("hi"); // 명시
30: const inferred = identity("hi");         // T를 쓰지 않았다
31: ```
32: 
33: 두 번째 호출에서도 결과는 동일하게 동작한다. compiler가 `T`를 알아낸 것이다.
34: 
35: 앞선 글에서 다룬 type inference는 초기값과 문맥으로 변수의 타입을 계산하는 것이었다. 제네릭 추론은 그것과 성격이 조금 다르다. 여기서는 **미지수를 푸는** 일에 가깝다.
36: 
37: > compiler는 어떤 절차로 `T`의 값을 결정하며, 그 절차는 언제 실패하는가?
38: 
39: # 0. 단일화(unification)
40: 
41: `identity("hi")`에서 벌어지는 일은 다음과 같다.
42: 
43: ```
44: 매개변수 선언 타입:  T
45: 실제 인자의 타입:    "hi"
46:         │
47:         │ 두 식을 맞춰본다
48:         ▼
49: T := "hi"
50: ```
51: 
52: 미지수를 포함한 두 타입 식을 맞춰 미지수의 값을 구하는 것, 이를 **단일화(unification)** 라고 한다.
53: 
54: `T`가 여러 자리에 등장하면 각 자리에서 하나씩 **후보(candidate)** 가 모인다.
55: 
56: ```ts
57: function pair<T>(x: T, y: T): T[] { return [x, y]; }
58: 
59: pair("a", "b"); // 후보 = { "a", "b" } → T := string
60: ```
61: 
62: ## 0.1 매개변수 타입은 패턴이다
63: 
64: 방정식을 푸는 것이라면 미지수를 어디에 심느냐에 따라 답이 달라진다. 매개변수 타입을 `T`로 쓰는 것과 `T[]`로 쓰는 것은 서로 다른 방정식이다.
65: 
66: ```ts
67: declare function fA<T>(xs: T[]): T;
68: declare function fB<T>(xs: T): T;
69: 
70: fA([dog, cat]); // Cat | Dog
71: fB([dog, cat]); // (Cat | Dog)[]
72: ```
73: 
74: 둘 다 정상적으로 컴파일된다. 다만 `T`가 묶이는 대상이 다르다.
75: 
76: ```
77: fA:  T[]  =  (Cat | Dog)[]    →  양변의 [] 를 벗긴다  →  T = Cat | Dog
78: fB:  T    =  (Cat | Dog)[]    →  그대로              →  T = (Cat | Dog)[]
79: ```
80: 
```


## performative-prediction

원본: `~/projects/portfolio/src/content/notes/ko/AI/performative-prediction/performative-prediction.md`


```text
22: 
23: # 0. GMS theorem: 우리의 예측이 정확할 수 있는가
24: 
25: 기존의 Machine Learning의 기법은 **Data($Z$)의 분포($D$)가 fixed**($Z\sim D$)된 환경에서 동작하도록 설계되었다.
26: 
27: 그러나 1954년, Grunberg와 Modigliani 그리고 Simon는 prediction 자체가 환경을 바꿀 수 있는 power를 가질 경우를 생각하게 된다. 이를 **public prediction**이라고 하며 우리의 예측($\hat{y}$)이 공개된 뒤 사회의 실제 반응($R(\hat{y})$)이 우리의 예측과 동일할 수 있는지에 대한 질문이다.
28: 
29: $$
30: \hat{y} = R(\hat{y})
31: $$
32: 
33: 위에 대한 존재성은 $R$의 연속성과 Brouwer 고정점 정리를 통해 존재 가능하다는 것이 증명되었다.
34: 
35: 다만 GMS는 해의 존재성만을 증명하며 스칼라값에서만 동작한다. 이를 분포로 확장하고 해를 구하는 방식으로 확장한 ML 기법이 Performative Prediction(PP)이다.
36: 
37: # 1. Performative Prediction: 어떻게 정확한 예측값을 찾을 수 있는가
38: 
39: ## GMS Theorem formulate
40: 
41: 앞서 간단하게 살펴본 GMS theorem의 문제를 정의해본다.
42: 
43: - 결과 공간인 $S \in [0,1]$ 이며 compact, convex 하다.
44: - 응답함수인 $R: S \rightarrow S$ 이며 연속이다.
45: 
46: 이때, $\exists\hat{y}^* \in S\::\:\hat{y}^*=R(\hat{y}^*)$ 이 성립하는가?
47: 
48: 위 문제를 ML에 직접 적용하기에는 아래와 같은 제약이 존재한다.
49: 
50: 1. 예측이 스칼라 집계량이다.
51:    - GMS에서 $\hat{y}$은 스칼라 하나다. 하지만 ML에서는 **함수인 $f_\theta$**를 예측해야 한다. 그리고 함수의 input은 여러 특성이 모인 벡터 이상의 $x$가 된다.
52: 2. 결과가 값이지 분포가 아니다.
53:    - 1번과 유사하게 GMS에서 $R(\hat{y})$의 결과값인 $y$는 하나의 스칼라일 뿐이다. ML에서 요구하는 $(x,y)$ 쌍의 결합 분포가 아니다. 이를 해결하기 위해서는 분포에서 사용할 거리 개념을 다시 세워야 한다.
54: 3. 해의 존재성만을 보여준다.
55:    - GMS는 해의 존재성만을 증명하기에 **"좋은 예측"이라는 개념이 부재**하다. 특히, $\hat{y}=R(\hat{y})$는 완벽한 예측을 요구하기에 ML에서는 실현할 수 없다.
56: 4. $R$을 안다고 가정한다.
57:    - GMS는 응답함수 $R$을 수학적으로 주어진 함수로 취급한다. ML에서는 $\mathcal{D}(\theta)$는 알 수 없다. 배포한 뒤 유한적인 데이터만을 관측할 수 있다.
58: 
59: # 2. Extends GMS to PP
60: 
61: 위 제약들을 해결하여 GMS를 ML로 확장한 것이 PP이다. 각 제약을 어떻게 풀어냈는지 살펴보자.
62: 
63: ## 2.0 **Distribution Map - "key conceptual device"**
64: 
```


```text
84: $$
85: 
86: PP가 묻는 질문은 이제 두 가지가 된다.
87: 
88: 1. 이 모델이 자기가 만든 분포에서 고정점인가(stability)
89: 2. 가능한 모든 모델-환경 쌍 중 최선인가(optimality).
90: 
91: 우리는 위 두 질문에 대해 각각의 평가 기준을 세워서 평가하고자 한다.
92: 
93: ## 2.1 Performative Stability: GMS fixed Point
94: 
95: $$
96: \theta_{\text{PS}}\in\argmin_\theta \mathbb{E}_{Z\sim \mathcal{D}(\theta_{\text{PS}})}\ell(Z;\theta)
97: $$
```


```text
228: \begin{align}
229: \;\Vert G(\theta)-G(\theta')\Vert_2\leq\varepsilon\frac{\beta}{\gamma}\Vert\theta-\theta'\Vert_2,\;for\;all \;\theta,\theta'\in\Theta
230: \end{align}
231: $$
232: 
233: 위 식에서 앞으로 $\varepsilon\frac{\beta}{\gamma}$를 $q$로 대체하겠다. 이 경우 식 (1)은 두 모델 $\theta, \theta'$에 대해서 배포한 뒤 결과 모델 $G(\theta),G(\theta')$ 사이의 거리가 멀어지는 정도를 제한한다.
234: 
235: ```text
236: 현재 모델 차이
237: ‖θ - θ′‖
238:      ↓ retraining operator G
239: 다음 모델 차이
240: ‖G(θ) - G(θ′)‖
241:      ≤ (εβ/γ) ‖θ - θ′‖
242: ```
243: 
244: 위에서 봤던 변수들($\varepsilon,\beta,\gamma$)의 역할을 정리하면 아래와 같다.
245: 
246: | 상수         | 의미                                                 | ($q=\epsilon\beta/\gamma$)에 미치는 영향 |
247: | ------------ | ---------------------------------------------------- | ---------------------------------------- |
248: | ($\epsilon$) | 모델 변화가 distribution을 얼마나 변화시키는가       | 클수록 불안정                            |
249: | ($\beta$)    | 데이터 또는 모델 변화가 gradient에 얼마나 전달되는가 | 클수록 불안정                            |
250: | ($\gamma$)   | objective가 minimizer로 되돌리는 곡률                | 클수록 안정                              |
251: 
```


```text
351: # 4. 정리 — 무엇을 답했고 무엇이 남았는가
352: 
353: 이번 글은 한 가지 질문에 답했다. **"모델이 데이터 분포를 바꾸는 환경에서, 재학습은 한 점으로 수렴하는가?"**
354: 
355: 조건부로 성립한다. 손실이 $\gamma$-strong convex, $\beta$-smoothness이고 분포 맵이 $\varepsilon$-sensitive일 때 재학습 연산자 $G$는 축약 사상이 되고
356: 
357: $$
358: \varepsilon < \frac{\gamma}{\beta}
359: \qquad\Longleftrightarrow\qquad
360: \underbrace{\varepsilon\beta}_{\text{분포가 도망가는 속도}}
361: \;<\;
362: \underbrace{\gamma}_{\text{최적화가 당기는 속도}}
363: $$
364: 
365: 이면 유일한 안정점 $\theta_{\text{PS}}$로 선형 수렴한다. 세 가정 중 어느 하나만 빼도 발산하는 반례가 존재하므로 이 결과는 더 약화할 수 없다.
366: 
367: 그러나 여기까지는 **"재학습이 어디로 가는가"** 에 대한 답이다. 아직 두 가지가 남아 있다.
368: 
369: ## 남은 문제 1: 모집단 가정
370: 
371: 위 논의는 모두 "모집단 수준(population level)"에서 이루어졌다. 즉 $\mathcal{D}(\theta_t)$에 대한 기댓값을 정확히 계산할 수 있다고 가정했다. 그러나 1장에서 지적했듯 현실에서 우리가 관측하는 것은 배포 이후의 **유한한 표본**뿐이다. 원 논문은 이 경우에도 고확률로 안정점 근방에 도달하고 그 안에 머문다는 것을 보인다(RERM/REGD).
372: 
373: ## 남은 문제 2: $\theta_{\text{PS}}$는 $\theta_{\text{PO}}$가 아니다
374: 
375: 더 근본적인 문제가 남았다. 2장에서 우리는 해 개념을 **2가지**로 정의했다.
376: 
377: | | 정의 | 성격 |
378: | --- | --- | --- |
379: | $\theta_{\text{PS}}$ | 자기가 만든 분포에서 재학습해도 그대로 | 고정점 — **도달 가능** |
380: | $\theta_{\text{PO}}$ | 모든 모델-환경 쌍 중 손실 최소 | 전역 최적 — **우리가 원하던 것** |
381: 
382: 그리고 앞서 3장 전체는 **$\theta_{\text{PS}}$** 만 다뤘다. 우리가 도달한 곳은 "원하던 최선"이 아니라 "재학습이 데려다준 곳"이다.
383: 
384: $\theta_{\text{PS}}$는 자신이 유발한 데이터로는 반박되지 않는다. 지금 조건에서 데이터를 모아 위험 최소화를 다시 풀어도 같은 모델이 나오므로 **그 안에서는 더 개선할 여지가 보이지 않는다**. 그러나 이는 더 나은 모델이 없다는 뜻과 동치가 아니다.
385: 
386: 그렇다면 아래와 같은 질문이 남는다.
387: 
388: > **도달한 안정점은 원하던 최적점과 얼마나 다른가?**
389: 
390: 안정점과 최적점의 차이가 크지 않아야 앞서 살펴본 방식이 정당화된다.
391: 
```


```text
399: # 참고문헌
400: - Hardt, Moritz, and Celestine Mendler-Dünner. "Performative prediction: Past and future." Statistical Science 40.3 (2025): 417-436.
401: - Perdomo, Juan, et al. "Performative prediction." International Conference on Machine Learning. PMLR, 2020.
402: 
403: # 연결
404: 
405: - 관련 프로젝트: staged DDA matgo
406: - 관련 실험:
407: - 다음에 확인할 질문: RRM에서의 해답은 PO를 만족할 수 있는가?
```


## bundler-vite-vs-webpack

원본: `~/projects/portfolio/src/content/notes/ko/web/bundler-vite-vs-webpack.md`


```text
23: # 1. 1편이 남긴 질문
24: 
25: [1편](/notes/tenant-split-frontend-backend/)에서 프론트엔드를 사업자마다 별도 빌드하기로 했다. 근거는 명세의 C2였다.
26: 
27: > 비활성 모듈의 화면·탭은 **빌드에서 제외**된다
28: 
29: 그리고 이런 제약이 따라 나왔다. **런타임 조건문으로는 이 요구를 만족할 수 없다.**
30: 
31: 실행 중에 `if (config.enabledModules.includes("reward"))`로 판정하면 리워드 화면 코드는 어차피 번들에 들어 있다. 화면에 안 보일 뿐 사용자는 그 코드를 다운로드한다.
32: 
33: 그래서 번들러 선택이 아키텍처 결정이 되었고 Vite를 채택했다. 이 글은 그때 미뤄 둔 세 가지를 갚는다.
34: 
35: 1. 번들러는 대체 무엇을 하는 도구인가
36: 2. 어떤 원리로 안 쓰는 코드를 없애는가
37: 3. Vite와 Webpack은 그 원리의 어디에서 갈라지며, 왜 이 프로젝트에는 Vite인가
38: 
39: ---
40: 
41: # 2. 번들러는 원래 무엇을 하는 도구였나
42: 
43: 시작은 단순한 문제였다. **브라우저가 모듈 시스템을 몰랐다.**
44: 
45: `<script>` 태그로 파일을 순서대로 불러오던 시절, 파일이 수십 개가 되면 순서 하나만 틀려도 앱이 죽었다. 전역 네임스페이스는 서로를 덮어썼다. 그래서 CommonJS·AMD 같은 모듈 규약이 등장했는데 브라우저는 그걸 실행할 줄 몰랐다.
46: 
47: 번들러의 최초 임무는 여기서 나왔다. **여러 모듈을 브라우저가 이해하는 하나의 파일로 합치는 일이었다.** 이름 그대로 묶는(bundle) 도구였다.
48: 
49: 그런데 지금은 사정이 다르다. 브라우저가 ES Module을 네이티브로 지원하고 HTTP/2가 다중 요청 비용을 낮췄다. "합치는 것" 자체는 예전만큼 절박하지 않다.
50: 
51: 대신 남은 게 있다. 번들러가 모듈 그래프 전체를 들여다보는 김에 하게 된 일들이다.
52: 
53: | 하는 일 | 내용 |
54: |---|---|
55: | **변환** | TypeScript·JSX를 브라우저가 아는 형태로 |
56: | **그래프 분석** | 무엇이 무엇을 import 하는지 전체 지도 작성 |
57: | **최적화** | 안 쓰는 코드 제거, 상수 인라인, 이름 축약 |
58: | **분할** | 초기 로드에 필요 없는 부분을 별도 청크로 |
59: | **자산 처리** | 이미지·CSS를 해시 붙은 파일로, 참조 경로 재작성 |
60: 
61: 우리에게 중요한 건 세 번째다. **번들러가 그래프 전체를 알고 있어서 "이건 아무도 안 쓴다"를 판정할 수 있다는 것.**
```


```text
80: 이 탐색이 끝나면 **도달 가능한 모듈의 집합**이 나온다. 여기에 없는 파일은 프로젝트에 존재해도 번들에 들어가지 않는다. 첫 번째 필터가 여기서 걸린다.
81: 
82: ## 3.2 안 쓰는 export를 털어낸다 — tree-shaking
83: 
84: 도달 가능한 모듈 안에서도 안 쓰는 부분이 있다.
85: 
86: ```ts
87: // utils.ts
88: export function formatPrice(n: number) { /* ... */ }
89: export function formatDate(d: Date) { /* ... */ }   // 아무도 안 쓴다
90: 
91: // main.ts
92: import { formatPrice } from "./utils";
93: ```
94: 
95: `formatDate`는 최종 번들에서 빠진다. 이걸 **tree-shaking**이라고 부른다. 그래프를 나무로 보고 안 쓰는 가지를 흔들어 떨어뜨린다는 비유다.
96: 
97: **이게 되는 이유는 ES Module이 정적이기 때문이다.** `import`/`export`는 파일 최상단에만 올 수 있고 이름이 실행 전에 확정된다. 그래서 번들러가 코드를 **실행하지 않고도** 누가 무엇을 쓰는지 알 수 있다.
```


```text
294: 
295: > 결정 근거는 "Vite가 더 좋다"가 아니라 **"우리가 기대는 사슬이 Vite에서는 기본값이고, 반복 빌드에서 속도가 곧 확장 한계"** 다.
296: 
297: ---
298: 
299: # 8. Vite가 불리한 경우
300: 
301: 다음 경우에는 trade-off가 Webpack 쪽으로 기운다.
302: 
303: - **CommonJS 레거시 의존성이 많은 경우.** ESM 기반 분석의 이점이 줄고 상호운용 처리에서 Webpack의 축적된 대응이 유리할 수 있다
304: - **Webpack 생태계에만 있는 특수 loader가 필요한 경우.** 오래된 사내 툴체인에서 흔하다
305: - **Module Federation을 쓰는 마이크로프론트엔드.** Webpack이 이 영역의 사실상 표준이고 성숙도 차이가 있다
306: - **빌드 산출물을 아주 세밀하게 통제해야 하는 경우.** 설정 표면이 큰 쪽이 유리하다
307: 
308: 우리 프로젝트는 신규이고 의존성이 현대적이며 마이크로프론트엔드가 아니다. 그래서 위 항목에 하나도 걸리지 않는다. **조건이 달랐다면 답도 달랐을 것이다.**
309: 
310: ---
311: 
312: # 9. 다음 글
313: 
314: 번들러 이야기는 여기서 닫는다. 정리하면 이렇다.
315: 
316: > tree-shaking은 **값이 정적으로 확정될 때만** 성립한다. 우리는 그 성질에 기대어 C2를 만족시켰고 그 사슬이 기본 경로인 도구를 골랐다.
317: 
318: 다음 글은 상태 계층으로 넘어간다. 백엔드가 진실 소스가 되는 순간 프론트엔드가 들고 있는 데이터의 성격이 바뀐다. **서버 데이터를 값이 아니라 캐시로 취급한다는 게 무슨 뜻인지**, 그 관점이 라이브러리 선택을 어떻게 결정했는지 다룬다.
319: 
320: ---
321: 
322: # 참고
323: 
324: - [Vite 8 Beta: The Rolldown-powered Vite](https://vite.dev/blog/announcing-vite8-beta) — Rolldown 통합과 벤치마크
```
