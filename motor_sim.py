import numpy as np
import matplotlib.pyplot as plt

# Rango de RPM
rpm = np.linspace(1000, 7000, 100)

# Parámetros simples del motor
max_torque = 250   # Nm
rpm_max_torque = 4000

# Modelo simple de torque
torque = max_torque * np.exp(-((rpm - rpm_max_torque) / 2000)**2)

# Potencia (HP)
power = torque * rpm / 9549

# Gráficas
plt.figure()
plt.plot(rpm, torque)
plt.xlabel("RPM")
plt.ylabel("Torque (Nm)")
plt.title("Curva de Torque del Motor")
plt.savefig("curva_torque.png")
plt.show()

plt.figure()
plt.plot(rpm, power)
plt.xlabel("RPM")
plt.ylabel("Potencia (HP)")
plt.title("Curva de Potencia del Motor")
plt.savefig("curva_potencia.png")
plt.show()