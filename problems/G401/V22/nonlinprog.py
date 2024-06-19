from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 5*x1**2 + 7*x2**2 - 4*x1*x2 - 1*x1 - 7*x2
g1 = 3*x1 - 4*x2 + 12 # <=
g2 = 1*x1 + 1*x2 - 10 # <=
g3 = x1 # >=
g4 = x2 # >=
x0 = Matrix([1, 5])

sol_k = [[2, 3], [3, 4]]
sol_lins = None