# Python 학습 노트 — 미션 2: 퀴즈 게임 준비

> 코디세이 입학연수 미션 2 「컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기」를 위해 공부한 내용을 정리한 노트입니다.

## 진행 현황

| 단계 | 주제 | 상태 |
|---|---|---|
| 1 | 개발 환경 준비 | ✅ 완료 |
| 2-1 | 변수와 자료형 | ✅ 완료 |
| 2-2 | 입력/출력, f-string | ✅ 완료 |
| 2-3 | 조건문 `if` | ✅ 완료 |
| 2-4 | 반복문 `for` | ✅ 완료 |
| 2-5 | 반복문 `while`, `break` | ✅ 완료 |
| 3 | 오류 처리 `try`/`except` | ✅ 완료 |
| 2-6 | 함수 | ✅ 완료 (`input_number` 작성) |
| 4 | 클래스와 객체 | ✅ 완료 (`Quiz`, `QuizGame`) |
| 5 | 파일과 JSON | ✅ 구현 완료 (`state.json` 저장/불러오기) |
| 6 | Git과 GitHub | ✅ 완료 (커밋, 브랜치, 병합) |
| 7 | 프로그램 완성 | ✅ 기능 구현·스크린샷·README |
| 8 | clone/pull 실습 | ⏳ 남음 |

---

## 1. 변수

변수는 **값에 붙이는 이름표**입니다.

```python
score = 0
score = score + 1
print(score)   # 1
```

- `=`는 "같다"가 아니라 **오른쪽 값을 왼쪽 이름에 저장한다**는 뜻입니다.
- 비교할 때는 `==`를 씁니다.

## 2. 자료형

| 자료형 | 의미 | 예시 | 퀴즈 게임에서의 쓰임 |
|---|---|---|---|
| `int` | 정수 | `80` | 점수 |
| `str` | 문자열 | `"대한민국의 수도는?"` | 문제 |
| `bool` | 참/거짓 | `True`, `False` | 정답 여부 |
| `list` | 순서 있는 묶음 | `["부산", "서울"]` | 선택지 |
| `dict` | 이름표가 붙은 묶음 | `{"answer": 2}` | 퀴즈 1개의 정보 |

```python
choices = ["부산", "광주", "서울", "제주"]
print(choices[0])        # 부산  ← 리스트는 0번부터

quiz = {"question": "대한민국의 수도는?", "answer": 3}
print(quiz["question"])  # 키 이름으로 값을 찾음
```

### 괄호의 쓰임

| 괄호 | 용도 | 예시 |
|---|---|---|
| `( )` | 함수 실행 | `print(question)` |
| `[ ]` | 리스트 생성, 항목 꺼내기 | `choices[0]` |
| `{ }` | 딕셔너리 생성 | `{"answer": 2}` |

## 3. 입력과 출력

```python
user_answer = int(input("정답 입력: "))
```

- `input()`으로 받은 값은 숫자를 입력해도 **항상 문자열(`str`)** 입니다.
- 계산하거나 숫자와 비교하려면 `int()`로 바꿔야 합니다.

## 4. f-string

문자열 앞에 `f`를 붙이면 `{ }` 안의 변수나 계산 결과가 그 값으로 바뀝니다. (`f`는 format의 약자)

```python
answer = 3
print("정답은 {answer}번입니다.")   # 정답은 {answer}번입니다.
print(f"정답은 {answer}번입니다.")  # 정답은 3번입니다.
```

- `f`는 **여는 따옴표 바로 앞**에 붙입니다.
- `{ }` 안에서 계산도 가능합니다: `f"{i + 1}번"`
- `print`와 `f`는 별개입니다. `f`로 문자열을 만들고, `print`로 출력합니다.

## 5. 조건문 `if`

```python
if user_answer == answer:
    print("정답입니다!")
else:
    print(f"오답입니다. 정답은 {answer}번입니다.")
```

```python
if score >= 90:
    print("아주 잘했어요!")
elif score >= 60:
    print("합격입니다!")
else:
    print("다시 도전해 보세요!")
```

