from RPi import GPIO
import time
from time import sleep



import socket

GPIO.setmode(GPIO.BCM)
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = ""
UDP_PORT_NO = 5005
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
GPIO.setup(segments, GPIO.OUT, initial=0)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
GPIO.setup(digits, GPIO.OUT, initial=1)
 
#          (a,b,c,d,e,f,g,dp)
num = {' ':(0,0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0,0),
    '1':(0,1,1,0,0,0,0,0),
    '2':(1,1,0,1,1,0,1,0),
    '3':(1,1,1,1,0,0,1,0),
    '4':(0,1,1,0,0,1,1,0),
    '5':(1,0,1,1,0,1,1,0),
    '6':(1,0,1,1,1,1,1,0),
    '7':(1,1,1,0,0,0,0,0),
    '8':(1,1,1,1,1,1,1,0),
    '9':(1,1,1,1,0,1,1,0),
    'B':(1,1,1,1,1,1,1,1),
    'y':(0,1,1,1,0,1,1,0),
    'E':(1,0,0,1,1,1,1,0),
    'A':(1,1,1,0,1,1,1,0),
    'L':(0,0,0,1,1,1,0,0),
    'X':(0,1,1,0,1,1,1,0)}

 
def seg():
    for digit in range(4):
        GPIO.output(segments, (num[display_string[digit]]))
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)
try:
	while True:
	    data, addr = serverSock.recvfrom(1024)
	    print ("Message: ", data.decode('utf-8'))
	    display_string = data.decode('utf-8').rjust(4)
	    k = 100
	    while k >= 0:
	    	seg()
	    	k -= 1
	    

    # n = 9999
    # while n >= 0:
    #     display_string = str(n).rjust(4)
    #     if n == 0:
    #         display_string = ' byE'
    #     k = 100
    #     while k >= 0:
    #     	#sleep(1)
    #     	seg()
    #     	k -= 1
    #     n -= 1
    # n = 1000
    # while n >= 0:
    #     if n <= 500:
    #         display_string = 'ALEX'
    #     seg()
    #     n -= 1
finally:
    GPIO.cleanup()





