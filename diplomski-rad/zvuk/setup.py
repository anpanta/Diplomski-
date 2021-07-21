import numpy as np

A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

fs = 44100  # 44100 samples per second
seconds=1  # Note duration of 1 seconds


t=np.linspace(0, seconds, seconds * fs, False)
A_note = np.sin(A_freq * t * 2 * np.pi)
C_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)

n=len(t)
#A_note = A_note.astype(np.int16)
#C_note = C_note.astype(np.int16)
#E_note = E_note.astype(np.int16)
    
def nota (i):
        if i==0:
            return E_note
        elif i==1:
            return C_note
        elif i==2:
            return A_note
            
    

abc={
        "A":["short1","long","start_end"],
        "B":["long","short0","long"],
        "C":["short1","short0","short1"],
        "D":["long","start_end","long"],
        "E":["long","long","long"],
        "F":["long","long","short0"],
        "G":["short1","three","short1"],
        "H":["start_end","long","start_end"],
        "I":["short1","short1","short1"],
        "J":["short2","short2","long"],
        "K":["start_end","short0","start_end"],
        "L":["short0","short0","long"],
        "M":["three","start_end","start_end"],
        "N":["start_end","three","start_end"],
        "O":["short1","start_end","short1"],
        "P":["short1","short1","short0"],
        "Q":["short1","start_end","three"],
        "R":["short1","short1","start_end"],
        "S":["short1","long","short1"],
        "T":["long","short1","short1"],
        "U":["start_end","start_end","long"],
        "V":["start_end","start_end","short1"],
        "W":["start_end","start_end","three"],
        "X":["start_end","short1","start_end"],
        "Y":["start_end","short1","short1"],
        "Z":["long","short1","long"],
        " ":0
    } 

    
    
    