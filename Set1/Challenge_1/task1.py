import codecs
from base64 import b64decode, b64encode

# Convert hex => base64

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(string) :
    from base64 import b64encode, b64decode
    string_base64 = b64encode(bytes.fromhex(string)).decode()
    return string_base64

result = hex_to_base64(string)
print(result)