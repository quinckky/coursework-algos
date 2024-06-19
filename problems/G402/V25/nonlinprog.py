from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -7*x1**2 - 4*x2**2 + x1*x2 - 4*x1 - x2
g1 = 2*x1 - 7*x2 + 14
g2 = 3*x1 + 7*x2 - 49
g3 = x1
g4 = x2
x0 = Matrix([2, 4])

sol_k = None
sol_lins = None