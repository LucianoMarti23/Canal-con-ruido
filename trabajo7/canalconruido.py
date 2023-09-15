import socket
import random
def EnviarCadenas(peticion):   # Creo una funcion para enviar los mensajes independientemente si sufrio modificaciones o no
    mi_socket = socket.socket()

    mi_socket.connect(('192.168.1.2' , 10000)) # la conexion con la ip y el puerto de comunicacion pactado


   
    nueva =  canal_con_ruido(str(peticion)) # nueva hace referencia al mensaje , puede o no haber recibido modificacion
    mi_socket.send(nueva.encode("utf-8"))

    mi_socket.close()


def separacionhash(cadena): # Funcion creada para separar el dato enviado del hash
    indicecorte = 0  
    cadenaDato = ""
    for i in cadena:
        if i == "/":
            break
        cadenaDato +=i    
        indicecorte+=1
        
    return [cadenaDato , indicecorte+1]

def canal_con_ruido(cadena:str): # funcion creada para modificar la cadena segun el % de aleatoridad pactado (30%)
        cadenaDos  = separacionhash(cadena)
        cadenaDato = cadenaDos[0]
        cadenahash = cadenaDos[1]
    # Calcula el porcentaje de cadenas que deben ser modificadas
        porcentaje_modificacion = 0.3
    
    # Verifica si la cadena debe ser modificada
        if random.random() <= porcentaje_modificacion:
                cadena_modificada = ""
                cadenaDato += random.choice('abcdefghijklmnopqrstuvwxyz')
                return cadena_modificada + cadenaDato + "/" + cadena[cadenahash:]
    
        # Modifica la cadena original
        
        else:
        # No se realiza ninguna modificación en la cadena
            return cadena














miotro_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creacion de la parte de escucha con el cliente

miotro_socket.bind(('127.0.0.1' , 10001)) # direccion y puerto pactado
miotro_socket.listen(5)

while True: 
    conexion , adres = miotro_socket.accept()
    peticion = conexion.recv(1024)
    EnviarCadenas(peticion) # Envio la cadena al "Destinatario"

    





