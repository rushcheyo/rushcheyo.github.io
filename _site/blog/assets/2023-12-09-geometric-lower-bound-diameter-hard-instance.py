import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt

# Generate a larger set of points on the northern hemisphere within an epsilon range of the north pole
def generate_points_near_pole(n, pole, epsilon=0.05):
    # Generate random points on the sphere
    phi = np.random.uniform(0, 2 * np.pi, n)
    cos_theta = np.random.uniform(np.cos(epsilon), 1, n)
    theta = np.arccos(cos_theta)

    # Spherical to Cartesian conversion
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    # Rotate the points so that they are around the chosen pole
    if pole.lower() == 'south':
        z = -z  # Invert the z-axis to get the south pole region

    points = np.vstack((x, y, z)).T
    return points

def generate_sphere_wireframe(subdiv=30):
    phi = np.linspace(0, np.pi, subdiv)  # azimuth angle
    theta = np.linspace(0, 2 * np.pi, subdiv)  # polar angle

    phi, theta = np.meshgrid(phi, theta)
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    return x, y, z

# Set the number of points and epsilon
n_points = 700
epsilon = 0.3  # Epsilon is the angle in radians from the pole

# r = R.random()
r = R.from_rotvec(np.pi / 2 * np.array([1, 0, 0]))

# Generate points near the north pole and the south pole point
north_pole_points = r.apply(generate_points_near_pole(n_points, 'north', epsilon))
south_pole = r.apply(np.array([[0, 0, -1]]))

# Plotting the points
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the points near the north pole
ax.scatter(north_pole_points[:, 0], north_pole_points[:, 1], north_pole_points[:, 2], color='blue', s=1)

# Mark the south pole in red
ax.scatter(south_pole[:, 0], south_pole[:, 1], south_pole[:, 2], color='red', s=50, label='South Pole')

ax.plot([south_pole[0, 0], -south_pole[0, 0]],
        [south_pole[0, 1], -south_pole[0, 1]],
        [south_pole[0, 2], -south_pole[0, 2]],
        'r-',
        linewidth=0.5)

# Hide the axes
ax.axis('off')

# Set the aspect ratio to be equal
ax.axis('equal')

sphere_x, sphere_y, sphere_z = generate_sphere_wireframe()
ax.plot_wireframe(sphere_x, sphere_y, sphere_z,  color='gray', alpha=0.5, linewidth=0.3)

# Show the plot
# plt.show()

plt.savefig('2023-12-09-geometric-lower-bound-diameter-hard-instance.png', dpi=300, bbox_inches='tight', pad_inches = 0)

