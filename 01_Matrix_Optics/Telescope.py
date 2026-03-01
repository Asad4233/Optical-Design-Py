import numpy as np
import matplotlib.pyplot as plt

def propagate(d):
    # new_height = height + d * angle
    # new_angle = angle (unchanged)
    return np.array([[1, d],
                     [0, 1]])

def thin_lens(f):
    # new_height = height (unchanged)
    # new_angle = angle - height/f
    return np.array([[1, 0],
                     [-1/f, 1]])
f_obj = 500   # objective focal length mm
f_eye = 50    # eyepiece focal length mm
separation = f_obj + f_eye
# Initial ray [height, angle]
ray = np.array([5, 0.0])   # 5 mm height, small angle
positions = [0]
heights = [ray[0]]  # starting height before any optics

ray_current = thin_lens(f_obj) @ ray
heights.append(ray_current[0])
positions.append(0)  # objective is at position 0

step = 50
z = 0

for i in range(0, separation, 50):
    ray_current = propagate(50) @ ray_current   # propagate by ONE step
    z += step                                     # update position
    positions.append(z)                           # store position
    heights.append(ray_current[0])  
    
# Add here — after loop, before prints
ray_current = thin_lens(f_eye) @ ray_current
positions.append(separation)
heights.append(ray_current[0])             # store ray height



M = thin_lens(f_eye) @ propagate(separation) @ thin_lens(f_obj)

# Final ray
ray_out = M @ ray

print("Positions:", positions)
print("Heights:", heights)


print("Output ray (Full system):", ray_out)

plt.figure(figsize=(12, 5))
plt.plot(positions, heights)

# Draw vertical lines for the lenses
plt.axvline(x=0, color='black', linewidth=2, label='Objective')
plt.axvline(x=separation, color='gray', linewidth=2, label='Eyepiece')

# Draw optical axis
plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')

plt.xlabel('Position along optical axis (mm)')
plt.ylabel('Ray height (mm)')
plt.title('Telescope Ray Diagram')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
plt.savefig('ray_diagram.png', dpi=150, bbox_inches='tight')