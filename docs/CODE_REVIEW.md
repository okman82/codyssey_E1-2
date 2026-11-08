# 🔍 코드 리뷰 — `main.py`

> 이 문서는 `main.py`의 주요 코드를 **"왜 이렇게 썼는가"** 중심으로 설명합니다.
> 각 항목은 **일반적인(처음 배울 때 흔히 쓰는) 방식**과 **이 프로젝트의 방식**을 비교하고, 더 다듬을 수 있는 부분도 함께 적었습니다.

## 한눈에 보기

| 구분 | 내용 |
|---|---|
| 👍 잘한 점 | 입력 검사를 함수 하나로 재사용 · 클래스 2개로 역할 분리 · 저장 파일 내용까지 검증 · `finally`로 종료 시 항상 저장 · 실행 위치와 무관한 파일 경로 |
| 🐞 발견한 버그 | ① `state.json`이 `[]`처럼 **리스트**면 프로그램이 멈춤 ② 정답이 `true`여도 **통과**함 (3장) |
| 🔧 다듬을 점 | 입력 함수 2개의 중복 코드 · `save_state` 들여쓰기 · `if __name__ == "__main__":` 없음 |

### 프로그램 구조

```text
main.py
├─ STATE_FILE                    저장 파일 경로 (프로젝트 루트 고정)
├─ input_number(prompt, low, high)   범위 안의 숫자를 받을 때까지 반복
├─ input_text(prompt)                빈칸이 아닌 글자를 받을 때까지 반복
├─ class Quiz                    퀴즈 카드 1장 (문제·보기·정답, 채점, JSON 변환)
├─ class QuizGame                게임 진행자 (메뉴, 풀기·추가·목록·점수, 저장·불러오기)
└─ default_quizzes → QuizGame(...).run()   실행 시작
```

---

## 1. 파일 경로 — `Path(__file__).parent`

```python
STATE_FILE = Path(__file__).parent / "state.json"
```

**일반적인 방식**

```python
open("state.json", "w")
```

