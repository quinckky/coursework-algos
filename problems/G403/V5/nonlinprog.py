from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 6*x1**2 + 6*x2**2 - 1*x1*x2 + 8*x1 - 8*x2
g1 = 1*x1 - 2*x2 + 2
g2 = 1*x1 + 1*x2 - 7
g3 = x1
g4 = x2
x0 = Matrix([0.5, 2])

sol_k = None
sol_lins = None