# 변수

# score = 0
# print(score)


# score = score + 1
# print(score)



# 자료형

# choices = ["Guido", "Linus", "Bjarne", "James"]
# print(choices[0])        # Guido

# quiz = {"question": "Python의 창시자는?", "answer": 1}
# print(quiz["question"])  # Python의 창시자는?


# answer = input("정답 입력: ")   # 3을 입력하면 "3"
# print(type(answer))            # <class 'str'>

# answer = int(answer)           # 3
# print(type(answer))            # <class 'int'>


# practice.py 파일을 만들고 아래 내용을 코드로 작성해 실행해 보세요.

# 문제를 question 변수에 저장합니다.
# 선택지 4개를 choices 리스트에 저장합니다.
# 정답 번호를 answer 변수에 숫자로 저장합니다.
# 문제와 첫 번째 선택지를 출력합니다.
# input()으로 번호를 받아 int()로 바꾼 뒤, 
# print(user_answer == answer)로 정답 여부를 출력합니다.



# question = "대한민국의 수도는 어디일까요?"
# choices = ["부산", "서울", "대전", "광주"]
# answer = 2

# print(question)
# print(f"1. {choices[0]}")
# print(f"2. {choices[1]}")
# print(f"3. {choices[2]}")
# print(f"4. {choices[3]}")



# user_answer = input("정답 입력: ")
# user_answer = int(user_answer)
# print(user_answer == answer)



# score = 100

# if score >= 90:
#     print("아주 잘했어요!")
# elif score >= 60:
#     print("합격입니다!")
# else:
#     print("다시 도전해 보세요!")
    

# question = "대한민국의 수도는 어디일까요?"
# choices = ["부산", "서울", "대전", "광주"]
# answer = 2

# print(question)
# print(f"1. {choices[0]}")
# print(f"2. {choices[1]}")
# print(f"3. {choices[2]}")
# print(f"4. {choices[3]}")

# user_answer = input("정답 입력: ")
# user_answer = int(user_answer)
# if user_answer == answer:
#     print("정답입니다!")
# else:
#     print(f"오답입니다. 정답은 {answer}번 {choices[answer-1]}입니다.")



# 반복문 for

# for i in range(3):
#     print(i)


# fruts = ["사과", "바나나", "체리"]

# for i in range(3):
#     print(f"{i+1}번 과일 : {fruts[i]}")


# for문 2줄로 같은 결과가 나오게 바꿔 보세요.

# choices = ["부산", "서울", "대전", "광주"]
# for i in range(len(choices)):
#     print(f"{i+1}. {choices[i]}")

# 반복문 while

# count = 1

# while count <= 3:
#     print(f"{count}번째 반복")
#     count = count + 1


# while True와 break

# while True:
#     text = input ("종료하려면 'q'를 입력하세요: ")
#     if text == 'q':
#         break
#     print(f"입력한 값: {text}")

# print("프로그램 종료")

# 직접 해 보기

# 미션의 메뉴를 만들어 보세요.

# 아래 메뉴를 출력합니다.
# text
#    1. 퀴즈 풀기
#    2. 퀴즈 추가
#    3. 퀴즈 목록
#    4. 점수 확인
#    5. 종료
# 번호를 입력받습니다.
# 1~4를 입력하면 퀴즈 풀기를 선택했습니다.
# 처럼 선택한 기능 이름을 출력하고 다시 메뉴로 돌아옵니다.
# 5를 입력하면 프로그램을 종료합니다.를 출력하고 끝납니다.


menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

for i in range(len(menu)):
    print(f"{i+1}. {menu[i]}")

input_num = input("번호를 입력하세요: ")    
input_num = int(input_num)

while input_num != 5:
    if input_num == 1:
        print("퀴즈 풀기를 선택했습니다.")
    elif input_num == 2:
        print("퀴즈 추가를 선택했습니다.")
    elif input_num == 3:
        print("퀴즈 목록을 선택했습니다.")
    elif input_num == 4:
        print("점수 확인을 선택했습니다.")
    else:
        print("잘못된 번호입니다.")

    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    input_num = input("번호를 입력하세요: ")    
    input_num = int(input_num)

print("프로그램을 종료합니다.")    