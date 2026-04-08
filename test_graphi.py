import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы
s = np.array([-0.75, -0.50, -0.40, -0.30, -0.20, -0.10, 0.00,
              0.10, 0.115, 0.20, 0.30, 0.40, 0.50, 0.587,
              0.75, 1.00, 1.25, 1.50, 1.75, 2.00])
omega = 104.72 * (1 - s)

M_k0 = np.array([-194.5, -119.7, -96.1, -74.0, -54.7, -37.3, 0,
                 25.2, 28.2, 41.1, 50.3, 55.2, 57.4, 57.8,
                 56.7, 52.9, 48.5, 44.4, 40.7, 37.5])
M_k002 = np.array([-66.0, -69.0, -67.1, -61.8, -53.1, -40.5, 0,
                   11.5, 13.1, 21.3, 29.4, 36.0, 41.4, 45.2,
                   50.6, 55.4, 57.4, 57.8, 57.2, 55.9])
M_k004 = np.array([-46.6, -52.8, -53.5, -51.7, -47.1, -38.7, 0,
                   7.5, 8.5, 14.2, 20.2, 25.6, 30.4, 34.0,
                   39.9, 46.7, 51.4, 54.5, 56.4, 57.5])
M_k008 = np.array([-34.9, -41.6, -43.1, -42.9, -40.6, -35.1, 0,
                   4.4, 5.0, 8.5, 12.4, 16.0, 19.4, 22.2,
                   27.1, 33.5, 38.8, 43.2, 46.8, 49.7])

plt.figure(figsize=(10,6))
plt.plot(M_k0, omega, 'k-', linewidth=2, label='k = 0')
plt.plot(M_k002, omega, 'k--', linewidth=1.5, label='k = 0,025')
plt.plot(M_k004, omega, 'k-.', linewidth=1.5, label='k = 0,05')
plt.plot(M_k008, omega, 'k:', linewidth=1.5, label='k = 0,1')
plt.xlabel('Момент M, Н·м')
plt.ylabel('Скорость ω, рад/с')
plt.title('Задание 2. Механические характеристики со схемой включения R_д')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-70, 70)
plt.ylim(-150, 200)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('graph_task2_final.png', dpi=300)
print('График сохранён как graph_task2_final.png')