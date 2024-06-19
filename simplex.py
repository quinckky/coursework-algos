from copy import deepcopy
from fractions import Fraction

import inquirer
import numpy as np
import pandas as pd
from sympy import diff, symbols

from problems.G402.V13.linprog import (extr, f, g1, g2, g3, g4, sol_d, sol_i,
                                       sol_s)


def create_table(g1, g2, g3, g4, f, extr, problem="straight", integer=False, sol_s=None, sol_d=None, sol_i=None, sol_k=None, sol_lin=None):
    match problem:
        case "straight":
            # Creating a simplex table for a direct problem
            g1 = np.roll(g1, 1).tolist()
            g2 = np.roll(g2, 1).tolist()
            g2 = [-x for x in g2]
            g3 = np.roll(g3, 1).tolist()
            g4 = np.roll(g4, 1).tolist()
            m = [-x for x in g1]
            f = [0] + f
            if extr == "max":
                f = [-x for x in f]
            a = [g1, g2, g3, g4, f, m]
            if len(a[0]) == 5:
                b_var = ["R", "x5", "x6", "x7", "F", "M"]
                nb_var = ["C", "x1", "x2", "x3", "x4"]
            elif len(a[0]) == 4:
                b_var = ["R", "x4", "x5", "x6", "F", "M"]
                nb_var = ["C", "x1", "x2", "x3"]
            sol = sol_s

        case "dual":
            # Creating a simplex table for a dual problem
            f = np.array([f])
            if extr=="max":
                a = [g1, [-x for x in g2], g3, g4]
            if extr=="min":
                a = [g1, g2, [-x for x in g3], [-x for x in g4]]
            b = []
            for i in range(len(a)):
                b.append(a[i].pop(-1))
            a = np.array(a).T
            b = np.array([b])
            if extr=="max":
                a = -a
                f = -f
            if extr=="min":
                b = -b
            f, b = b, f
            a = np.hstack((b.T, a))
            a = np.vstack(
                (a, np.hstack(
                    (np.zeros((1, 1)), f)))).tolist()
            if len(a) == 5:
                b_var = ["y5", "y6", "y7", "y8", "F"]
                nb_var = ["C", "y1", "y2", "y3", "y4"]
            elif len(a) == 4:
                b_var = ["y5", "y6", "y7", "F"]
                nb_var = ["C", "y1", "y2", "y3", "y4"]
            sol = sol_d

        case "kyn-takker":
            # Creating a simplex table for Kun-Takker problem
            x1, x2 = symbols("x1:3")
            l1, l2 = symbols("l1:3")
            if extr == "max":
                g1 *= -1
                g2 *= -1
                print("Так как задача на максимум, то ограничения приводятся к виду >=")
            else:
                print("Так как задача на минимум, то ограничения приводятся к виду <=")

            f = f + l1*g1 + l2*g2
            print(f"Функция примет вид {f}")

            g1 = diff(f, x1)
            print(f"Первое ограничение примет вид {g1}")

            g2 = diff(f, x2)
            print(f"Второе ограничение примет вид {g2}")

            g3 = diff(f, l1)
            print(f"Третье ограничение примет вид {g3}")

            g4 = diff(f, l2)
            print(f"Четвертое ограничение примет вид {g4}")
            g1 = [-g1.coeff(x1, 0).coeff(x2, 0).coeff(l1, 0).coeff(l2, 0),
                  g1.coeff(x1), g1.coeff(x2), g1.coeff(l1), g1.coeff(l2)]
            g2 = [-g2.coeff(x1, 0).coeff(x2, 0).coeff(l1, 0).coeff(l2, 0),
                  g2.coeff(x1), g2.coeff(x2), g2.coeff(l1), g2.coeff(l2)]
            g3 = [-g3.coeff(x1, 0).coeff(x2, 0).coeff(l1, 0).coeff(l2, 0),
                  g3.coeff(x1), g3.coeff(x2), g3.coeff(l1), g3.coeff(l2)]
            g4 = [-g4.coeff(x1, 0).coeff(x2, 0).coeff(l1, 0).coeff(l2, 0),
                  g4.coeff(x1), g4.coeff(x2), g4.coeff(l1), g4.coeff(l2)]
            if extr == "min":
                g1 = [-x for x in g1]
                g2 = [-x for x in g2]
            elif extr == "max":
                g3 = [-x for x in g3]
                g4 = [-x for x in g4]
            a = [g1, g2, g3, g4]
            b_var = ["v1", "v2", "w1", "w2"]
            nb_var = ["C", "x1", "x2", "λ1", "λ2"]
            sol = sol_k

        case "lin_comb":
            # Creating a simplex table for linear combinations problem
            x1, x2 = symbols("x1:3")
            g1 = [-g1.coeff(x1, 0).coeff(x2, 0), g1.coeff(x1), g1.coeff(x2)]
            g2 = [-g2.coeff(x1, 0).coeff(x2, 0), g2.coeff(x1), g2.coeff(x2)]
            f = [0, float(f[0]), float(f[1])]
            if extr == "max":
                f = [-x for x in f]
            a = [g1, g2, f]
            b_var = ["x3", "x4", "F"]
            nb_var = ["C", "x1", "x2"]

            sol = None

    if integer:
        # Creating a simplex table for a partially integer problem
        if sol is None:
            a, b_var, nb_var = solve(
                a, b_var, nb_var, mode="manual", output=True)
        else:
            a, b_var, nb_var = solve(
                a, b_var, nb_var, sol, mode="auto", output=False)
        if "R" in nb_var:
            i_R = nb_var.index("R")
            nb_var.remove("R")
            b_var.remove("M")
            for i in range(len(a)):
                a[i] = a[i][:i_R] + a[i][i_R+1:]
            a = a[:-1]
        sol = sol_i
        i = 0
        for row in a:
            cI = row[0] % 1
            if i == 0:
                i += 1
                continue
            if cI:
                gI = [-x if x > 0 else -x * cI/(cI - 1) for x in row]
                break
        else:
            print("Решение уже является полностью целочисленным")
            return None, None, None, None
        a = a[:-1] + [gI] + a[-1:]
        gI[0] = -cI
        b_var = b_var[:-1] + ['int'] + b_var[-1:]

    return a, b_var, nb_var, sol


