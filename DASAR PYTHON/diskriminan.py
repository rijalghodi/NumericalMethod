'''Program Python untuk Mengidentifikasi 
Banyak Akar Persamaan Kudarat'''

#Masukkan koefisien persamaan kuadrat y = ax^2 + bx + c

a = 5
b = 3
c = -9

#definisikan diskriminan
def diskriminan(a,b,c):
    result = b**2 - 4*a*c
    return result

# Uji diskriminan
if diskriminan (a, b, c) > 0:
    print("punya dua akar real berbeda")
elif diskriminan (a, b, c) = 0:
    print('punya dua akar real kembar')
else:
    print('punya dua akar imajiner')
    