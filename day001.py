def print_poly(t_x, f_x) -> str:

    poly_expression = "f(x) = "

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]

        if coefficient >= 0 and i != 0:  # 맨 앞에는 +부호 붙이지 않음
            poly_expression += "+"
        poly_expression += f'{coefficient}X^{term} '

    return poly_expression


def calculation_poly(x_value, t_x, f_x) -> int:
    return_value = 0


    for i in range(len(fx)):
        term = tx[i]
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, term)


    return return_value

fx = [2, 3, 4]
tx = [500, 10, 0]

if __name__ == "__main__":

    print(print_poly(tx, fx))

    pxValue = calculation_poly(int(input("X 값 : ")), tx, fx)
    print(pxValue)


