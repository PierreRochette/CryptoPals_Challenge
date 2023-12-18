def hex_to_base64(string) :
    from base64 import b64encode, b64decode
    string_base64 = b64encode(bytes.fromhex(string)).decode()
    return string_base64

