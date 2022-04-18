from numpy import*

def kalimatrix(P,Q):
    m = len(P.transpose()[0])
    o = len(Q.transpose()[0])
    n = len (Q[0])
    E = zeros((m,n))
    for i in range (0, m):
        for j in range (0, n):
            for k in range (0,o):
                E[i,j] = E[i,j] + P[i,k]*Q[k,j]
    return E

