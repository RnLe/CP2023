import matplotlib.pyplot as plt
import numpy as np

def y(t):
    return np.exp(-t)

# a)

interval = (0, 10)
steps = 100
step = interval[-1]/steps

y_e_0 = 1

# y(t)_euler_a)
y_e_a = []
y_e_a.append(y_e_0)
# Euler
for i in range(steps):
    y_e_a.append(y_e_a[i]*(1-step))


# y(t)_symmetricEuler_a)
y_se_a = []
y_se_a.append(y_e_0)
y_se_a.append(np.exp(-step))
# Symmetric Euler
for i in range(steps-1):
    y_se_a.append(-2*step*y_se_a[i+1]+y_se_a[i])
    
    
# Analytical solution
t = np.linspace(interval[0], interval[-1], 200)
t_d = np.array(range(steps+1))/interval[-1]

plt.plot(t_d, y_se_a, 'k.-', label="Symmetric Euler Method")
plt.plot(t_d, y_e_a, 'x', color='tab:orange', label="Euler Method")
plt.plot(t, y(t), label="Analytical solution")

plt.legend()

plt.savefig('3a.pdf')

plt.close()

# b)

y_e_0 = 1 - step

# y(t)_euler_b)
y_e_b = []
y_e_b.append(y_e_0)
# Euler
for i in range(steps):
    y_e_b.append(y_e_b[i]*(1-step))


# y(t)_symmetricEuler_b)
y_se_b = []
y_se_b.append(1)
y_se_b.append(1 - step)
# Symmetric Euler
for i in range(steps-1):
    y_se_b.append(-2*step*y_se_b[i+1]+y_se_b[i])
    
# Plot everything
# Symmetric Euler
plt.plot(t, y(t), label="Analytical solution")
plt.plot(t_d, y_se_a, 'k.-', label="Symmetric Euler Method")
plt.plot(t_d, y_se_b, '.-', color='tab:grey', label="Symmetric Euler Method, b)")
plt.legend()

plt.savefig('3b_symm.pdf')

plt.close()

# Euler
plt.plot(t, y(t), label="Analytical solution")
plt.plot(t_d, y_e_a, 'x', color='tab:orange', label="Euler Method")
plt.plot(t_d, y_e_b, 'x', color='#dea768', label="Euler Method b)")

plt.legend()

plt.savefig('3b_.pdf')