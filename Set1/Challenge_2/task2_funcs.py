# STEP 1 : Convert hexadecimal value to integer
def hex_to_int(hexvalue) :
    return int(hexvalue, 16)

# STEP 2 : Convert int value to bin value and remove prefix

def int_to_bin(intvalue) :
    return bin(intvalue)[2:]

# STEP 3.1 : Choose length to normalise bin values

def define_desired_length(binvalue1, binvalue2) : 
    if len(binvalue1) > len(binvalue2) :
        return len(binvalue1)
    else :
        return len(binvalue2)
    
## STEP 3.2 : Align binvalues length
    
def align_binvalues_length(binvalue, desired_length) :
    return binvalue.zfill(desired_length)

## STEP 4.1 : XOR

def XOR(binvalue1, binvalue2) :
    return [int(bit1) ^ int(bit2) for bit1, bit2 in zip(binvalue1, binvalue2)]

## STEP 4.2 : Convert list result to string

def list_to_string(list) : 
    return "".join(str(bit) for bit in list)

# STEP 5 : Convert string result to int then to hex
def final_ouput(string) :
    return hex(int(string, 2))[2:]

# NOW, all of this together : 

def Task2_func(hexvalue1, hexvalue2) : 

    int_value_1 = hex_to_int(hexvalue1)
    int_value_2 = hex_to_int(hexvalue2)

    bin_value_1 = int_to_bin(int_value_1)
    bin_value_2 = int_to_bin(int_value_2)

    desired_length = define_desired_length(bin_value_1, bin_value_2)

    aligned_bin_value_1 = align_binvalues_length(bin_value_1, desired_length)
    aligned_bin_value_2 = align_binvalues_length(bin_value_2, desired_length)

    xor = XOR(aligned_bin_value_1, aligned_bin_value_2)
    xor_to_string = list_to_string(xor)

    output_finale = final_ouput(xor_to_string)

    return output_finale
