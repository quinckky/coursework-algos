from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -4*x1**2 - 5*x2**2 + 2*x1*x2 + x1 + 8*x2
g1 = 4*x1 - 3*x2 + 6
g2 = -x1 + 3*x2 - 15
g3 = x1
g4 = x2
x0 = Matrix([1, 5])

sol_k = [[1, 2], [3, 4], [2, 3]]
sol_lins = None