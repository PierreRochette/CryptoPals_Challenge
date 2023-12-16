# int(a, base)
# a : number to be converted to int
# base : base of the number
# 'hex' system = number system consisting of 16 symbols, so hex base is 16 

# CRYPTOPALS SET 1 CHALLENGE 2 : FIXED XOR

hex_value1 = "1c0111001f010100061a024b53535009181c"
hex_value2 = "686974207468652062756c6c277320657965"
#step 1-2

bin_value1 = bin(int(hex_value1, 16))[2:]
bin_value2 = bin(int(hex_value2, 16))[2:]

#step 3

desired_length = len(bin_value1) if len(bin_value1) > len(bin_value2) else len(bin_value2)
bin_value1 = bin_value1.zfill(desired_length)
bin_value2 = bin_value2.zfill(desired_length)
#step 4


result = [int(bit1) ^ int(bit2) for bit1,bit2 in zip(bin_value1,bin_value2)]

string_result = "".join([str(bits) for bits in result])
print("String result : (provided)", string_result)
print(type(string_result))


string_result = "".join(str(bit) for bit in result)
print("String result (test) : ", string_result)
print(type(string_result))

#step 5
final_output = hex(int(string_result, 2))[2:]