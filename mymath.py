
def factorial(number) -> int:  # 반복문 바로 바로 꺼내서 쓸 수 있음
    '''
    factorial repetiton
    '''
    result = 1
    for i in range(1, number+1):
        result = result*i
    return result

# def factorial(number) -> int: # 재귀 함수 성능 느림 -- 창고에 쌓아둔 책들
#     '''
#     factorial by recursion
#     :param number : number(int)
#     :return: factorial result (int)
#     '''
#
#     if number == 1:
#         return 1
#     else:
#         return number *factorial(number-1)



def nCr(n, r) -> int:
    '''
    조합함수
    :param n: 전체 수
    :param r: 뽑는 대상 수
    :return: 조합의 결과 정수 반환
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

