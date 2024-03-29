#from pythonosc import udp_client
import socket

import RPi.GPIO as GPIO
import time


UDP_IP = "10.10.1.20"
UDP_PORT = 5005

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

KEYPAD = [
    [1,2,3,'A'],
    [4,5,6,'B'],
    [7,8,9,'C'],
    ["*",0,'#','D'] ]

ROW         = [7,11,13,15]
COL         = [12,16,18,22]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.sendto("TETCOS".encode('utf-8'), (UDP_IP, UDP_PORT))



for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        for j in range(4):
            GPIO.output(COL[j],0)
            
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    print (KEYPAD[i][j])
                    sock.sendto(str(KEYPAD[i][j]).encode('utf-8'), (UDP_IP, UDP_PORT))
                    while(GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()

