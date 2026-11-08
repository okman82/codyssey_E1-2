# 🎯 나만의 퀴즈 게임

터미널에서 실행하는 Python 퀴즈 게임입니다.
퀴즈를 풀고, 새 퀴즈를 추가하고, 최고 점수를 기록할 수 있으며, 프로그램을 종료했다가 다시 실행해도 퀴즈와 점수가 유지됩니다.

## 1. 프로젝트 개요

- **목적**: Python 기초 문법, 클래스, 파일 입출력, Git 사용법을 하나의 프로그램을 완성하며 익히기
- **언어**: Python 3.10 이상 (외부 라이브러리 없이 표준 라이브러리만 사용)
- **핵심 구조**
  - `Quiz` 클래스: 퀴즈 1개(문제, 선택지 4개, 정답 번호)를 표현
  - `QuizGame` 클래스: 메뉴, 게임 진행, 퀴즈 추가·목록·점수, 파일 저장·불러오기를 관리
- **데이터 영속성**: 퀴즈 목록과 최고 점수를 `state.json`에 저장

## 2. 퀴즈 주제와 선정 이유

**주제: Python 기초 문법**

<!-- ✏️ 직접 작성하세요. 아래는 예시입니다. -->
Python을 처음 배우면서 헷갈렸던 문법(리스트 기호, 함수 정의, 반복문 등)을 퀴즈로 만들면 프로그램을 만드는 동시에 복습도 할 수 있다고 생각해 선정했습니다.

## 3. 실행 방법

```bash
# 저장소 복제
git clone https://github.com/<아이디>/<저장소이름>.git
cd <저장소이름>

# 실행
python main.py
```

- `python` 명령이 동작하지 않으면 Windows에서는 `py main.py`, macOS/Linux에서는 `python3 main.py`로 실행합니다.
- 실행 위치와 관계없이 `state.json`은 `main.py`와 같은 폴더에 저장됩니다.

## 4. 기능 목록

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 등록된 퀴즈를 순서대로 출제하고 정답/오답을 알려줌. 끝나면 `5문제 중 4문제 정답! (80점)` 형식으로 결과 표시 |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력받아 새 퀴즈를 등록하고 파일에 저장 |
| 3 | 퀴즈 목록 | 등록된 퀴즈의 문제를 번호와 함께 출력 |
| 4 | 점수 확인 | 최고 점수 출력. 아직 풀지 않았으면 안내 메시지 출력 |
| 5 | 종료 | 데이터를 저장하고 프로그램 종료 |

### 최고 점수 기준

- 최고 점수는 **100점 만점 점수**로 저장합니다. (`정답 수 × 100 ÷ 전체 문제 수`, 소수점 버림)
- 퀴즈를 추가해 문제 수가 달라져도 같은 기준으로 비교할 수 있도록 정답 개수가 아닌 점수를 사용했습니다.
- 퀴즈를 풀 때마다 최고 점수와 비교해 더 높으면 갱신하고 즉시 저장합니다.

### 입력 및 예외 처리

| 상황 | 처리 |
|---|---|
| 입력 앞뒤 공백 (예: ` 1 `) | 공백 제거 후 처리 |
| 숫자가 아닌 입력 (예: `abc`) | 안내 메시지 출력 후 다시 입력 |
| 범위 밖 숫자 (예: 메뉴 `9`, 정답 `0`) | 허용 범위 안내 후 다시 입력 |
| 빈 입력 (그냥 Enter) | 안내 메시지 출력 후 다시 입력 |
| `Ctrl + C`, 입력 스트림 종료 | 안내 메시지 출력 후 저장하고 안전하게 종료 |
| 퀴즈가 하나도 없을 때 | 퀴즈 풀기·목록에서 안내 메시지 출력 |
| `state.json`이 없을 때 | 기본 퀴즈 5개로 시작하고 파일 생성 |
| `state.json`이 손상되었을 때 | 안내 메시지 출력 후 기본 퀴즈로 복구 |

## 5. 파일 구조

```text
.
├── main.py              # 프로그램 전체 코드 (Quiz, QuizGame 클래스, 입력 함수)
├── state.json           # 퀴즈·최고 점수 저장 파일 (실행 시 자동 생성)
├── README.md            # 프로젝트 설명
├── .gitignore           # Git에서 제외할 파일 목록
└── docs/
    └── screenshots/     # 실행 화면 캡처
```

### `main.py` 구성

| 구분 | 이름 | 역할 |
|---|---|---|
| 함수 | `input_number(prompt, low, high)` | 범위 안의 숫자를 입력받을 때까지 반복 (공백·빈 입력·문자·범위 검사) |
| 함수 | `input_text(prompt)` | 비어 있지 않은 문자열을 입력받음 |
| 클래스 | `Quiz` | `show()` 퀴즈 출력, `is_correct()` 정답 확인, `to_dict()`/`from_dict()` JSON 변환 |
| 클래스 | `QuizGame` | `run()` 메뉴 반복, `play_quiz()`, `add_quiz()`, `show_quizzes()`, `show_best_score()`, `save_state()`, `load_state()` |

