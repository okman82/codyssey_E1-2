def input_number(prompt, low, high):
    while True:
        try:
            value = input(prompt).strip()
        except KeyboardInterrupt:
            print("\n입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
            return None
        except EOFError:
            print("\n입력 스트림이 종료되었습니다. 프로그램을 안전하게 종료합니다.")
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

def input_text(prompt):
    while True:
        try:
            value = input(prompt).strip()
        except KeyboardInterrupt:   
            print("\n입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
            return None
        except EOFError:
            print("\n입력 스트림이 종료되었습니다. 프로그램을 안전하게 종료합니다.")
            return None

        if value == "":
            print("입력이 비어 있습니다.")
            continue

        return value


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 번호로 저장

    def show(self):
        print(f"\n문제: {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

default_quizzes = [
    Quiz("Python에서 리스트를 만드는 기호는?", ["()", "{}", "[]", "<>"], 3),
    Quiz("문자열 길이를 구하는 함수는?", ["size()", "len()", "count()", "length()"], 2),
    Quiz("반복문에 해당하는 것은?", ["if", "def", "for", "class"], 3),
    Quiz("함수를 정의할 때 사용하는 키워드는?", ["func", "define", "def", "lambda"], 3),
    Quiz("조건이 참일 때 실행되는 문장은?", ["if", "for", "while", "import"], 1),
]


quiz = default_quizzes[0]
quiz.show()

answer = input_number("정답 번호를 입력하세요: ", 1, 4)

if answer is None:
    print("프로그램을 종료합니다.")
elif quiz.is_correct(answer):
    print("정답입니다!")
else:
    print(f"오답입니다. 정답은 {quiz.answer}번입니다.")