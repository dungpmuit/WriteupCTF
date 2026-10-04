#!/usr/bin/env python

from random  import shuffle

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}"
test_result_del_for_prod   = "ctdrPaqyQM_ygp{dk[{gAiWn|}WOpScJu]NVsOoUDaniktblIemT`hwHyMnif"

def encrypt(s, m):
    betalph = [c for c in alphabet]
    shuffle(betalph)

    for i, c in enumerate(s):
        betalph[m*i % len(betalph)] = c
    
    return ''.join(betalph)

def decrypt(c, m):
    print("TODO: Implement for prod")
    return c

if __name__=='__main__':
    secret = input("Secret: ")
    a = int(input("A: "))
    
    result = encrypt(secret, a)
    print("Here is your encoded message: ", result)
