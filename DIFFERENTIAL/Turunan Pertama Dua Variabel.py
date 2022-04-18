#df/dx pada (1,2) di mana f = x^2*y^2 Menggunakan metode forward
def turdx(x,y):
    f_lama = ((x)**2)*(y**2)
    x = x + 0.0001
    f_baru = (x**2)*(y**2)
    turdx =  (f_baru - f_lama)/0.0001
    return turdx
print(turdx(1,2))
