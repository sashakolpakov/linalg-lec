"""
fig_stripes: Contrast between anti-diagonal and main-diagonal modes.
N=32, K=4: main-diagonal eigenvalue = |p-q| = 0.4 (DECAYS), anti-diagonal = p+q = 2.0 (grows).
Shown without normalisation, fixed vmax=1: anti-diagonal stays saturated, main-diagonal fades.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

N = 32
p, q = 1.2, 0.8
K = 4
m_idx, n_idx = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')

def step(u):
    return p * np.roll(np.roll(u, -1, axis=0), -1, axis=1) \
         + q * np.roll(np.roll(u, +1, axis=0), +1, axis=1)

def wave(k, direction='anti'):
    phase = 2 * np.pi * k * ((m_idx - n_idx) if direction == 'anti'
                              else (m_idx + n_idx)) / N
    return np.cos(phase)

T_steps = [0, 2, 4, 6, 10]
u_anti = wave(K, 'anti')
u_main = wave(K, 'main')

# Evolve
anti_frames = [u_anti.copy()]
main_frames = [u_main.copy()]
u_a, u_m = u_anti.copy(), u_main.copy()
for t in range(max(T_steps)):
    u_a = step(u_a);  u_m = step(u_m)
    anti_frames.append(u_a.copy())
    main_frames.append(u_m.copy())

# Eigenvalue magnitudes
lam_anti = p + q             # = 2.0
lam_main = abs(p - q)        # = 0.4 for K=N/4

fig, axes = plt.subplots(2, len(T_steps), figsize=(13, 5.5))
opts = dict(cmap='seismic', vmin=-1, vmax=1, origin='lower',
            interpolation='nearest')

for j, t in enumerate(T_steps):
    amp_a = lam_anti ** t
    amp_m = lam_main ** t

    axes[0, j].imshow(anti_frames[t], **opts)
    axes[0, j].set_title(f'$t={t}$\n'
                          r'amp $\times$' + f'{amp_a:.0f}', fontsize=9)
    axes[0, j].axis('off')

    axes[1, j].imshow(main_frames[t], **opts)
    axes[1, j].set_title(f'$t={t}$\n'
                          r'amp $\times$' + f'{amp_m:.4f}', fontsize=9)
    axes[1, j].axis('off')

fig.text(0.01, 0.73,
         r'anti-diag $K=4$' + '\n' + r'$|\lambda|=p{+}q=2.0$',
         va='center', fontsize=9, rotation=90, color='navy')
fig.text(0.01, 0.27,
         r'main-diag $K=4$' + '\n' + r'$|\lambda|=|p{-}q|=0.4$',
         va='center', fontsize=9, rotation=90, color='darkred')

fig.suptitle(
    r'Fixed colour scale $[-1,\,1]$: anti-diagonal grows (saturates), '
    r'main-diagonal decays  ($N=32$, $K=4$)',
    fontsize=11)
plt.tight_layout(rect=[0.04, 0, 1, 0.95])
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