def solve(a, b_var, nb_var, sol=None, mode="manual", output=False):
    if a is None or b_var is None or nb_var is None:
        return
    if mode == "auto" and sol is None:
        print("Оптимальное решение не задано!")
        return
    if mode == "auto":
        ij = iter(sol)

    n = len(a)
    m = len(a[0])

    for i in range(n):
        for j in range(m):
            a[i][j] = Fraction(a[i][j])
    if output:
        print(pd.DataFrame(a, columns=nb_var, index=b_var))

    while True:
        if mode == "manual":
            i = int(input("Ведущий i = ") or 0) or None
            j = int(input("Ведущий j = ") or 0) or None
        elif mode == "auto":
            i, j = next(ij, (None, None))
            if output:
                print(f"Ведущий i = {i}")
                print(f"Ведущий j = {j}")
        if i is None and j is None:
            if output:
                print("Процесс решения завершен", end='\n\n')
            break
        i -= 1
        j -= 1
        pivot = a[i][j]
        if output:
            print(f"Ведущий = {pivot}")
        b = deepcopy(a)

        for k in range(n):
            for r in range(m):
                if k == i and r == j:
                    b[k][r] = 1/pivot
                elif k == i:
                    b[k][r] = a[i][r]/pivot
                elif r == j:
                    b[k][r] = -a[k][j]/pivot
                else:
                    b[k][r] -= (a[k][j]*a[i][r])/pivot

        nb_var[j], b_var[i] = b_var[i], nb_var[j]
        a = deepcopy(b)
        if output:
            print(pd.DataFrame(a, columns=nb_var, index=b_var))

    return a, b_var, nb_var


if __name__ == "__main__":
    questions = [
        inquirer.List(
            "Problem",
            message="Какой задачи хотите искать решение?",
            choices=["Прямая", "Двойственная"],
        ),
    ]
    problem = "straight" if inquirer.prompt(
        questions)["Problem"] == "Прямая" else "dual"
    questions = [
        inquirer.List(
            "Integer",
            message="Решать задачу с условием частичной целочисленности?",
            choices=["Да", "Нет"],
        ),
    ]
    integer = True if inquirer.prompt(questions)["Integer"] == "Да" else False
    table = create_table(g1, g2, g3, g4, f, extr,
                         problem, integer, sol_s, sol_d, sol_i)
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
    solve(*table, mode, output=True)
