import socket
import rsa

from Crypto.PublicKey import RSA

import AES


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 9998))
    server_socket.listen(5)
    print ("Server is listening....")
    (server_pubkey, server_privkey) = rsa.newkeys(512)

    connection, address = server_socket.accept()
    print(f"Connection from {address} has been established!")
    connection.send(server_pubkey._save_pkcs1_pem())
        
    encrypted_key = connection.recv(1024)
    AES_key = rsa.decrypt(encrypted_key, server_privkey)
    print("AES key: {}".format(AES_key))
    
    while True:
        message = connection.recv(1024)
        decrypted_data = AES.decrypt(AES_key, message)
        
        if not decrypted_data:
            break
        
        print("From connected user: " + str(decrypted_data.decode()))
        
        data = input("You: ")
        encrypted_data = AES.encrypt(AES_key, data.encode())

        connection.send(encrypted_data)
    
    connection.close()
    
        
        
if __name__ == '__main__':
    server()