**왜 이렇게 썼나**
- `"state.json"`만 쓰면 **터미널의 현재 위치** 기준으로 파일을 찾습니다. 상위 폴더에서 `python codyssey_E1-2/main.py`로 실행하면 엉뚱한 곳에 새 파일이 생기고, 저장한 퀴즈가 "사라진 것처럼" 보입니다.
- `__file__`(이 파일의 경로) → `.parent`(그 폴더)를 기준으로 삼아, 어디서 실행해도 미션 조건인 **프로젝트 루트의 `state.json`**을 씁니다.
- `/`는 나눗셈이 아니라 `pathlib`의 **경로 연결** 연산자입니다. `os.path.join(...)`보다 짧고, Windows(`\`)와 macOS/Linux(`/`)의 구분자 차이도 알아서 처리합니다.

**대문자 이름(`STATE_FILE`)**: 바뀌지 않는 값(상수)이라는 Python의 관례 표시입니다.

---

## 2. 공통 입력 함수 — `input_number`

```python
def input_number(prompt, low, high):
    while True:
        try:
            value = input(prompt).strip()
        except KeyboardInterrupt:
            ...
            return None
        except EOFError:
            ...
            return None

        if value == "":
            print("입력이 비어 있습니다.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if low <= number <= high:
            return number

        print(f"{low}에서 {high} 사이의 숫자를 입력하세요.")
```

### 2-1. 함수 하나로 재사용

**일반적인 방식**: 메뉴, 정답 입력, 퀴즈 추가 등 **필요한 곳마다** `try/except`를 복사해 씁니다. 한 곳을 고치면 나머지도 다 고쳐야 하고, 하나를 빠뜨리면 그곳만 오류가 납니다.

**이 프로젝트**: 범위를 매개변수(`low`, `high`)로 받아 한 함수로 모든 숫자 입력을 처리합니다.

```python
choice = input_number("번호를 입력하세요: ", 1, len(self.menu))   # 메뉴 1~5
answer = input_number("정답 번호를 입력하세요: ", 1, 4)            # 정답 1~4
```

메뉴를 6개로 늘려도 `len(self.menu)` 덕분에 이 줄은 고칠 필요가 없습니다.

### 2-2. `while True` + `return` (상태 변수 없이 반복)

**일반적인 방식**: "올바른 값이 들어왔는가"를 저장하는 변수를 둡니다.

```python
valid = False
while not valid:
    value = input(prompt)
    if value.isdigit():
        valid = True
return int(value)
```

**이 프로젝트**: 올바른 값이면 그 자리에서 `return` → **반복과 함수가 동시에 끝납니다.** 잘못된 값이면 `continue`로 처음으로 돌아갑니다. 상태 변수(`valid`)가 필요 없어 흐름이 위에서 아래로 그대로 읽힙니다.

### 2-3. `try`를 두 개로 나눈 이유

**일반적인 방식**: 큰 `try` 하나로 전부 감쌉니다.

```python
try:
    number = int(input(prompt))
except ValueError:
    ...
```

**이 프로젝트**: ① 입력 받기(`Ctrl+C`·EOF 가능) ② 숫자 변환(`ValueError` 가능)을 **따로** 감쌌습니다.
- `try`는 **오류가 날 수 있는 줄만** 좁게 감싸야 어떤 오류를 잡는지 분명합니다.
- 넓게 감싸면 다른 줄의 예상치 못한 오류까지 "숫자만 입력하세요"로 덮어 버려 버그를 찾기 어려워집니다.

### 2-4. `int()` vs `isdigit()`

`value.isdigit()`로 미리 검사하는 방식도 많이 씁니다. 하지만 `isdigit()`은 `-1`을 `False`로, `²` 같은 특수 숫자 문자를 `True`로 판단하는 등 예외가 있습니다. **"일단 바꿔 보고, 실패하면 처리"**(`try int()`)하는 방식이 Python에서 더 일반적인 관례(EAFP)이고 정확합니다.

### 2-5. 강제 종료 시 `None`을 돌려주는 이유

입력 함수는 "게임을 끝낼 권한"이 없습니다. 그래서 **`None`이라는 신호**만 돌려주고, 호출한 쪽(`QuizGame`)이 `self.running = False`로 게임을 끝냅니다. 입력 처리와 게임 진행의 **책임을 나눈 것**입니다.


---

## 3. `Quiz` 클래스

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 번호로 저장
```

### 3-1. 딕셔너리 대신 클래스를 쓴 이유

**일반적인 방식**: 퀴즈를 딕셔너리로 다룹니다.

```python
quiz = {"question": "...", "choices": [...], "answer": 3}
if user_answer == quiz["answer"]: ...
```

**이 프로젝트**: 데이터(문제·보기·정답)와 **그 데이터로 하는 일**(출력 `show`, 채점 `is_correct`)을 한 곳에 묶었습니다.
- 채점 규칙이 바뀌어도(예: 부분 점수) `is_correct`만 고치면 됩니다.
- `quiz["anwser"]` 같은 오타는 실행해 봐야 알지만, 메서드 이름 오타는 편집기가 바로 알려 줍니다.

### 3-2. 정답을 1~4로 저장한 이유

리스트 인덱스는 0부터 시작하지만 사용자는 1부터 입력합니다. 정답을 **사람 기준 번호**로 저장하면 `user_answer == self.answer`로 바로 비교되어 `- 1` 계산이 필요 없습니다. 미션 문서도 이 방식을 권장합니다.

### 3-3. `is_correct`가 `True`/`False`를 그대로 반환

**일반적인 방식**

```python
def is_correct(self, user_answer):
    if user_answer == self.answer:
        return True
    else:
        return False
```

**이 프로젝트**: `==` 비교의 결과가 이미 `True`/`False`이므로 그대로 돌려줍니다. **4줄 → 1줄.**

```python
return user_answer == self.answer
```

### 3-4. `to_dict` / `from_dict` — JSON과 객체 사이의 통역

`json` 모듈은 `Quiz` 객체를 저장하는 방법을 모릅니다(`TypeError: Object of type Quiz is not JSON serializable`). 그래서
- 저장할 때: `Quiz` → 딕셔너리 (`to_dict`)
- 불러올 때: 딕셔너리 → `Quiz` (`from_dict`)

로 바꿔 주는 메서드를 두었습니다. 변환 규칙이 클래스 안에 있어서 속성이 늘어나도(예: 힌트) 이 두 곳만 고치면 됩니다.

**`@classmethod`를 쓴 이유**: `from_dict`는 **아직 객체가 없을 때** 객체를 만드는 메서드라서 `self`가 아니라 클래스 자체(`cls`)를 받습니다. `Quiz.from_dict(item)`처럼 클래스 이름으로 호출합니다. "딕셔너리에서 만들기"라는 의도가 이름에 드러나는 것이 장점입니다.


---

## 4. 반복문 — `enumerate`

```python
for i, choice in enumerate(self.choices, start=1):
    print(f"{i}. {choice}")
```

**일반적인 방식**

```python
for i in range(len(self.choices)):
    print(f"{i + 1}. {self.choices[i]}")
```

**이 프로젝트**: `enumerate`가 **번호와 값을 함께** 꺼내 줍니다.
- `self.choices[i]`로 다시 꺼낼 필요가 없습니다.
- `start=1`로 1부터 세므로 `i + 1` 계산이 사라집니다.
- 실제로 개발 중 `choices[i + 1]`로 써서 `IndexError`가 났던 실수를 구조적으로 막아 줍니다.

메뉴 출력(`show_menu`), 퀴즈 목록(`show_quizzes`), 문제 번호(`play_quiz`)에서 같은 패턴을 일관되게 썼습니다.

---

## 5. 리스트 컴프리헨션

```python
"quizzes": [quiz.to_dict() for quiz in self.quizzes]
```

**일반적인 방식**

```python
quizzes = []
for quiz in self.quizzes:
    quizzes.append(quiz.to_dict())
```

**이 프로젝트**: "모든 퀴즈를 딕셔너리로 바꾼 리스트"를 **한 줄**로 표현합니다. 빈 리스트 만들기 → 반복 → `append` 세 단계가 하나로 줄고, 결과가 무엇인지 바로 읽힙니다.

조건 검사나 `print`가 섞이는 복잡한 반복(예: `add_quiz`의 선택지 입력)은 일반 `for`문으로 썼습니다. **단순 변환만 컴프리헨션**으로 쓰는 것이 읽기 좋은 기준입니다.

---

## 6. 기본 퀴즈 복사 — `copy_quizzes`

```python
def copy_quizzes(self, quizzes):
    return [Quiz(q.question, list(q.choices), q.answer) for q in quizzes]
```

**일반적인 방식**

```python
self.quizzes = default_quizzes
```

**왜 복사했나**: Python에서 `=`는 리스트를 **복사하지 않고 같은 리스트에 이름만 하나 더** 붙입니다.

```python
a = [1, 2]
b = a
b.append(3)
print(a)   # [1, 2, 3]  ← a도 바뀜!
```

그대로 쓰면 퀴즈를 추가할 때 **기본 퀴즈 원본까지** 바뀌고, 나중에 손상된 파일을 "기본 퀴즈로 복구"할 때 원래 5개가 아닌 바뀐 목록으로 복구됩니다.

- 리스트만 새로 만들면(`list(quizzes)`) 안의 `Quiz` 객체는 여전히 공유됩니다.
- 그래서 `Quiz` 객체와 선택지 리스트(`list(q.choices)`)까지 **새로** 만들었습니다(깊은 복사).

**더 짧게 쓰는 방법**: 표준 라이브러리의 `copy.deepcopy`가 같은 일을 합니다.

```python
import copy
self.quizzes = copy.deepcopy(default_quizzes)
```

직접 만든 방식은 **무엇을 복사하는지 코드로 보여 준다**는 장점이 있습니다.

---

## 7. 저장 — `save_state`

```python
with open(self.state_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
```

### 7-1. `with`문

**일반적인 방식**

```python
file = open("state.json", "w")
json.dump(data, file)
file.close()
```

`dump`에서 오류가 나면 `close()`가 실행되지 않아 파일이 열린 채로 남을 수 있습니다. `with`는 블록이 **어떻게 끝나든 자동으로 파일을 닫습니다.**

### 7-2. 옵션

| 옵션 | 없으면 | 있으면 |
|---|---|---|
| `encoding="utf-8"` | Windows는 기본 인코딩이 달라 한글이 깨질 수 있음 | 어디서나 같은 결과 (미션 요구사항) |
| `ensure_ascii=False` | `"파이썬"`처럼 저장 | `"파이썬"` 그대로 저장 |
| `indent=4` | 한 줄로 길게 저장 | 사람이 읽고 고치기 쉬운 형태 |

### 🔧 다듬을 점: 들여쓰기

`save_state`의 본문만 **8칸**으로 들여쓰여 있습니다(다른 메서드는 4칸). 동작에는 문제가 없지만 일관성을 위해 4칸으로 맞추세요. VS Code에서 해당 줄을 선택하고 `Shift + Tab`을 한 번 누르면 됩니다.

---

## 8. 불러오기 — `load_state`

### 8-1. `data.get("quizzes")` vs `data["quizzes"]`

`data["quizzes"]`는 키가 없으면 `KeyError`로 멈춥니다. `.get()`은 키가 없으면 `None`을 돌려주므로, 바로 다음 줄의 `isinstance` 검사에서 "형식 오류"로 함께 처리할 수 있습니다.

### 8-2. 내용까지 검사하는 이유

`json.load`는 **문법**만 확인합니다. 아래 파일은 문법상 완벽하지만 게임을 망가뜨립니다.

```json
{"quizzes": [{"question": "Q", "choices": ["A", "B"], "answer": 9}], "best_score": 80}
```

보기가 2개뿐이고 정답이 9번이라 영원히 맞힐 수 없습니다. 그래서 `isinstance()`로 **자료형**과 **범위**까지 검사합니다.

### 8-3. 문제를 모두 `ValueError`로 모은 이유

검사에 실패하면 직접 `raise ValueError(...)`를 일으킵니다. 그러면 "JSON 문법 오류"와 "내용 오류"를 **같은 `except` 한 곳**에서 처리할 수 있습니다.

```python
except (json.JSONDecodeError, ValueError, OSError):
    # 안내 후 기본 퀴즈로 복구
```

**일반적인 방식**은 검사마다 `if ...: print(...); 복구 코드` 를 반복하는 것인데, 복구 코드가 5번 넘게 반복됩니다.

### 8-4. `except` 순서

`FileNotFoundError`는 `OSError`의 **하위 종류**입니다. 순서를 반대로 쓰면 `OSError`가 먼저 잡아 버려 "파일이 없음"과 "손상됨"을 구분하지 못합니다. **구체적인 예외를 먼저** 쓰는 것이 규칙이고, 이 코드는 그 순서를 지켰습니다.

### 8-5. 검증된 데이터만 반영

검사 중에는 `loaded_quizzes`라는 **임시 리스트**에 담고, 모두 통과한 뒤에야 `self.quizzes`에 넣습니다. 중간에 실패해도 게임 데이터가 반쯤 바뀐 상태로 남지 않습니다.

---

## 9. 퀴즈 풀기 — 점수 계산

```python
percent = score * 100 // len(self.quizzes)
```

**일반적인 방식**

```python
percent = int(score / len(self.quizzes) * 100)
# 또는
percent = round(score / len(self.quizzes) * 100)
```

**이 프로젝트**: 정수 나눗셈 `//` 한 번으로 소수점을 버립니다.
- **곱하기를 먼저** 해야 합니다. `4 // 5 * 100`은 `4 // 5 = 0`이 되어 0점이 됩니다.
- `/`는 항상 실수(`0.8`)를 만들어 `int()` 변환이 한 번 더 필요하지만, `//`는 정수끼리 계산해 바로 정수가 나옵니다.
- 4/6 = 66.6…은 `//`면 66점, `round`면 67점입니다. 이 프로젝트는 "버림"을 택했고 README에 명시했습니다.

**왜 정답 개수가 아니라 점수인가**: 퀴즈를 추가하면 문제 수가 바뀝니다. "4개 정답"은 5문제(80점)와 6문제(66점)에서 의미가 다르므로, 100점 기준으로 바꿔야 최고 점수 비교가 공정합니다.

### `best_score = None`

처음부터 `0`으로 두면 "0점을 받았다"와 "아직 안 풀었다"를 구분할 수 없습니다. `None`으로 "값이 없음"을 표현하고, `is None`으로 검사합니다(`None` 비교는 `==`보다 `is`가 관례).

---

## 10. 실행 루프 — `run`

```python
def run(self):
    try:
        while self.running:
            ...
    finally:
        self.save_state()
```

### 10-1. `try / finally`

`finally`는 **정상 종료(메뉴 5), 강제 종료, 예상하지 못한 오류** 중 어느 경우든 마지막에 반드시 실행됩니다. 종료 경로마다 `save_state()`를 따로 적지 않아도 저장이 보장됩니다.

### 10-2. `self.running` 깃발

`break`는 **자기가 속한 반복문**만 빠져나올 수 있습니다. `play_quiz` 안에서 `Ctrl+C`가 눌리면 `run`의 `while`을 직접 멈출 방법이 없어서, 객체 속성 `self.running`을 `False`로 바꿔 "게임 종료"를 알립니다. 어느 메서드에서든 게임을 끝낼 수 있는 **공용 스위치**입니다.

---

## 11. 실행 시작부 — `if __name__ == "__main__":`

```python
game = QuizGame(default_quizzes)   # 현재: 파일 맨 아래에서 바로 실행
game.run()
```

**일반적인(권장) 방식**

```python
if __name__ == "__main__":
    game = QuizGame(default_quizzes)
    game.run()
```

`python main.py`로 **직접 실행할 때만** 게임이 시작되고, 다른 파일에서 `from main import Quiz`로 가져다 쓸 때(예: 테스트 코드)는 게임이 실행되지 않습니다. 지금 구조에서는 `import main`만 해도 게임이 시작됩니다.

---

## 12. 발견한 버그와 수정 방법

직접 실행해 확인한 문제입니다.

### 🐞 ① `state.json` 최상위가 리스트면 프로그램이 멈춤

```json
[]
```

이 파일은 **JSON 문법상 올바르기 때문에** `JSONDecodeError`가 나지 않고, 리스트에는 `.get()`이 없어 다음 오류로 프로그램이 종료됩니다.

```text
AttributeError: 'list' object has no attribute 'get'
```

미션 요구사항("파일이 손상되어도 실행 가능")에 걸리는 부분이라 **수정을 권장**합니다. `json.load` 바로 다음에 한 줄을 추가하세요.

```python
            data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("최상위 형식 오류")
```

### 🐞 ② 정답이 `true`여도 통과함

Python에서 `bool`은 `int`의 하위 종류라서 `isinstance(True, int)`가 `True`입니다. `"answer": true`인 파일을 불러오면 정답이 1번으로 처리됩니다. `best_score`도 같습니다.

```python
if type(answer) is not int or not (1 <= answer <= 4):
```

`type(...) is int`는 `bool`을 제외하고 **정확히 정수만** 허용합니다. 같은 이유로 `choices` 안의 값이 모두 문자열인지도 검사하면 더 안전합니다.

```python
if not isinstance(choices, list) or len(choices) != 4 \
        or not all(isinstance(c, str) for c in choices):
```

### 수정 후 확인 방법

`state.json`을 아래 내용으로 바꾸고 실행해 각각 "손상되었거나 읽을 수 없어 기본 퀴즈로 복구합니다"가 나오는지 확인합니다.

| 넣을 내용 | 기대 결과 |
|---|---|
| `[]` | 복구 안내 |
| `{"quizzes": [{"question": "Q", "choices": ["a","b","c","d"], "answer": true}], "best_score": null}` | 복구 안내 |
| `{"quizzes": "abc", "best_score": 80}` | 복구 안내 (이미 동작) |

---

## 13. 평가에서 받을 수 있는 질문

| 질문 | 답변 요지 |
|---|---|
| 클래스를 왜 2개로 나눴나요? | 퀴즈 1개를 다루는 일(`Quiz`)과 게임 전체를 다루는 일(`QuizGame`)의 책임을 분리. 퀴즈 형식이 바뀌면 `Quiz`만, 메뉴가 바뀌면 `QuizGame`만 고치면 됨 |
| `self`는 무엇인가요? | 메서드를 호출한 **그 객체 자신**. `quiz.show()`를 호출하면 `self`가 `quiz` |
| JSON을 왜 썼나요? | 사람도 읽을 수 있는 텍스트 형식이고, Python의 `dict`/`list`와 구조가 같아 표준 라이브러리 `json`으로 바로 변환 가능 |
| `state.json`이 깨지면 어떻게 되나요? | 문법 오류는 `JSONDecodeError`, 내용 오류는 직접 `raise ValueError` → 같은 곳에서 잡아 기본 퀴즈로 복구 |
| `Ctrl+C`를 누르면? | 입력 함수가 `KeyboardInterrupt`를 잡아 `None` 반환 → `running=False` → `finally`에서 저장 후 종료 |
| 기본 퀴즈를 왜 복사하나요? | `=`는 같은 리스트를 공유하므로, 복사하지 않으면 퀴즈 추가 시 원본 기본 퀴즈까지 바뀜 |
| 점수를 왜 100점 기준으로? | 퀴즈 추가로 문제 수가 바뀌어도 공정하게 비교하기 위해 |
| `--no-ff`로 병합한 이유는? | 병합 커밋을 남겨 `git log --graph`에 브랜치 작업 흔적이 보이도록 |

---

## 수정 우선순위

| 순위 | 항목 | 이유 |
|---|---|---|
| 1 | 🐞 ① 최상위 리스트 검사 | 미션 요구사항(손상 파일 처리) 위반 |
| 2 | 🐞 ② `bool` 정답 검사 | 잘못된 데이터가 통과 |
| 3 | `if __name__ == "__main__":` | 파이썬 표준 관례, 한 줄 추가 |
| 4 | `save_state` 들여쓰기 | 일관성 |
| 5 | 입력 함수 중복 제거 | 선택 (설명할 수 있을 때만) |

권장 커밋 메시지 예시

```bash
git commit -m "Fix: 최상위가 객체가 아닌 state.json을 손상 파일로 처리"
git commit -m "Fix: 정답·점수의 bool 값을 형식 오류로 처리"
git commit -m "Refactor: 실행부를 __main__ 블록으로 이동"
git commit -m "Docs: 코드 리뷰 문서 추가"
```
