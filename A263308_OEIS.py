""" This program generates the data for the entries in OEIS sequence number A263308.
It does NOT simply print the sequence verbatim. Please see the article referenced in the OEIS entry. """ 

import numpy as np
import itertools
from copy import copy
from sympy.ntheory.residue_ntheory import primitive_root
def psieve():
    for n in [2, 3, 5, 7]:
        yield n
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:
            step = D.pop(i)
        elif i < psq:
            yield i
            continue
        else:
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step
def check_p_m_v6(p, m, g):
    ''' checks a prime p with primitive root g for m colors '''
    X0 = np.array( [pow(g, i, p) for i in range(0, p-m, m) ] )
    certificates = np.array([ pow(g, i, p) for i in range(m) ])
    C_minus_X0 = ( ( certificates[:, np.newaxis] - X0 ) % p )
    C_minus_X0_sets = [ set(L) for L in C_minus_X0 ]
    for i in range(m):
        Xi = {pow(g, x+i, p) for x in range(0, p-m, m)}
        for j in range(i, m):
            if bool(Xi.intersection(C_minus_X0_sets[j])) == bool(j == 0):
                return False
    return True
def main(mikelist):
    ''' Accepts a list of m's, checks all candidate primes until it finds one that works.
        Will NOT terminate for m=8 or m=13 '''
    lget = primitive_root     ### GIVE FUNCTIONS LOCAL NAMES ###
    lcheck = check_p_m_v6
    with open("401output.csv", 'a') as file:
        for mike in mikelist:
            primes = psieve()
            prime = next(primes)
            while prime < 2*mike**2 - 4*mike:
                prime = next(primes)
            while True:
                if (prime-1)/2 % mike == 0:
                    gen = lget(prime)
                    p_out = lcheck(prime, mike, gen)
                    if p_out == True:
                        print( mike, prime, gen )
                        file.write(str(mike) + ', ' + str(prime) + ', ' + str(gen) + '\n')
                        break
                prime = next(primes)
mrange = list(range(2, 8)) + list(range(9, 13)) + list(range(14, 101))  # a good place to start
main(mrange)





