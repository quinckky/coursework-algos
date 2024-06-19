from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -3*x1**2 - 6*x2**2 - x1*x2 + 8*x1 + 5*x2
g1 = -5*x1 + 3*x2 + 9
g2 = 5*x1 - x2 - 23
g3 = x1
g4 = x2
x0 = Matrix([3, 1]) 

sol_k = [[1, 2], [3, 4], [2, 3]]
sol_lins = None