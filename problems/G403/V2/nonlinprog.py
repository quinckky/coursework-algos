from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 4*x1**2 + 4*x2**2 - 3*x1*x2 - 1*x1 - 7*x2
g1 = -2*x1 + 3*x2
g2 = 44*x1 + 9*x2 - 450
g3 = x1
g4 = x2
x0 = Matrix([2, 1])

sol_k = [[1, 2], [3, 4], [2, 3]]
sol_lins = None