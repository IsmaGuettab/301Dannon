# 301Dannon
Benchmarking d'algorithme 

Notes temporaire


On vous demande 5 Algorithmes, on va traiter en détails chaque algo.

L'algo du  tri de selection.

On parcourt tout le tableau pour trouver  le plus petit élements du tableau, et le placer à la première position, on recommence l'opération en cherchant le 2ème plus petit élement
en commencant à la deuxième position du tableau. Le plus petit élément trouvé est placé à la deuxième position. Après chaque nouvel élement positionné on réitère notre recherche
en commencait par la position suivante du tableau et ce, jusqu'à la fin du tableau

Le tri par insertion.

On a une variable temp qui sera notre clé, on considère que le premier élement ne bouge pas, et que l'élement numéro 1 devient la clé (la variable temporaire) et on compare
la clé aux valeurs précédentes, si la clé est + petite que la valeur précédente, alors on fait glisser la valeur précédente sur la case de l'élément numéro 1.

Une fois que tout est trié, on part sur l'élément numéro 2 de liste qu'on va mettre en tant que clé. On compare la valeur de la clé aux élements précedents, que nous avon déjà
ordonéess	 


Tri à bulle

Le tri à bulle c'est un des plus connus je pense que vous le connaissez tous, pour rappel le tri à bulle à pour but de prendre les 2 premiers élements d'une liste et 
d'inverser leur position si ils ne sont pas triés , une fois cela fait, on incrémente notre index dans la liste et on continue de changer la position des 2 valeurs jusqu'à la fin de la liste
On remarquera qu'à la fin de notre premier tour le plus grand élement de la liste sera bien positionné à la fin. On isole cet élement et on recommence le processus.

Le tri fusion

Pour faire un tri par fusion il y a 2 étapes, l'étape de découpe, et l'étape de tri/fusion.

La phase de découpe fonctionne de la manière suivante :  

On découpe le tableau principal en 2 sous tableaux.

Chaque sous tableaux sera découpé en 2 sous-tableaux égaux.

on continue comme ceci jusqu'à obtenir des sous tableaux de taille 1 

Pour la phase de fusion : 
On fusionne les sous-tableaux 2 à 2 de facon à obtenir des sous tableaux de tailles 2 triés
On fusionne les sous-tableaux 2 à 2 de facon à obtenir des sous tableaux de tailles 4 triés
Ainsi de suite jusqu'à l'obtention du tableau entier.


Le tri rapide

On a un tableau et on choisit un pivot.
Le tri rapide utilise un pivot en 2 petits tableaux, dans lesquels un tableau va contenir des valeurs plus petit que le pivot et un autre tableau va contenir des valeurs plus grandes que le pivot.
On compare le pivot en partant des élements par la gauche, si l’élément est plus petit que le pivot, on passe à l’élément suivant. Si l’élement est supérieur au pivot on les swap.
Après le swap on commence à comparer par la fin.
Cette fois -ci, si l’élement est plus grand que le pivot on va à l’élement suivant sinon si il est plus petit on les swap.
Une fois que nous avons nos deux tableaux. on prend celui de gauche on choisit un pivot et on applique la même logique.
Une  fois que le tri est fait on isole le pivot et on prend les autres élements dans un sous tableau et on recommence.

