import hashlib
import os

def gerarsal():
    salsa = os.urandom(32)
    return salsa

sal = gerarsal()

try:
    with open("senhas.txt","x") as dados:
        dados.close()
except:

    usuario = input('Digite o Usuario:')
    senha = input('Digite a senha:')

    chave = hashlib.pbkdf2_hmac('sha256', senha.encode('utf8'), sal, 100000)
    chave = chave.hex()
    print(chave)


    with open("senhas.txt","a") as dados:
        dados.write(usuario + ":" + chave + "\n")
        dados.close()

print("sucesso")