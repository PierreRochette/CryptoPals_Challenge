# ENONCE : SINGLE-BYTE XOR CYPHER

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

# SITES CONSULTES

https://www.codementor.io/@arpitbhayani/deciphering-single-byte-xor-ciphertext-17mtwlzh30



# ABOUT BYTES

Un byte est un groupe de 8 bits. Un bit peut être 1 ou 0. 
Un byte correspond à 256 combinaisons différentes (2^8). 

## FONCTION SINGLE_BYTE_XOR

Le paramètre "text" prend un texte sous forme de bytes : le texte doit être encodé en bytes avant d'être passé à la fonction. 

Le paramètre key doit être compris entre 0 et 255. Il s'agit d'une clef de chiffrement. 

### Détails

Le retour de la fonction est une liste. 
