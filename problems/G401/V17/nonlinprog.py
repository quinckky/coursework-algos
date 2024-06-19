from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 7*x1**2 + 1*x2**2 - 2*x1*x2 + 1*x1 + 5*x2
g1 = 9*x1 - 4*x2 # <=
g2 = -1*x1 + 4*x2 - 32 # <=
g3 = x1 # >=
g4 = x2 # >=
x0 = Matrix([0.5, 2])

sol_k = None
sol_lins = None