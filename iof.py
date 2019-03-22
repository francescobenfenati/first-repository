import os
def check_for_equals(a):                               #restituisce liste degli indici di membri uguali
    coppie = []    

    for i in range(len(a)):
        if i != 0:                          #istruzioni dal secondo elemento
            for x in range(0,i+1):          #cerca se c'è uno uguale fra precedenti
                if a[i]!=a[x]:
                    continue
                elif x==i:                  #se non c'è nessuno uguale procedi
                    coppia = []
                    coppia.append(i)
                    for j in range(i+1,len(a)): #cerca gli uguali fra i successivi
                        if a[i]==a[j]:
                            coppia.append(j)    #appendi ogni indice trovato uguale
                        else:
                            continue
                    coppie.append(coppia)
                else:                           #se uno uguale fra precedenti skippa e procedi
                    break
            
        if i == 0:                          #istruzioni per primo elemento (uguali a sopra)
             coppia=[]
             coppia.append(i)
             for j in range(i+1,len(a)):
                        if a[i]==a[j]:
                            coppia.append(j)
                        else:
                            continue
             coppie.append(coppia)
                
        
    return coppie

def sum_transactions(filename,out):
    f=open(filename,'r')
    w = open(out,'w')
    names = []
    money = []
    line_counter = 0 
    for line in f:
        line_counter +=1
    f.seek(0)
    for x in range(line_counter): #leggo ogni riga
        line = f.readline()
        line_size = len(line)
        a = []
        f.seek(f.tell()-line_size, os.SEEK_SET) 
        for i in range(line_size):              #leggo byte per byte
            a.append(f.read(1))
            if a[i] == "\t":                    #dopo il tab leggo i soldi
                b = f.read(1)
                leggo = f.read(1)
                if leggo is "":
                    #print("end of file")
                    break
                while leggo != "\n":
                    b+=leggo
                    leggo = f.read(1)
                break
        name = ''.join(a[0:-1])
        names.append(name)
        b = int(b)
        money.append(b)
    f.close()
    equals = check_for_equals(names)
    for i in range(len(equals)):                #scrivo i nomi una sola volta
        w.write(names[equals[i][0]])
        w.write("\t")
        tot = 0
        for j in range(len(equals[i])):
            tot += money[equals[i][j]]          #con i soldi totali
        w.write(str(tot))
        w.write("\n")
    w.close()
    return

sum_transactions("test.txt","merged.txt")

