from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 6*x1**2 + 6*x2**2 + x1*x2 + 2*x1 + 7*x2
g1 = -9*x1 + 4*x2 + 12 # <= 
g2 = 5*x1 + 2*x2 - 32 # <=
g3 = x1 # >=
g4 = x2 # >=
x0 = Matrix([2, 1])

sol_k = None
sol_lins = None