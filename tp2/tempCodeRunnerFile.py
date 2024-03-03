import matplotlib.pyplot as plt

# Plot the original data points
plt.scatter(x[:, 0], y, color='blue', label='Original data')

# Plot the regression line
plt.plot(x[:, 0], y_hat, color='red', label='Regression line')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()

# Show plot
plt.show()