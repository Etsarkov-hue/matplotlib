import numpy as np
import matplotlib.pyplot as plt

# Данные двигателя МТМ111-6
omega0 = 104.72  # рад/с

# Диапазон скольжений
s = np.array([-0.75, -0.5, -0.25, -0.1, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 
              0.4, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0])

# Моменты для естественной характеристики (рассчитаны ранее)
M_nat = np.array([-64.0, -83.3, -110.6, -109.3, 0, 47.5, 69.9, 79.4, 83.6, 
                  85.1, 85.4, 84.0, 81.2, 70.5, 59.7, 50.9, 44.0, 38.4, 33.8])

# Скорость для всех точек
omega = omega0 * (1 - s)

print("Построение графиков...")

# ==================== ГРАФИК 1: Изменение напряжения ====================
plt.figure(figsize=(10, 6))

# Естественная характеристика
plt.plot(M_nat, omega, 'k-', linewidth=2, label='U = U_н')

# Характеристики при пониженном напряжении
for u in [0.8, 0.6, 0.4, 0.2]:
    M_u = M_nat * u**2
    plt.plot(M_u, omega, '--', linewidth=1.5, label=f'U = {u}·U_н')

plt.xlabel('Момент M, Н·м')
plt.ylabel('Скорость ω, рад/с')
plt.title('Рис. 1. Механические характеристики при изменении напряжения статора')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-100, 100)
plt.ylim(-150, 200)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Сохраняем график 1
plt.savefig('graph_voltage.png', dpi=300, bbox_inches='tight')
print("✓ График 1 сохранен: graph_voltage.png")

# ==================== ГРАФИК 2: Изменение сопротивления ротора ====================
plt.figure(figsize=(10, 6))

# Моменты для разных R_д
M_r0 = M_nat  # R_д = 0
M_r1 = np.array([-58.5, -78.1, -111.2, -112.5, 0, 43.8, 68.2, 80.2, 85.5, 
                 87.2, 87.2, 84.8, 81.0, 68.0, 55.8, 48.3, 39.5, 32.8, 29.2])
M_r2 = np.array([-53.2, -73.0, -110.8, -115.0, 0, 41.2, 66.5, 80.8, 87.0, 
                 89.0, 88.8, 85.2, 80.2, 65.0, 52.2, 45.0, 36.0, 30.2, 26.8])
M_r3 = np.array([-45.9, -68.3, -108.4, -116.2, 0, 39.1, 63.9, 81.0, 88.0, 
                 90.5, 90.0, 85.0, 78.5, 61.2, 48.7, 41.5, 34.2, 28.0, 25.9])

# Построение
plt.plot(M_r0, omega, 'k-', linewidth=2, label='R_д = 0')
plt.plot(M_r1, omega, '--', linewidth=1.5, label='R_д = 0.025·U_н/I_1н')
plt.plot(M_r2, omega, '-.', linewidth=1.5, label='R_д = 0.05·U_н/I_1н')
plt.plot(M_r3, omega, ':', linewidth=1.5, label='R_д = 0.1·U_н/I_1н')

plt.xlabel('Момент M, Н·м')
plt.ylabel('Скорость ω, рад/с')
plt.title('Рис. 2. Механические характеристики при введении сопротивления в цепь ротора')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-100, 100)
plt.ylim(-150, 200)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Сохраняем график 2
plt.savefig('graph_rheostat.png', dpi=300, bbox_inches='tight')
print("✓ График 2 сохранен: graph_rheostat.png")

print("\nГотово! Графики сохранены в текущей папке:")
print("  - graph_voltage.png")
print("  - graph_rheostat.png")