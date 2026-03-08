"""
fig12: Determinant as signed area.
Two vectors a, b from origin; parallelogram they span shaded.
det([[a1,b1],[a2,b2]]) = signed area.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

a = np.array([2.0, 0.5])
b = np.array([0.8, 2.0])

det = a[0]*b[1] - a[1]*b[0]   # = 3.6

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, 4.0); ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.6); ax.axvline(0, color='k', lw=0.6)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
ax.plot(0, 0, 'ko', ms=5, zorder=5)

# parallelogram vertices: 0, a, a+b, b
verts = np.array([[0,0], a, a+b, b])
poly = Polygon(verts, closed=True)
ax.add_collection(PatchCollection([poly], alpha=0.25, facecolor='#1f77b4',
                                   edgecolor='none', zorder=1))
# parallelogram edges (dashed for the "far" sides)
ax.plot([0, a[0]], [0, a[1]], color='#1f77b4', lw=0.9, ls='--', alpha=0.5)
ax.plot([0, b[0]], [0, b[1]], color='#d62728', lw=0.9, ls='--', alpha=0.5)
ax.plot([b[0], (a+b)[0]], [b[1], (a+b)[1]], color='#1f77b4', lw=0.9, ls='--', alpha=0.5)
ax.plot([a[0], (a+b)[0]], [a[1], (a+b)[1]], color='#d62728', lw=0.9, ls='--', alpha=0.5)

# vectors a and b from origin
for tip, col, lbl, off in [
        (a, '#1f77b4', '$a$', np.array([ 0.08, -0.22])),
        (b, '#d62728', '$b$', np.array([-0.28,  0.10]))]:
    ax.annotate('', xy=tip, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.4,
                                mutation_scale=16, zorder=6))
    ax.text(tip[0]+off[0], tip[1]+off[1], lbl, fontsize=15, color=col)

# area label in the centre of the parallelogram
cx, cy = (a + b) / 2
ax.text(cx, cy, r'$|\det A|$', fontsize=14, color='#1f77b4',
        ha='center', va='center')

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig12_determinant.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
