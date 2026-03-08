"""
fig07: Eigenvalues — unit circle mapped to ellipse.
A = [[2,1],[1,2]], eigenvalues 1 (v1) and 3 (v2).
Shows: unit circle, ellipse (image), a few grey u->Au pairs, eigenvectors labeled.
"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2., 1.],
              [1., 2.]])

# eigenvectors: lambda=1 -> v1=(1,-1)/sqrt2, lambda=3 -> v2=(1,1)/sqrt2
v1 = np.array([ 1., -1.]) / np.sqrt(2)   # lambda = 1
v2 = np.array([ 1.,  1.]) / np.sqrt(2)   # lambda = 3

fig, ax = plt.subplots(figsize=(7, 6.5))
ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.6); ax.axvline(0, color='k', lw=0.6)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
ax.plot(0, 0, 'ko', ms=5, zorder=5)

# unit circle
th = np.linspace(0, 2*np.pi, 400)
circle = np.vstack([np.cos(th), np.sin(th)])
ax.plot(circle[0], circle[1], 'k--', lw=1.2, alpha=0.5)

# ellipse = image of unit circle
ellipse = A @ circle
ax.plot(ellipse[0], ellipse[1], color='#1f77b4', lw=2.0)

# a few grey u -> Au pairs (avoid eigenvector directions ±45°, ±135°)
sample_angles = np.radians([0, 90, 180, 270])
for ang in sample_angles:
    u  = np.array([np.cos(ang), np.sin(ang)])
    Au = A @ u
    ax.annotate('', xy=Au, xytext=u,
                arrowprops=dict(arrowstyle='->', color='gray',
                                lw=1.2, mutation_scale=10, alpha=0.7))
    ax.plot(*u,  'o', color='gray', ms=4, alpha=0.6, zorder=4)
    ax.plot(*Au, 'o', color='gray', ms=4, alpha=0.6, zorder=4)

# eigenvector v1: lambda=1, Av1 = v1 (same point on circle and ellipse)
ax.annotate('', xy=v1, xytext=(0,0),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=2.4, mutation_scale=14))
ax.text(v1[0]+0.08, v1[1]-0.24,
        '$v_1$', fontsize=13, color='#d62728')
ax.text(v1[0]+0.08, v1[1]-0.44,
        r'$Av_1 = v_1$', fontsize=11, color='#d62728')

# eigenvector v2: lambda=3, Av2 = 3*v2
Av2 = A @ v2   # = 3*v2
ax.annotate('', xy=v2,  xytext=(0,0),
            arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=2.4, mutation_scale=14))
ax.annotate('', xy=Av2, xytext=(0,0),
            arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=2.4,
                            mutation_scale=14, linestyle='dashed'))
ax.text(v2[0]+0.10,  v2[1]-0.10,  '$v_2$',           fontsize=13, color='#2ca02c')
ax.text(Av2[0]+0.08, Av2[1]+0.10, r'$Av_2 = 3\,v_2$', fontsize=11, color='#2ca02c')

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
