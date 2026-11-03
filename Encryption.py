# Create password encryption program 
# This for encode 
import base64

def encrypt_pass(password):
    encode_byte = base64.b64encode(password.encode())
    print(encode_byte)


user_pass = (input('Enter your password: '))
print(encrypt_pass(user_pass))


# output is b'cGFzcw==' this is base64 part of the password

import base64

def encrypt_pw(password):
    encode_byte = base64.b64encode(password.encode)
    print(encode_byte)


user_input = input('Take your password: ')
print(encrypt_pw(user_input))


# the output of encode is called byte such as :  b'U2VlbmppcmF3aW5AMjU0OA==' of Seenjirawin@2548

# this is for decdoe
import base64

def decode_pass(password):
    decode_byte = base64.b64decode(password)
    decode_data = decode.byte.decode()
    print(f'decoded password {decode_data}')
   



user_string= input('Enter the base64 string: ')
decode_pass(user_input)