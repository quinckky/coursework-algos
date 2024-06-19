import inquirer
import numpy as np
from sympy import Matrix, N, Poly, Symbol, diff, pprint, solve, symbols
from sympy.core.relational import Relational

from problems.G402.V24.nonlinprog import f, g1, g2, g3, g4, x0

if __name__ == '__main__':
    x1, x2 = symbols("x1:3")
    a0 = Symbol('a0')
    extr = "min" if diff(f, x1, 2) > 0 else "max"
    g_eq = [g1, g2, g3, g4]

    if extr == "min":
        print(f"Так как вторая производная по х1 >0 то это задача минимума")
    elif extr == "max":
        print(f"Так как вторая производная по х1 <0 то это задача максимума")

    grad = [diff(f, x1), diff(f, x2)]
    print(f"Градиент задается как = {N(grad[0], 10), N(grad[1], 10)}")
    print(f"Начальная точка x0 = {x0[0], x0[1]}", end='\n\n')
    s = None
    borders = []
    for i in range(1, 7):
        print(f"Шаг {i}")
        grad_x0 = Matrix([x.subs(zip((x1, x2), x0)) for x in grad])
        print(f"Градиент в точке x{i-1} = {N(grad_x0[0], 10), N(grad_x0[1], 10)}")

        if extr == "max":
            if s is not None and np.dot(np.array(grad_x0.T), np.array(s)) == 0:
                print(f"Направление S перпендикулярно градиенту, значит оптимальное решение найдено", end='\n\n')
                break
        elif extr == "min":
            if s is not None and np.dot(np.array(-grad_x0.T), np.array(s)) == 0:
                print(f"Направление S перпендикулярно антиградиенту, значит оптимальное решение найдено", end='\n\n')
                break
        
        lims = [g1 <= 0, g2 <= 0, g3 >= 0, g4 >= 0]
        if extr == "max":
            x_out = x0 + grad_x0*0.1
        if extr == "min":
            x_out = x0 - grad_x0*0.1

        if not all([x.subs(zip((x1, x2), x_out)) for x in lims]):
            borders = []
            for j in range(len(g_eq)):
                if -0.0001 <= g_eq[j].subs(zip((x1, x2), x0)) <= 0.0001: 
                    borders.append(j)

        if borders:
            print(f"Градиент выводит за ОДЗП, переходим к поиску S")
            if len(borders) > 1:
                questions = [
                    inquirer.List(
                        "S",
                        message="Точка лежит на вершине. По какому из ограничений пойти далее?",
                        choices=[x+1 for x in borders],
                    ),
                ]
                choice = inquirer.prompt(questions)
                j = choice["S"] - 1
            else:
                j = borders[0]

            s1, s2 = symbols("s1:3")
            s = [g_eq[j].coeff(x1)*s1 + g_eq[j].coeff(x2)*s2, (s1**2 + s2**2)**(1/2) - 1]
            print(f"Точка лежит на ограничении {j+1}, подставляем коэффициенты этого ограничения, получим {s[0]} = 0, {s[1]} = 0")
            
            s_g, s_ag = solve(s, s1, s2)
            print(f"Направление s1_1 = {s_g[0]} и s1_2 = {s_g[1]}")
            print(f"Направление s2_1 = {s_ag[0]} и s2_2 = {s_ag[1]}")

            deg1 = np.dot(np.array(s_g), np.array(grad_x0))
            print(f"Скалярное произведение s1 и градиента = {deg1}")

            deg2 = np.dot(np.array(s_ag), np.array(grad_x0))
            print(f"Скалярное произведение s2 и градиента = {deg2}")
            if extr == "max":
                if np.dot(np.array(s_g), np.array(grad_x0)) > 0:
                    s = Matrix(s_g)
                    print(f"Направление s1 составляет острый угол с градиентом, поэтому выбираем это направление")
                elif np.dot(np.array(s_ag), np.array(grad_x0)) > 0:
                    s = Matrix(s_ag)
                    print(f"Направление s2 составляет острый угол с градиентом, поэтому выбираем это направление")
            elif extr == "min":
                if np.dot(np.array(s_g), np.array(-grad_x0)) > 0:
                    s = Matrix(s_g)
                    print(f"Направление s1 составляет острый угол с антиградиентом, поэтому выбираем это направление")
                elif np.dot(np.array(s_ag), np.array(-grad_x0)) > 0:
                    s = Matrix(s_ag)
                    print(f"Направление s2 составляет острый угол с антиградиентом, поэтому выбираем это направление")

            next_x = x0 + a0*s

        elif extr == 'max':
            next_x = x0 + a0*grad_x0
        elif extr == 'min':
            next_x = x0 - a0*grad_x0
        print(f"Следующая точка x{i} задается как = {N(next_x[0], 10), N(next_x[1], 10)}")

        lims = [g1 <= 0, g2 <= 0, g3 >= 0, g4 >= 0]
        if borders:
            lims = lims[:j] + lims[j+1:]
        lims = [x.subs(zip((x1, x2), next_x)) for x in lims]
        lims = solve(lims, a0)
        print(f"Подставляя координаты точки в ограничения, получим: {lims}")

        f_a = f.subs(zip((x1, x2), next_x))
        print(f"Подставляя эту точку в функцию, получим")
        pprint(Poly(f_a).as_expr(), num_columns=1000)

        step = diff(f_a, a0)
        print(f"Продифференцируем, получим {N(step, 10)}")

        step = solve(step, a0)[0]
        print(f"Приравняв к нулю, находим a0 = {N(step, 10)}")

        max_step = max(lim.canonical.rhs for lim in lims.atoms(Relational))
        if step > max_step:
            print("a0 не входит в диапазон своих допустимых значений, поэтому берем ближайший предел")
            step = max_step
            print(f"Откуда a0 = {N(step, 10)}")

        if -0.0001 < step < 0.0001:
            print(f"Шаг равен нулю, значит оптимальное решение найдено", end='\n\n')
            break

        x0 = Matrix([x.subs(a0, step) for x in next_x])
        print(f"Тогда следующая точка x{i} = {N(x0[0], 10), N(x0[1], 10)}", end='\n\n')

    extr_x = x0
    extr_f = f.subs(zip((x1, x2), x0))
    print(f"Условный экстремум функции в точке x{i-1} = {N(extr_x[0], 10), N(extr_x[1], 10)}")
    print(f"Значение функции в этой точке f = {N(extr_f, 10)}")