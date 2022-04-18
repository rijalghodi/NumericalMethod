print ("Program Angka Prima")
angka = int(input("Masukkan angka: "))

if angka > 1 :
    for i in range (2,angka):
        if (angka % i) == 0 :
            print (" bukan bilangan prima")
            print (" Faktor primanya adalah ", str(i) , " dan " , str(int(angka/i)) )
            break
    else :
        print ("bilangan prima")
else :
    print (" bilangan prima ")

