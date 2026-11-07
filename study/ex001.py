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



question = "대한민국의 수도는 어디일까요?"
choices = ["부산", "서울", "대전", "광주"]
answer = 2

print(question)
print(f"1. {choices[0]}")
print(f"2. {choices[1]}")
print(f"3. {choices[2]}")
print(f"4. {choices[3]}")



user_answer = input("정답 입력: ")
user_answer = int(user_answer)
print(user_answer == answer)



