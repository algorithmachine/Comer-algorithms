import numpy as np
                
def comer_symmetric(p,m,g):
    assert (p-1) % 2*m == 0
    X0 = np.array( [pow(g, i, p) for i in range(0, p-m, m) ] )
    certificates_master = np.array([ pow(g, i, p) for i in range(m) ])
    C_minus_X0 = ( ( certificates_master[:, np.newaxis] - X0 ) % p )
    C_minus_X0_sets = [ set(L) for L in C_minus_X0 ]
    Xs = [{pow(g, x+i, p) for x in range(0, p-m, m)} for i in range(m)]
    forb_cycles = []
    for i in range(m):
        for j in range(i,m):
            if not bool(Xs[i].intersection(C_minus_X0_sets[j])):
                forb_cycles.append((0,i,j))
    return forb_cycles

def comer_asymmetric(p,n,g):
    assert n%2 == 0
    assert int((p-1) / n) % 2 == 1
    m = int(n / 2)
    X0 = np.array( [pow(g, i, p) for i in range(0, p-n, n) ] )
    certificates_master = np.array([ pow(g, i, p) for i in range(n) ])
    C_minus_X0 = ( ( certificates_master[:, np.newaxis] - X0 ) % p )
    C_minus_X0_sets = [ set(L) for L in C_minus_X0 ]
    Xs = [{pow(g, x+i, p) for x in range(0, p-n, n)} for i in range(n)]
    forb_cycles = []
    for i in range(m):
        for j in range(i+m,n+m):
            if not bool(Xs[i].intersection(C_minus_X0_sets[j%n])):
                forb_cycles.append((0,i,j%n))
    return sorted(forb_cycles)
