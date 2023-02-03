import socket
import rsa
import os

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

import AES

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 9998))

(client_pubkey, client_privkey) = rsa.newkeys(512)

client_socket.send(client_pubkey._save_pkcs1_pem() )

server_pubkey = client_socket.recv(1024)
print(server_pubkey)
key = RSA.importKey(server_pubkey)
print("key: {}".format(key))

AES_key = os.urandom(16)
print(AES_key)
encrypted_key = rsa.encrypt( AES_key, key )
client_socket.send(encrypted_key)

data = b'Hello, World!'
encrypted_data = AES.encrypt(AES_key, data)

client_socket.send(encrypted_data)


