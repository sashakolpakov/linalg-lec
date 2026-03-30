"""
fig_perturbation: Amplification maps side-by-side for r=0 (diagonal-only) and r=0.05
(with axis-aligned coupling). Shows how the perturbation breaks anti-diagonal symmetry.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

p, q = 1.2, 0.8
k1 = np.linspace(-np.pi, np.pi, 512)
K1, K2 = np.meshgrid(k1, k1, indexing='ij')

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for ax, r_val, title in [
    (axes[0], 0.00, r'$r=0$  (diagonal-only, anti-diag axis special)'),
    (axes[1], 0.05, r'$r=0.05$  (axis-aligned coupling added)'),
]:
    lam_r = np.abs(p * np.exp(1j*(K1+K2)) + q * np.exp(-1j*(K1+K2))
                   + 2*r_val*(np.cos(K1) + np.cos(K2)))
    cf = ax.contourf(k1, k1, lam_r, levels=50, cmap='RdBu_r', vmin=0, vmax=2.5)
    ax.contour(k1, k1, lam_r, levels=[1.0], colors='k', linewidths=2)
    ax.axline((0, 0), slope= 1, color='lime',   lw=1.5, ls='--')
    ax.axline((0, 0), slope=-1, color='yellow', lw=1.5, ls='--')
    ax.set(title=title, xlabel=r'$k_1$', ylabel=r'$k_2$')
    plt.colorbar(cf, ax=ax, label=r'$|\lambda_r(k_1,k_2)|$')
plt.suptitle('Amplification maps: adding axis-aligned coupling breaks anti-diagonal symmetry')
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