- 위에서부터 확인하다가 **처음으로 참인 부분 하나만** 실행합니다.
- 조건 끝에 콜론 `:`을 붙이고, 실행할 코드는 들여씁니다.
- 범위 비교: `1 <= num <= 4` → "1 이상 4 이하"

## 6. 반복문 `for`

**횟수가 정해진** 반복에 씁니다.

```python
choices = ["부산", "서울", "대전", "광주"]

for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")
```

```text
1. 부산
2. 서울
3. 대전
4. 광주
```

- `range(4)` → `0, 1, 2, 3` (4는 포함하지 않음)
- `len(choices)` → 리스트의 개수. 숫자를 직접 쓰지 않으면 선택지 수가 바뀌어도 고칠 필요가 없습니다.

### ⭐ 인덱스 vs 화면 번호

| 구분 | 시작 | 쓰는 곳 |
|---|---|---|
| 인덱스 (컴퓨터용) | 0 | `choices[i]` |
| 화면 번호 (사람용) | 1 | `f"{i + 1}."` |

화면 번호를 인덱스로 바꿀 때는 `menu[input_num - 1]`처럼 1을 뺍니다.

## 7. 반복문 `while`

**조건이 참인 동안** 반복합니다. 몇 번 반복할지 모를 때 씁니다.

```python
count = 1
while count <= 3:
    print(f"{count}번째 반복")
    count = count + 1   # 이 줄이 없으면 무한 반복
```

### `while True` + `break`

```python
menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

while True:
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    input_num = int(input("번호를 입력하세요: "))

    if input_num == 5:
        print("프로그램을 종료합니다.")
        break
    elif 1 <= input_num <= 4:
        print(f"{menu[input_num - 1]}를 선택했습니다.")
    else:
        print("잘못된 번호입니다.")
```

- `break`: 반복문을 빠져나옵니다.
- `continue`: 아래 코드를 건너뛰고 반복의 처음으로 돌아갑니다.
- 메뉴 출력과 입력 코드는 **한 번만** 쓰는 것이 좋습니다. 중복 코드는 수정할 때 버그의 원인이 됩니다.

## 8. 오류 처리 `try`/`except`

```python
try:
    num = int(input("숫자 입력: "))
    print(f"입력한 숫자: {num}")
except ValueError:
    print("숫자만 입력하세요.")
```

- `try`: 오류가 날 수 있는 코드
- `except ValueError`: 그 오류가 나면 실행할 코드
- 오류가 나는 순간 `try`의 나머지 줄은 건너뜁니다.
- `try`는 **오류가 날 수 있는 줄만** 감싸는 것이 좋습니다. 어떤 오류를 잡는지 분명해집니다.
- `text.strip()`: 문자열 앞뒤 공백 제거
- `continue`: 반복의 처음으로 돌아가기

### 완성한 메뉴 코드

```python
menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

while True:
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    try:
        input_num = input("번호를 입력하세요: ").strip()
        if input_num == "":
            print("입력이 비어 있습니다.")
            continue
        input_num = int(input_num)
    except ValueError:
        print("숫자만 입력하세요.")
        continue

    if input_num == 1:
        print("퀴즈 풀기를 선택했습니다.")
    elif input_num == 2:
        print("퀴즈 추가를 선택했습니다.")
    elif input_num == 3:
        print("퀴즈 목록을 선택했습니다.")
    elif input_num == 4:
        print("점수 확인을 선택했습니다.")
    elif input_num == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 번호입니다.")
```

| 입력 | 결과 |
|---|---|
| ` 1 ` (앞뒤 공백) | 퀴즈 풀기를 선택했습니다. ✅ |
| `abc` | 숫자만 입력하세요. ✅ |
| 그냥 Enter | 입력이 비어 있습니다. ✅ |
| `9` | 잘못된 번호입니다. ✅ |
| `Ctrl + C` | ⚠️ 아직 오류로 멈춤 → 저장 기능과 함께 처리 예정 |

## 9. 함수

반복해서 쓸 코드를 이름 하나로 묶습니다.

```python
def greet(name):
    message = f"안녕하세요, {name}님!"
    return message

result = greet("Mani")
print(result)  # 안녕하세요, Mani님!
```

