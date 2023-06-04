"""
Possiveis erros!
Ultilize Python versão 3.5 pra cima
lembre-se de atualizar o pip com o comando: pip install --upgrade pip
verifique se o interpretador python esta configurado corretamente
Instale a biblioteca Tkinter caso não tenha: pip install tkinter
Instale a biblioteca PIL caso não tenha: pip insstall Pillow
Para executar o codigo, de preferencia abra um terminal e digite: python rad.py
Confira se os Endereçoes das Imagens estão corretos, atualmente são 3
Lembre de Estar com o Modulo testcrypt.py na mesma pagina do rad.py
Lembre de importar o modulo: from testcrypt import encryptar
"""
#!/usr/bin/python

import tkinter as tk #Importando a GUI tkinter que vai ser chamada usando "tk"
from PIL import Image, ImageTk #Biblioteca de processamento de imagem, para depois serem usadas no Tk
from tkinter import messagebox #Importando o messagebox
import sys
import hashlib
from testcrypt import encryptar

def testar():
    tela.withdraw()
    login()

def criar_arquivo():
    with open("dados.txt","w") as dadosabertos:
        admin_base = "123"
        admin_base = encryptar(admin_base)
        dadosabertos.write("admin:" + admin_base + "\n")
        dadosabertos.close()

try:
    with open("dados.txt","r") as ler:
        ler.close()
except FileNotFoundError:
    criar_arquivo()

