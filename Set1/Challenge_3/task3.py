xstring = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

import task3_funcs as f3

test = f3.single_byte_xor(b'a', 69)
print(test)

result = bytes(test)
print("Result: ", result)
print(type(result))

test = f3.single_byte_xor(b'ab', 69)
print(test)

result = bytes(test)
print("Result: ", result)
print(type(result))

test = f3.single_byte_xor(b'abc', 69)
print(test)

result = bytes(test)
print("Result: ", result)
print(type(result))

test = f3.single_byte_xor(b'abcd', 69)
print(test)
print(type(test))

result = bytes(test)
print("Result: ", result)
print(type(result))

print(b'36')