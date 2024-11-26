from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def ode_func(x, t, n):
    dxdt = n
    return dxdt

# Initial condition
x0 = 0.0
# Time
t = np.linspace(0, 5, 100)
# Parameter n
n = 2

# Solve the differential equation using odeint
solution = odeint(ode_func, x0, t, args=(n,))

# Display the solution
plt.plot(t, solution[:, 0], label='Displacement (x)')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.legend()
plt.show()
