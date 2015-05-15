# buzzpi
Buzzer buttons on Raspberry Pi (first wins)

## Requirements
 * Python 3
 * RPi.GPIO (raspian `apt-get install python3-rpi.gpio`)

## Usage
 * Clamp some buttons to your Raspberry Pi (pressing a button should pull the RasPi pin to GND).
 * Change `mapping` dict in source file (key is BCM Pin number, value is your number of the button).
 * The Program shows which button was pressed first.
 * Hit RETURN to start again.
