import inquirer
from sympy import N, diff, symbols

from problems.G403.V5.nonlinprog import f, g1, g2, g3, g4, sol_k
from simplex import create_table
from simplex import solve as simplex_solve

if __name__ == '__main__':
    x1, x2 = symbols("x1:3")
    l1, l2 = symbols("l1:3")
    extr = "min" if diff(f, x1, 2) > 0 else "max"
    if extr == "min":
        print(f"Так как вторая производная по х1 >0 то это задача минимума")
    elif extr == "max":
        print(f"Так как вторая производная по х1 <0 то это задача максимума")
    print("Добавим в функцию ограничения с коэффициентами λ, продиффернцируем по каждой переменной и получим новую систему ограничений")

    table = create_table(g1, g2, g3, g4, f, extr, problem="kyn-takker", integer=False, sol_k=sol_k)
    print("Составим и решим по ней симплекс-таблицу")
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
    xL = [0, 0, 0, 0]
    for i in range(len(b_var)):
        if b_var[i] in "x1x2λ1λ2":
            xL[i] = a[i][0]
    
    print(f"Получим x1 = {xL[0]}, x2 = {xL[1]}, λ1 = {xL[2]}, λ2 = {xL[3]}")
    extr_x = xL[:2]
    extr_f = f.subs(zip((x1, x2, l1, l2), xL))
    print(f"Условный экстремум функции в точке {N(extr_x[0], 10), N(extr_x[1], 10)}")
    print(f"Значение функции в этой точке f = {N(extr_f, 10)}")