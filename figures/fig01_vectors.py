"""
fig01: Same vectors in R^3 (oblique projection) and P_2 (polynomial curves).
v1 + v2: x^2 coefficients cancel -> sum is a straight line.
"""
import numpy as np
import matplotlib.pyplot as plt

# ── oblique projection  (x1: lower-right, x2: lower-left, x3: up) ────────────
ex1 = np.array([ 1.0, -0.30])
ex2 = np.array([-0.60, -0.30])
ex3 = np.array([ 0.0,  1.0])

def p3(x1, x2, x3):
    return x1*ex1 + x2*ex2 + x3*ex3

# ── vectors ───────────────────────────────────────────────────────────────────
#  v1 = (2, 0, 1)  →  p1(x) = 2       + x^2   (upward parabola)
#  v2 = (0, 2,-1)  →  p2(x) = 2x - x^2        (downward parabola)
#  v1+v2=(2, 2, 0) →  (p1+p2)(x) = 2 + 2x     (line; x^2 cancels!)
v1 = np.array([2, 0,  1])
v2 = np.array([0, 2, -1])
vs = v1 + v2
C  = {'v1':'#1f77b4', 'v2':'#d62728', 'sum':'#2ca02c'}

fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5))

# ── LEFT: oblique 3-D drawing ─────────────────────────────────────────────────
axL.set_aspect('equal')
axL.axis('off')

O = p3(0,0,0)
def arrow(ax, tip, col, lw=2.2):
    ax.annotate('', xy=tip, xytext=O,
                arrowprops=dict(arrowstyle='->', color=col,
                                lw=lw, mutation_scale=14))

# coordinate axes
for tip, lbl, off in [
        (p3(4.5,0,0), '$x_1$',  ( 0.12, -0.08)),
        (p3(0,3.5,0), '$x_2$',  (-0.32, -0.06)),
        (p3(0,0,2.8), '$x_3$',  (-0.10,  0.14))]:
    arrow(axL, tip, 'k', lw=1.3)
    axL.text(tip[0]+off[0], tip[1]+off[1], lbl, fontsize=12)

# vector arrows + labels
for vec, lbl, col, loff in [
        (v1, r'$v_1=(2,0,1)$',   C['v1'],  ( 0.10,  0.08)),
        (v2, r'$v_2=(0,2,-1)$',  C['v2'],  (-0.28, -0.18)),
        (vs, r'$v_1+v_2=(2,2,0)$', C['sum'],( 0.08, -0.16))]:
    tip = p3(*vec)
    arrow(axL, tip, col)
    axL.text(tip[0]+loff[0], tip[1]+loff[1], lbl,
             color=col, fontsize=10.5, va='center')

# auto-fit limits
pts = [p3(*v) for v in [v1, v2, vs, (4.5,0,0),(0,3.5,0),(0,0,2.8)]]
xs = [q[0] for q in pts];  ys = [q[1] for q in pts]
axL.set_xlim(min(xs)-.5, max(xs)+1.0)
axL.set_ylim(min(ys)-.5, max(ys)+.5)
axL.set_title(r'Vectors in $\mathbb{R}^3$', fontsize=13, pad=10)

# ── RIGHT: polynomial curves ──────────────────────────────────────────────────
x = np.linspace(-1.1, 1.1, 300)
curves = [
    (r'$p_1(x)=2+x^2$',          v1[0]+v1[1]*x+v1[2]*x**2, C['v1']),
    (r'$p_2(x)=2x-x^2$',         v2[0]+v2[1]*x+v2[2]*x**2, C['v2']),
    (r'$(p_1+p_2)(x)=2+2x$',     vs[0]+vs[1]*x+vs[2]*x**2, C['sum']),
]
for lbl, y, col in curves:
    axR.plot(x, y, color=col, lw=2.2, label=lbl)

axR.axhline(0, color='k', lw=0.6)
axR.axvline(0, color='k', lw=0.6)
axR.grid(True, alpha=0.25)
axR.set_xlabel('$x$', fontsize=12)
axR.set_ylabel('$p(x)$', fontsize=12)
axR.set_title(r'Same vectors in $\mathcal{P}_2$', fontsize=13)
axR.legend(fontsize=10.5, loc='upper left')

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig01_vectors.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
