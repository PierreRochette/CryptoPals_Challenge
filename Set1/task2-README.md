#TASK2

I was learning cryptography while doing all Cryptopals challenges. I did this readme so I can remember what I wrote. 
I know I could have resolved this challenge (and the other ones) quickier and easier, but I really wanted to decompose my code in little steps for a better understanding. 

Starting from now, everything will be written in French. Maybe I will translate it in english later. 

## STEP 1

Il faut d'abord convertir les deux valeurs héxadécimales fournies dans l'énoncé. 

Hex 1 : 1c0111001f010100061a024b53535009181c
Hex 2 : 686974207468652062756c6c277320657965

Pour effectuer des opérations mathématiques ou logiques, comme XOR, il est plus pratique de les convertir en entiers. Une fois converties, ces valeurs peuvent être traitées comme des nombres binaires, permettant de réaliser l'opération XOR de façon appropriée. C'est une pratique courante dans pour une plus grande simplicité et lisibilité du code. 

On utilise ici la fonction int(hex, base) où base est égal à 16. 

## STEP 2

Il faut ensuite convertir les deux entiers obtenus en valeurs binaires. C'est une étape essentielle pour réaliser l'opération XOR bit par bit. 

XOR est une opération binaire qui se réalise bit par bit : on compare les bits correspondant de deux nombres. En convertissant les entiers en binaire, on transforme les données d'une façon où chaque bit peut être comparé et manipulé individuellement. 

On utilise ici la fonction bin(value) pour convertir les hexadécimaux obtenus précédemment en nombre binaire. On enlève des valeurs binaires obtenues le préfixe "0b". 

## STEP 3 

On aligne ensuite la longueur des deux valeurs binaires obtenues avant d'effectuer l'opération XOR. 

On choisit la plus grande longueur. L'objectif est de s'assurer que les deux chaînes binaires ont suffisamment de bits. En choisissant la plus grande longueur, on garantit que tous les bits des deux chaînes sont pris en compte dans l'opération XOR. Les bits supplémentaires (s'il y en a) de la chaîne la plus longue sont conservés et des "0" sont ajoutés au début de la chaîne la plus courte pour l'aligner. 

On définit d'abord la valeur à choisir avec un if..else, on stocke le résultat obtenu dans une variable (desired_length) et on utilise ensuite la fonction zfill sur chacune des valeurs binaires, avec comme paramètre la variable desired_length. 

__Pourquoi égaliser la longueur des valeurs binaires ?__

XOR compare bit par bit : il faut que les valeurs aient le même nombre de bits. En ajoutant des zéros au début de la chaîne la plus courte, on aligne les deux chaînes en longueur. Les 0 ajoutés n'affectent pas le résultat de l'opération XOR. 

__Cela garantit que l'opération XOR est effectuée correctement sur chaque paire de bits__

## STEP 4

* On utilise ensuite la fonction zip() de Python, avec les deux valeurs binaires afin de créer des paires de bits. 

* On réalise l'opération XOR en convertissant chaque bit en entier, et on itère l'opération pour chaque paire de bits. 

* On stocke le résultat obtenu sous forme de liste (compréhension de liste). Il faut ensuite convertir ce résultat en string. 

## STEP 5

On convertit le résultat obtenu en valeur héxadécimale et on supprime les deux premiers caractères. 