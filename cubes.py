import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axis
ax.set_title("Try it Yourself - Cubes", fontsize=24)
ax.set_xlabel("Input Value", fontsize=14)
ax.set_ylabel("Cube of Input", fontsize=14)

ax.axis([0, 5000, 0, 50000000000])

plt.show()