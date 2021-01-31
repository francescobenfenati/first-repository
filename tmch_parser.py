import numpy as np
import pandas as pd

f = open("prova_parser.txt","r")

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

dom_list = []
dom_i = []
b = ""

while True:
    riga = f.readline()
    dom_id = []
    a0 = []
    a1 = []
    a2 = []
    if riga in doms_a0:
#        print("segue compass0 del DOM",doms[doms_a0.index(riga)])
        x = ""
        while x != doms_a1[doms_a0.index(riga)]:
            x = f.readline()
            if x == doms_a1[doms_a0.index(riga)]:
                riga = x
                break
            y = x.replace(" System.Double\n","")
#            print(y)
            a0.append(y)
            dom_id.append(doms[doms_a0.index(riga)])
        dom_i.append(dom_id)    
        dom_i.append(a0)

    if riga in doms_a1:
#        print("segue compass1 del DOM",doms[doms_a1.index(riga)])
        x = ""
        while x != doms_a2[doms_a1.index(riga)]:
            x = f.readline()
            if x == doms_a2[doms_a1.index(riga)]:
                riga = x
                break
#            y = x.replace(" System.Double\n","")
            print(y)
            a1.append(y)
        dom_i.append(a1)
                    
    if riga in doms_a2:
#        print("segue compass2 del DOM",doms[doms_a2.index(riga)])
        x = ""
        for i in range(61):
            x = f.readline()
            y = x.replace(" System.Double\n","")
#            print(y)
            a2.append(y)
        dom_i.append(a2)  
        dom_list.append(dom_i)
        list_of_tuples = list(zip(dom_id,a0,a1,a2))
    if riga == "":
        break

#print(dom_list)

df = pd.DataFrame(list_of_tuples,columns=['DOM','a[0]','a[1]','a[2]'])
print(df)
