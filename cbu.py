#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:05:49 2018

@author: epassaro
"""

import sys

#%%

def check_len(x,n):
    
    if len(x) != n:
    
        print("\n\nERROR: Número de dígitos incorrecto.\n")
        input("\n<<< Presione ENTER para salir >>>")
    
        sys.exit(1)
    
    pass

    
def get_digit(dif):
    
    for i in range(10):

        if i != 0 and dif == i:
            dv = i

        if i == 0 and dif == 10:
            dv = i
    
    return dv


#%%

print("\n////// CALCULADORA CBU //////\n")
print("author: epassaro15@gmail.com\n\n")
    
banco = input("ENTIDAD BANCARIA (3 dígitos): ")
x1 = [ int(i) for i in banco ]
check_len(x1,3)

sucursal = input("SUCURSAL (4 dígitos): ")
x2 = [ int(i) for i in sucursal ]
check_len(x2,4)

cuenta = input("CUENTA (13 dígitos): ") 
x3 = [ int(i) for i in cuenta ]
check_len(x3,13)


#%%

sum1 = sum([ a*b for a,b in zip(x1,[7,1,3]) ]) + sum([ a*b for a,b in zip(x2,[9,7,1,3]) ])
dif1 = 10 -int(str(sum1)[-1])
dv1 = get_digit(dif1)

sum2 = sum([ a*b for a,b in zip(x3,[3,9,7,1,3,9,7,1,3,9,7,1,3]) ])
dif2 = 10 -int(str(sum2)[-1])
dv2 = get_digit(dif2)

        
#%%

print("\nCBU:", banco + sucursal + str(dv1) + cuenta + str(dv2), "\n")
input("\n<<< Presione ENTER para salir >>>")

sys.exit(0)