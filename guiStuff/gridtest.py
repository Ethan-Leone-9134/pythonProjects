import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot with Custom Grid Line Width')

# Disable autoscaling
ax.autoscale(enable=False)
ax.set_xlim(0,5)
ax.set_ylim(0,5)


# Set grid line width
plt.grid(which='both', axis='both', linestyle='-', linewidth=1.5)

# Show the plot
plt.show()
