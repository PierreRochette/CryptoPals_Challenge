def infos(parameter) : 

    infos = {
        'parameter' : parameter,  
        'type' : type(parameter), 
    }

    print(infos)

    return None

def single_byte_xor(text: bytes, key: int) -> bytes :

    return [b ^ key for b in text]

def single_byte_xor_bis(text: bytes, key: int) -> bytes :

    return bytes([b ^ key for b in text])