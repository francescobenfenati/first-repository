#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_for_equals(a):                               #restituisce liste degli indici di membri uguali
    coppie = []
    
    for i in range(len(a)):
        if i != 0:                          #istruzioni dal secondo elemento
            for x in range(0,i+1):          #cerca se c'è uno uguale fra precedenti
                if a[i]!=a[x]:
                    continue
                elif x==i:                  #se non c'è nessuno uguale procedi
                    coppia = []
                    coppia.append(i)
                    for j in range(i+1,len(a)): #cerca gli uguali fra i successivi
                        if a[i]==a[j]:
                            coppia.append(j)    #appendi ogni indice trovato uguale
                        else:
                            continue
                    if len(coppia)!=1:          #appendi l'array di indici uguali solo se >1
                        coppie.append(coppia)
                else:                           #se uno uguale fra precedenti skippa e procedi
                    break
    
        if i == 0:                          #istruzioni per primo elemento (uguali a sopra)
            coppia=[]
            coppia.append(i)
            for j in range(i+1,len(a)):
                if a[i]==a[j]:
                    coppia.append(j)
                        else:
                            continue
                                if len(coppia)!= 1:
                                    coppie.append(coppia)
                            

                                        return coppie

a = ['francesco','sara','mario','sara','roberto','francesco','mario','mario']
b = [3,2,5,6]
print(check_for_equals(a))

