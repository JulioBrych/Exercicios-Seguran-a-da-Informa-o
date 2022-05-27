import hashlib
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from pathlib import Path
from tkinter.ttk import Combobox

from matplotlib.pyplot import get

caminho_do_arquivo_entrada = Path()

def selecionarArquivoEntrada():
    global caminho_do_arquivo_entrada
    global janela
    global tipoEntrada
    caminho_do_arquivo_entrada = Path(askopenfilename(
        title='Selecionar Arquivo',
        initialdir='/'))
    box1.config(text=caminho_do_arquivo_entrada)

def gerarhash():
    global caminho_do_arquivo_entrada
    selecionado = combo.current()
    if(len(caminho_do_arquivo_entrada.name) > 5):
        arquivo = open(caminho_do_arquivo_entrada,'rb')
        data = arquivo.read()
        resultado = ''
        if(selecionado == 0):
            resultado = hashlib.md5(data)
        elif(selecionado == 1):
            resultado = hashlib.sha1(data)
        elif(selecionado == 2):
            resultado = hashlib.sha256(data)
        else:
            messagebox.showerror("Erro!","Tipo de Hash Invalido")
        resultado = str(resultado.hexdigest())
        if(resultado != ''):
            if(resultado == hashComparacao.get()):
                messagebox.showinfo("Sucesso","Hash Compativel com o arquivo")
            else:
                messagebox.showerror("NOOP","Hash Incompativel com o arquivo")        
    else:
        messagebox.showerror("Erro!","Selecione um arquivo")

    
        


janela = Tk()
janela.title("Exercicio 7 - 2")
janela.minsize(700,180)
label1 = Label(janela,text="Arquivo:")
label1.place(x=20,y=20)
box1= Label(janela,text=caminho_do_arquivo_entrada, width = 60)
box1.place(x=80,y=20)
botao1 = Button(janela,text="Buscar",command=selecionarArquivoEntrada)
botao1.place(x=450,y=15)
label2 = Label(janela,text="Tipo de Hash:")
label2.place(x=20,y=50)
combo = Combobox(janela,values=["MD5","SHA-1","SHA-256"])
combo.place(x=100,y=50)
botao2 = Button(janela,text="Verificar",command=gerarhash)
botao2.place(x=20,y=110)
label3 = Label(janela,text="Hash:")
label3.place(x=20,y=80)
hashComparacao = StringVar()
saidaHash = Entry(janela,textvariable=hashComparacao,width=80)
saidaHash.place(x=60,y=80)
janela.mainloop()