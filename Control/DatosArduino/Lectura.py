import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()


def iluminacion(line):
   if int(line) < 800:
      dato = "noche"
   else:
      dato = "dia"
   return dato
while True:
   try:
      lineBytes = ser.readline()
      line = lineBytes.decode('utf-8').strip()
      print(line)

      mensaje = iluminacion(line).encode('latin-1')
      ser.write(mensaje)
      time.sleep(0.5)
   except KeyboardInterrupt:
      break
