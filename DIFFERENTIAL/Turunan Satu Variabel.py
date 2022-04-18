def f (x): #fungsi
    y = x**3
    return y

def turpertama (x): #turunan pertama
    y1 = (f(x + 0.01) - f(x))/0.01
    return y1

def turkedua (x): #turunan kedua
    y2 = (turpertama(x + 0.01)-turpertama(x))/0.01
    return y2

print(turkedua(2)) #pemanggilan tur 2
print(turpertama(10)) #pemanggilan tur 1
print(f(1)) #pemanggilan fungsi