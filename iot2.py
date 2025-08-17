import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(3)
print(ser.readline())

while True: 
    n = input("ingrese el mensaje: ")
    ser.write(n.encode('ascii')) 
    time.sleep(0.3)
    print(ser.readline())
    time.sleep(0.1)
    if n == 'x':
        print('Proceso finalizado')
        break

ser.close()


# Primera tarea: escribir en python permita entrar string como "Secuencia6 , repeticiones, velocidad"
# ejemplo : secuencia2,4, 100 milisegundos

# Segunda tarea: vcc:5v senal gnd 