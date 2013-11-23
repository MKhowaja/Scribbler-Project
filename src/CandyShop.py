import time
from Myro import *  # Import the myro module
init("COM7")   # Use the robot simulator

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


beep(0.25, G)
time.sleep(0.075)
beep(0.015, G)
beep(0.015, A2)
beep(0.015, G)
beep(0.015, A2)
beep(0.025, G)
time.sleep(0.075)
beep(0.25, Fs)
time.sleep(0.075)
beep(0.25, Fs)
time.sleep(0.3)
beep(1, bass)

beep(0.25, G)
time.sleep(0.075)
beep(0.25, G)
time.sleep(0.4)
beep(0.25, Fs)
time.sleep(0.3)
beep(1, bass)

beep(0.25, G)
time.sleep(0.075)
beep(0.015, G)
beep(0.015, A2)
beep(0.015, G)
beep(0.015, A2)
beep(0.025, G)
time.sleep(0.075)
beep(0.25, E)
time.sleep(0.075)
beep(0.25, Fs)
time.sleep(0.3)
beep(1, bass)

beep(0.25, E)
time.sleep(0.075)
beep(0.25, Fs)
time.sleep(0.075)
beep(0.25, G)
time.sleep(0.075)
beep(0.25, A2)
time.sleep(0.075)
beep(0.25, Fs)
