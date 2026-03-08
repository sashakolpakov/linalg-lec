"""
fig09: SVD geometry — unit circle mapped to ellipse.
A = [[3,1],[0,2]]: non-symmetric, so input directions v_i and output u_i differ.
Shows: unit circle, ellipse, right singular vectors v1/v2, left singular vectors u1/u2.
"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3., 1.],
              [0., 2.]])

U, s, Vt = np.linalg.svd(A)
V = Vt.T   # columns are right singular vectors

fig, ax = plt.subplots(figsize=(7, 6.5))
ax.set_xlim(-4, 4); ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.6); ax.axvline(0, color='k', lw=0.6)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
ax.plot(0, 0, 'ko', ms=5, zorder=5)

# unit circle and ellipse
th = np.linspace(0, 2*np.pi, 400)
circle  = np.vstack([np.cos(th), np.sin(th)])
ellipse = A @ circle
ax.plot(circle[0],  circle[1],  'k--', lw=1.1, alpha=0.4)
ax.plot(ellipse[0], ellipse[1], color='#1f77b4', lw=2.0)

# right singular vectors v_i (on unit circle)
for i, (col, vs, ls) in enumerate(zip(['#d62728','#2ca02c'],
                                       [V[:,0], V[:,1]],
                                       ['-', '-'])):
    ax.annotate('', xy=vs, xytext=(0,0),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.2,
                                mutation_scale=14))
    off = np.array([-0.12, 0.12]) if vs[0] < 0 else np.array([0.08, 0.10])
    ax.text(vs[0]+off[0], vs[1]+off[1],
            f'$v_{i+1}$', fontsize=13, color=col)

# left singular vectors scaled by sigma_i: sigma_i * u_i (on ellipse)
for i, col in enumerate(['#d62728', '#2ca02c']):
    tip = s[i] * U[:, i]
    ax.annotate('', xy=tip, xytext=(0,0),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.2,
                                linestyle='dashed', mutation_scale=14))
    off = np.array([0.10, 0.10]) if tip[1] >= 0 else np.array([0.10, -0.22])
    ax.text(tip[0]+off[0], tip[1]+off[1],
            f'$\\sigma_{i+1} u_{i+1}$', fontsize=12, color=col)

# grey arrows: one upper, two lower — angles chosen where shear rotation is visible
# 90°: (0,1) -> (1,2): straight up bends to upper-right  (27° rotation)
# 240°: lower-left bends further left                    (~24° rotation)
# 280°: near-straight-down bends past vertical to lower-left (~24° rotation)
for ang in np.radians([90, 240, 280]):
    u  = np.array([np.cos(ang), np.sin(ang)])
    Au = A @ u
    ax.annotate('', xy=Au, xytext=u,
                arrowprops=dict(arrowstyle='->', color='gray',
                                lw=1.4, mutation_scale=10, alpha=0.7))
    ax.plot(*u,  'o', color='gray', ms=5, alpha=0.6)
    ax.plot(*Au, 'o', color='gray', ms=5, alpha=0.6)

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
