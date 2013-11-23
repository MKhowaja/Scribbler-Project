from Myro import *  # Import the myro module
init("COM7")   # Use the robot simulator
import time

setS2Volume(100)

bass=392
A  = 440.0
As = 466.164
B  = 493.88

C  = 523.25
Cs = 554.37
D  = 587.33
Ds = 622.25
E  = 659.26
F  = 698.46
Fs = 739.99
G  = 783.99
Gs = 830.61
A2  = 880
As2 = 932.33
B2  = 987.77
C2 = 1046.50

for i in range(2):
    beep(0.15, Ds)
    time.sleep(0.05)
    beep(0.15, Ds)
    time.sleep(0.05)
    beep(0.2, Ds)
    beep(0.15, As2)
    time.sleep(0.05)
    beep(0.15, As2)
    time.sleep(0.05)
    beep(0.2, As2)
    beep(0.2, B2)
    beep(0.2, As2)
    beep(0.2, B2)
    beep(0.15, As2)
    time.sleep(0.05)
    beep(0.1, As2)
    beep(0.15, Gs)
    time.sleep(0.05)
    beep(0.1, Gs)
    time.sleep(0.05)
    beep(0.2, Gs)
    beep(0.15, Fs)
    time.sleep(0.05)
    beep(0.2, Fs)
