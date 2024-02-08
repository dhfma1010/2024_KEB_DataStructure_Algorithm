import random

num = int(input("1부터 100사이 숫자 입력: "))

answer = random.randint(1,100)

count = 0

while True:

    if num == answer:
        print("정답 입니다.")
        count = count + 1
        print(f"{count}번 만에 맞히셨습니다.")
        break
    elif num < answer:
        print("입력한 숫자 보다 큽니다.")
        num = int(input("1부터 100사이 숫자 입력: "))
        count = count + 1

    elif num > answer:
        print("입력한 숫자 보다 작습니다.")
        num = int(input("1부터 100사이 숫자 입력: "))
        count = count + 1





