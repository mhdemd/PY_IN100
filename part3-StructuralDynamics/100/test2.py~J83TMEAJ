
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define parameters
m = 1.0  # Mass
k = 1.0  # Spring constant
p0 = 1.0  # Amplitude of the harmonic force
omega = 0.2  # Frequency of the harmonic force
omega_n = np.sqrt(k / m)  # Natural frequency

# Define the equation of motion
def equation_of_motion(u, t):
    return [u[1], -k * u[0] / m + p0 * np.sin(omega * t) / m]

# Define time
t = np.linspace(0, 100, 1000)

# Initial conditions
u0 = [0.5 * p0 / k, omega_n * p0 / (k * omega)]

# Solve the equation of motion
solution = odeint(equation_of_motion, u0, t)

# Calculate the steady-state response
steady_state_response = p0 / (m * np.sqrt((k - m * omega**2)**2 + (m * omega)**2)) \
                        * np.sin(omega * t - np.arctan2(m * omega, k - m * omega**2))

# Plot both responses on the same plot
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Total Response')
plt.plot(t, steady_state_response, label='Steady-state Response')
plt.xlabel('Time')
plt.ylabel('Displacement (u)')
plt.title('Total and Steady-state Responses of the Undamped System to Harmonic Force')
plt.grid(True)
plt.legend()
plt.show()
