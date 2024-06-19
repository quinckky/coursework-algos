from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 3*x1**2 + 4*x2**2 - 2*x1*x2 + 4*x1 + 5*x2
g1 = 4*x1 - 7*x2 + 7
g2 = 1*x1 + 7*x2 - 42
g3 = x1
g4 = x2
x0 = Matrix([1, 2])

sol_k = None
sol_lins = None