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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["answer"])

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = None
        self.menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]
        self.running = True

    def show_menu(self):
        print()
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item}")

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = input_number("정답 번호를 입력하세요: ", 1, 4)

            if answer is None:
                self.running = False
                return

            if quiz.is_correct(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n퀴즈 종료! 점수: {score}/{len(self.quizzes)}")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

    def add_quiz(self):
        print("\n새 퀴즈를 추가합니다.")

        question = input_text("문제를 입력하세요: ")
        if question is None:
            self.running = False
            return

        choices = []
        for i in range(4):
            choice = input_text(f"{i + 1}번 선택지를 입력하세요: ")
            if choice is None:
                self.running = False
                return
            choices.append(choice)

        answer = input_number("정답 번호를 입력하세요 (1~4): ", 1, 4)
        if answer is None:
            self.running = False
            return

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n퀴즈 목록")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"현재 최고 점수: {self.best_score}")

    def run(self):
        while self.running:
            self.show_menu()
            choice = input_number("번호를 입력하세요: ", 1, len(self.menu))

            if choice is None:
                self.running = False
                break

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                print("프로그램을 종료합니다.")
                self.running = False

                
# menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

default_quizzes = [
    Quiz("Python에서 리스트를 만드는 기호는?", ["()", "{}", "[]", "<>"], 3),
    Quiz("문자열 길이를 구하는 함수는?", ["size()", "len()", "count()", "length()"], 2),
    Quiz("반복문에 해당하는 것은?", ["if", "def", "for", "class"], 3),
    Quiz("함수를 정의할 때 사용하는 키워드는?", ["func", "define", "def", "lambda"], 3),
    Quiz("조건이 참일 때 실행되는 문장은?", ["if", "for", "while", "import"], 1),
]


# quiz = default_quizzes[0]
# quiz.show()

# answer = input_number("정답 번호를 입력하세요: ", 1, 4)

# if answer is None:
#     print("프로그램을 종료합니다.")
# elif quiz.is_correct(answer):
#     print("정답입니다!")
# else:
#     print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

game = QuizGame(default_quizzes)
game.run()