import sys

# ['pwd_2.py', 'add', 'update']

if sys.argv[1] == "add":
    usuario = input("Digite o username: ")
    chave = input("Crie uma senha: ")

    try:
        with open("password.txt","x") as password:
            password.close()
    except FileExistsError:
        with open("password.txt","a") as password:
            password.write(usuario + ":" + chave + "\n")
            password.close()

if sys.argv[1] == "update":
    with open("password.txt","r") as password:
        usuario = str(input("Digite Seu usuario: ")).strip()
        verify = password.readlines()
        entrou = False
        for linha in verify:
            usuario1,senha = linha.split(":")
            if usuario1 == usuario:
                senha_nova = str(input("Digite Nova senha: "))
                entrou = True
                break
    if not entrou:
        print("Usuario Não existe")
        password.close()

print("#####################################")