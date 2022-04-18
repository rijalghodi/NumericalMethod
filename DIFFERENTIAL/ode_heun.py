''' dy/dx = x + y'''
from math import*
h = 0.1
y = 1
yuli = []
x = 0
xenon = []
delta = 1
for i in range (0,100):
	grad_1 = x + y
	y_sementara = y + grad_i*h
	grad_2 = (x + h) + y_sementara
	grad = (grad_1 + grad_2)/2

	x = x + h
	xenon = xenon + [x]
	y = y + grad * h
	yuli = yuli + [y]
plot(xenon,yuli)