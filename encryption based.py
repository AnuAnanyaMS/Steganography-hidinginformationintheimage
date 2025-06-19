#secret, key stegno stego object + encryption key cipher
import cv2
import string
import os
from Crypto.Cipher import AES #AES cipher
from Crypto.Util.Padding import pad, unpad #ensure input text fits AES Block size
from Crypto.Random import get_random_bytes
import hashlib

#key generation
#encryption
#decryption

def derive_key(userkey):
    return hashlib.sha256(userkey.encode()).digest()[:16]

def encrypt_message(msg,userkey):
    key=derive_key(userkey) #hashing key
    cipher=AES.new(key, AES.MODE_CBC) #AES Cipher
    ct=cipher.encrypt(pad(msg.encode(),AES.block_size))
    return cipher.iv + ct

def decrypt_message(cipher_bytes,userkey):
    key=derive_key(userkey) #hashing key
    iv=cipher_bytes[:16]
    ct=cipher_bytes[16:]
    cipher=AES.new(key,AES.MODE_CBC,iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

d={}
c={}
for i in range(256):
    d[chr(i)]=i
    c[i]=chr(i)

x=cv2.imread(r"C:\Users\Anu\Downloads\WhatsApp Image 2025-06-18 at 7.37.04 PM.jpeg")
print(x)

key="0701"
text="TOP secret"

encrypted_bytes=encrypt_message(text, key)
l=len(encrypted_bytes)
print(l)

n=0 #number of rows
m=0 #number of columns
z=0 # colour panel
kl=0
for i in range (l):
    x[n,m,z]=encrypted_bytes[i]^d[key[kl]] #important
    #print(f"Embedding '{text[i]}' (ASCII {d[text[i]]}) XOR '{key[kl]}' (ASCII {d[key[kl]]})={new_val} at pixel ({n},{m},{z}) {orig_val}]")
    n=n+1
    m=m+1
    m=(m+1)%3
    z=(z+1)%3
    kl=(kl+1)%len(key)

cv2.imwrite("encrypting.jpg",x)
os.startfile("encrypting.jpg")
print("Success")
