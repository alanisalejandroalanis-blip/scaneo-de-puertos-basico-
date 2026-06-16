import socket
import sys
#empezamos guardando en variables lo que capture sys 
ip = sys.argv[1]

puerto = int (sys.argv[2])

#aqui guardamos los parametros de socket que vamos a usar en una variable como .AF_INET que le dice que vamos a usar ipv4 y SOCK_STREAM le dice que use el protocolo tcp
sockete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#aqui usamos la variable que creamos en este caso sockete y con el .connect_exe le decimos executalo con los parametro que le pones dentro de los parentesis en este caso son ip y puerto lo que capturo sys 
resultado = sockete.connect_ex((ip,puerto))

if resultado == 0: print ("efectivamente estimado el puerto ", puerto, " esta abierto")
