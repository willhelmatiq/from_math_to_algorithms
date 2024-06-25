import numpy as np
from matplotlib import pyplot as plt

beacons = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3)]
pos_real = (2, 2)
d2 = [(pos_real[0] - beacons[i][0]) ** 2 + (pos_real[1] - beacons[i][1]) ** 2 + (np.random.rand() - 0.5)*5 for i in range(len(beacons))]

A = np.zeros((len(beacons) - 1, 2))
b = np.zeros(len(beacons) - 1)
x1 = beacons[0][0]
y1 = beacons[0][1]
for i in range(1, len(beacons)):
    A[i - 1, 0] = 2 * (x1 - beacons[i][0])
    A[i - 1, 1] = 2 * (y1 - beacons[i][1])
    b[i - 1] = d2[i] - d2[0] + x1 ** 2 + y1 ** 2 - beacons[i][0] ** 2 - beacons[i][1] ** 2

print(A)
print(b)

z = np.linalg.solve(A.T @ A, A.T @ b)
print(z)
# Plotting the beacons and the real position
beacon_x, beacon_y = zip(*beacons)
plt.scatter(beacon_x, beacon_y, color='blue', label='Beacons')
plt.scatter(pos_real[0], pos_real[1], color='red', label='Real Position')

# Optionally plot the estimated position for comparison
plt.scatter(z[0], z[1], color='green', label='Estimated Position', marker='x')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Beacons and Real Position')
plt.legend()
plt.grid(True)
plt.show()



