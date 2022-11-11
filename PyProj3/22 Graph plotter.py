import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 9, 12]
y1 = [2, 3, 6, 7, 10, 12]

plt.plot(x1,y1, label = "line 1")
x2 = [1, 2, 3, 4, 7, 11]
y2 = [1, 2, 3, 6, 8, 10]

plt.plot(x2, y2, label = "Line 2")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Demo Graph - Two Lines")

plt.legend()
plt.show()