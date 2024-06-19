from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 3*x1**2 + 1*x2**2 + 1*x1*x2 - 5*x1
g1 = -5*x1 + 8*x2
g2 = 5*x1 - 2*x2 - 30
g3 = x1
g4 = x2
x0 = Matrix([5, 1]) 

sol_k = None
sol_lins = None