import mymath
import time

if __name__ == "__main__":  # 모듈, 여러 개의 파일 중 main 파일의 안쪽 코드 실행!!!!!
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    # start = time.time()
    print(f"{n}C{r} = {mymath.nCr(n, r)}")
    # end = time.time()
    # print (f"소요시간 : {end - start}")

    # # factorial 테스트용
    # f = int(input())
    # print(mymath.factorial(f))