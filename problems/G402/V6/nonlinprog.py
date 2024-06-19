from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 5*x1**2 + 6*x2**2 + 5*x1*x2 + 9*x1 - 5*x2
g1 = 11*x1 - 3*x2 - 18 # <= 
g2 = -1*x1 + 1*x2 - 2 # <=
g3 = x1 # >=
g4 = x2 # >=
x0 = Matrix([1, 1])

sol_k = [[2, 3]]
sol_lins = None