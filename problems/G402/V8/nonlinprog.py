from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -4*x1**2 - 4*x2**2 + 3*x1*x2 - 8*x1 - 5*x2
g1 = 3*x1 - 2*x2
g2 = -x1 + x2 - 1
g3 = x1
g4 = x2
x0 = Matrix([0.5, 1]) 

sol_k = None
sol_lins = None