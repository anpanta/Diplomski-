import numpy as np
import simpleaudio as sa
import setup as se


class AUD:
    zvuk=[np.zeros(3*se.n), np.zeros(3*se.n), np.zeros(3*se.n)]
    for i in range(3):
        zvuk[i]=zvuk[i].astype(np.float64)
    
    def __init__(self, value):
        if value != 0:
            tip=[value[0], value[1], value[2]]
            for i in range(3):
                if tip[i]=="start_end":
                    self.start_end(i)
                elif tip[i]=="long":
                    self.long(i)
                elif tip[i]=="short0":
                    self.short(i,0)
                elif tip[i]=="short1":
                    self.short(i,1)
                elif tip[i]=="short2":
                    self.short(i,2)
                elif tip[i]=="three":
                    self.three(i)
              
            for i in range(3):
                self.zvuk[i] = self.zvuk[i] * (2**15 - 1) / np.max(np.abs(self.zvuk[i]))
                self.zvuk[i] = self.zvuk[i].astype(np.int16)
        
            
    def start_end(self, note):
            self.zvuk[note][0:se.n]+=se.nota(note)
            self.zvuk[note][2*se.n:3*se.n]+=se.nota(note)
       
        
    def long(self, note):
            self.zvuk[note][0:se.n]+=se.nota(note)
            self.zvuk[note][se.n:2*se.n]+=se.nota(note)
            self.zvuk[note][2*se.n:3*se.n]+=se.nota(note)
       
    def short(self, note, where): #where=0,1,2
            self.zvuk[note][where*se.n:se.n+where*se.n]+=se.nota(note)
        
            
    def three(self, note):
            self.long(note)
            self.zvuk[note][se.n:se.n+10000]=np.zeros(10000)
            self.zvuk[note][2*se.n:2*se.n+10000]=np.zeros(10000)
    


try:
    file = open("test.txt", mode='r', encoding='utf-8')
  
    while 1:
        char = file.read(1)          
        
        if not char: 
            break
        if char!="\n":
            CHAR=char.upper()
            
            print(CHAR)
            if CHAR!=" ":
                print(se.abc[CHAR])
            
            audio=AUD(se.abc[CHAR])
            
            play_obj=[np.zeros(3*se.n), np.zeros(3*se.n), np.zeros(3*se.n)]
            
            for i in range(3):
                play_obj[i] = sa.play_buffer(audio.zvuk[i], 1, 2, se.fs)
                
                 
            for i in range(3):
                play_obj[i].wait_done()
            
finally:
    file.close()