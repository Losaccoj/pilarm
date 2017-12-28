import os
import RPi.GPIO as GPIO
import time


#set GPIO # mode, DD input pin
GPIO.setmode(GPIO.BCM)
##GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Off
##GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Radio
GPIO.setup(14,GPIO.IN) # Vol Up
GPIO.setup(15,GPIO.IN) # Vol Down
GPIO.setup(18,GPIO.IN) # Off
GPIO.setup(23,GPIO.IN) # Play/pause
GPIO.setup(24,GPIO.IN) # Snooze/dim

##GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # Play
##GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Sounds
##GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # EXB
##GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Snooze
##GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Play
##GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #
##GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 

##GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Radio
##GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Snooze
##GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # Off
##GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Vol Down
##GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Vol Up
##GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # Source
##GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 
##GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #
##GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 

##i = -1500

try:
    while True:
        os.system("mpc status")

###################    Vol Down    ##########################        
        if GPIO.input(15) == 0:
            print ()
          
        else:
            print ("Vol Down")
##            os.system("mpc add http://ice1.somafm.com/spacestation-128-mp3")
##            os.system("mpc play")
            os.system("mpc volume - 15")
            time.sleep(0.15)
            
#####################    Snooze   ########################## 
        if GPIO.input(24) == 0:
            print ()
            
        else:
            print ("Snooze")
            os.system("mpc pause")
            time.sleep(1200)
            os.system("mpc play")
            time.sleep(0.15)

###################    Off     ########################## 
        if GPIO.input(18) == 0:
            print ()
            
        else:
            print ("Off")
            os.system("mpc pause")
            time.sleep(0.15)


###################    Vol Up  ######################## 
        if GPIO.input(14) == 0:
            print ()
         
        else:
            print ("Vol Up")
            os.system("mpc volume + 15")
##            i = i-250
##            abc = "amixer cset numid=1 -- " +str(i)
##            os.system(abc)
            time.sleep(0.15)
##            time.sleep(1)

###################    Vol Up    ########################
##        if GPIO.input(23) == 0:
##            print ()
##            
##        else:
##            print ("Vol Up")
####            i = i+250
####            abc = "amixer cset numid=1 -- " +str(i)
####            os.system(abc)
##            time.sleep(0.15)
####            time.sleep(1)
            
###################    Source    ########################## 
##        if GPIO.input(18) == 1:
##            print ()
##            
##        else:
##            print ("Source")
####            os.system("mpc stop")
####            os.system("mpc add http://ice1.somafm.com/sonicuniverse-192-mp3")
####            os.system("mpc play")
##            time.sleep(1)
         
###################    Reset    ########################### 
##        if GPIO.input(24) == 0:
##            print ()
##            
##        else:
##            print ("Reset")
##            time.sleep(1)
####            os.execv(/home/pi/Desktop/but2.py, sys.argv)

###################    Sounds   ########################### 
##        if GPIO.input(17) == 0:
##            print ()
##            
##        else:
##            print ("Sounds")
##            time.sleep(1)
######            os.execv(/home/pi/Desktop/but2.py, sys.argv)
##
#####################    EXB   ########################### 
##        if GPIO.input(27) == 0:
##            print ()
##            
##        else:
##            print ("EXB")
##            time.sleep(1)
######            os.execv(/home/pi/Desktop/but2.py, sys.argv)
            
#####################  Radio  ########################### 
##        if GPIO.input(23) == 0:
##            print ()
##            
##        else:
##            print ("Radio")
##            time.sleep(0.15)
######            os.execv(/home/pi/Desktop/but2.py, sys.argv)          

            
#####################    Play    ########################## 
        if GPIO.input(23) == 0:
            print ()
            
        else:
            print ("Play")
##            os.system("mpc stop")
##            os.system("mpc add http://ice1.somafm.com/sonicuniverse-192-mp3")
            os.system("mpc play")
            time.sleep(0.15)
         

except KeyboardInterrupt:
    GPIO.cleanup()
##finally:
##    #cleanup GPIO before ending
##    GPIO.cleanup()
