"""
fig_glider: Conway's Game of Life glider on a 20x20 toroidal grid.
Shows 5 snapshots at t=0,4,8,12,16 (one full glider period = 4 ticks).
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def gol_step(grid):
    N = np.zeros_like(grid, dtype=int)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            N += np.roll(np.roll(grid, di, axis=0), dj, axis=1)
    return ((grid == 1) & ((N == 2) | (N == 3))) | ((grid == 0) & (N == 3))

# Canonical GoL glider (.X. / ..X / XXX), placed near top-left
#   row 1: col 2
#   row 2: col 3
#   row 3: col 1,2,3
SIZE = 20
G = np.zeros((SIZE, SIZE), dtype=int)
for r, c in [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]:
    G[r, c] = 1

fig, axes = plt.subplots(1, 5, figsize=(13, 3))
g = G.copy()
for ax, t in zip(axes, range(0, 20, 4)):
    ax.imshow(g, cmap='binary', interpolation='nearest', vmin=0, vmax=1)
    ax.set_title(f'$t = {t}$', fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])
    for _ in range(4):
        g = gol_step(g)

fig.suptitle("GoL glider: one diagonal step every 4 ticks", fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
