# csgames_exam_dele_2018

# AI --> FruitSweeper

Basé sur MinesSweeper (Démineur), FruitSweeper est une version CLI du jeu. Lorsqu'on explore un carré
de la carte dans le jeu, on risque de tomber sur un fruit. Comme nous sommes allergiques
aux fruits, nous mourront instantannément. Si une case est explorée et elle ne contient rien, elle 
affiche le nombre de fruits qui sont autour, en comptant les diagonales. La valeur du chiffre que 
peut prendre une tuile est donc dans l'intervale [0,8]. Le nombre 0 signifie qu'aucun fruit n'est 
contenu dans les tuiles environnantes, tandis que 8 veut dire que la case est complètement entourée
de fruits! Ainsi, pour gagner, vous devez identifier la position de tous les fruits en les flaggant. 

##  VALEUR DE RETOUR 

Vous devez completer le fichier AI.py, la fonction play. Vous devez retourner un dictionnaire
qui suit le format suivant: 
      {"action":"[(explore)(flag)(unflag)]", "X":0, "Y": 0}

Les actions possibles sont:
	"flag" --> marque une case d'un P pour indiquer que l'on pense qu'il y a un fruit en dessous
	"unflag" --> retire le P et remet un X à la place, la case est de nouveau une simple case non
			explorée
	"explore" --> Explore la case de la carte pour savoir combien de fruits il y a autour

X représente la position en X où on veut faire l'action
Y représente la position en Y où on veut faire l'action

Ainsi, si je veux explorer la case [5,6] de la carte, je vais retourner l'objet suivant: 
	{"action":"explore", "X":5, "Y": 6}

## game_map --> paramètre d'entrée

Le paramètre game_map est une liste de listes de strings qui contient les détails du jeu 
comme il est présentement. Les valeurs possibles des cases de la liste à deux dimensions
sont donc les suivantes:
	"X" --> représente une case inexplorée. Au début, toutes les cases sont des X	
	"P" --> représente une case flaggée, on pense donc qu'il y a un fruit en dessous
	"2" --> un nombre représente le nombre de fruit autour de cette case. Les nombres
		peuvent prendre les valeurs [0,8]
