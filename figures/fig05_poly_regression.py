"""
fig05: Polynomial regression — underfitting vs good fit vs overfitting.
Single panel: noisy data, degree-1 underfit, degree-4 good fit, degree-9 overfit.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)

# true signal: a smooth cubic
x_data = np.linspace(-1, 1, 18)
y_true = 0.8*x_data**3 - 0.5*x_data + 0.3
y_data = y_true + rng.normal(0, 0.12, len(x_data))

x_plot = np.linspace(-1.05, 1.05, 400)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x_data, y_data, color='k', s=30, zorder=5, label='data')

styles = [
    (1,  '#d62728', '-',  'degree 1'),
    (4,  '#2ca02c', '-',  'degree 4'),
    (9,  '#ff7f0e', '--', 'degree 9'),
]

for deg, col, ls, lbl in styles:
    coeffs = np.polyfit(x_data, y_data, deg)
    y_fit  = np.polyval(coeffs, x_plot)
    # clip extreme overfit excursions for readability
    y_fit  = np.clip(y_fit, -1.8, 1.8)
    ax.plot(x_plot, y_fit, color=col, lw=2.2, linestyle=ls, label=lbl)

ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.6, 1.6)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12, rotation=0, labelpad=10)
ax.legend(fontsize=11, loc='upper left')

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig05_poly_regression.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
