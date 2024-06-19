from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -6*x1**2 - 7*x2**2 + 3*x1*x2 + 2*x1 + 4*x2
g1 = -4*x1 + 3*x2
g2 = 4*x1 + 3*x2 - 48
g3 = x1
g4 = x2
x0 = Matrix([0.36, 0.36])

sol_k = None
sol_lins = None