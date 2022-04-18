''' dy/dx = (x-1)/(y*exp(y))'''
from math import *

h = 0.1
y = 1
yuli = []
x = 0
xenon = []


def f(a, b):
	result = a + b
	return result


for i in range(0, 100):
	xenon = xenon + [x]
	yuli = yuli + [y]

	k1 = f(x,y)
	k2 = f(x+0.5*h , y+0.5*k1*h)
	k3 = f(x+h, y - k1*h + 2*k2*h)

	grad = (1/6)*f(k1 , 4*k2 + k3)
	y = y + grad * h

	x = x + h


plot(xenon, yuli)