#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:05:49 2018

@author: epassaro
"""

import sys
import csv

#%%

def check_len(x,n):
    
    if len(x) != n:
    
        print("\n\nERROR: Número de dígitos incorrecto.")
        input("\n<<< Presione ENTER para salir >>>")
    
        sys.exit(1)
    
    pass


#%%
    
def check_key(k,d):
    
    if k in d:
      
        pass
    
    else:
        
        print("\n\nERROR: Sucursal desconocida.")
        input("\n<<< Presione ENTER para salir >>>")
    
        sys.exit(1)
    
    pass
        

#%%
    
def get_digit(dif):
    
    for i in range(10):

        if i != 0 and dif == i:
            dv = i

        if i == 0 and dif == 10:
            dv = i
    
    return dv

    
#%%

bapros = {}
with open('/home/epassaro/Desktop/bapro_sucursales.csv') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    next(csv_reader) # Skips header    
    for row in csv_reader:
        bapros[row[0]] = row[1]


#%%

print("\n////// CALCULADORA CBU BAPRO //////\n")
    
x1 = [0,1,4]

sucursal = input("SUCURSAL (4 dígitos): ")
check_key(sucursal, bapros)
x2 = [ int(i) for i in bapros[sucursal] ]
check_len(x2,4)

cuenta = input("CUENTA (7 dígitos): ")
x3 = [ int(i) for i in ("03" + sucursal + cuenta) ]
check_len(x3,13)


#%% 

sum1 = sum([ a*b for a,b in zip(x1,[7,1,3]) ]) + sum([ a*b for a,b in zip(x2,[9,7,1,3]) ])
dif1 = 10 -int(str(sum1)[-1])
dv1 = get_digit(dif1)
    
sum2 = sum([ a*b for a,b in zip(x3,[3,9,7,1,3,9,7,1,3,9,7,1,3]) ])
dif2 = 10 -int(str(sum2)[-1])
dv2 = get_digit(dif2)
        

#%%

print("\nCBU: 014" + bapros[sucursal] + str(dv1) + "03" + str(sucursal) + str(cuenta) + str(dv2))
input("\n<<< Presione ENTER para salir >>>")

sys.exit(0)