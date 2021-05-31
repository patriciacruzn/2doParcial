
"""
Created on Fri May 28 17:14:55 2021
@author: patricia cruz
"""
import pandas as pd
import numpy as np
import random as rn


def lectura():
    data = pd.read_csv("uno.csv")
    nodos = list(data.columns)
    distancias = np.array(data)
    return nodos, distancias
def generar_Poblacion(n, nc):
    pob = []
    for i in range(n):
        orden = []
        for i in range(nc):
            a = rn.randint(0, nc-1)
            while a in orden:
                a = rn.randint(0, nc-1) 
            orden.append(a)
        
        pob.append(orden)
    return pob 
def evaluar_Camino(cmn,dist):
    cmn.append(cmn[0])
    sum = 0
    for i in range(len(cmn)-1):
        sum += dist[cmn[i]][cmn[i+1]]*2
    return sum
def normalizar(l):
    s = 0
    nl = []
    for i in l:
        s+=i
    ns = 0
    for i in l:
        v = s-i
        ns+=v
        nl.append(v)
    for i in range(len(nl)):
        nl[i] /=ns
    sl = 0
    for i in nl:
        sl+=i
        
    return nl
def cruzar(pob, dist):
    fitness = []
    for i in pob:
        ev = evaluar_Camino(i, dist)
        fitness.append(ev)
    
    fitness = normalizar(fitness)
    
    for i in range(len(fitness)):
        fitness[i] =(int)(fitness[i]*len(fitness)*2)
    
    gen = []
    for i in range(len(fitness)):
        for j in range(fitness[i]):
            gen.append(pob[i])
    
    
    newPob = []
    for i in range(len(pob)):
        p1 = gen[rn.randint(0, len(gen)-1)]
        p2 = gen[rn.randint(0, len(gen)-1)]
        newPob.append(transversal(p1,p2))
    return newPob
    
def transversal(a,b):
    ini = rn.randint(0, len(a)-2)
    fin = rn.randint(ini+1, len(a)-1)
    newc = a[ini:fin]
    for i in b:
        if i not in newc:
            newc.append(i)
    return newc
def mutar(pob, pr):
    for i in pob:
        if (pr > rn.random()):
            a = rn.randint(0,len(i)-1)
            b = rn.randint(0,len(i)-1)
            i = intercambio(i, a, b)
    return pob 
def intercambio(a,i,j):
    b = a[i]
    a[i] = a[j]
    a[j] = b
    return a
def mejor_recorrido(pob, dist):
    k = -1
    mj = 1000000000000000000000
    for i in range(len(pob)):
        ev = evaluar_Camino(pob[i], dist)
        if(mj > ev):
            mj = ev
            k = i
    return k
def gen(lug, dist):
    rn.seed(100)
    pob = generar_Poblacion(50, len(lug))
    for i in range(5):
        pob = cruzar(pob,dist)
        pob = mutar(pob,0.1)
    indb = mejor_recorrido(pob, dist)
    bst= pob[indb]
    return bst[:-1], pob 


def mostrar(bst, distancias):
    print("El mejor recorrido: ", end = "\n\t")
    
    for i in bst:
        print(nodos[i], end = ", " if i != bst[len(bst)-1] else "\n")
    
  
    total = 0
    for i in range(len(bst)-1):
        total+= distancias[bst[i]][bst[i+1]]
    total+= distancias[bst[0]][bst[len(bst)-1]];
    
    print("Suma del recorrido: ",total)
    
    
if __name__ == "__main__":    
    nodos, distancias = lectura()
    print(nodos)
    print(distancias)
    bst, pob = gen(nodos, distancias)
    mostrar(bst, distancias)