import matplotlib.pyplot as plt
xmin = -20
xmax = 20
itr = 0.1
x = (xmin, xmax, itr)
y = e**(0.1*x) + 0.2*x - 10

plt.plot(x,y)
plt.show()
