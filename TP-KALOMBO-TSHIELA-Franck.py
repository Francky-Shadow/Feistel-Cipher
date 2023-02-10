# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 08:00:55 2023

@author: Shadow-007
"""


def xor_funct_withdecallage(t1,t2):
    tab=[]
    decallagegauche=[]
    for j in range(0,4):
        tab.append(t1[j]^t2[j])
        
    decallagegauche.append(tab[2])
    decallagegauche.append(tab[3])
    decallagegauche.append(tab[0])
    decallagegauche.append(tab[1])
    return decallagegauche


def and_functwithdecallage(t1,t2):
    tab=[]
    decallagedroite=[]
    for j in range(0,4):
        tab.append(t1[j]&t2[j])
    decallagedroite.append(tab[3])
    decallagedroite.append(tab[0])
    decallagedroite.append(tab[1])
    decallagedroite.append(tab[2])
    return decallagedroite

def chiffrement(t1,t2):
    N=input("Veuillez entrer un bloc de taille 8 bits \n")
    bloc=list(N)
    permut=input("Veuillez saisir PI la clé de permutation \n")
    pi=list(permut)
    key=[eval(i) for i in bloc]
    yapermut=[eval(j) for j in pi]
    kw=[]
    for i in range(0,8):
        a=yapermut[i]
        kw.append(key[a])
    go=kw[0:4]
    do=kw[4:8]

    d1=[]
    for j in range(0,4):
        d1.append(go[j]^xor_funct_withdecallage(t1, t2)[j])

    g1=[]
    for j in range(0,4):
        g1.append(do[j]^(do[j]|xor_funct_withdecallage(t1, t2)[j]))

    d2=[]
    for j in range(0,4):
        d2.append(g1[j]^and_functwithdecallage(t1,t2)[j])
    g2=[]
    for j in range(0,4):
        g2.append(d2[j]^(do[j]|xor_funct_withdecallage(t1, t2)[j]))
    return d1
bloc=0
pi=0
N=0
"""while(len(bloc)<8 or len(pi)<8):"""
N=input("Veuillez entrer un bloc de taille 8 bits \n")
bloc=list(N)
permut=input("Veuillez saisir PI la clé de permutation \n")
pi=list(permut)


key=[eval(i) for i in bloc]
yapermut=[eval(j) for j in pi]


kw=[]
for i in range(0,8):
    a=yapermut[i]
    kw.append(key[a])
k1=kw[0:4]
k2=kw[4:8]
print("LES CLES GENEREES SONT \n")
print(xor_funct_withdecallage(k1, k2))
print(and_functwithdecallage(k1, k2))
print(chiffrement(k1, k2))