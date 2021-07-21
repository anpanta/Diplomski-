import numpy as np
import simpleaudio as sa
import setup as se

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

    
    
    

class AUD:
    E=np.zeros(3*n)
    C=np.zeros(3*n)
    A=np.zeros(3*n)    
    
    def __init__(self, value):
        if value != 0:
            typeE=value[0]
            typeC=value[1]
            typeA=value[2]
        
            if typeE=="start_end":
                self.start_end(E_note)
            elif typeE=="long":
                self.long(E_note)
            elif typeE=="short0":
                self.short(E_note,0)
            elif typeE=="short1":
                self.short(E_note,1)
            elif typeE=="short2":
                self.short(E_note,2)
            elif typeE=="three":
                self.three(E_note)
            
            if typeC=="start_end":
                self.start_end(C_note)
            elif typeC=="long":
                self.long(C_note)
            elif typeC=="short0":
                self.short(C_note,0)
            elif typeC=="short1":
                self.short(C_note,1)
            elif typeC=="short2":
                self.short(C_note,2)
            elif typeC=="three":
                self.three(C_note)
            
            if typeA=="start_end":
                self.start_end(A_note)
            elif typeA=="long":
                self.long(A_note)
            elif typeA=="short0":
                self.short(A_note,0)
            elif typeA=="short1":
                self.short(A_note,1)
            elif typeA=="short2":
                self.short(A_note,2)
            elif typeA=="three":
                self.three(A_note)
        
        
            self.A = self.A * (2**15 - 1) / np.max(np.abs(self.A))
            self.C = self.C * (2**15 - 1) / np.max(np.abs(self.C))
            self.E = self.E * (2**15 - 1) / np.max(np.abs(self.E))
        
            self.A = self.A.astype(np.int16)
            self.C = self.C.astype(np.int16)
            self.E = self.E.astype(np.int16)
        
    def start_end(self, note):
        if note.all()==se.A_note.all():
            self.A[0:n]+=note
            self.A[2*n:3*n]+=note
        elif note.all()==C_note.all():
            self.C[0:n]+=note
            self.C[2*n:3*n]+=note
        elif note.all()==E_note.all():
            self.E[0:n]+=note
            self.E[2*n:3*n]+=note
        
    def long(self, note):
        if note.all()==A_note.all():
            self.A[0:n]+=note
            self.A[n:2*n]+=note
            self.A[2*n:3*n]+=note
        elif note.all()==C_note.all():
            self.C[0:n]+=note
            self.C[n:2*n]+=note
            self.C[2*n:3*n]+=note
        elif note.all()==E_note.all():
            self.E[0:n]+=note
            self.E[n:2*n]+=note
            self.E[2*n:3*n]+=note
    

    def short(self, note, where): #where=0,1,2
        if note.all()==A_note.all():
            self.A[where*n:n+where*n]+=note
        elif note.all()==C_note.all():
            self.C[where*n:n+where*n]+=note
        elif note.all()==E_note.all():
            self.E[where*n:n+where*n]+=note
            
    def three(self, note):
        self.long(note)
        if note.all()==se.A_note.all():
            self.A[n:n+10000]=np.zeros(10000)
            self.A[2*n:2*n+10000]=np.zeros(10000)
        elif note.all()==C_note.all():
            self.C[n:n+10000]=np.zeros(10000)
            self.C[2*n:2*n+10000]=np.zeros(10000)
        elif note.all()==E_note.all():
            self.E[n:n+10000]=np.zeros(10000)
            self.E[2*n:2*n+10000]=np.zeros(10000)
            


try:
    file = open("test.txt", mode='r', encoding='utf-8')
  
    while 1:
        char = file.read(1)          
        
        if not char: 
            break
        if char!="\n":
            CHAR=char.upper()
            print(CHAR)
            audio=AUD(se.abc[CHAR])
            play_objA = sa.play_buffer(audio.A, 1, 2, fs)
            play_objC = sa.play_buffer(audio.C, 1, 2, fs)
            play_objE = sa.play_buffer(audio.E, 1, 2, fs)

            play_objA.wait_done()
            play_objC.wait_done()
            play_objE.wait_done()

finally:
    file.close()