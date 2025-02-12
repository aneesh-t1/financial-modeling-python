import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")


print("Current working directory:", os.getcwd())

plt.savefig("test_plot.png")


if os.path.exists("test_plot.png"):
    print("Plot saved as test_plot.png")
else:
    print("Failed to save plot")