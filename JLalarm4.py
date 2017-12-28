from omxplayer import OMXPlayer
from time import time
from time import sleep
import os
import RPi.GPIO as GPIO
##import alsaaudio

#Set GPIO # mode, DD input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Snooze
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Off
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Vol Down
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Vol Up

#Initialize vol lvl
i = -1500

#Play alarm
file_path = '/home/pi/Downloads/Dangerous.mp3'
player = OMXPlayer(file_path)
##m = alsaaudio.Mixer()
vol = amixer cget numid=3
vol = int(vol[0])

##i = -1500

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

    if GPIO.input(18) == 0:
        print ()
            
    else:
        print ("Vol Down")
##        i = i-250
##        abc = "amixer cset numid=1 -- " +str(i)
##        os.system(abc)
        newVol = vol - 10
        amixer cset numid=3 25%
        sleep(0.15)
         
    if GPIO.input(23) == 0:
         print ()
            
    else:
         print ("Vol Up")
##         i = i+250
##         abc = "amixer cset numid=1 -- " +str(i)
##         os.system(abc)
         newVol = vol + 10
         amixer cset numid=3 75%
         sleep(0.15)

    count = count+1

##Kill the player gracefully
##player.quit()

##finally:
##    GPIO.cleanup()

