# Fonction pour convertir un horaire en secondes
def conversion_temps(h, m, s):
    return h * 3600 + m * 60 +s

def temps_ecoule(h1,m1,s1,h2,m2,s2):
    T1 = conversion_temps(h1,m1,s1)
    T2 = conversion_temps(h2,m2,s2)
    temps_ecoule_seconde = abs(T1-T2)
    return temps_ecoule_seconde

# Fonction pour convertir une distance en mètres
def conversion_distance(km, m, cm):
    return km * 1000 + cm/100 + m

# Fonction pour calculer la vitesse en m/s
def vitesse(km, m, cm ,heures ,minutes, secondes):
    temps_secondes = conversion_temps(heures ,minutes, secondes)
    distance_m = conversion_distance(km, m, cm)
    if temps_secondes == 0:
        return 0 
    else:
        return distance_m / temps_secondes

# Test
heures , minutes, secondes = 2 , 30 , 45
temps = conversion_temps(heures, minutes, secondes)
print(f"L'horaire {heures}h {minutes}min {secondes}s = {temps} secondes.")


T = temps_ecoule(12, 9, 20 ,10, 29, 40)
print(f"Le temps écoulé entre les deux horaires en secondes est : {T} secondes.")

km, m, cm = 100 , 5 , 400
dist = conversion_distance(23, 400, 30)
print(f"La distence {km}km {m}m {m}cm = {dist}km")

vitesse_mps = vitesse(km, m, cm ,heures ,minutes, secondes)
print(f"la vitesse en m/s : {vitesse_mps}")