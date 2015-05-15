#!/usr/bin/env python3

# requires python3-rpi.gpio package (raspian)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Judge:

    blocked = 0
    pressed_buzzer = 0

    def __init__(self, mapping):
        self.mapping = mapping

    def buzz(self, channel):
        if not self.blocked:
            buzzer = mapping[channel]
            print("pressed buzzer {} (channel {})".format(buzzer, channel))
            self.blocked = 1
            self.pressed_buzzer = buzzer

    def unblock(self):
        self.blocked = 0
        print("Unblocking buzzers!")

    def get_buzzer(self):
        print(self.pressed_buzzer)



mapping = {17:1, 22:2, 23:3, 24:4}

judge = Judge(mapping)

judge.unblock()

for key in mapping:
    GPIO.setup(key, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(key, GPIO.FALLING, callback=judge.buzz, bouncetime=20)

## setup button on BCM 27 as unblock button
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while(1):
        input()
        judge.unblock()
        #GPIO.wait_for_edge(27, GPIO.FALLING)
        #judge.unblock()

except KeyboardInterrupt:
    pass

print("")
print("Exiting...")
GPIO.cleanup()           # clean up GPIO on normal exit
