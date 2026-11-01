# Create password encryption program 
import base64

def encrypt_pass(password):
    encode_bypt = base64.b64encode(password.encode())
    print(encode_bypt)


user_pass = (input('Enter your password: '))
print(encrypt_pass(user_pass))


# output is b'cGFzcw==' this is base64 part of the password