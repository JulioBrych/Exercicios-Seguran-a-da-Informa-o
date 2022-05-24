import os

from path import Path
caminho = "Binario.bin"
s = open(caminho,"wb")
s.write("Ola Mundo".encode())
split = os.path.splitext(caminho)
print(split[1])
s.close()
e = open("Binario.bin","rb")
a = e.read(1)
print(type(e.read(1)))