from omxplayer import OMXPlayer
from time import time
import time
from time import sleep
import os
import RPi.GPIO as GPIO

#Set GPIO # mode, DD input pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Snooze
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Off
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Vol Down
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Vol Up

#GPIO ports for the 7seg pins
segments =  (11,20,5,8,7,10,6,25)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# GPIO ports for the digit 0-3 pins 
digits = (13,16,1,26)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

##try:
while True:
    n = time.ctime()[11:13]+time.ctime()[14:16]
    s = str(n).rjust(4)
    for digit in range(4):
        for loop in range(0,7):
            GPIO.output(segments[loop], num[s[digit]][loop])
            if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                GPIO.output(25, 1)
            else:
                GPIO.output(25, 0)
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)

#Initialize vol lvl
i = -1500

#Play alarm
file_path = '/home/pi/Downloads/Dangerous.mp3'
player = OMXPlayer(file_path)
i = -1500

count = 0
while (count < 1200):
    player.play()

if GPIO.input(17) == 0:
    print ()
    
else:
    print ("Snooze")
##            player.pause(1200)
    player.pause()
##            sleep(1200)
    sleep(3)
    player.play()
 
if GPIO.input(4) == 0:
    print ()
    
else:
    print ("OFF")
    player.quit()
    sleep(5)

if GPIO.input(27) == 0:
    print ()
        
else:
    print ("Vol Down")
    i = i-250
    abc = "amixer cset numid=1 -- " +str(i)
    os.system(abc)
    sleep(0.15)
     
if GPIO.input(22) == 0:
     print ()
        
else:
     print ("Vol Up")
     i = i+250
     abc = "amixer cset numid=1 -- " +str(i)
     os.system(abc)
     sleep(0.15)

count = count+1

##Kill the player gracefully
##player.quit()

##finally:
##    GPIO.cleanup()

