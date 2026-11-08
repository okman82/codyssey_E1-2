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
| 4 | 클래스와 객체 | 🔄 진행 중 (`Quiz` 클래스 과제) |
| 6 | Git과 GitHub | 🔄 진행 중 (저장소 초기 설정) |
| 5 | 파일과 JSON | ⏳ 예정 |

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

### 📝 현재 과제: `Quiz` 클래스

| 구분 | 이름 | 내용 |
|---|---|---|
| 속성 | `question` | 문제 |
| 속성 | `choices` | 선택지 4개 (리스트) |
| 속성 | `answer` | 정답 번호 (1~4) |
| 메서드 | `display()` | 문제와 선택지를 번호와 함께 출력 |
| 메서드 | `is_correct(user_answer)` | 정답이면 `True`, 아니면 `False` 반환 |

아래 코드가 그대로 동작하면 완성:

```python
quiz = Quiz("대한민국의 수도는 어디일까요?", ["부산", "광주", "서울", "제주"], 3)
quiz.display()

user_answer = input_number("정답 입력: ", 1, 4)
if quiz.is_correct(user_answer):
    print("정답입니다!")
else:
    print(f"오답입니다. 정답은 {quiz.answer}번입니다.")
```

체크 포인트: 메서드 안에서는 `self.choices`처럼 `self.`을 붙인다. 정답(3)과 오답(1)을 모두 확인한다.

---

## 미션 구현 로드맵

> 원래 문서 순서와 달리 **저장 기능을 앞당김** — 퀴즈 추가·점수 기능이 저장을 필요로 하기 때문

| 순서 | 할 일 | 커밋 예시 | 상태 |
|---|---|---|---|
| 1 | 저장소 생성, `.gitignore`·`README.md` | `Chore: 프로젝트 초기 설정` | 🔄 |
| 2 | 메뉴 + 입력 처리 | `Feat: 메뉴 및 입력 검증 구현` | ✅ 연습 완료 |
| 3 | `Quiz` 클래스 | `Feat: Quiz 클래스 구현` | 🔄 |
| 4 | 기본 퀴즈 5개 이상 | `Feat: 기본 퀴즈 데이터 추가` | ⏳ |
| 5 | `state.json` 저장/불러오기 | `Feat: state.json 저장/불러오기` | ⏳ |
| 6 | 퀴즈 풀기 (**별도 브랜치**) | `Feat: 퀴즈 풀기 기능` → main 병합 | ⏳ |
| 7 | 퀴즈 추가 | `Feat: 퀴즈 추가 기능` | ⏳ |
| 8 | 퀴즈 목록 | `Feat: 퀴즈 목록 기능` | ⏳ |
| 9 | 점수 확인·최고 점수 갱신 | `Feat: 최고 점수 기능` | ⏳ |
| 10 | `QuizGame` 클래스로 정리 | `Refactor: QuizGame 구조 정리` | ⏳ |
| 11 | Ctrl+C·EOF 안전 종료 | `Fix: 강제 종료 시 저장 처리` | ⏳ |
| 12 | README 완성 후 최종 push | `Docs: README 작성` | ⏳ |
| 13 | clone → 수정 → push → 원래 폴더에서 pull | `Docs: README 한 줄 추가` | ⏳ |

### 미션 필수 조건 요약

- Python 3.10 이상, 외부 라이브러리 금지(표준 라이브러리는 가능)
- 클래스 2개 이상(`Quiz`, `QuizGame`), 기능별 함수/메서드 분리
- 데이터: 프로젝트 루트 `state.json`, UTF-8
- 파일이 없으면 기본 퀴즈 사용, 깨졌으면 안내 후 기본 퀴즈로 복구
- 커밋 10개 이상, 브랜치 생성·병합 1회 이상
- Git 명령 7종 각 1회 이상: `init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`
- ⚠️ `best_score`를 **점수(80점)** 로 할지 **정답 수(4개)** 로 할지 정해서 README에 적기

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

### README 필수 항목

프로젝트 개요 · 퀴즈 주제와 선정 이유 · 실행 방법 · 기능 목록 · 파일 구조 · `state.json` 설명(경로·역할·스키마)

---

## Git 저장소 초기 설정 (진행 중)

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

✅ 사용한 명령: `init`, `add`, `commit`, `push` / ⏳ 남은 명령: `checkout`, `pull`, `clone`

---

## 만났던 오류와 해결

**오류 메시지는 맨 아래부터 읽습니다.** 마지막 줄에 오류 이름과 이유, 그 위에 줄 번호가 나옵니다.

| 오류 | 원인 | 해결 |
|---|---|---|
| `TypeError: can only concatenate str (not "int") to str` | 문자열과 숫자를 `+`로 이어 붙임 | f-string 사용: `f"정답은 {answer}번"` |
| `IndexError: list index out of range` | `choices[i + 1]`처럼 리스트에 없는 칸을 꺼냄 | 인덱스는 `choices[i]`, 화면 번호에만 `i + 1` |
| `ValueError: invalid literal for int()` | `int("abc")`처럼 숫자로 못 바꾸는 값 | `try`/`except ValueError` |

## 자주 하는 실수 체크리스트

- [ ] `input()` 결과를 `int()`로 바꿨는가?
- [ ] 비교에 `=`가 아니라 `==`를 썼는가?
- [ ] `if`, `for`, `while` 끝에 콜론 `:`을 붙였는가?
- [ ] 실행할 코드를 들여썼는가?
- [ ] f-string의 `f`를 따옴표 앞에 붙였는가?
- [ ] 리스트 인덱스가 0부터 시작함을 고려했는가?
- [ ] 선택지 데이터에 `"1.부산"`처럼 번호를 넣지 않았는가? (번호는 출력할 때 붙임)

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
python3 main.py     # WSL(Ubuntu)
```

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
