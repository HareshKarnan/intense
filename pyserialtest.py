from serial import *
import time
ser = Serial(port='/dev/ttyACM0',baudrate=115200,bytesize=EIGHTBITS,parity=PARITY_NONE,
                stopbits=STOPBITS_ONE)

ser.isOpen();
while(1):
    start_time = time.time()
    x=ser.readline()
    print 1.0/(time.time()-start_time) 
    