- `def`: 함수 정의. 정의만 해서는 실행되지 않고, **호출**해야 실행됩니다.
- 매개변수(`name`): 함수에 넘겨주는 값을 받는 변수
- `return`: 결과를 호출한 곳으로 돌려주고, 함수를 **즉시 끝냅니다.**

### 완성한 `input_number` 함수

빈 입력·문자·범위 밖 숫자를 모두 처리하고, 올바른 숫자만 돌려줍니다.

```python
def input_number(prompt, low, high):
    while True:
        try:
            input_num = input(prompt).strip()
            if input_num == "":
                print("입력이 비어 있습니다.")
                continue
            input_num = int(input_num)
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if low <= input_num <= high:
            return input_num
        else:
            print(f"{low}에서 {high} 사이의 숫자를 입력하세요.")
```

한 함수로 여러 곳에서 재사용합니다.

```python
choice = input_number("번호를 입력하세요: ", 1, 5)   # 메뉴
user_answer = input_number("정답 입력: ", 1, 4)      # 퀴즈 정답
```

- `while True` 안에서 `return`하면 반복과 함수가 함께 끝납니다.
- 메뉴 코드의 입력 처리 부분을 이 함수 한 줄로 바꿔 두기.

## 10. 클래스와 객체

- **클래스**: 관련된 데이터와 기능을 하나로 묶는 **설계도**
- **객체**: 설계도로 만든 실제 결과물

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 멍멍!")

dog1 = Dog("초코", 3)
dog2 = Dog("콩이", 5)

dog1.bark()                # 초코: 멍멍!
dog1.age = dog1.age + 1
print(dog1.age)            # 4
print(dog2.age)            # 5  ← 객체마다 값을 따로 가짐
```

| 용어 | 의미 |
|---|---|
| `class Dog` | 설계도 정의. 이름은 대문자로 시작 |
| `__init__` | 객체를 만들 때 **자동 실행**되어 처음 값을 채움 (밑줄 앞뒤 2개씩) |
| `self` | 지금 다루는 **바로 그 객체** |
| 속성 | `self.name`처럼 객체에 저장된 값 |
| 메서드 | 클래스 안의 함수. 첫 매개변수는 `self`, 호출할 때는 `self`를 넘기지 않음 |

### `__init__` 이해하기

`__init__`이 없으면 값을 하나씩 직접 넣어야 하고, 빠뜨려도 알 수 없습니다.

```python
dog1 = Dog()
dog1.name = "초코"
dog1.age = 3
```

`Dog("초코", 3)`을 실행하면:

1. 빈 객체를 만든다.
2. `__init__`을 자동 호출: `self` ← 빈 객체, `name` ← `"초코"`, `age` ← `3`
3. `self.name = name` → "이 객체의 name 칸에 초코를 저장"
4. 완성된 객체를 `dog1`에 저장

**`self` 자리에 `dog1`을 넣어 읽으면** 쉽습니다.
비유: 클래스 = 회원 등록 양식, `__init__` = 양식 작성 단계, 객체 = 작성된 회원 카드

### 완성한 `Quiz` 클래스

| 구분 | 이름 | 내용 |
|---|---|---|
| 속성 | `question` | 문제 |
| 속성 | `choices` | 선택지 4개 (리스트) |
| 속성 | `answer` | 정답 번호 (1~4) |
| 메서드 | `show()` | 문제와 선택지를 번호와 함께 출력 |
| 메서드 | `is_correct(user_answer)` | 정답이면 `True`, 아니면 `False` 반환 |
| 메서드 | `to_dict()` | JSON 저장용 딕셔너리로 변환 |
| 메서드 | `from_dict(data)` | 딕셔너리로부터 `Quiz` 객체 생성 |

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 번호로 저장

    def show(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer
```

- 메서드 안에서는 `self.choices`처럼 `self.`을 붙인다.

### `QuizGame` 클래스 구조

게임 전체를 관리합니다.

