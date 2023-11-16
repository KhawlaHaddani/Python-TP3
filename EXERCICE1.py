def somme(m,n):
    if m >= n:
        return -1
    else:
        totale = 0
        for i in range(m , n+1):
            totale += i
        return totale

resultat = somme(5,8)
if resultat == -1:
    print("erreur")
else:
    print(resultat)