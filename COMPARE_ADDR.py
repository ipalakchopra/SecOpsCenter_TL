import re

file_1 = open("sp5.txt", "r")
file_2 = open("sp4.txt", "r")
output = open("output.res", "w")
n=0
for line_1 in file_1:
    n+=1
    print(n)

    file_2 = open("sp4.txt", "r")

    for line_2 in file_2:

        n+=1
        print(n)
        print("")
        list_1 = re.split(" ,",line_1 )
        #print(list_1)
        list_2 = re.split(" ,",line_2)
        #print(list_2)
        if(list_1[1] == list_2[1]):
            print(list_2[1])
            output.write("(in file 1)"+list_1[0]+" "+list_1[1]+" "+list_1[2]+" "+"(in file 2)"+list_2[0]+" "+list_2[1]+" "+list_2[2]+'\n')
    file_2.close()


