import inquirer
from sympy import Matrix, N, Symbol, diff, expand, solve, symbols

from problems.G403.V5.nonlinprog import f, g1, g2, g3, g4, sol_lins, x0
from simplex import create_table
from simplex import solve as simplex_solve

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
    for i in range(1, 7):
        print(f"Шаг {i}")
        grad_x0 = Matrix([x.subs(zip((x1, x2), x0)) for x in grad])
        print(f"Градиент в точке x{i-1} = {N(grad_x0[0], 10), N(grad_x0[1], 10)}")
        pred_f = f.subs(zip((x1, x2), x0))

        w0 = (grad_x0.T * Matrix([x1, x2]))[0]
        print(f"Линейная функция задается как {w0}")
        print(f"Решим эту задачу симплекс-методом")

        if sol_lins is not None:
            sol_lin = sol_lins[i-1]
        else:
            sol_lin = None

        table = create_table(g1, g2, g3, g4, grad_x0, extr, problem="lin_comb", integer=False, sol_lin=sol_lin)
        if table[-1] is not None:
            questions = [
                inquirer.List(
                    "Mode",
                    message="Существует оптимальное решение задачи. Хотите использовать его или найти решение вручную?",
                    choices=["Использовать существующее решение", "Решить вручную"],
                ),
            ]
            choice = inquirer.prompt(questions)
            mode = "manual" if choice["Mode"] == "Решить вручную" else "auto"
        else:
            mode = "manual"

        a, b_var, nb_var = simplex_solve(*table, mode, output=True)
        x_lin = Matrix([0, 0])
        for j in range(len(b_var)):
            if b_var[j] == "x1":
                x_lin[0] = a[j][0]
            elif b_var[j] == "x2":
                x_lin[1] = a[j][0]
        print(f"Откуда x1 = {x_lin[0]}, x2 = {x_lin[1]}")

        next_x = x0 + a0*(x_lin - x0)
        if next_x == x0:
            print("Следующая точка равна предыдущей, следовательно решение найдено")
            break
        print(f"Следующая точка задается как {N(next_x[0], 10), N(next_x[1], 10)}")

        f_a = f.subs(zip((x1, x2), next_x))
        print(f"Подставляя эту точку в функцию, получим {N(expand(f_a), 10)}")

        step = diff(f_a, a0)
        print(f"Продифференцируем, получим {N(step, 10)}")

        step = solve(step, a0)[0]
        print(f"Приравняв к нулю, находим a0 = {N(step, 10)}")

        if not (0 <= step <= 1):
            step = 1
            print(f"a0 не входит в диапазон [0; 1], поэтому присвоим a0 = 1")
        
        if step == 0:
            print("Шаг равен нулю, значит решение найдено")
            break

        x0 = Matrix([x.subs(a0, step) for x in next_x])
        print(f"Тогда следующая точка равна x{i} = {N(x0[0], 10), N(x0[1], 10)}", end='\n\n')

        f_x0 = f.subs(zip((x1, x2), x0))
        print("Значение функции в этой точке", N(f_x0, 10))

        print("Точность равна", float(abs(f_x0 - pred_f)/(abs(f_x0))))

    extr_x = x0
    extr_f = f.subs(zip((x1, x2), x0))
    print(f"Условный экстремум функции в точке x{i} = {N(extr_x[0], 10), N(extr_x[1], 10)}")
    print(f"Значение функции в этой точке f = {N(extr_f, 10)}")