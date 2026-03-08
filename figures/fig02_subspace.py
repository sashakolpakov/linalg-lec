"""
fig02: Subspace vs affine subspace in R^2.
All vectors drawn from the origin. Dashed lines show the parallelogram sides.
Left:  line through origin — closed under addition (u+v stays on the line).
Right: line x2=1 — NOT closed (u+v lands on x2=2, off the set).
"""
import numpy as np
import matplotlib.pyplot as plt

def draw_vec(ax, tip, col, lw=2.2, zorder=4):
    ax.annotate('', xy=tip, xytext=(0,0),
                arrowprops=dict(arrowstyle='->', color=col,
                                lw=lw, mutation_scale=14, zorder=zorder))

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5))

for ax in (axL, axR):
    ax.set_xlim(-3, 3); ax.set_ylim(-2.4, 3.2)
    ax.set_aspect('equal')
    ax.axhline(0, color='k', lw=0.7)
    ax.axvline(0, color='k', lw=0.7)
    ax.grid(True, alpha=0.2)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)

C = {'u':'#1f77b4', 'v':'#d62728', 's':'#2ca02c'}

# ── LEFT: subspace — line through origin ─────────────────────────────────────
t = np.linspace(-3, 3, 200)
axL.plot(t, 0.8*t, color='#1f77b4', lw=2, alpha=0.4)

u = np.array([ 2.0,  1.6])
v = np.array([-1.5, -1.2])
s = u + v                          # = (0.5, 0.4) — still on the line

# vectors from origin
draw_vec(axL, u, C['u'])
draw_vec(axL, v, C['v'])
draw_vec(axL, s, C['s'])

# parallelogram dashed sides (auxiliary, not main vectors)
axL.plot([u[0], s[0]], [u[1], s[1]], '--', color=C['v'], lw=1.2, alpha=0.6)
axL.plot([v[0], s[0]], [v[1], s[1]], '--', color=C['u'], lw=1.2, alpha=0.6)

# labels
axL.text(u[0]+0.12, u[1]+0.10, '$u$',   fontsize=13, color=C['u'])
axL.text(v[0]-0.35, v[1]-0.18, '$v$',   fontsize=13, color=C['v'])
axL.text(s[0]+0.12, s[1]+0.10, '$u+v$', fontsize=13, color=C['s'])
axL.plot(0, 0, 'ko', ms=6, zorder=5)

# ── RIGHT: affine — line x2 = 1 ──────────────────────────────────────────────
axR.axhline(1, color='#1f77b4', lw=2, alpha=0.5)   # the set

u2 = np.array([-1.5, 1.0])
v2 = np.array([ 1.0, 1.0])
s2 = u2 + v2                       # = (-0.5, 2.0) — NOT on x2=1

draw_vec(axR, u2, C['u'])
draw_vec(axR, v2, C['v'])
draw_vec(axR, s2, C['s'])

axR.plot([u2[0], s2[0]], [u2[1], s2[1]], '--', color=C['v'], lw=1.2, alpha=0.6)
axR.plot([v2[0], s2[0]], [v2[1], s2[1]], '--', color=C['u'], lw=1.2, alpha=0.6)

axR.text(u2[0]-0.35, u2[1]+0.12, '$u$',   fontsize=13, color=C['u'])
axR.text(v2[0]+0.12, v2[1]+0.12, '$v$',   fontsize=13, color=C['v'])
axR.text(s2[0]+0.12, s2[1]+0.10, '$u+v$', fontsize=13, color=C['s'])

# mark origin (NOT on x2=1)
axR.plot(0, 0, 'ko', ms=6, zorder=5)
# mark where x2=1 line is
axR.text(2.2, 1.15, '$x_2=1$', fontsize=11, color='#1f77b4')
# show x2=2 line where u+v lands
axR.axhline(2, color='#2ca02c', lw=1.5, alpha=0.5, linestyle='--')
axR.text(2.2, 2.15, '$x_2=2$', fontsize=11, color='#2ca02c')

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig02_subspace.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
