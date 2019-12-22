import math, random
import operator
import os

class KNN:
    
#The generate method
    def generate(self):
        f = open("Data", "+w")
        for i in range(100):
            value = random.random()
            if value<0.5:
                type="c"
            else:
                type="t"
            x = round(random.uniform(0,10),2)
            y = round(random.uniform(0,10),2)
            f.write(str(x)+" "+str(y)+" "+type+"\n")
        f.close()
        
#The predire method      
    def predire(self,x,y,k):
        f = open("Data", "r", encoding='utf8')
        d1 = {}
        d2 = {}
        for i in range(100):
            s = f.readline()
            tab=s.split()
            x1=float(tab[0])
            y1=float(tab[1])
            d=math.sqrt(pow((x1-x),2)+pow((y1-y),2))
            d1[i] =d
            d2[i] =tab[2]
        sorte = sorted(d1.items(), key=operator.itemgetter(1))
        nc=0
        nt=0
        for i in range(k):
            if d2[sorte[i][0]]=="c":
                nc=nc+1
            elif d2[sorte[i][0]]=="t":
                nt=nt+1
        if nt<nc:
            res="c"
        else:
            res="t"
        f.close()
        return res

#The display method   
    def display(self,r):
        if r=="c":
            print("The type of the new element is a Circle")
        elif r=="t":
            print("The type of the new element is a Triangle")
            
#Inserting elements         
x = input("Give the number x :")
y = input("Give the number y :")  
k = input("Give the margin of correspondence :")           
#Using the class
obj=KNN()
#Using the generate method
obj.generate()
#Using the predire method
r=obj.predire(int(x),int(y),int(k))
#Using the display method
obj.display(r)
os.system("pause")