def salvardados():
    global valor_usuario, valor_senha

    valor_usuario = entrada_usuario1.get()
    valor_senha = igualsenha1.get()
    existe = False

    with open("dados.txt","r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        if valor_usuario in linha:
            existe = True
            arquivo.close()
            break

    if existe:
        messagebox.showerror("Erro","Usuário já existe",parent=tela_adicionar)
        entrada_usuario1.delete(0,'end')
        igualsenha1.delete(0,'end')
        igualsenha2.delete(0,'end')
        entrada_usuario1.focus()
        print("não vai gravar")
    else:
        print("Vai gravar")
        with open("dados.txt","a") as dados0:
            valor_senha = encryptar(valor_senha)
            dados0.write(valor_usuario + ":" + valor_senha + "\n")
            dados0.close()
            messagebox.showinfo("SUUUUCESSO","Usuário adicionado corretamente")
            tela_adicionar.destroy()
            #tela.deiconify()
 
def login():
    global tela_login, usuario_verify, senha_verify, entrada_usuario, entrada_senha, wallpaper_login, label4, botao1, usuario, senha

    # Criação da janela de login
    tela_login = tk.Toplevel(tela)
    tela_login.title("Login")
    tela_login.geometry("400x300+500+200")
    tela_login.resizable(False, False)

    # Carregamento e redimensionamento da imagem de fundo
    fundo_login = Image.open(r"imagens\login.jpg")
    fundo_login = fundo_login.resize((400, 300), Image.LANCZOS)
    wallpaper_login = ImageTk.PhotoImage(fundo_login)

    # Criação do label para a imagem de fundo
    label4 = tk.Label(tela_login, image=wallpaper_login)
    label4.place(x=0, y=0, relwidth=1, relheight=1)
    label4.bind('<Configure>', attframewallpaper_login)

    # Criação das variáveis de verificação do usuário e senha
    usuario_verify = tk.StringVar()
    senha_verify = tk.StringVar()

    # Criação dos widgets de entrada de usuário e senha e do botão de login
    label2 = tk.Label(tela_login, text="Usuário", bg="White")
    label2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario = tk.Entry(tela_login, textvariable=usuario_verify)
    entrada_usuario.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entrada_usuario.focus()
    label3 = tk.Label(tela_login, text="Senha", bg="White")
    label3.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha = tk.Entry(tela_login, textvariable=senha_verify, show='*')
    entrada_senha.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    botao1 = tk.Button(tela_login, text="Login", width=10, height=1, command=lambda: verificarlogin(entrada_usuario.get(), entrada_senha.get()))
    botao1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    tela_login.bind('<Return>', pressionar_enter)
    # Configuração do comportamento do botão fechar da janela de login
    tela_login.protocol("WM_DELETE_WINDOW", fechar)
    
def verificarlogin(usuario, senha):
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        # separa a linha em usuário e senha usando o caractere ":" como separador
        usuario_arquivo, senha_arquivo = linha.strip().split(":")
        senha_hash = senha
        senha_hash = hashlib.sha256(senha.encode("utf8"))
        senha_hash = senha_hash.hexdigest()
        
        if usuario == usuario_arquivo and senha_hash == senha_arquivo:
            print("Acesso Liberado")
            tela_login.destroy()
            tela.deiconify()
            return True
        else:
            erro = True
    if erro == True:
        print("Acesso Negado")
        messagebox.showerror("Erro","Usuário ou senha Inválidos")
        entrada_usuario.delete(0,'end')
        entrada_senha.delete(0,'end')
        entrada_usuario.focus()

    return False

def pressionar_enter(event):
    botao1.invoke()

def pressionar_enter1(event):
    botao2.invoke()

def attframewallpaper_login(event):
    global wallpaper_login, label4
    
    # obtém a nova largura e altura da janela
    largura = event.width
    altura = event.height
    
    # redimensiona a imagem de fundo
    fundo_login = Image.open(r"imagens\login.jpg")
    fundo_login = fundo_login.resize((largura, altura), Image.LANCZOS)
    wallpaper_login = ImageTk.PhotoImage(fundo_login)
    
    # atualiza a imagem do label
    label4.configure(image=wallpaper_login)

def fechar():
    tela_login.destroy()
    sys.exit()

def criar_tela():
    global tela, wallpaper
    tela = tk.Tk() #Criando a janela Tkinter usando o construtor toolkit tkinter
    tela.geometry("800x600+350+200") #Aqui eu defino o width e height da janela, e o posicionamento inicial dela
    tela.resizable(False,False) #tornar False o redimensionamento da janela, tanto width quanto heigth 
    tela.title("RAD") #Titulo da aplicação
    fundo = Image.open(r"imagens\sound_2-wallpaper-1366x768.jpg") #abrindo a imagem
    fundo = fundo.resize((800,600), Image.LANCZOS) #Redimensionando a imagem
    wallpaper = ImageTk.PhotoImage(fundo) #Objeto Photoimage sendo criado e recebendo a imagem preparada "fundo", esse objeto é atribuido à variavel wallpaper
    label0 = tk.Label(tela, image=wallpaper) #É aqui que eu carrego a imagem na interface, estou criando um objeto label e atribuindo uma imagem como segundo argumento, o primeiro argumento é a 'tela' que é onde o label vai ser adicionado, tudo isso sendo atribuido à variavel label0
    label0.pack() #isso aqui posiciona o label0 no centro da tela
    tela.withdraw()

def fechar_adicionar():
    tela_adicionar.destroy()
    #tela.deiconify()

def criar_menu():
    # Vamo criar a barra de menu
    menubar = tk.Menu(tela) # Menu criado, atribuido à variavel menubar
    arquivo_menu = tk.Menu(menubar,tearoff=0) # arquivo_menu recebe o objeto menu,(menubar)/tearoff= Para que o usuario não separe o menu da janela
    editar_menu = tk.Menu(menubar,tearoff=0)
    ferramentas_menu = tk.Menu(menubar,tearoff=0)
    opcoes_menu = tk.Menu(menubar,tearoff=0)
    sobre_menu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Arquivo", menu=arquivo_menu) # O método add_cascade() é usado para adicionar um item de menu que abre um submenu
    menubar.add_cascade(label="Editar", menu=editar_menu) # Aqui eu estou criando varias opçoes na barra de menu
    menubar.add_cascade(label="Ferramentas", menu=ferramentas_menu) # Label argumento serve para colocar o texto na opção da menu bar
    menubar.add_cascade(label="Opções", menu=opcoes_menu) # O segundo argumento menu=arquivo_menu seleciona o menu que ta relacionado ao objeto
    menubar.add_cascade(label="Sobre", menu=sobre_menu) # tk.menu
    tela.config(menu=menubar) # Aqui a menubar esta sendo configurada, sendo associada à barra de menu da janela principal (tela) desse modo aparecendo no topo da janela principal (tela) permitindo que o menu seja acessado de qualquer tela da aplicação 
    arquivo_menu.add_command(label="Novo")
    arquivo_menu.add_command(label="Abrir")
    arquivo_menu.add_command(label="Salvar")
    editar_menu.add_command(label="Atualizar", command=testar)
    editar_menu.add_command(label="Copiar")
    editar_menu.add_command(label="Colar")
    editar_menu.add_command(label="Cortar")
    editar_menu.add_command(label="Pesquisar")
    sobre_menu.add_command(label="Creditos")
    sobre_menu.add_command(label="Versão")
    opcoes_menu.add_command(label="Idioma")
    opcoes_menu.add_command(label="Config")
    opcoes_menu.add_command(label="Config")
    opcoes_menu.add_command(label="Config")
    ferramentas_menu.add_command(label="Adicionar", command=adicionar_tela)
    ferramentas_menu.add_command(label="Visualizar")
    ferramentas_menu.add_command(label="Remover")
    ferramentas_menu.add_command(label="Buscar")
    ferramentas_menu.add_command(label="Filtrar")

def adicionar_tela():
    #tela.withdraw()
    global tela_adicionar, label5, igualsenha1, igualsenha2, botao2, botao3, entrada_usuario1, entrada_senha1, entrada_confirmar, botao2
    tela_adicionar = tk.Toplevel(master=tela)
    tela_adicionar.title("Adicionando Usuário")
    tela_adicionar.geometry("400x300+700+200")
    tela_adicionar.resizable(0,0)
    tela_adicionar.transient(tela)
    #tela_adicionar.overrideredirect(True)

    igualsenha1 = tk.StringVar()
    igualsenha2 = tk.StringVar()
    entrada_usuario1 = tk.StringVar()

    label5 = tk.Label(tela_adicionar, text="Usuário")
    label5.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario1 = tk.Entry(tela_adicionar)
    entrada_usuario1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    label6 = tk.Label(tela_adicionar, text="Senha")
    label6.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha1 = tk.Entry(tela_adicionar, textvariable=igualsenha1)
    entrada_senha1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label7 = tk.Label(tela_adicionar, text="Confirmar Senha")
    label7.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    entrada_confirmar = tk.Entry(tela_adicionar, textvariable=igualsenha2)
    entrada_confirmar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    botao2 = tk.Button(tela_adicionar, text="Salvar", width=10, height=1, command=verificar_igual, bg="#80ff80", activebackground="#b3ffb3")
    botao2.place(relx=0.2, rely=0.8)
    tela_adicionar.bind('<Return>', pressionar_enter1)
    botao3 = tk.Button(tela_adicionar, text="Cancelar", width=10, height=1, command=fechar_adicionar, bg="#ff3333", activebackground="#ff6666")
    botao3.place(relx=0.6, rely=0.8)

def verificar_igual():
    if len(igualsenha1.get()) > 0 and len(entrada_usuario1.get()) > 0:
        if igualsenha1.get() == igualsenha2.get(): 
            print("Sucesso")
            salvardados()
        else:
            messagebox.showerror("Erro","Verifique a senha criada", parent=tela_adicionar)
    else:
        messagebox.showerror("Erro","Não deixe vazia as entradas",parent=tela_adicionar)

criar_tela()
tela.withdraw()
login()
criar_menu()
tela.mainloop() #Chama a tela principal