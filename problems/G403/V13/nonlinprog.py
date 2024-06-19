from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 3*x1**2 + 5*x2**2 - 5*x1*x2 + 7*x1 + 9*x2
g1 = -4*x1 + 5*x2 + 5
g2 = 12*x1 - 5*x2 - 45
g3 = x1
g4 = x2
x0 = Matrix([3, 1])

sol_k = [[1, 2], [3, 4], [2, 3]]
sol_lins = None