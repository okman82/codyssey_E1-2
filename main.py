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


menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

while True:
    print()
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")

    choice = input_number("번호를 입력하세요: ", 1, len(menu))

    if choice == 5 or choice is None:
        print("프로그램을 종료합니다.")
        break

    print(f"{menu[choice - 1]}를 선택했습니다.")