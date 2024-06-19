from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = 7*x1**2 + 7*x2**2 + 5*x1*x2 - 9*x1 + 9*x2
g1 = -7*x1 + 5*x2 + 5
g2 = 21*x1 + 5*x2 - 135
g3 = x1
g4 = x2
x0 = Matrix([2, 1])

sol_k = [[1, 2], [3, 4]]
sol_lins = None