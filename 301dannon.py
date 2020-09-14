#!/usr/bin/env python


 from math import pi
import sys
import os
import datetime

fusion_res = 0
quick_res = 0


def tri_par_selection(tab): 
    compteur = 0
    nb = len(tab)
    for elem in range(0, nb):
        plus_petit = elem
        for j in range(elem + 1, nb):
            compteur += 1
            if tab[j] < tab[plus_petit]:                  #On parcourt tout le tableau pour trouver  le plus petit élements du tableau, et le placer à la première position, on recommence l'opération en cherchant le 2ème plus petit élement
                plus_petit = j                            #en commencant à la deuxième position du tableau. Le plus petit élément trouvé est placé à la deuxième position. Après chaque nouvel élement positionné on réitère notre recherche
        if min is not elem:                               #en commencait par la position suivante du tableau et ce, jusqu'à la fin du tableau
            tmp = tab[elem]
            tab[elem] = tab[plus_petit]
            tab[plus_petit] = tmp
    return compteur


def tri_insertion(tab) :
    compteur = 0
    for i in range(1, len(tab)) :
        tmp = tab[i]
        j = i
        compteur = compteur + 1
        while j > 0 and tab[j-1] > tmp :                             #   On a une variable temp qui sera notre clé, on considère que le premier élement ne bouge pas, et que l'élement numéro 1 devient 
            tab[j] = tab[j-1]                                        #    la clé (la variable temporaire) et on compare la clé aux valeurs précédentes, si la clé est + petite que la valeur 
            compteur = compteur + 1                                  # précédente, alors on fait glisser la valeur précédente sur la case de l'élément numéro 1.
            j = j - 1
        tab[j] = tmp
    if compteur > 1 :
        print "tri par insertion : %d comparaisons" % compteur
    else:
        print "tri par insertion : %d comparaison" % compteur


                              
   


def     tri_a_bulles(mylist, size):
   tmplist = list(mylist)
   n = size
   compteur = 0
   for i in range (n - 1, 0, -1):
      for j in range(0, i, 1):
         if tmplist[j] > tmplist[j + 1]:
            tmp = mylist[j]                                          # prendre les 2 premiers élements d'une liste et                                           
            tmplist[j] = tmplist[j + 1]                              #inverser leur position si ils ne sont pas triés , une fois cela fait, on incrémente
            tmplist[j+1] = tmp                       # notre index dans la liste et on continue de changer la position des 2 valeurs jusqu'à la fin de la liste.
         compteur += 1
   print "tri à bulles :", compteur, "comparaisons"

def fusion(gauche, droite):
    result = []
    global fusion_res
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] < droite[index_droite]:
            result.append(gauche[index_gauche])
            index_gauche += 1
        else:                                                                 #On divise le tableau en 2 on a un tableau result qui sera le resultat de la fusion
            result.append(droite[index_droite])                               #du tableau de gauche et de droite , ensuite on divise les tableaux en sous tableaux    
        index_droite += 1                                                     #Jusqu'à obtenir  que des tableaux de un seul élement.
        fusion_res += 1                                                    
    if gauche:
        result.extend(gauche[index_gauche:])
    if droite:
        result.extend(droite[index_droite:])
    return result


def tri_fusion(m): 
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))



def partition(arr, petit, grand):
    i = (petit-1)         
    pivot = arr[grand]     # On choisit notre pivot
 
    for j in range(petit, grand):
        if arr[j] <= pivot:                           # Si le plus petit element est inférieur ou égal au pivot
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[grand] = arr[grand], arr[i+1]
    return (i+1)
 
def tri_rapide(arr, petit, grand):
    if len(arr) == 1:
        return arr
    if petit < grand:
        pi = partition(arr, petit, grand)  
        tri_rapide(arr, petit, pi-1)
        tri_rapide(arr, pi+1, grand)

def main():
    global fusion_res
    global quick_res
    try:
        sys.argv[1]
    except IndexError:
        exit(84)
    if sys.argv[1] == "-h":
        print(
            "USAGE\n\t./301dannon file\n\n\nDESCRIPTION\n\tfile\t le fichiers doit contenir que des chiffres et des nombres.")
        exit(0)
    if len(sys.argv) > 2:
        print("Il y a trop d'arguments")
        exit(84)
    if os.path.isfile(sys.argv[1]) == 0:
        print("Dommage, le fichier n'existe pas")
        exit(84)                                                           #gestion d'erreur & parsing du fichier
    if os.stat(sys.argv[1]).st_size == 0:
        print("Dommage le fichier est vide")
        exit(84)
    f = open(sys.argv[1], "r")
    content = f.read()
    try:
        elements = [float(s) for s in content.split()]
    except:
        print("Tout les caractères ne sont pas des nombres.")
        exit(84)
    if len(elements) <= 1:
        print("{} element".format(len(elements)))
    else:
        print("{} elements".format(len(elements)))
    if len(elements) >= 1000:
        sys.setrecursionlimit(len(elements) * 3)
    tmp = elements[:]
    nb = tri_par_selection(tmp)
    if nb <= 1:
        print("select sort: {} comparison".format(nb))
    else:
        print("select sort: {} comparisons".format(nb))
    tmp = elements[:]
    nb = insertion_sort(tmp)
    if nb <= 1:
        print("insertion sort: {} comparison".format(nb))
    else:
        print("insertion sort: {} comparisons".format(nb))
    tmp = elements[:]
    nb = bubble_sort(tmp)
    if nb <= 1:
        print("bubble sort: {} comparison".format(nb))
    else:
        print("bubble sort: {} comparisons".format(nb))
    tmp = elements[:]                                                              #on affiche le resultat de chaque algo de tri
    tri_fusion(tmp)
    if fusion_res <= 1:
        print("fusion sort: {} comparison".format(fusion_res))
    else:
        print("fusion sort: {} comparisons".format(fusion_res))
    tmp = elements[:]
    tri_rapide(tmp)
    nb = quick_res
    if nb <= 1:
        print("tri_rapide: {} comparison".format(nb))
    else:
        print("tri_rapide: {} comparisons".format(nb))
    return 0


if __name__ == '__main__':
    main()