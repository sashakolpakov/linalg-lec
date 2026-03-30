"""
fig_amplification_map: Heat map of |lambda(k1,k2)| over the Brillouin zone [-pi,pi)^2.
Black curve = stability boundary |lambda|=1.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

p, q = 1.2, 0.8
k1 = np.linspace(-np.pi, np.pi, 512)
k2 = np.linspace(-np.pi, np.pi, 512)
K1, K2 = np.meshgrid(k1, k2, indexing='ij')
lam_abs = np.sqrt(p**2 + q**2 + 2*p*q*np.cos(2*(K1 + K2)))

fig, ax = plt.subplots(figsize=(7, 6))
cf = ax.contourf(k1, k2, lam_abs, levels=50, cmap='RdBu_r')
plt.colorbar(cf, ax=ax, label=r'$|\lambda(k_1, k_2)|$')
ax.contour(k1, k2, lam_abs, levels=[1.0], colors='k', linewidths=2)
ax.axline((0, 0), slope= 1, color='lime',   lw=1.5, ls='--',
          label=r'main diagonal $k_1 = k_2$')
ax.axline((0, 0), slope=-1, color='yellow', lw=1.5, ls='--',
          label=r'anti-diagonal $k_1 = -k_2$')
ax.set(xlabel=r'$k_1$', ylabel=r'$k_2$',
       title=r'Amplification factor $|\lambda(k_1,k_2)|$ (black = stability boundary)')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
