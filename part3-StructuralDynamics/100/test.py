
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the dynamical function of the undamped system under harmonic force
def undamped_harmonic_force(u, t, omega, omega_n, p0_over_m):
    """
    Dynamical function of the undamped system under harmonic force
    u[0]: displacement
    u[1]: velocity
    """
    return [u[1], -omega_n**2 * u[0] + p0_over_m * np.sin(omega * t)]

# Given parameters
omega_n = 1.0  # Natural frequency of the system
omega_over_omega_n = 0.2
u0 = 0.5  # Initial displacement relative to p0/m
u_dot0 = omega_n  # Initial velocity relative to omega_n
p0_over_m = 1.0  # Ratio of p0 to m (amplitude of harmonic force to mass)
omega = omega_n * omega_over_omega_n  # Frequency of the harmonic force


# Initial conditions
initial_conditions = [u0, u_dot0]

# Time span
t = np.linspace(0, 100, 1000)

# Solve the differential equations
sol = odeint(undamped_harmonic_force, initial_conditions, t, args=(omega, omega_n, p0_over_m))

# Calculate the steady-state response
A = p0_over_m / np.sqrt((omega_n**2 - omega**2)**2 + (2 * omega * omega_n)**2)
phi = np.arctan2(2 * omega * omega_n, omega_n**2 - omega**2)

# Calculate the steady-state response
steady_state_response = A * np.sin(omega * t - phi)

# Plot the displacement of the system over time
plt.plot(t, sol[:, 0], label='Total Response')
plt.plot(t, steady_state_response, label='Steady-State Response')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Response of Undamped System to Harmonic Force')
plt.legend()
plt.grid(True)
plt.show()
