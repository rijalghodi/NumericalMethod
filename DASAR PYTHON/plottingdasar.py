import numpy as np
import matplotlib.pylab as mt

#Plotting Dasar
x = np.array ([1,2,3,4,5,6,7])
y = np.array ([3,4,5,8,9,10,15])
y1 = np.array ([4,2,4,5,6,7,9])
mt.plot(x,y,'r')
mt.scatter (x, y1)
mt.show()

#Plotting tiga fungsi
x = np.linspace (0,6, num = 100)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)

mt.plot (x ,y1, 's')
mt.plot (x, y2, 'r*')
mt.plot (x, y3, 'g--')




