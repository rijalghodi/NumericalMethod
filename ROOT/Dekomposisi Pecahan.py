from sympy import*
x, y, z = symbols('x y z')
persamaan = (x**2 + 6*x + 8)/(x**3 + 5*x**2 + 8*x + 8)
akar = apart(persamaan)
print(akar)