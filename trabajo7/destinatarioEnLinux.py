import socket
import hashlib

def hashing(cadena): # Funcion para calcular el hash
    hash_md5 = hashlib.md5()
    hash_md5.update(cadena.encode('utf-8'))
    resultado = hash_md5.hexdigest()
    return resultado

def separacionHash(hola): # Funcion para separar el dato y el hash
        contadorIndice = 0
        cadenaDato = ""
        for i in hola[4:]:
             if i == "/":
                  break
             cadenaDato += i
             contadorIndice+= 1
        hash = ""
        for j in hola[contadorIndice+5:]:
                if j == "'":
                     break
                hash += j        

        return [cadenaDato , hash]


mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_socket.bind(('192.168.1.2' , 10000))
mi_socket.listen(5)

while True:
    conexion , adrres  = mi_socket.accept()
    print("Nueva conexion establecida")
    print(adrres)
    peticion = conexion.recv(1024)
    hola = str(peticion)
    verificacion = separacionHash(hola)
    if hashing(verificacion[0]) == verificacion[1]: # Evaluo si el hash coincide con el dato 
        print("Hash correcto")
        print(verificacion , hashing(verificacion[0]))
    else : print(f"Hash Incorrecto , \nhay un intruso! \n {verificacion[0]}" )    
    conexion.close()
        
    


