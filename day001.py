import mymath

if __name__ == "__main__":  # 모듈, 여러 개의 파일 중 main 파일의 안쪽 코드 실행!!!!!
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {mymath.nCr(n, r)}")

    # # factorial 테스트용
    # f = int(input())
    # print(mymath.factorial(f))