| 메서드 | 역할 |
|---|---|
| `__init__` | 기본 퀴즈 복사, 메뉴·최고 점수 초기화, `load_state()` 호출 |
| `copy_quizzes(quizzes)` | 원본과 분리된 퀴즈 복사본 생성 |
| `save_state()` / `load_state()` | `state.json` 저장 / 불러오기 |
| `show_menu()` | 메뉴 출력 |
| `play_quiz()` | 퀴즈 출제, 채점, 최고 점수 갱신 |
| `add_quiz()` | 새 퀴즈 입력받아 추가·저장 |
| `show_quizzes()` | 퀴즈 목록 출력 |
| `show_best_score()` | 최고 점수 출력 |
| `run()` | 메뉴 반복, 종료 시 저장 |

- 클래스 2개로 역할을 나눔: `Quiz`는 **퀴즈 1개**, `QuizGame`은 **게임 전체**.

## 11. 프로그램을 완성하며 새로 배운 문법

### `enumerate` — 번호와 값을 함께 꺼내기

```python
for i, quiz in enumerate(self.quizzes, start=1):
    print(f"\n[문제 {i}]")
    quiz.show()
```

- `for i in range(len(...))` + `리스트[i]`를 한 번에 해 줍니다.
- `start=1`이면 번호가 1부터 시작해 `i + 1` 계산이 필요 없습니다.

### `//` — 정수 나눗셈 (소수점 버림)

```python
percent = score * 100 // len(self.quizzes)   # 4 * 100 // 5 → 80
```

- **곱하기를 먼저** 해야 합니다. `4 // 5 * 100`은 `0`이 됩니다.

### `None` — 값이 아직 없음

```python
if self.best_score is None:
    print("아직 퀴즈를 풀지 않았습니다.")
```

- `0점`과 "아직 안 풀었음"을 구분하기 위해 씁니다.
- `None`과 비교할 때는 `==`보다 `is`를 씁니다.

### `A if 조건 else B` — 한 줄짜리 if

```python
score_text = "없음" if best_score is None else f"{best_score}점"
```

아래 4줄과 같은 뜻입니다.

```python
if best_score is None:
    score_text = "없음"
else:
    score_text = f"{best_score}점"
```

### `Path(__file__).parent` — 프로젝트 루트 경로

```python
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json"
```

- `__file__`: 지금 실행 중인 파일(`main.py`)의 경로
- `.parent`: 그 파일이 있는 폴더
- `/ "state.json"`: 경로 이어 붙이기 (나눗셈 아님)
- `"state.json"`만 쓰면 **실행 위치 기준**이라, 다른 폴더에서 실행하면 엉뚱한 곳에 파일이 생깁니다.

### 파일 저장/불러오기 (JSON)

```python
import json

# 저장
with open(self.state_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 불러오기
with open(self.state_file, "r", encoding="utf-8") as file:
    data = json.load(file)
```

| 코드 | 의미 |
|---|---|
| `with open(...) as file` | 파일을 열고, 블록이 끝나면 자동으로 닫음 |
| `"w"` / `"r"` | 쓰기(덮어쓰기) / 읽기 |
| `encoding="utf-8"` | 한글이 깨지지 않게 |
| `json.dump()` / `json.load()` | 파이썬 데이터 → JSON 파일 / JSON 파일 → 파이썬 데이터 |
| `ensure_ascii=False` | 한글을 `\uXXXX`가 아닌 글자 그대로 저장 |
| `indent=4` | 사람이 읽기 좋게 들여쓰기 |

- `Quiz` 객체는 JSON에 바로 저장할 수 없어서 `to_dict()`로 딕셔너리로 바꿔 저장합니다.

### 파일 오류 처리

| 상황 | 잡는 오류 | 처리 |
|---|---|---|
| 파일 없음 | `FileNotFoundError` | 기본 퀴즈로 시작, 파일 생성 |
| JSON 문법이 깨짐 | `json.JSONDecodeError` | 안내 후 기본 퀴즈로 복구 |
| 키 누락·정답 범위 오류 등 | `ValueError` (`raise`로 직접 발생) | 안내 후 기본 퀴즈로 복구 |
| 읽기/쓰기 실패 | `OSError` | 안내 |

### 강제 종료 처리

