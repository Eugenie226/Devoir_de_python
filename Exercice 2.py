#Explication du programme
'''Importation du module operator
import operator

Création d'une liste lst1 contenant les nombres de 1200, une fin de 2000 avec un pas de 135
lst1 = list(range(1200, 2000, 135)) 

Création d'une liste lst2. Chaque élément i de lst1 est multiplié par 2 seulement si i est divisible par 2
lst2 = [i * 2 for i in lst1 if i % 2 == 0]  

Création d'un tuple numbers contenant les nombres de 1 à 9
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

Création d'une liste o en utilisant la fonction filter avec une fonction lambda et l'opérateur operator pour sélectionner les éléments pairs de numbers
o = list(filter(lambda x: operator.mod(x, 2) == 0, numbers))

Création d'une liste e en utilisant la fonction filter avec une fonction lambda et l'opérateur operator pour sélectionner les éléments impairs de numbers
e = list(filter(lambda x: operator.mod(x, 2) != 0, numbers))

Affichons des résultats
print(lst1)
print(lst2)
print(o)
print(e)'''

#Ecrivons un autre programme qui fait exactement la même chose (en utilisant des boucles et des conditions).
lst1=[]
lst2=[]
o=[]
e=[]
for i in range(1200, 2000, 135):
    lst1.append(i)

for i in lst1:
    if i % 2 == 0:
        lst2.append(i * 2)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for x in numbers:
    if x % 2 == 0:
        o.append(x)
    else:
        e.append(x)

# affichons des résultats
print(lst1)
print(lst2)
print(o)
print(e)



