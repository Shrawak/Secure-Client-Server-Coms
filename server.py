import socket
import rsa
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

import AES
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 9998))
server_socket.listen(5)
print('listening')
(server_pubkey, server_privkey) = rsa.newkeys(512)
print(server_pubkey)


while True:
    client_socket, address = server_socket.accept()
    # Receive client's public key
    client_encrypted_pubkey = client_socket.recv(1024)
    client_pubkey = RSA.importKey(client_encrypted_pubkey)
    client_socket.send(server_pubkey._save_pkcs1_pem())
    
    encrypted_key = client_socket.recv(1024)
    AES_key = rsa.decrypt(encrypted_key, server_privkey)
    print(AES_key)

    print(f"Connection from {address} has been established!")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))
    message = client_socket.recv(1024)
    decrypted_data = AES.decrypt(AES_key, message)
    
    print(decrypted_data)
    # Close the socket
    # data = b'Hello, World!'
    # encrypted_data = AES.encrypt(AES_key, data)
    # client_socket.send(encrypted_data)
    
    client_socket.close()