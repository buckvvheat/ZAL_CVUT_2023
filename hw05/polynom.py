def polyEval(poly, x):
    vysledek = 0
    for i in range(len(poly)):
        curr_vysledek = poly[i]*(x**i)
        vysledek += curr_vysledek
    return vysledek
 
def polySum(poly1, poly2):
    poly3 = []
    delka = max(len(poly1), len (poly2))
    if len(poly1) < delka:
        poly1 += [0] * (delka - len(poly1))
    if len(poly2) < delka:
        poly2 += [0] * (delka - len (poly2))
    for i in range(delka):
       poly3.append(poly1[i] + poly2[i])
    while poly3[-1] == 0:
        poly3.pop()
    return poly3
 
def polyMultiply(poly1, poly2):
    poly3 = [0]*(len(poly1) +len (poly2)-1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            poly3[i + j] += poly1[i] * poly2[j]
    return poly3