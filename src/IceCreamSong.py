from myro import *
init("COM40")
## Musical notes in the scale, as they correspond to beep frequency
pitchA4  = 440.0
pitchBf4 = 466.164
pitchAs4 = 466.164 
pitchB4  = 493.883
pitchC5  = 523.251
pitchDf5 = 554.37
pitchCs5 = 554.37 
pitchD5  = 587.33
pitchEf5 = 622.25
pitchDs5 = 622.25
pitchE5  = 659.26
pitchF5  = 698.46
pitchGf5 = 739.99
pitchFs5 = 739.99 
pitchG5  = 783.99
pitchAf5 = 830.61
pitchGs5 = 830.61
pitchA5  = 880
pitchBf5 = 932.33
pitchAs5 = 932.33
pitchB5  = 987.77


def main():
    i = 0

  ## Infinite loop to play the song while moving
    while(1):

        ## Move in a circle
        motors(.1,1)
 
        beep(0.25, pitchB5)
        beep(0.25, pitchA5)
        beep(0.5, pitchG5)
        beep(0.5, pitchG5)
        beep(0.5, pitchG5)
        
        motors(-.1,-1)

        beep(0.25, pitchB4)
        beep(0.25, pitchC5)
        beep(0.20, pitchD5)
        beep(0.20, pitchE5)
        beep(0.20, pitchD5)
        beep(0.20, pitchB4)
        beep(0.40, pitchD5)

        motors(1,.1)
  
        beep(0.25, pitchG5)
        beep(0.25, pitchA5)
        beep(0.20, pitchB5)
        beep(0.20, pitchB5)
        beep(0.20, pitchB5)
        beep(0.20, pitchB5)
        beep(0.50, pitchB5)

        motors(-1,-.1)
  
        beep(0.25, pitchG5)
        beep(0.25, pitchA5)
        beep(0.20, pitchB5)
        beep(0.20, pitchA5)
        beep(0.20, pitchA5)
        beep(0.20, pitchGs5)
        beep(0.50, pitchA5)

        motors(.1,1)
 
        beep(0.25, pitchB5)
        beep(0.25, pitchA5)
        beep(0.20, pitchG5)
        beep(0.20, pitchA5)
        beep(0.20, pitchG5)
        beep(0.20, pitchA5)
        beep(0.20, pitchG5)
        beep(0.20, pitchD5)
 
        motors(-.1,-1)

        beep(0.20, pitchB4)
        beep(0.20, pitchC5)
        beep(0.20, pitchD5)
        beep(0.20, pitchE5)
        beep(0.20, pitchD5)
        beep(0.20, pitchB4)
        beep(0.20, pitchD5)
        beep(0.20, pitchD5)

        motors(1,.1)

        beep(0.20, pitchG5)
        beep(0.20, pitchA5)
        beep(0.7, pitchB5)
        beep(0.8, pitchA5)
        beep(1.1, pitchG5)
 ## main


main()
