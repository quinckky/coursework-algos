from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -5*x1**2 - 4*x2**2 - 1*x1*x2 + 1*x1 + 7*x2
g1 = 3*x1 - 2*x2 + 6
g2 = 0*x1 + 1*x2 - 9
g3 = x1
g4 = x2
x0 = Matrix([1, 5]) 

sol_k = None
sol_lins = None