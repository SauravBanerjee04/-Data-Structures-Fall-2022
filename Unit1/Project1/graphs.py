import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

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
