import math
def leibnizPi(init):
    jmenovatel = 1
    vysledek = 0
    count = 1
    while count <= init:
        if count%2==0:
            vysledek -= 4/jmenovatel
            jmenovatel+=2
            count+=1
        else : 
            vysledek += 4/jmenovatel
            jmenovatel+=2
            count+=1
                
    return vysledek
     
 
 
def nilakanthaPi(iterations):
    jmenovatel = 3
    vysledek = 3
    count = 1
    for i in range (iterations-1):
            vysledek += count*(4.0/(jmenovatel*(jmenovatel-1)*(jmenovatel+1)))
            count*=-1
            jmenovatel+=2     
    return vysledek
 
 
def newtonPi(iterations:float)-> float:
    predchozi = iterations
    while True:
        sinn = math.sin(predchozi)
        coss = math.cos(predchozi)
        vysledek = predchozi - (sinn/coss)
        if abs(vysledek - predchozi) <= 1e-14:
            return vysledek
        predchozi = vysledek    
         