```python
try:
    value = input(prompt).strip()
except KeyboardInterrupt:   # Ctrl + C
    ...
    return None
except EOFError:            # 입력 스트림 종료
    ...
    return None
```

```python
def run(self):
    try:
        while self.running:
            ...
    finally:
        self.save_state()   # 어떻게 끝나든 반드시 저장
```

- `finally`: 오류가 나든 안 나든 **마지막에 반드시 실행**됩니다.

---

## 미션 구현 로드맵

> 원래 문서 순서와 달리 **저장 기능을 앞당김** — 퀴즈 추가·점수 기능이 저장을 필요로 하기 때문

| 순서 | 할 일 | 상태 |
|---|---|---|
| 1 | 저장소 생성, `.gitignore`·`README.md` | ✅ |
| 2 | 메뉴 + 입력 처리 | ✅ |
| 3 | `Quiz` 클래스 | ✅ |
| 4 | 기본 퀴즈 5개 이상 | ✅ (Python 기초 문법 5문제) |
| 5 | `state.json` 저장/불러오기 | ✅ |
| 6 | 퀴즈 풀기·추가·목록·점수 | ✅ |
| 7 | `QuizGame` 클래스로 정리 | ✅ |
| 8 | Ctrl+C·EOF 안전 종료 | ✅ |
| 9 | 경로 고정, 테스트 코드 정리 (`main`) | ✅ |
| 10 | 퀴즈 풀기 화면 개선 (`feature/play-quiz` 브랜치) | ✅ |
| 11 | 브랜치 `--no-ff` 병합 | ✅ |
| 12 | 스크린샷, README 작성 | ✅ |
| 13 | clone → 수정 → push → 원래 폴더에서 pull | ⏳ |

### 미션 필수 조건 요약

- Python 3.10 이상, 외부 라이브러리 금지(표준 라이브러리는 가능)
- 클래스 2개 이상(`Quiz`, `QuizGame`), 기능별 함수/메서드 분리
- 데이터: 프로젝트 루트 `state.json`, UTF-8
- 파일이 없으면 기본 퀴즈 사용, 깨졌으면 안내 후 기본 퀴즈로 복구
- 커밋 10개 이상, 브랜치 생성·병합 1회 이상
- Git 명령 7종 각 1회 이상: `init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`
- ✅ `best_score`는 **100점 만점 점수**로 결정 (문제 수가 바뀌어도 공정하게 비교), README에 명시

```json
{
    "quizzes": [
        {"question": "...", "choices": ["...", "...", "...", "..."], "answer": 1}
    ],
    "best_score": 80
}
```

### 제출물

1. GitHub 저장소 URL
2. 개발 환경 스크린샷 (VS Code, Python 버전, Git 설정)
3. 실행 스크린샷 (추가, 목록, 풀기, 점수)
4. `git log --oneline --graph` 스크린샷

### 스크린샷 목록 (`docs/screenshots/`)

| 파일 | 내용 | 필수 |
|---|---|---|
| `env.png` | `python --version`, `git --version`, `git config` 결과 | ✅ |
| `menu.png` | 메뉴 화면 | ✅ |
| `play.png` | 퀴즈 풀기 ~ 결과(80점), 새로운 최고 점수 | ✅ |
| `add_quiz.png` | 퀴즈 추가 | ✅ |
| `list.png` | 퀴즈 목록 | ✅ |
| `score.png` | 점수 확인 | ✅ |
| `git_log.png` | `git log --oneline --graph` (**clone/pull 실습 후** 촬영) | ✅ |
| `invalid_input.png`, `reload.png`, `broken_file.png`, `ctrl_c.png` | 예외 처리·데이터 유지 증거 | 선택 |

추천 촬영 순서: `state.json` 삭제 → 실행 → 메뉴 → 4번(아직 안 풀었음) → 1번 풀기 → 2번 추가 → 3번 목록 → 4번 점수
캡처: `Win + Shift + S`

### README 필수 항목

프로젝트 개요 · 퀴즈 주제와 선정 이유 · 실행 방법 · 기능 목록 · 파일 구조 · `state.json` 설명(경로·역할·스키마)

---

## Git 저장소 초기 설정

### 1) 사용자 정보 확인·설정

