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


# menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]

# for i in range(len(menu)):
#     print(f"{i+1}. {menu[i]}")

# input_num = input("번호를 입력하세요: ")    
# input_num = int(input_num)

# while input_num != 5:
#     if input_num == 1:
#         print("퀴즈 풀기를 선택했습니다.")
#     elif input_num == 2:
#         print("퀴즈 추가를 선택했습니다.")
#     elif input_num == 3:
#         print("퀴즈 목록을 선택했습니다.")
#     elif input_num == 4:
#         print("점수 확인을 선택했습니다.")
#     else:
#         print("잘못된 번호입니다.")

#     for i in range(len(menu)):
#         print(f"{i+1}. {menu[i]}")

#     input_num = input("번호를 입력하세요: ")    
#     input_num = int(input_num)

# print("프로그램을 종료합니다.")    


# 빠진 부분 하나
# 5를 입력하면 반복은 끝나지만 프로그램을 종료합니다.가 출력되지 않습니다. 반복문이 끝난 뒤, 들여쓰기 없이 맨 아래에 print를 추가하세요.

# 더 좋게 만들 부분: 중복 코드
# 메뉴 출력과 입력 코드가 반복문 위와 안쪽에 두 번 있습니다. 나중에 메뉴 문구나 입력 방식을 바꿀 때 두 곳을 모두 고쳐야 하고, 한 곳을 빠뜨리면 버그가 생깁니다.

# 앞에서 배운 while True와 break를 쓰면 한 번만 쓸 수 있습니다. 구조는 이렇습니다.

# python
# while True:
#     # 1. 메뉴 출력
#     # 2. 번호 입력
#     # 3. 5면 종료 문구 출력 후 break
#     # 4. 1~4면 선택한 기능 출력
#     # 5. 나머지는 잘못된 번호 안내
# 직접 해 보기

# 위 구조대로 코드를 고쳐 보세요. 메뉴 출력과 입력 코드가 한 번씩만 나오면 성공입니다.

# 도전 과제(선택): 1~4번의 if/elif 4개를 줄일 수도 있습니다. 메뉴 이름이 이미 menu 리스트에 있으니, 입력한 번호로 리스트에서 이름을 꺼내 f-string에 넣으면 됩니다. 번호와 인덱스의 차이에 주의하세요.





# menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]


# while True:

#     for i in range(len(menu)):
#         print(f"{i+1}. {menu[i]}")

#     input_num = input("번호를 입력하세요: ")    
#     input_num = int(input_num)


#     if input_num == 1:
#         print("퀴즈 풀기를 선택했습니다.")
#     elif input_num == 2:
#         print("퀴즈 추가를 선택했습니다.")
#     elif input_num == 3:
#         print("퀴즈 목록을 선택했습니다.")
#     elif input_num == 4:
#         print("점수 확인을 선택했습니다.")
#     elif input_num == 5:
#         print("프로그램을 종료합니다.")
#         break         
#     else:
#         print("잘못된 번호입니다.")


# 오류 처리 try/except

# try:
#     num = int(input("숫자를 입력하세요: "))
#     print(f"입력한 숫자는 {num}입니다.")    
# except ValueError:
#     print("올바른 숫자를 입력하세요.")


# text = "     1      "
# print(text.strip())  # 1


# 직접 해 보기

# 위 메뉴 코드의 입력 부분을 고쳐서 아래 입력을 모두 처리해 보세요.

# 입력	결과
# 1 (앞뒤 공백)	퀴즈 풀기를 선택했습니다.
# abc	숫자만 입력하세요. 출력 후 메뉴로
# 그냥 Enter	입력이 비어 있습니다. 출력 후 메뉴로
# 9	잘못된 번호입니다. 출력 후 메뉴로


# menu = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]


# while True:

#     for i in range(len(menu)):
#         print(f"{i+1}. {menu[i]}")

#     try:
#         input_num = input("번호를 입력하세요: ").strip()
#         if input_num == "":
#             print("입력이 비어 있습니다.")
#             continue

#         input_num = int(input_num)
#     except ValueError:
#         print("숫자만 입력하세요.")
#         continue

#     if input_num == 1:
#         print("퀴즈 풀기를 선택했습니다.")
#     elif input_num == 2:
#         print("퀴즈 추가를 선택했습니다.")
#     elif input_num == 3:
#         print("퀴즈 목록을 선택했습니다.")
#     elif input_num == 4:
#         print("점수 확인을 선택했습니다.")
#     elif input_num == 5:
#         print("프로그램을 종료합니다.")
#         break         
#     else:
#         print("잘못된 번호입니다.")

# 함수

# def greet(name):
#     message = f"안녕하세요, {name}님!"
#     return message

# result = greet("홍길동")
# print(result)  # 안녕하세요, 홍길동님!


# def is_in_range(num, low, high):
#     return low <= num <= high

# print(is_in_range(3,1,4))
# print(is_in_range(9,1,5))   


# 직접 해 보기

# 숫자를 입력받는 함수 input_number(prompt, low, high)를 만들어 보세요.

# prompt: 화면에 보여줄 안내 문구
# low, high: 허용 범위
# 빈 입력, 숫자가 아닌 값, 범위 밖 숫자면 안내 후 함수 안에서 다시 입력받습니다.
# 올바른 숫자를 입력하면 그 숫자를 return합니다.

# 완성하면 메뉴 코드는 이렇게 짧아집니다.

# python
# choice = input_number("번호를 입력하세요: ", 1, 5)

# 힌트: 함수 안에 while True를 두고, 지금 작성한 입력 처리 코드를 옮기세요. 
# 올바른 숫자일 때 break 대신 return을 쓰면 반복과 함수가 함께 끝납니다.

# def input_number(prompt, low, high):
#     while True:
#         try:
#             input_num = input(prompt).strip()
#             if input_num == "":
#                 print("입력이 비어 있습니다.")
#                 continue

#             input_num = int(input_num)
#         except ValueError:
#             print("숫자만 입력하세요.")
#             continue

#         if low <= input_num <= high:
#             return input_num
#         else:
#             print(f"{low}에서 {high} 사이의 숫자를 입력하세요.")

# choice = input_number("번호를 입력하세요: ", 1, 5)

# print(f"입력한 번호는 {choice}입니다.")

# 클래스와 객체

# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name}가 짖습니다. 멍멍!")

# dog1 = dog("바둑이", 3)
# dog2 = dog("초코", 5)

# dog1.bark()  # 바둑이가 짖습니다. 멍멍!
# print(dog2.age)  # 5

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# dog1 = Dog("초코", 3)
# dog2 = Dog("콩이", 5)

# print(dog1.name)
# print(dog2.age)
# dog1.age = dog1.age + 1
# print(dog1.age)