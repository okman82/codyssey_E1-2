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
| 3 | 오류 처리 `try`/`except` | 🔄 진행 중 (연습 과제 남음) |
| 2-6 | 함수 | ⏳ 예정 |
| 4 | 클래스와 객체 | ⏳ 예정 |
| 5 | 파일과 JSON | ⏳ 예정 |
| 6 | Git과 GitHub | ⏳ 예정 |

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

## 8. 오류 처리 `try`/`except` (진행 중)

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
- `text.strip()`: 문자열 앞뒤 공백 제거

### 📝 남은 연습 과제

메뉴 코드의 입력 부분을 고쳐서 아래를 모두 처리하기

| 입력 | 결과 |
|---|---|
| ` 1 ` (앞뒤 공백) | 퀴즈 풀기를 선택했습니다. |
| `abc` | `숫자만 입력하세요.` 출력 후 메뉴로 |
| 그냥 Enter | `입력이 비어 있습니다.` 출력 후 메뉴로 |
| `9` | `잘못된 번호입니다.` 출력 후 메뉴로 |

힌트: `strip()` → 빈 문자열 확인 → `try`로 숫자 변환 → 둘 다 `continue`

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