## 6. 주요 코드 설명
<!-- > 각 코드를 왜 이렇게 썼는지, 일반적인 방식과 비교한 자세한 설명은 [코드 리뷰 문서](CODE_REVIEW.md)에 정리했습니다. -->

### 6-1. 프로그램 실행 흐름

```text
main.py 실행
  └─ QuizGame(default_quizzes) 생성
       └─ load_state()      state.json 불러오기 (없거나 손상 → 기본 퀴즈)
  └─ game.run()
       └─ while 반복: 메뉴 출력 → 번호 입력 → 기능 실행
            1 play_quiz()  2 add_quiz()  3 show_quizzes()  4 show_best_score()  5 종료
       └─ finally: save_state()   어떻게 끝나든 저장
```

### 6-2. 공통 입력 함수 `input_number`

숫자 입력이 필요한 모든 곳(메뉴 1~5, 정답 1~4)에서 같은 함수를 재사용합니다.

```python
def input_number(prompt, low, high):
    while True:
        try:
            value = input(prompt).strip()      # 앞뒤 공백 제거
        except KeyboardInterrupt:              # Ctrl + C
            print("\n입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
            return None
        except EOFError:                       # 입력 스트림 종료
            print("\n입력 스트림이 종료되었습니다. 프로그램을 안전하게 종료합니다.")
            return None

        if value == "":                        # 빈 입력
            print("입력이 비어 있습니다.")
            continue

        try:
            number = int(value)                # 숫자 변환
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if low <= number <= high:              # 범위 확인
            return number

        print(f"{low}에서 {high} 사이의 숫자를 입력하세요.")
```

- 올바른 숫자를 입력할 때까지 `while True`로 반복하고, 올바르면 `return`으로 반복과 함수를 함께 끝냅니다.
- 강제 종료 시 `None`을 돌려주고, 호출한 쪽에서 `None`이면 `self.running = False`로 게임을 끝냅니다.
- 범위를 매개변수(`low`, `high`)로 받아 메뉴와 정답 입력 모두에 쓸 수 있습니다.

### 6-3. `Quiz` 클래스와 JSON 변환

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 번호로 저장

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):                 # 객체 → 딕셔너리 (저장용)
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @classmethod
    def from_dict(cls, data):          # 딕셔너리 → 객체 (불러오기용)
        return cls(data["question"], data["choices"], data["answer"])
