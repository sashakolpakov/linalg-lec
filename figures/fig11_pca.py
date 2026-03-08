"""
fig11: PCA on a 2D data cloud.
Shows: centered scatter, PC1 (max variance direction), PC2 (orthogonal),
and the projection of one example point onto PC1.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# generate correlated 2D data
n = 80
cov = np.array([[3.0, 1.8],
                [1.8, 1.2]])
L = np.linalg.cholesky(cov)
X = (L @ rng.standard_normal((2, n))).T   # shape (n, 2)
X -= X.mean(axis=0)                        # center

# PCA via SVD of centered data matrix
_, s, Vt = np.linalg.svd(X, full_matrices=False)
# variance explained by each PC
var = s**2 / (n - 1)
pc1 = Vt[0]   # first principal component
pc2 = Vt[1]   # second principal component
# orient so pc1 points toward positive x1 (upper-right quadrant)
if pc1[0] < 0:
    pc1 = -pc1
if pc2[1] < 0:
    pc2 = -pc2

# scale arrows by std along each PC for visibility
scale1 = np.sqrt(var[0]) * 2.0
scale2 = np.sqrt(var[1]) * 2.0

fig, ax = plt.subplots(figsize=(7, 6.5))
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.5, alpha=0.4)
ax.axvline(0, color='k', lw=0.5, alpha=0.4)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)

# data cloud
ax.scatter(X[:, 0], X[:, 1], color='#aec7e8', s=22, alpha=0.7, zorder=2)

# pick a point with substantial scores on BOTH axes (non-degenerate parallelogram)
scores1 = X @ pc1
scores2 = X @ pc2
candidates = (np.abs(scores1) > 0.8) & (np.abs(scores2) > 0.6)
idx = np.where(candidates)[0][np.argmax(np.abs(scores2[candidates]))]
xp = X[idx]
z1 = xp @ pc1
z2 = xp @ pc2
foot1 = z1 * pc1   # foot on PC1 axis
foot2 = z2 * pc2   # foot on PC2 axis

# arrow: origin -> xp
ax.annotate('', xy=xp, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.8,
                            mutation_scale=13, zorder=6))

# dashed parallelogram sides: foot1->xp (parallel to PC2), foot2->xp (parallel to PC1)
ax.plot([foot1[0], xp[0]], [foot1[1], xp[1]],
        color='#2ca02c', lw=1.1, linestyle='--', alpha=0.6, zorder=3)
ax.plot([foot2[0], xp[0]], [foot2[1], xp[1]],
        color='#1f77b4', lw=1.1, linestyle='--', alpha=0.6, zorder=3)

ax.plot(*foot1, 'o', color='#1f77b4', ms=6, zorder=4)
ax.plot(*foot2, 'o', color='#2ca02c', ms=6, zorder=4)
ax.plot(*xp,    'o', color='#d62728', ms=8, zorder=7)

# PC arrows from origin, with dashed extension beyond the arrow tip
L_ext = 5.0   # how far to extend the dashed line
for tip, pc, lbl, col, off in [
        ( scale1 * pc1, pc1, '$\\mathrm{PC}_1$', '#1f77b4', np.array([ 0.15,  0.10])),
        ( scale2 * pc2, pc2, '$\\mathrm{PC}_2$', '#2ca02c', np.array([-0.85,  0.25]))]:
    # dashed full axis line through origin in both directions
    ax.plot([-L_ext*pc[0], L_ext*pc[0]], [-L_ext*pc[1], L_ext*pc[1]],
            color=col, lw=1.0, linestyle='--', alpha=0.35, zorder=1)
    ax.annotate('', xy=tip, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.4,
                                mutation_scale=16, zorder=6))
    ax.text(tip[0] + off[0], tip[1] + off[1], lbl, fontsize=13, color=col)

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
