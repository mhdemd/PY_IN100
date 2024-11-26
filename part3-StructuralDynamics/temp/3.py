from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def ode_system(y, t, n):
    x, v = y
    dydt = [v, n - v - x]
    return dydt

# Initial conditions
y0 = [0.0, 0.0]
# Time
t = np.linspace(0, 5, 100)
# Parameter n
n = 2

# Solve the system of differential equations using odeint
solution = odeint(ode_system, y0, t, args=(n,))

# Display the solution
plt.plot(t, solution[:, 0], label='Displacement (x)')
plt.plot(t, solution[:, 1], label='Velocity (v)')
plt.xlabel('Time (t)')
plt.ylabel('Displacement and Velocity')
plt.legend()
plt.show()
