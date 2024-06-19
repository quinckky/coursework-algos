from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 1*x1**2 + 5*x2**2 + 3*x1*x2 + 9*x1 - 9*x2
g1 = 1*x1 - 1*x2 + 3
g2 = 1*x1 + 2*x2 - 18
g3 = x1
g4 = x2
x0 = Matrix([1, 5]) 

sol_k = None
sol_lins = None