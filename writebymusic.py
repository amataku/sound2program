import librosa
import math

f_name = input("make file name : ")
file_path = "./BF/" + f_name + ".bf"

load_path = input("load file path : ")

f = open(file_path,'a')

y,sr = librosa.load(load_path)

C = librosa.feature.chroma_cens(y=y, sr=sr)

for i in range(math.floor(C.shape[1]/43)):
    pos = ((i + 1) * 43) -22
    lst = []

    for i,_ in enumerate(["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]):
        lst.append(C[i][pos])

    scale = lst.index(max(lst))

    if scale in {0,1}:
        print("do")
        f.write('+')
    elif scale in {2,3}:
        print("re")
        f.write('-')
    elif scale == 4:
        print("mi")
        f.write('>')
    elif scale in {5,6}:
        print("fa")
        f.write('<')
    elif scale in {7,8}:
        print("so")
        f.write('[')
    elif scale == 9:
        print("ra")
        f.write(']')
    elif scale == 10:
        print("ras")
        f.write('.')
    elif scale == 11:
        print("si")
        f.write(',')

f.close()