```

- `Quiz` 객체는 JSON 파일에 바로 쓸 수 없어서 `to_dict()`로 딕셔너리로 바꿔 저장합니다.
- 불러올 때는 반대로 `from_dict()`로 딕셔너리를 `Quiz` 객체로 되돌립니다.
- `@classmethod`는 객체가 아직 없는 상태에서 클래스 이름으로 호출하는 메서드입니다. (`Quiz.from_dict(item)`)
- 정답은 리스트 인덱스(0~3)가 아니라 **화면 번호(1~4)** 로 저장해 사용자가 입력한 값과 바로 비교합니다.

### 6-4. 저장 `save_state`

```python
data = {
    "quizzes": [quiz.to_dict() for quiz in self.quizzes],
    "best_score": self.best_score
}
with open(self.state_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
```

- `[... for quiz in self.quizzes]`: 모든 퀴즈를 딕셔너리로 바꿔 새 리스트를 만듭니다.
- `with open(...)`: 블록이 끝나면 파일을 자동으로 닫습니다.
- `ensure_ascii=False`: 한글을 글자 그대로 저장합니다.
- 쓰기 실패(`OSError`) 시 안내 메시지를 출력하고 프로그램은 계속 실행합니다.

### 6-5. 불러오기와 손상 파일 검증 `load_state`

```python
try:
    with open(self.state_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    # 각 퀴즈의 question(str), choices(4개 list), answer(1~4 int) 형식 검사
    # 형식이 다르면 raise ValueError(...)
except FileNotFoundError:
    # 첫 실행: 기본 퀴즈로 시작하고 파일 생성
except (json.JSONDecodeError, ValueError, OSError):
    # 손상: 안내 후 기본 퀴즈로 복구
```

| 상황 | 원인 | 처리 |
|---|---|---|
| 파일 없음 | `FileNotFoundError` | 기본 퀴즈로 시작, 파일 생성 |
| JSON 문법 오류 (괄호 누락 등) | `json.JSONDecodeError` | 안내 후 기본 퀴즈로 복구 |
| 문법은 맞지만 내용이 잘못됨 (키 누락, 정답 9 등) | 직접 `raise ValueError` | 안내 후 기본 퀴즈로 복구 |
| 읽기 권한 등 파일 오류 | `OSError` | 안내 후 기본 퀴즈로 복구 |

- JSON 문법만 검사하면 `"answer": 9`처럼 **형식은 맞지만 잘못된 데이터**를 그대로 불러와 게임 중 오류가 날 수 있어, `isinstance()`로 자료형과 범위를 직접 검사합니다.
- 정상적으로 불러오면 `저장된 데이터를 불러왔습니다. (퀴즈 N개, 최고 점수 N점)`을 출력합니다.

### 6-6. 기본 퀴즈 복사 `copy_quizzes`

```python
def copy_quizzes(self, quizzes):
    return [Quiz(q.question, list(q.choices), q.answer) for q in quizzes]
```

- 기본 퀴즈를 그대로 쓰면 게임 중 퀴즈를 추가할 때 **원본 기본 퀴즈 목록까지 함께 바뀝니다.**
- 새 `Quiz` 객체와 새 선택지 리스트(`list(...)`)로 복사해, 손상 파일 복구 시 항상 처음 상태의 기본 퀴즈를 쓸 수 있게 합니다.

### 6-7. 퀴즈 풀기와 점수 계산 `play_quiz`

```python
for i, quiz in enumerate(self.quizzes, start=1):
    print(f"\n[문제 {i}]")
    quiz.show()
    answer = input_number("정답 번호를 입력하세요: ", 1, 4)
    ...
percent = score * 100 // len(self.quizzes)

if self.best_score is None or percent > self.best_score:
    self.best_score = percent
    self.save_state()
```

- `enumerate(..., start=1)`: 문제 번호(1부터)와 퀴즈를 함께 꺼냅니다.
- `score * 100 // 문제 수`: **곱하기를 먼저** 해야 정수 나눗셈에서 0이 되지 않습니다.
- `best_score is None`: 아직 한 번도 풀지 않은 상태(`0점`과 구분)입니다.
- 최고 점수가 갱신되면 즉시 저장해, 도중에 강제 종료되어도 기록이 남습니다.

### 6-8. 안전한 종료 `run`

```python
def run(self):
    try:
        while self.running:
            ...
    finally:
        self.save_state()
```

- `finally`는 정상 종료(메뉴 5), 강제 종료(`Ctrl + C`), 예상치 못한 오류 등 **어떤 경우에도 마지막에 실행**됩니다.
- `self.running`을 `False`로 바꾸면 반복이 끝나도록 해, 각 기능 안에서도 게임 종료를 요청할 수 있습니다.

### 6-9. 프로젝트 루트 경로 고정

```python
STATE_FILE = Path(__file__).parent / "state.json"
```

- `"state.json"`만 쓰면 **명령을 실행한 위치**를 기준으로 파일을 찾습니다.
- `__file__`(`main.py`의 경로)의 폴더(`.parent`)를 기준으로 삼아, 어디서 실행해도 프로젝트 루트의 `state.json`을 사용합니다.

## 7. 데이터 파일 설명 (`state.json`)

- **경로**: 프로젝트 루트 (`main.py`와 같은 폴더)
- **역할**: 프로그램을 종료해도 퀴즈 목록과 최고 점수가 유지되도록 저장
- **인코딩**: UTF-8 (한글이 그대로 보이도록 `ensure_ascii=False`로 저장)
- **저장 시점**: 퀴즈 추가 시, 최고 점수 갱신 시, 프로그램 종료 시

### 스키마

```json
{
    "quizzes": [
        {
            "question": "Python에서 리스트를 만드는 기호는?",
            "choices": ["()", "{}", "[]", "<>"],
            "answer": 3
        }
    ],
    "best_score": 80
}
```

| 키 | 자료형 | 설명 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list (str 4개) | 선택지 |
| `quizzes[].answer` | int (1~4) | 정답 번호 |
| `best_score` | int 또는 null | 최고 점수 (100점 만점). 아직 풀지 않았으면 `null` |

불러올 때 위 형식과 다르면(키 누락, 선택지 개수 오류, 정답 범위 오류 등) 손상된 파일로 판단해 기본 퀴즈로 복구합니다.

## 8. 실행 화면

### 메뉴
![메뉴](docs/screenshots/menu.png)
       doc/screenshots/menu.png
### 퀴즈 풀기
![퀴즈 풀기](docs/screenshots/play.png)

### 퀴즈 추가
![퀴즈 추가](docs/screenshots/add_quiz.png)

### 퀴즈 추가가 재시작시 퀴즈 추가여부 확인
![퀴즈 추가후 재시작시 퀴즈 목록](docs/screenshots/add_quiz_restart.png)


### 퀴즈 목록
![퀴즈 목록](docs/screenshots/list.png)

### 점수 확인
![점수 확인](docs/screenshots/score.png)

## 9. Git 작업 기록

- 기능 단위로 커밋 (`Feat`, `Fix`, `Refactor`, `Docs`)
- 퀴즈 풀기 화면 개선은 `feature/play-quiz` 브랜치에서 작업 후 `main`에 `--no-ff`로 병합
- 사용한 명령: `init`, `add`, `commit`, `push`, `checkout`, `merge`, `clone`, `pull`

![git log](docs/screenshots/git_log.png)
