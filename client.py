import socket
import rsa
import os

# from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

import AES
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(), 9998))
    server_pubkey = client_socket.recv(1024)
    key = RSA.importKey(server_pubkey)

    AES_key = os.urandom(16)
    encrypted_key = rsa.encrypt( AES_key, key )
    client_socket.send(encrypted_key)
    data = input("Write your message: ")
    
    while data.lower().strip() != 'bye':
        encrypted_data = AES.encrypt(AES_key, data.encode())
        client_socket.send(encrypted_data)

        message = client_socket.recv(1024)
        decrypted_data = AES.decrypt(AES_key, message)
            
        print("Server: " +decrypted_data.decode())
        data = input("You: ")
        
    client_socket.close()
    
if __name__ == '__main__':
    client()
        

