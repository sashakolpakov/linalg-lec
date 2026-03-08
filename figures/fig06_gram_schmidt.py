"""
fig06: Gram-Schmidt orthogonalization in R^2.
Left:  original vectors v1, v2 (not orthogonal).
Right: orthonormal result e1, e2, with the projection step shown.
"""
import numpy as np
import matplotlib.pyplot as plt

def draw_vec(ax, tip, col, lw=2.2, ls='-', alpha=1.0, origin=(0,0)):
    ax.annotate('', xy=tip, xytext=origin,
                arrowprops=dict(arrowstyle='->', color=col, lw=lw,
                                linestyle=ls, mutation_scale=14,
                                alpha=alpha, zorder=4))

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5))

for ax in (axL, axR):
    ax.set_xlim(-1.2, 3.2); ax.set_ylim(-0.4, 3.0)
    ax.set_aspect('equal')
    ax.axhline(0, color='k', lw=0.7); ax.axvline(0, color='k', lw=0.7)
    ax.grid(True, alpha=0.2)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
    ax.plot(0, 0, 'ko', ms=5, zorder=5)

# original vectors
v1 = np.array([2.5, 0.5])
v2 = np.array([1.2, 2.4])

# ── LEFT: original basis ──────────────────────────────────────────────────────
draw_vec(axL, v1, '#1f77b4')
draw_vec(axL, v2, '#d62728')
axL.text(v1[0]+0.1, v1[1]+0.1, '$v_1$', fontsize=14, color='#1f77b4')
axL.text(v2[0]+0.1, v2[1]+0.1, '$v_2$', fontsize=14, color='#d62728')

# show the angle between them (not 90 deg)
theta1 = np.degrees(np.arctan2(v1[1], v1[0]))
theta2 = np.degrees(np.arctan2(v2[1], v2[0]))
from matplotlib.patches import Arc
arc = Arc((0,0), 0.8, 0.8, angle=0, theta1=theta1, theta2=theta2,
          color='gray', lw=1.2)
axL.add_patch(arc)
mid_angle = np.radians((theta1 + theta2)/2)
axL.text(0.55*np.cos(mid_angle), 0.55*np.sin(mid_angle), r'$\theta$',
         fontsize=11, color='gray', ha='center', va='center')

# ── RIGHT: Gram-Schmidt result ────────────────────────────────────────────────
e1 = v1 / np.linalg.norm(v1)
proj = np.dot(v2, e1) * e1          # projection of v2 onto e1
resid = v2 - proj                    # orthogonal component
e2 = resid / np.linalg.norm(resid)

# scale for visibility
scale = 2.2
e1s = scale * e1
e2s = scale * e2

# faint original vectors for reference
draw_vec(axR, v1, '#1f77b4', lw=1.2, alpha=0.25)
draw_vec(axR, v2, '#d62728', lw=1.2, alpha=0.25)

# projection step: show proj of v2 onto e1
proj_tip = proj   # unscaled, actual projection point
# offset the projection arrow perpendicular to e1 so it clears the blue e1 arrow
off = 0.06 * e2
draw_vec(axR, proj_tip + off, '#2ca02c', lw=1.8, ls='dashed', alpha=0.9,
         origin=tuple(off))
# residual from proj_tip to v2
draw_vec(axR, v2, '#ff7f0e', lw=1.5, ls='dashed', alpha=0.7,
         origin=tuple(proj_tip))
axR.plot(*proj_tip, 'o', color='#2ca02c', ms=6, zorder=5)

# right-angle marker at proj_tip
s = 0.16
v_dir = e1
r_dir = e2
corner = proj_tip + s*r_dir + s*v_dir
axR.plot([proj_tip[0]+s*r_dir[0], corner[0], proj_tip[0]+s*v_dir[0]],
         [proj_tip[1]+s*r_dir[1], corner[1], proj_tip[1]+s*v_dir[1]],
         color='k', lw=1.2)

# final orthonormal vectors (scaled)
draw_vec(axR, e1s, '#1f77b4', lw=2.5)
draw_vec(axR, e2s, '#d62728', lw=2.5)

# right-angle marker between e1 and e2 — place at a visible distance from origin
s2 = 0.55
corner2 = s2*e1 + s2*e2
axR.plot([s2*e1[0], corner2[0], s2*e2[0]],
         [s2*e1[1], corner2[1], s2*e2[1]], color='k', lw=1.2)

axR.text(e1s[0]+0.12, e1s[1]-0.22, '$e_1$', fontsize=14, color='#1f77b4')
axR.text(e2s[0]-0.38, e2s[1]+0.06, '$e_2$', fontsize=14, color='#d62728')
axR.text(v1[0]+0.08, v1[1]+0.08, '$v_1$', fontsize=11,
         color='#1f77b4', alpha=0.4)
axR.text(v2[0]+0.08, v2[1]+0.08, '$v_2$', fontsize=11,
         color='#d62728', alpha=0.4)

plt.tight_layout()
plt.savefig('/Users/sasha/linalg-lec/figures/fig06_gram_schmidt.png',
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
