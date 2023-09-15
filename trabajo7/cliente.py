import socket
import hashlib

def hashing(cadena): # Funcion para calcular el hash de la cadena

   hash_md5 = hashlib.md5()
   hash_md5.update(cadena.encode('utf-8'))
   resultado = hash_md5.hexdigest()
   return resultado







def mandarMensaje(mensaje : str): # funcion para mandar la cadena con su hash
   mi_socket = socket.socket()

   mi_socket.connect(('127.0.0.1' , 10001))
   mensae = mensaje + "/" + hashing(mensaje)
   return mi_socket.send(mensae.encode('utf-8'))








while True: # Aqui es donde se ingresa la cadena a enviar
   mensaje = input("Ingrese el mensaje que quiera mandar :  ")
   mandarMensaje(mensaje) # Enviamos el mensaje
   









