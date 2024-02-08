import time
# def factorial(number) -> int:  # 반복문 바로 바로 꺼내서 쓸 수 있음
#     """'''
#     factorial repetiton
#     '''"""
#     result = 1
#     for i in range(1, number+1):
#         result = result*i
#     return result

def factorial(number) -> int: # 재귀 함수 성능 느림 -- 창고에 쌓아둔 책들
    '''
    factorial by recursion
    :param number : number(int)
    :return: factorial result (int)
    '''
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)



# def nCr(n, r) -> int:   ## 함수 하나가 두 가지 일(시간, 조합계산)하고 있음, 단일 책임원칙 위배 --> decorator로 확장!
#     '''
#     조합함수
#     :param n: 전체 수
#     :param r: 뽑는 대상 수
#     :return: 조합의 결과 정수 반환
#     '''
#     start = time.time()
#     numerator = factorial(n)
#     denominator = factorial(n-r) * factorial(r)
#     end = time.time()
#     print(f"소요시간 : {end-start}")
#     return int(numerator / denominator)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time elapsed: {end - start}")
        return result
    return wrapper # 클로저는 괄호 없음!


@timer
def nCr(n, r) -> int: # SRP , OCP
    '''
    조합함수
    :param n: 전체 수
    :param r: 뽑는 대상 수
    :return: 조합의 결과 정수 반환
    '''

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)