```bash
git --version
git config --global user.name "내 이름"
git config --global user.email "github가입@이메일.com"
```

이메일은 GitHub 가입 이메일과 같게. 이 화면은 **개발 환경 스크린샷**으로 캡처.

### 2) GitHub에 빈 저장소 생성

- New repository → 이름 입력 → **Public**
- README, .gitignore 등은 **체크하지 않기** (첫 push 충돌 방지)

### 3) `.gitignore`, `README.md` 작성

```text
__pycache__/
*.pyc
.vscode/
```

### 4) 로컬 저장소와 첫 커밋

```bash
git init
git status
git add .gitignore README.md
git commit -m "Chore: 프로젝트 초기 설정"
```

| 명령 | 의미 |
|---|---|
| `git init` | 이 폴더를 Git이 관리하기 시작 (`.git` 폴더 생성) |
| `git status` | 현재 상태 확인 |
| `git add` | 커밋할 파일 고르기 (장바구니에 담기) |
| `git commit` | 고른 파일을 하나의 기록으로 저장 (결제하기) |

### 5) GitHub에 올리기

```bash
git branch -M main
git remote add origin https://github.com/아이디/저장소이름.git
git push -u origin main
```

| 명령 | 의미 |
|---|---|
| `git branch -M main` | 기본 브랜치 이름을 `main`으로 |
| `git remote add origin 주소` | GitHub 저장소를 `origin`으로 연결 |
| `git push -u origin main` | GitHub로 올리기. 다음부터는 `git push`만 써도 됨 |

- 다음 커밋부터는 `git push`만 쓰면 됩니다.
- 커밋 전에는 항상 `git status`로 의도하지 않은 파일이 섞이지 않았는지 확인합니다.

## 브랜치 작업과 병합

### 브랜치란?

`main`의 현재 상태를 복사해 **따로 작업하는 공간**입니다. 브랜치에서 커밋해도 `main`에는 영향이 없고, 작업이 끝나면 `main`에 합칩니다(병합). 기능을 만들다 실패해도 `main`이 안전합니다.

### 진행한 순서

```bash
# 1. 브랜치 만들고 이동
git checkout -b feature/play-quiz
git branch                      # * 표시가 현재 브랜치

# 2. 브랜치에서 기능별로 커밋 (push는 병합 후에)
git add main.py
git commit -m "Feat: 퀴즈 풀기 시작 안내와 문제 번호 표시"
git commit -m "Feat: 퀴즈 결과와 최고 점수를 100점 기준으로 변경"
git commit -m "Feat: 최고 점수 확인에 점수 단위 표시"
git commit -m "Feat: 저장 데이터 불러오기 성공 안내 출력"

# 3. main으로 돌아와 병합
git status                      # working tree clean 확인
git checkout main
git merge --no-ff feature/play-quiz -m "Merge: 퀴즈 풀기 화면 개선 브랜치 병합"

# 4. 확인하고 올리기
git log --oneline --graph
git push
```

