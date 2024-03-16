coverfile = open('Sort.cover','r')
insertion = 0
selection = 0
x = 1
for line in coverfile:
    #print(line)
    linetrimmed = line.strip()
    pos = linetrimmed.find(":")
    if (not(pos == -1)) and (x >= 5) and (x <= 12):
        insertion += int(linetrimmed[0:pos])
        if x == 9:
            insertion += int(linetrimmed[0:pos])
    if (not(pos == -1)) and (x >= 15) and (x <= 29):
        selection += int(linetrimmed[0:pos])
    x += 1 
coverfile.close()

print("Insertion: " + str(insertion))
print("Selection: " + str(selection))

#scp sbanerjee01@th121-11.cs.wm.edu:/home/sbanerjee01/values.csv ./values.csv