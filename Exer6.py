from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


#questa 1
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("ChavePrivada.txt", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("ChavePublica.txt", "wb")
file_out.write(public_key)
file_out.close()
print("Expoente:",key.e)
print("\nModulo:",key.n)

#questao 2
f = open('ChavePublica.txt','r')
key = RSA.import_key(f.read())
f.close()
file = open('textoSimples.txt','r')
data = file.read().encode("utf-8")
print("\nTexto Simples:",data)
encryptor = PKCS1_OAEP.new(key)
encrypted = encryptor.encrypt(data)
print("\nTexto Criptografado:",binascii.hexlify(encrypted))

#questa 3
f = open('ChavePrivada.txt','r')
key = RSA.import_key(f.read())
f.close()
encryptor = PKCS1_OAEP.new(key)
decrypted = encryptor.decrypt(encrypted)
print("\nTexto Descriptografado:",decrypted.decode())