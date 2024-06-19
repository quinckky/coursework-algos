from sympy import Matrix, N, Symbol, diff, expand, solve, symbols

from problems.G402.V24.nonlinprog import f, x0

if __name__ == '__main__':
    x1, x2 = symbols("x1:3")
    a0 = Symbol('a0')
    extr = "min" if diff(f, x1, 2) > 0 else "max"
    if extr == "min":
        print(f"Так как вторая производная по х1 >0 то это задача минимума")
    elif extr == "max":
        print(f"Так как вторая производная по х1 <0 то это задача максимума")

    grad = [diff(f, x1), diff(f, x2)]
    print(f"Градиент задается как = {N(grad[0], 10), N(grad[1], 10)}")

    print(f"Начальная точка x0 = {x0[0], x0[1]}")

    f_x0 = f.subs(zip((x1, x2), x0))
    print(f"Значение функции в этой точке = {N(f_x0, 10)}", end='\n\n')

    for i in range(1, 4):
        print(f"Шаг {i}")
        grad_x0 = Matrix([x.subs(zip((x1, x2), x0)) for x in grad])
        print(f"Градиент в точке x{i-1} = {N(grad_x0[0], 10), N(grad_x0[1], 10)}")

        if extr == 'max':
            next_x = x0 + a0*grad_x0
        elif extr == 'min':
            next_x = x0 - a0*grad_x0
        print(f"Следующая точка x{i} задается как = {N(next_x[0], 10), N(next_x[1], 10)}")

        f_a = f.subs(zip((x1, x2), next_x))
        print(f"Подставляя эту точку в функцию, получим {expand(f_a).evalf(10)}")

        step = diff(f_a, a0)
        print(f"Продифференцируем, получим {N(step, 10)}")

        step = solve(step, a0)[0]
        print(f"Приравняв к нулю, находим a0 = {N(step, 10)}")

        x0 = Matrix([x.subs(a0, step) for x in next_x])
        print(f"Тогда следующая точка x{i} = {N(x0[0], 10), N(x0[1], 10)}")

        f_x0 = f.subs(zip((x1, x2), x0))
        print(f"Значение функции в этой точке = {N(f_x0, 10)}", end='\n\n')

    extr_x = x0
    extr_f = f_x0
    print(f"Безусловный экстремум функции в точке x{i} = {N(extr_x[0], 10), N(extr_x[1], 10)}")
    print(f"Значение функции в этой точке f = {N(extr_f, 10)}")