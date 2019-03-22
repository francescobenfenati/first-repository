
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


f=open("test.txt",'r')
t=open("test.txt",'r')
l=open("test.txt",'r')
w = open("merged",'w')
nomi = []
money = []
line_counter = 0
for line in l:
    line_counter +=1
    
for x in range(line_counter):
    size = len(f.readline())
    a = []
    for i in range(size):
        a.append(t.read(1))
    
        if a[i] == "\t":
            b = t.read(1)
            leggo = t.read(1)
            if leggo is "":
                print("end of file")
                break
            while leggo != "\n":
                b+=leggo
                leggo = t.read(1)
            break
    nome = ''.join(a[0:-1])
    nomi.append(nome)
    b = int(b)
    money.append(b)
f.close()
t.close()
print(nomi,money)
equals = check_for_equals(nomi)
print(equals)
for i in range(len(equals)):
    w.write(nomi[equals[i][0]])
    w.write("\t")
    tot = 0
    for j in range(len(equals[i])):
        tot += money[equals[i][j]]
    w.write(str(tot))
    w.write("\n")
w.close()


