"""
fig_blip: Single-cell blip evolving under the diagonal transfer rule.
Uses N=64 so the spreading diagonal is clearly visible in each panel.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

N = 64
p, q = 1.2, 0.8

def step(u):
    return p * np.roll(np.roll(u, -1, axis=0), -1, axis=1) \
         + q * np.roll(np.roll(u, +1, axis=0), +1, axis=1)

def simulate(u0, T):
    u = u0.copy()
    frames = [u.copy()]
    for _ in range(T):
        u = step(u)
        frames.append(u.copy())
    return frames

u0 = np.zeros((N, N))
u0[N//2, N//2] = 1.0
frames = simulate(u0, T=20)

fig, axes = plt.subplots(1, 4, figsize=(13, 4))
for ax, t in zip(axes, [0, 5, 10, 20]):
    clip = max(np.max(np.abs(frames[t])), 1e-12)
    ax.imshow(frames[t] / clip, cmap='seismic', vmin=-1, vmax=1,
              origin='lower', interpolation='nearest',
              extent=[-N//2, N//2, -N//2, N//2])
    ax.set_title(f'$t = {t}$', fontsize=12)
    ax.set_xlabel('$m$'); ax.set_ylabel('$n$')
fig.suptitle("Single-cell blip: spreads only along the main-diagonal axis $m = n$",
             fontsize=13)
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
