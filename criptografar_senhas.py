import base64
def encript_password(password):

    password_bytes = password.encode('utf-8')
    encode_bytes = base64.b64encode(password_bytes)
    return  encode_bytes.decode('utf-8')


user_pass = input("Digite a senha para criptogafar:")
encripted_password = encript_password(user_pass)
print(f"A senha criptograda é {encripted_password}")

