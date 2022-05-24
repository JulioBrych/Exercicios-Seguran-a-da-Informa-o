from Crypto.Cipher import AES
import base64

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE

# PKCS7 method
PADDING = '\x06'
mode = AES.MODE_CBC
iv = '\x08' * 16 # static vector: dangerous for security. This could be changed periodically
# 

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)



def CryptIt(password, secret):
    cipher = AES.new(secret, mode, iv)
    encoded = EncodeAES(cipher, password)
    return encoded

def DeCryptIt(encoded, secret):
    cipher = AES.new(secret, mode, iv)
    decoded = DecodeAES(cipher, encoded)
    return decoded