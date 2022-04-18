'''Program Mencari akar-akar Pers. Kuadrat 
ax^2 + bx + c = 0 '''

#import modul math
import math
#deklarasikan koefisien a, b, c pada pers. kuadrat
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
c = float(input("Masukkan c: "))

#deklarasikan fungsi yang berisi diskriminan
def diskriminan (a, b, c):
   nilai_diskriminan = b**2 - 4*a*c
   return nilai_diskriminan

#akar-akar dicari menggunakan rumus ABC
x1 = (-b + math.sqrt(diskriminan (a,b,c)))/2*a
x2 = (-b - math.sqrt(diskriminan (a,b,c)))/2*a

#Tampilkan akar-akar pada layar
if diskriminan (a,b,c) > 0 :
    print("Akar-akarnya adalah " + str(x1) + " dan " + str(x2) )
elif diskriminan (a,b,c) == 0 :
    print("Akarnya adalah " + str(x1))
else:
    print("Akar-akar tidak real")
    



