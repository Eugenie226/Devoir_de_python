def transform(chain):
    liste1 = set(map(int, chain[0].split(', ')))
    liste2 = set(map(int, chain[1].split(', ')))
    intersection = liste1.intersection(liste2)

    if intersection:
        #Trions les entiers et les convertir en chaine de caractère
        resultat = ','.join(map(str, sorted(intersection)))
        #Ajoutons ":nom_prenom_classe" à la fin de la chaine trié
        resultat += ":nom_prenom_classe"
        return resultat
    else:
        return None
        
# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out) # doit afficher ---> 31,4,1:nom_prenom_classe
    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out) # doit afficher ---> None
        
    