"""
fig08: PSD quadratic form x^T A x = c.
A = [[2,1],[1,2]], eigenvalues 1 and 3.
Level curves are ellipses whose principal axes align with the eigenvectors.
"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2., 1.],
              [1., 2.]])

vals, vecs = np.linalg.eigh(A)   # vals = [1, 3]
v1 = vecs[:, 0]   # lambda = 1: (1,-1)/sqrt(2)
v2 = vecs[:, 1]   # lambda = 3: (1, 1)/sqrt(2)

fig, ax = plt.subplots(figsize=(7, 6.5))
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.6); ax.axvline(0, color='k', lw=0.6)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
ax.plot(0, 0, 'ko', ms=5, zorder=5)

# level curves x^T A x = c  via contour
x1 = np.linspace(-3, 3, 400)
X1, X2 = np.meshgrid(x1, x1)
Z = A[0,0]*X1**2 + 2*A[0,1]*X1*X2 + A[1,1]*X2**2

levels = [1, 3, 6]
colors = ['#1f77b4', '#ff7f0e', '#9467bd']
for c, col in zip(levels, colors):
    cs = ax.contour(X1, X2, Z, levels=[c], colors=[col], linewidths=1.8)
    # label each ellipse at a convenient point: along v1 axis
    r = np.sqrt(c / vals[0])          # semi-axis length along v1
    pt = r * v1 * 1.05
    ax.text(pt[0]+0.08, pt[1]+0.30, f'$c={c}$', fontsize=10, color=col)

# eigenvector axes — drawn as double-headed arrows through origin
L = 2.7
for ev, lam, col, lbl, loff in [
        (v1, 1, '#d62728', r'$\lambda_1=1$',  (-0.85, -0.15)),
        (v2, 3, '#2ca02c', r'$\lambda_2=3$',  ( 0.10,  0.12))]:
    ax.annotate('', xy= L*ev, xytext=-L*ev,
                arrowprops=dict(arrowstyle='<->', color=col,
                                lw=1.6, mutation_scale=12, alpha=0.7,
                                linestyle='dashed'))
    ax.text(L*ev[0]+loff[0], L*ev[1]+loff[1], lbl, fontsize=12, color=col)

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig08_psd_quadratic.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