| 명령 | 의미 |
|---|---|
| `git checkout -b 이름` | 브랜치를 만들고 이동 (미션 요구로 `switch` 대신 사용) |
| `git checkout main` | `main`으로 이동. 브랜치 변경은 병합 전이라 안 보이는 게 정상 |
| `git merge --no-ff 이름` | 병합 커밋을 따로 만들어 그래프에 **갈래가 보이게** 병합 |
| `git log --oneline --graph` | 커밋 기록을 그래프로 보기. `\|\`에서 갈라지고 `\|/`에서 합쳐짐 |

- `--no-ff` 없이 병합하면 일직선으로 합쳐져 브랜치를 쓴 흔적이 안 보일 수 있습니다.
- 커밋 메시지 형식: `Feat:` 기능 / `Fix:` 버그 수정 / `Refactor:` 구조 정리 / `Docs:` 문서

### 남은 실습: clone과 pull

1. 저장소를 다른 폴더에 `git clone`
2. 복제한 폴더에서 README에 한 줄 추가 → `commit` → `push`
3. 원래 작업 폴더에서 `git pull`로 변경사항 가져오기
4. 반영됐는지 확인 → `git log --oneline --graph` 스크린샷

✅ 사용한 명령: `init`, `add`, `commit`, `push`, `checkout`, `merge` / ⏳ 남은 명령: `clone`, `pull`

---

## 만났던 오류와 해결

**오류 메시지는 맨 아래부터 읽습니다.** 마지막 줄에 오류 이름과 이유, 그 위에 줄 번호가 나옵니다.

| 오류 | 원인 | 해결 |
|---|---|---|
| `TypeError: can only concatenate str (not "int") to str` | 문자열과 숫자를 `+`로 이어 붙임 | f-string 사용: `f"정답은 {answer}번"` |
| `IndexError: list index out of range` | `choices[i + 1]`처럼 리스트에 없는 칸을 꺼냄 | 인덱스는 `choices[i]`, 화면 번호에만 `i + 1` |
| `ValueError: invalid literal for int()` | `int("abc")`처럼 숫자로 못 바꾸는 값 | `try`/`except ValueError` |
| `AttributeError: 'QuizGame' object has no attribute 'copy_quizzes'` | 정의하지 않은 메서드를 호출 (파일이 없거나 깨졌을 때만 실행돼 늦게 발견) | `copy_quizzes` 메서드 추가. `state.json`을 지우고 실행해 보는 테스트가 중요 |
| `IndentationError: unexpected indent` | `def ...:` 뒤에 다음 줄이 붙어 한 줄짜리 함수로 읽힘 | `:` 뒤에서 줄바꿈하고 들여쓰기 맞추기 |
| 1~4를 골라도 문구가 안 나옴 | `print`가 `if` 블록 안(`break` 아래)에 들어감 | 들여쓰기를 `if`와 같은 칸으로 |

## 자주 하는 실수 체크리스트

- [ ] `input()` 결과를 `int()`로 바꿨는가?
- [ ] 비교에 `=`가 아니라 `==`를 썼는가?
- [ ] `if`, `for`, `while` 끝에 콜론 `:`을 붙였는가?
- [ ] 실행할 코드를 들여썼는가?
- [ ] f-string의 `f`를 따옴표 앞에 붙였는가?
- [ ] 리스트 인덱스가 0부터 시작함을 고려했는가?
- [ ] 선택지 데이터에 `"1.부산"`처럼 번호를 넣지 않았는가? (번호는 출력할 때 붙임)
- [ ] `state.json`을 지운 경우, 깨뜨린 경우에도 실행해 봤는가?
- [ ] 커밋 전에 `git status`와 현재 브랜치 이름을 확인했는가?

---

## 개발 환경 메모

### VS Code 단축키

| 동작 | Windows |
|---|---|
| 디버깅 없이 실행 | `Ctrl + F5` |
| 디버깅 모드로 실행 | `F5` |
| 터미널 열기/닫기 | ``Ctrl + ` `` |
| 저장 | `Ctrl + S` |
| 명령 팔레트 | `Ctrl + Shift + P` |

### 터미널 실행

```bash
python main.py      # Windows
py main.py          # Windows (python이 안 될 때)
python3 main.py     # WSL(Ubuntu), macOS
```

- 터미널 위치가 `main.py`가 있는 폴더인지 확인 (아니면 `cd`로 이동)
- 실행 중단: `Ctrl + C`

### WSL 폴더를 VS Code로 열 때

- PowerShell에서 WSL 폴더를 열면 경로가 길어지고 Windows/Ubuntu 도구가 섞일 수 있습니다.
- WSL 확장 설치 → `Ctrl + Shift + P` → `WSL: Reopen Folder in WSL`
- 또는 Ubuntu 터미널에서 `cd ~/okman82/codyssey_E1-2` 후 `code .`
- 경로를 짧게 표시: `echo 'export PROMPT_DIRTRIM=1' >> ~/.bashrc && source ~/.bashrc`

---

## 공부 원칙

- 예제 코드는 복사하지 말고 직접 입력한다.
- 오류가 나면 마지막 줄부터 읽고 원인을 먼저 추측해 본다.
- AI에게 받은 코드는 각 줄을 설명할 수 있을 때만 사용한다.
