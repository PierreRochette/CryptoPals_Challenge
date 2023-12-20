xstring = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

import task3_funcs as f3

print("a")
text = b'a'
print("Texte :" , text)
print(type(text))

for b in text : 
    f3.infos(text)
    test_array = []
    f3.infos(b)
    result = b ^ 69
    f3.infos(result)
    test_array.append(result)
    

print("Test_array : ", test_array)

print("TEST")
print(b'a')
print(b'\x61')
print(b'97')
print(b'1')