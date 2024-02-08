def factorial(number) -> int:
    result = 1
    for i in range(1, number+1):
        result = result*i
    return result

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


if __name__ == "__main__":  # 모듈, 여러 개의 파일 중 main 파일의 안쪽 코드 실행!!!!!
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n, r)}")
