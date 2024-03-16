import os 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ORIENTATIONS = ["increasing", "decreasing", "random"]
VALUES = [10000, 20000, 30000, 40000, 50000]

writer = open("values1.csv", "w")
writer.write("orientation,value,insertion,selection\n")



def counts():
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
    return(insertion, selection)

for y in VALUES:
    for x in ORIENTATIONS:
        os.system("python -m trace --count -C . Sort.py " + str(y) + " " + str(x))
        (z1,z2) = counts()
        writer.write(str(x) +"," + str(y) +","+ str(z1) + "," + str(z2)+"\n")
        print(str(x) +"," + str(y) +","+ str(z1) + "," + str(z2)+"\n")

writer.close()

df = pd.read_csv ('values1.csv')
newpath = r'./Graphs'
if not os.path.exists(newpath):
    os.makedirs(newpath)

increasing = df[df['orientation'] == "increasing"] 

plt.title("Increasing Insertion")
plt.plot(increasing.loc[:,"value"], increasing.loc[:,"insertion"], color='blue', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Increasing_Insertion.jpg')
plt.clf()

plt.title("Increasing Selection")
plt.plot(increasing.loc[:,"value"], increasing.loc[:,"selection"], color='red', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Increasing_Selection.jpg')
plt.clf()

decreasing = df[df['orientation'] == "decreasing"] 

plt.title("Decreasing Insertion")
plt.plot(decreasing.loc[:,"value"], decreasing.loc[:,"insertion"], color='blue', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Decreasing_Insertion.jpg')
plt.clf()

plt.title("Decreasing Selection")
plt.plot(decreasing.loc[:,"value"], decreasing.loc[:,"selection"], color='red', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Decreasing_Selection.jpg')
plt.clf()
random = df[df['orientation'] == "random"] 

plt.title("Random Insertion")
plt.plot(random.loc[:,"value"], random.loc[:,"insertion"], color='blue', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Random_Insertion.jpg')
plt.clf()

plt.title("Random Selection")
plt.plot(random.loc[:,"value"], random.loc[:,"selection"], color='red', marker='o',linestyle = "dotted")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.savefig('./Graphs/Random_Selection.jpg')
plt.clf()
