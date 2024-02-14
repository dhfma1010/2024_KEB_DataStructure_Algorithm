def fibo_repetition(number: int) -> int:  # 직관적 x
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a+b

def fibo_recursion(number: int) -> int:       # 직관적 -- 성능 문제
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else :
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)



n = int(input("Input number : "))
for i in range(0, n):
    print(i)
    print(fibo_recursion(i))

print("====================================")

for i in range(0, n):
    print(i)
    print(fibo_repetition(n))

print("====================================")


memo = [None for _ in range(100)]
def fibo_memoization(number: int, memo)-> int: # 반복 계산 안하고 배열에 저장, 메모리 공간 늘어나지만 순식간 계산
    """
    fibonacci function by recursion with memoization
    :param number: integer number
    :return: integer number
    """
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1, memo) +fibo_memoization(number-2, memo)

    memo[number] = result

    return result


for i in range(0, n):
    print(i)
    print(fibo_memoization(i, memo))