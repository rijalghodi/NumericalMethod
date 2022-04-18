
import numpy as np
    
#Enter the dependent variable
x = [2.54, 5.08, 7.62, 10.16, 12.7]
y = [0.028735, 0.0345, 0.043735, 0.052, 0.06388]
n = len(x)

#define the sum function
def sum (arr):
    ans = 0
    for i in range(len(arr)):
        ans = ans + arr[i]
    return ans

#define the special multiplication of array
def kali(arr1, arr2):
    ans = []
    for i in range (len(arr1)):
        ans = ans + [arr1[i]*arr2[i]]
    return ans

#define the coefficient of linear eq
sumx = sum(x)
sumy = sum(y)
sumxy = sum(kali(x,y))
sumxx = sum(kali(x,x))
sumyy = sum(kali(y, y))

#definisikan koefisien fungsi lienar
a = (n*sumxy - sumx*sumy)/(n*sumxx-sumx**2)
b = (sumy-a*sumx)/n

print("fungsi regresi y = ", str(a) , " x + ", str(b))



# plot grafik
import matplotlib.pyplot as plt
xmin = x[0]
xmax = x[n-1]
print(xmin)
print(xmax)

varx = np.linspace (xmin, xmax, 100)
vary = a * varx + b

plt.plot(varx, vary)
plt.scatter(x,y)
plt.show()
