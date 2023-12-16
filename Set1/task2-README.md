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

On aligne ensuite la longueur des deux valeurs binaires pour qu'elles soient égales 