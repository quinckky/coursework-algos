from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -2*x1**2 - 3*x2**2 + 2*x1*x2 + 4*x1 - 8*x2
g1 = x1 - 2*x2
g2 = 2*x1 + 3*x2 - 21
g3 = x1
g4 = x2
x0 = Matrix([1, 1])

sol_k = [[1, 2], [3, 4], [2, 3]]
sol_lins = None