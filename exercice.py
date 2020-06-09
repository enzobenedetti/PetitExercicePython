# ici le resultat de l'exercice
# 1 - Lire le fichier data.txt
# 2 - calculer la somme des données
# 3 - Enregistrer le resultat dans un fichier result.txt
# Bon courage
f = open("data.txt")
data_str = f.read()
print(f"contenu {data_str}")

data = [int(x) for x in data_str.split(',')]

#Calculer la somme
s = 0
for x in data:
    s+=x

f.close()

f = open("result.txt", "wt")

f.write(str(s))
f.close()