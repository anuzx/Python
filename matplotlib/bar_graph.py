import matplotlib.pyplot as plt

#Data
categories = ["A","B","C","D"]
values = [10,20,30,40]

#bar plot
plt.bar(categories , values , color="skyblue")

#title and label
plt.title("bar-graph")
plt.xlabel("categories")
plt.ylabel("values")

#grid
plt.grid(axis='y' , linestyle='--' , alpha=0.7)#alpha is for opacity 

#display
plt.show()

#for horizontal bar use plt.barh
