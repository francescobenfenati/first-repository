import numpy as np
import pandas as pd

f = open("/Users/francescobenfenati/prova_parser.txt","r")

doms_a0 =["Data 3.4.3.2/V2-2-1/2.537-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.157-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.283-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.159-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.539-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.538-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.74-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.532-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.456-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.236-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.587-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.192-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.327-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.75-ahrs_a[0]\n" ,
          "Data 3.4.3.2/V2-2-1/2.143-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.586-ahrs_a[0]\n",
          "Data 3.4.3.2/V2-2-1/2.83-ahrs_a[0]\n"]

doms_a1 =["Data 3.4.3.2/V2-2-1/2.537-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.157-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.283-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.159-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.539-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.538-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.74-ahrs_a[1]\n" ,
          "Data 3.4.3.2/V2-2-1/2.532-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.456-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.236-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.587-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.192-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.327-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.75-ahrs_a[1]\n" ,
          "Data 3.4.3.2/V2-2-1/2.143-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.586-ahrs_a[1]\n",
          "Data 3.4.3.2/V2-2-1/2.83-ahrs_a[1]\n"]

doms_a2 =["Data 3.4.3.2/V2-2-1/2.537-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.157-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.283-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.159-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.539-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.538-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.74-ahrs_a[2]\n" ,
          "Data 3.4.3.2/V2-2-1/2.532-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.456-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.236-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.587-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.192-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.327-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.75-ahrs_a[2]\n" ,
          "Data 3.4.3.2/V2-2-1/2.143-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.586-ahrs_a[2]\n",
          "Data 3.4.3.2/V2-2-1/2.83-ahrs_a[2]\n"]

doms=[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18]

dom_list = [] #list which contains all dom_i lists for all DOMs NOT USUED
dom_i = [] #list which contains dom_id,time,a0,a1,a2 lists for each dom NOT USUED
dom_id = [] #repetitive list of DOM number
a0 = [] #list of a0 values for each dom
a1 = []
a2 = []
time_list = [] #list of times (given a DOM they are the same for a0,a1,a2)
while True:  #read file line by line
    riga = f.readline()
    
    if riga in doms_a0:
        x = ""
        line = ""
        while True:
            letter = ""
            time = ""
            a = 0 
            while letter != "M": #leggi lettera per lettera fino alla M
                letter = f.read(1)
                if letter == "D": #se è una D -> comincia la categoria successiva, raise flag a = 1
                    line = letter+f.readline()
                    a = 1
                    break
                time += letter

            if a == 0: #entra solo se se la prima lettera NON è una 'D'
                x  = f.readline() #completa lettura riga da dopo la 'M' -> valore del compass
                line = time+x
                
            if line == doms_a1[doms_a0.index(riga)]:
                riga = line
                break
         
            compass_value = x.replace(" System.Double\n","")
            a0.append(compass_value)
            time_list.append(time)
            dom_id.append(doms[doms_a0.index(riga)])
      #  dom_i.append(dom_id)
      #  dom_i.append(time_list)
      #  dom_i.append(a0)

    if riga in doms_a1:
        x = ""
        line = ""
        while True:
            letter = ""
            time = ""
            a = 0
            while letter != "M":
                letter = f.read(1)
                if letter == "D":
                    line = letter+f.readline()
                    a = 1
                    break
                time += letter

            if a == 0:
                x  = f.readline()
                line = time+x
                
            if line == doms_a2[doms_a1.index(riga)]:
                riga = line
                break
            
            compass_value = x.replace(" System.Double\n","")
            a1.append(compass_value)
       # dom_i.append(a1)
                    
    if riga in doms_a2:
        x = ""
        line = ""
        while True:
            letter = ""
            time = ""
            a = 0
            while letter != 'M':
                letter = f.read(1)
                if letter == 'D':
                    line = letter+f.readline()
                    a = 1
                    break
                time += letter
            if a == 0:
                x = f.readline()
                line = time+x
            elif a == 1: #in questo caso se la prima lettera è 'D' devo tornare a leggere righe fino ad a[0] del seguente DOM
                break
            compass_value = x.replace(" System.Double\n","")
            a2.append(compass_value)
            

#        dom_i.append(a2)  
#        dom_list.append(dom_i) #not used

    if riga == "":
        break

list_of_tuples = list(zip(dom_id,time_list,a0,a1,a2))            

df = pd.DataFrame(list_of_tuples,columns=['DOM','time','a[0]','a[1]','a[2]'])
print(df)
df.to_csv("datalog_parsed.csv",index=0)

f.close()
