notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
acordes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 'Am', 'A#m', 'Bm']

def scaleMajor(tonica):
    escala = []
    for i in range(len(notas)):
        if tonica == notas[i]:
            indice = i
            break
    escala.append(notas[indice])
    escala.append(notas[indice + 2])
    escala.append(notas[indice + 4])
    escala.append(notas[indice + 5])
    escala.append(notas[indice + 7])
    escala.append(notas[indice + 9])
    escala.append(notas[indice + 11])
    return escala   
 
def scaleMinor(tonica):
    escala = []
    for i in range(len(notas)):
        if tonica == notas[i]:
            indice = i
            break
    escala.append(notas[indice])
    escala.append(notas[indice + 2])
    escala.append(notas[indice + 3])
    escala.append(notas[indice + 5])
    escala.append(notas[indice + 7])
    escala.append(notas[indice + 8])
    escala.append(notas[indice + 10])
    return escala    

class CampoHarmonicoMaior:
    def __init__(self, tonica):
        self.tonica = tonica
        self.escala = scaleMajor(tonica)
        self.acordesList = ['1_M', '2_m', '3_m', '4_M', '5_M', '6_m', '7_d']
        self.acordes = {}
        for i, acorde in enumerate(self.acordesList):
            if i >= 5:
                self.acordes[acorde] = [self.escala[i], self.escala[i-5], self.escala[i-3]]
            elif i >= 3:
                self.acordes[acorde] = [self.escala[i], self.escala[i+2], self.escala[i-3]]
            else:
                self.acordes[acorde] = [self.escala[i], self.escala[i+2], self.escala[i+4]]

class CampoHarmonicoMenor:
    def __init__(self, tonica):
        self.tonica = tonica
        self.escala = scaleMinor(tonica)
        self.acordesList = ['1_m', '2_m', '3_M', '4_m', '5_m', '6_M', '7_M']
        self.acordes = {}
        for i, acorde in enumerate(self.acordesList):
            if i >= 5:
                self.acordes[acorde] = [self.escala[i], self.escala[i-5], self.escala[i-3]]
            elif i >= 3:
                self.acordes[acorde] = [self.escala[i], self.escala[i+2], self.escala[i-3]]
            else:
                self.acordes[acorde] = [self.escala[i], self.escala[i+2], self.escala[i+4]]
