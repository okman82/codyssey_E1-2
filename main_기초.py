import json
import os

# 파일 저장 경로를 단순한 문자열로 지정합니다.
STATE_FILE = "state.json"

# 기본 퀴즈 데이터 (딕셔너리와 리스트 활용)
default_quizzes = [
    {"question": "Python에서 리스트를 만드는 기호는?", "choices": ["()", "{}", "[]", "<>"], "answer": 3},
    {"question": "문자열 길이를 구하는 함수는?", "choices": ["size()", "len()", "count()", "length()"], "answer": 2},
    {"question": "반복문에 해당하는 것은?", "choices": ["if", "def", "for", "class"], "answer": 3},
    {"question": "함수를 정의할 때 사용하는 키워드는?", "choices": ["func", "define", "def", "lambda"], "answer": 3},
    {"question": "조건이 참일 때 실행되는 문장은?", "choices": ["if", "for", "while", "import"], "answer": 1},
]

def load_data():
    """저장된 퀴즈 데이터를 불러오는 함수입니다."""
    # 파일이 존재하는지 확인하고 불러옵니다.
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                print("저장된 데이터를 불러왔습니다.")
                return data
        except:
            print("파일을 읽는 중 오류가 발생해 기본 데이터로 시작합니다.")
            
    # 파일이 없거나 오류가 나면 기본 데이터를 반환합니다.
    return {"quizzes": default_quizzes.copy(), "best_score": 0}

def save_data(data):
    """현재 퀴즈 데이터를 파일에 저장하는 함수입니다."""
    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def input_number(prompt, low, high):
    """지정된 범위 내의 숫자를 안전하게 입력받는 함수입니다."""
    while True:
        try:
            number = int(input(prompt))
            if low <= number <= high:
                return number
            else:
                print(f"{low}에서 {high} 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자만 입력하세요.")

def play_quiz(data):
    """퀴즈를 푸는 기능을 담당하는 함수입니다."""
    quizzes = data["quizzes"]
    
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return

    score = 0
    print(f"\n퀴즈를 시작합니다! (총 {len(quizzes)}문제)")

    for i, quiz in enumerate(quizzes, start=1):
        print(f"\n[문제 {i}] {quiz['question']}")
        
        # 선택지 출력
        for j, choice in enumerate(quiz['choices'], start=1):
            print(f"{j}. {choice}")

        # 정답 입력받기
        answer = input_number("정답 번호를 입력하세요: ", 1, 4)

        if answer == quiz['answer']:
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz['answer']}번입니다.")

    # 점수 계산 및 최고 점수 갱신
    percent = score * 100 // len(quizzes)
    print(f"\n결과: {len(quizzes)}문제 중 {score}문제 정답! ({percent}점)")

    if percent > data["best_score"]:
        print("새로운 최고 점수입니다!")
        data["best_score"] = percent
        save_data(data) # 점수가 갱신되었으니 저장합니다.

def add_quiz(data):
    """새로운 퀴즈를 추가하는 함수입니다."""
    print("\n새 퀴즈를 추가합니다.")
    question = input("문제를 입력하세요: ")
    
    choices = []
    for i in range(1, 5):
        choice = input(f"{i}번 선택지를 입력하세요: ")
        choices.append(choice)

    answer = input_number("정답 번호를 입력하세요 (1~4): ", 1, 4)

    # 새로운 퀴즈를 딕셔너리 형태로 리스트에 추가합니다.
    new_quiz = {
        "question": question,
        "choices": choices,
        "answer": answer
    }
    data["quizzes"].append(new_quiz)
    save_data(data) # 퀴즈가 추가되었으니 저장합니다.
    print("퀴즈가 추가되었습니다.")

def show_quizzes(data):
    """등록된 퀴즈 목록을 보여주는 함수입니다."""
    quizzes = data["quizzes"]
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return

    print("\n퀴즈 목록")
    for i, quiz in enumerate(quizzes, start=1):
        print(f"{i}. {quiz['question']}")

def main():
    """프로그램의 메인 흐름을 담당하는 함수입니다."""
    data = load_data()
    
    while True:
        print("\n1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        
        choice = input_number("번호를 입력하세요: ", 1, 5)

        if choice == 1:
            play_quiz(data)
        elif choice == 2:
            add_quiz(data)
        elif choice == 3:
            show_quizzes(data)
        elif choice == 4:
            print(f"\n현재 최고 점수: {data['best_score']}점")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break

# 이 파일이 직접 실행될 때만 main() 함수를 호출합니다.
if __name__ == "__main__":
    main()