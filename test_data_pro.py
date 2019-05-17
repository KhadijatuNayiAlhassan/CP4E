file = open("CPA5_functions.txt","r")
outfile = open("CPA5_outfile.txt","w")

dict1 = {}
#list1 = []
list2 = []
for line in file:
    values = line.split(",")
    #dict1[values[0]] = values[1]
#     list1.append(values[0])
    list2.append(values[1])
# for i in list1 and j in list2:
#     dict1[list1[i]] = list2[j]
    #for i,j in values:
        #dict1[i] = j
    #print(dict1)
    #outfile.write(values[0]+" had " + str(values[1])+ " in their exam!" + "\n")
    print(file.readlines())
    print(getRange(list2))



#print(list1)
#print(list2)

file.close()
outfile.close()
