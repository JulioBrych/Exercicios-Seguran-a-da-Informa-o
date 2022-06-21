import hashlib
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from pathlib import Path
from tkinter.ttk import Combobox
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

from matplotlib.pyplot import get

caminho_do_arquivo_entrada = Path()
caminhho_chave_Privada = Path()
caminhho_chave_Publica = Path()

def selecionarArquivoEntrada():
    global caminho_do_arquivo_entrada
    global janela
    global tipoEntrada
    caminho_do_arquivo_entrada = Path(askopenfilename(
        title='Selecionar Arquivo',
        initialdir='/'))
    box1.config(text=caminho_do_arquivo_entrada)

def gerarChaves():
    keyPair = RSA.generate(bits=1024)
    priv = open("ChavePrivada.txt","w")
    priv.write(hex(keyPair.n))
    print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
    print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

janela = Tk()
janela.title("Exercicio 8")
janela.minsize(700,180)
label1 = Label(janela,text="Arquivo:")
label1.place(x=20,y=20)
box1= Label(janela,text=caminho_do_arquivo_entrada, width = 60)
box1.place(x=80,y=20)
botao1 = Button(janela,text="Buscar",command=selecionarArquivoEntrada)
botao1.place(x=450,y=15)
botao2 = Button(janela,text="Gerar Chaves",command=gerarChaves)
botao2.place(x=20,y=110)
janela.mainloop()