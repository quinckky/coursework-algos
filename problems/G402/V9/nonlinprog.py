from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -x1**2 - 3*x2**2 - 7*x1 - 3*x2
g1 = 4*x1 - x2 + 1
g2 = -x1 + x2 - 4
g3 = x1
g4 = x2
x0 = Matrix([0.5, 4]) 

sol_k = None
sol_lins = None