import os 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ORIENTATIONS = ["increasing", "decreasing", "random"]
VALUES = [10000, 20000, 30000, 40000, 50000]

writer = open("values.csv", "w")
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
        os.system("python3 -m trace --count -C . Sort.py " + str(y) + " " + str(x))
        (z1,z2) = counts()
        writer.write(str(x) +"," + str(y) +","+ str(z1) + "," + str(z2)+"\n")

writer.close()

df = pd.read_csv ('values.csv')
newpath = r'./Graphs'
if not os.path.exists(newpath):
    os.makedirs(newpath)

increasing = df[df['orientation'] == "increasing"] 

plt.title("Increasing Data")
plt.plot(increasing.loc[:,"value"], increasing.loc[:,"insertion"], color='blue', marker='o',linestyle = "dotted", label = "Insertion")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.plot(increasing.loc[:,"value"], increasing.loc[:,"selection"], color='red', marker='o',linestyle = "dotted", label = "Selection")
plt.legend()
plt.savefig('./Graphs/Increasing.jpg')
plt.clf()

decreasing = df[df['orientation'] == "decreasing"] 

plt.title("Decreasing Data")
plt.plot(decreasing.loc[:,"value"], decreasing.loc[:,"insertion"], color='blue', marker='o',linestyle = "dotted", label = "Insertion", alpha = 0.45)
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.plot(decreasing.loc[:,"value"], decreasing.loc[:,"selection"], color='red', marker='o',linestyle = "dotted", label = "Selection", alpha = 0.25)
plt.legend()
plt.savefig('./Graphs/Decreasing.jpg')
plt.clf()

random = df[df['orientation'] == "random"] 

plt.title("Random Data")
plt.plot(random.loc[:,"value"], random.loc[:,"insertion"], color='blue', marker='o',linestyle = "dashed", label = "Insertion")
plt.xlabel("Length of Array")
plt.ylabel("Sum")
plt.plot(random.loc[:,"value"], random.loc[:,"selection"], color='red', marker='o',linestyle = "dotted", label = "Selection")
plt.legend()
plt.savefig('./Graphs/Random.jpg')
plt.clf()
