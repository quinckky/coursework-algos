from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 7*x1**2 + x2**2 + x1*x2 - x1 + 8*x2
g1 = 6*x1 - 5*x2 + 5
g2 = x1 + 5*x2 - 40
g3 = x1
g4 = x2
x0 = Matrix([0.5, 2]) 

sol_k = None
sol_lins = None