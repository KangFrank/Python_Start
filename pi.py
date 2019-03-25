import matplotlib.pyplot as plt
import random
R = 60
R2 = R * R
x_in = []
y_in = []
x_out = []
y_out = []
for i in range(100000):
    x = random.random() * 2 * R - R
    y = random.random() * 2 * R - R
    if x * x + y * y > R2:
        x_out.append(x)
        y_out.append(y)
    else:
        x_in.append(x)
        y_in.append(y)
plt.figure(figsize=(16, 16))
plt.scatter(x_out, y_out, color='blue', marker='.', linewidths=0.1, alpha=0.3)
plt.scatter(x_in, y_in, color='red', marker='.', linewidths=0.1, alpha=0.3)
plt.scatter(0, 0, color='black')
plt.show()
print(len(x_in) / (len(x_in) + len(x_out)) * 4)