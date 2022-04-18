
#initial condition
T1 = 500; T2 = 500; T3 = 500; T4 = 500; T5 = 500; T6 = 500
T7 = 500; T8 = 500; T9 = 500; T10 = 500

#Mendefinisikan wadah untuk merekam riwayat suhu masing2 node
T1vek = []; T2vek = []; T3vek = []; T4vek = []; T5vek = []
T6vek = []; T7vek = []; T8vek = []; T9vek = []; T10vek = []

delta = 1
t = []              #Wadah untuk waktu
i = 0
while delta > 0.001:
    t = t + [i*0.1]         #0.1 adalah delta_x dan delta_y
    i=i+1
    Tlama = T1
    # Ini bukan gauss-saidel, tapi real solution
    T1 = 0.05*T2 + 0.85*T1 + 26.5
    T2 = 0.05*(T1 + T3) + 0.85*T2 + 1.5
    T3 = 0.05*(T2 + T4) + 0.85*T3 + 1.5
    T4 = 0.05*(T3 + T5) + 0.85*T4 + 1.5
    T5 = 0.05*(T4 + T6) + 0.85*T5 + 1.5
    T6 = 0.05*(T5 + T7) + 0.85*T6 + 1.5
    T7 = 0.05*(T6 + T8) + 0.85*T7 + 1.5
    T8 = 0.05*(T7 + T9) + 0.85*T8 + 1.5
    T9 = 0.05*(T8 + T10) + 0.85*T9 + 1.5
    T10 = 0.05*T9 + 0.85*T10 + 4.5
    T = [round(T1,1), round(T2,1), round(T3,1), round(T4,1), round(T5,1), \
         round(T6,1), round(T7,1) , round(T8,1), round(T9,1), round(T10,1)]
    print(T)
    delta = abs(T1 - Tlama)
