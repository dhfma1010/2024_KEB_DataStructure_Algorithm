
f0 = 0
f1 = 1
x = 0

number = int(input("Input number: "))

for i in range(number-1):
    if i == 0:
        x = x + i
    elif i == 1:
        x = x + i
    else:
        x = i + (i-1)
        print(x, end =' ')





def fibo(number: int) -> int:
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
