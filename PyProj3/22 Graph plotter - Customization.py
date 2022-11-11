import matplotlib.pyplot as plt

left = [2, 4, 6, 8, 10]
height = [10, 12, 14, 23, 36]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width=0.8, color = ["blue", "orange"])

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Demo Graph - Bar Chart")

plt.legend()
plt.show()