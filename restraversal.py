import re

hammer_5 = open("hammer_5.res","r")
sp5 = open("sp5.txt","a")
#regex = re.compile('VA=\s.*,\sPA=.*DA.*VA.*PA=.*DA.*VA=\s.*PA.*DA')
regex = re.compile(".*\|.*") 
regsplit = re.compile(".*:\sVA.*PA")

n = 0
a =[]
for line in hammer_5:
    n+=1
    if(bool(regex.match(line))):
        print("line number: ",n)    
        #print(line)
        #print(line.split(":",1)[1])

        linx = re.split(regsplit,line)
        print(linx[1])
        sp = line.split(":",1)[1]
        #print(sp.split("|"))

        sp5.write(line)
#VA= 0x7705d7b58000, PA=0x44260000 ,  DA = (0 0 0 1 1109   0) VA= 0x770546ec6000, PA=0x77e22000 ,  DA = (0 0 0 1 1df8   0) : VA= 0x7705d7b1a000, PA=0x44222000 ,  DA = (0 0 0 1 1108   0) 08d3|10|00 
#