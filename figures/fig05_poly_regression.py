"""
fig05: Polynomial regression — underfitting vs good fit vs overfitting.
True signal: sin(2*pi*x) on [0,1]. 13 noisy samples.
Degree 1 underfits. Degree 5 fits well. Degree 12 overfits wildly (Runge).
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

n = 13
x_data = np.linspace(0, 1, n)
y_true = np.sin(2 * np.pi * x_data)
y_data = y_true + rng.normal(0, 0.25, n)

x_plot = np.linspace(-0.02, 1.02, 600)

fig, ax = plt.subplots(figsize=(9, 5))
ax.scatter(x_data, y_data, color='k', s=35, zorder=5)

styles = [
    (1,  '#d62728', '-',  'degree 1'),
    (5,  '#2ca02c', '-',  'degree 5'),
    (12, '#ff7f0e', '--', 'degree 12'),
]

for deg, col, ls, lbl in styles:
    coeffs = np.polyfit(x_data, y_data, deg)
    y_fit  = np.polyval(coeffs, x_plot)
    y_fit  = np.clip(y_fit, -3.0, 3.0)
    ax.plot(x_plot, y_fit, color=col, lw=2.2, linestyle=ls, label=lbl, zorder=3)

ax.set_xlim(-0.15, 1.15); ax.set_ylim(-3.5, 3.5)
ax.axhline(0, color='k', lw=0.5)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12, rotation=0, labelpad=10)
ax.legend(fontsize=11, loc='upper left')

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
