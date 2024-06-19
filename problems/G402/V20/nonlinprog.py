from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 4*x1**2 + 6*x2**2 + 5*x1*x2 - 6*x1 + 7*x2
g1 = 5*x1 + 2*x2 - 30
g2 = -x1 + 2*x2 - 6
g3 = x1
g4 = x2
x0 = Matrix([1, 1]) 

sol_k = None
sol_lins = None