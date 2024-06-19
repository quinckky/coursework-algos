from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -6*x1**2 - 5*x2**2 + 7*x1*x2 - 7*x1 + 2*x2
g1 = 71*x1 - 5*x2 - 325
g2 = -3*x1 + 5*x2 - 15
g3 = x1
g4 = x2
x0 = Matrix([2, 2]) 

sol_k = None
sol_lins = None