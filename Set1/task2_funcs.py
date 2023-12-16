# STEP 1 : Convert hexadecimal value to integer
def hex_to_int(hexvalue) :
    return int(hexvalue)

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