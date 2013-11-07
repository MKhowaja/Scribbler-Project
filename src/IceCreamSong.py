from myro import *
init("COM40")
# Musical notes in the scale, as they correspond to beep frequency
# Notes are 4th and 5th octaves
#4th octave
A  = 440.0    #A
As = 466.164  # Asharp or Bflat
B  = 493.88   #B
#5th octave
C  = 523.25   #C 
Cs = 554.37   #Csharp or Dflat
D  = 587.33   #D
Ds = 622.25   #Dsharp or Eflat
E  = 659.26   #E
F  = 698.46   #F
Fs = 739.99   #Fsharp or Gflat
G  = 783.99   #G
Gs = 830.61   #G sharp or A flat
A2  = 880     #A octave higher
As2 = 932.33  #Asharp or Bflat octave higher
B2  = 987.77  #B octave higher


def playSong(n):
    
  ## Infinite loop to play the song until destination has been reached
    while(n):
 
        beep(0.25, B2)
        beep(0.25, A2)
        beep(0.5, G)
        beep(0.5, G)
        beep(0.5, G)

        beep(0.25, B)
        beep(0.25, C)
        beep(0.20, D)
        beep(0.20, E)
        beep(0.20, D)
        beep(0.20, B)
        beep(0.40, D)
  
        beep(0.25, G)
        beep(0.25, A2)
        beep(0.20, B2)
        beep(0.20, B2)
        beep(0.20, B2)
        beep(0.20, B2)
        beep(0.50, B2)
  
        beep(0.25, G)
        beep(0.25, A2)
        beep(0.20, B2)
        beep(0.20, A2)
        beep(0.20, A2)
        beep(0.20, Gs)
        beep(0.50, A2)

 
        beep(0.25, B2)
        beep(0.25, A2)
        beep(0.20, G)
        beep(0.20, A2)
        beep(0.20, G)
        beep(0.20, A2)
        beep(0.20, G)
        beep(0.20, D)

        beep(0.20, B)
        beep(0.20, C)
        beep(0.20, D)
        beep(0.20, E)
        beep(0.20, D)
        beep(0.20, B)
        beep(0.20, D)
        beep(0.20, D)

        beep(0.20, G)
        beep(0.20, A2)
        beep(0.7, B2)
        beep(0.8, A2)
        beep(1.1, G)
