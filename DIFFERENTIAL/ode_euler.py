''' dy/dx = (x-1)/(y*exp(y))'''
from math import*
h = 0.1
y = 1
yuli = []
x = 0
xenon = []
delta = 1
for i in range (0,100):
	grad = (x-1)/(y*exp(y))
	x = x + 0.1
	xenon = xenon + [x]
	y = y + grad * h
	yuli = yuli + [y]
plot(xenon,yuli)




