from sympy import Matrix, N, diff, pprint, symbols

from problems.G401.V25.nonlinprog import f, x0

if __name__ == "__main__":
    x1, x2 = symbols("x1:3")
    grad = [diff(f, x1), diff(f, x2)]
    print("gradF = ", end=" ")
    pprint(grad)
    
    grad_x0 = Matrix([x.subs(zip((x1, x2), x0)) for x in grad])
    print("gradF(x0) = ", end="\n\n")
    pprint(grad_x0)

    h = Matrix([[diff(f, x1, 2), diff(f, x1, x2)], [diff(f, x1, x2), diff(f, x2, 2)]])
    print("H = ", end="\n\n")
    pprint(h)

    inv_h = h.inv()
    print("Inversed H = ", end="\n\n")
    pprint(inv_h)

    extr_x = x0 - inv_h*grad_x0
    extr_f = f.subs(zip((x1, x2), extr_x))

    print("x* = ", end="\n\n")
    pprint(N(extr_x, 10))
    print(f"F(x*) = {N(extr_f, 10)}")