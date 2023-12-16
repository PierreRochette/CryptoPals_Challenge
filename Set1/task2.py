# int(a, base)
# a : number to be converted to int
# base : base of the number
# 'hex' system = number system consisting of 16 symbols, so hex base is 16 

# CRYPTOPALS SET 1 CHALLENGE 2 : FIXED XOR

hex_value1 = "1c0111001f010100061a024b53535009181c"
hex_key = "686974207468652062756c6c277320657965"

from task2_funcs import Task2_func
resultat = Task2_func(hex_value1, hex_key)
print(resultat)
