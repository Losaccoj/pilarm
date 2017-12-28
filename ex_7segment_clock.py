#!/usr/bin/env python

import time
import datetime

import SevenSegment
import HT16K33

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

print("Press CTRL+Z to exit")

# Continually update the time on a 4 char, 7-segment display
try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     # Tens
    segment.set_digit(1, hour % 10)          # Ones
    # Set minutes
    segment.set_digit(2, int(minute / 10))   # Tens
    segment.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    segment.set_colon(second % 2)              # Toggle colon at 1Hz
    # Control brightness
    if 6 <= hour <= 17:
      segment.set_brightness(15)            #Day time
    else:
      segment.set_brightness(1)             #Night time
      
##    if max(range(hour)) >= 20:
##      segment.set_brightness(1)                 # Night time
##    else:
##      segment.set_brightness(14)            # Day time
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(0.25)
except (KeyboardInterrupt, SystemExit):
##  raise
  print("JL KeyboardInterrupt received; stopping...")
  segment.clear()
  display.clear()
  
##  segment.write_display()
##finally:
##  segment.write_display()
##  segment.set_led(0,0)
##  segment.set_led(1,0)
##  segment.display_off
##  segment.set_led(1,0)
##  segment.set_led(2,0)
##  segment.set_led(3,0)

