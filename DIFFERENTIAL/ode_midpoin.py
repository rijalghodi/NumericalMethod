''' dy/dx = (x-1)/(y*exp(y))'''
from math import*
h = 0.1
y = 1
yuli = []
x = 0
xenon = []

def f(a,b):
	result = a + b
	return result

for i in range (0,100):
	xenon = xenon + [x]
	yuli = yuli + [y]

	grad_1 = f(x,y)
	y_sementara = y + grad_1*0.5*h

	grad = f(x+0.5, y_sementara)

	y = y + grad*h

	x = x + 0.1

plot(xenon,yuli)