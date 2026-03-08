"""
fig04: Orthogonal projection of u onto v.
Shows u, v, the projection hat_u = (u·v/|v|^2)v, and the residual u - hat_u
perpendicular to v. Right-angle marker at the foot.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_vec(ax, tip, col, lw=2.2, alpha=1.0, ls='-'):
    ax.annotate('', xy=tip, xytext=(0,0),
                arrowprops=dict(arrowstyle='->', color=col, lw=lw,
                                linestyle=ls, mutation_scale=14,
                                alpha=alpha, zorder=4))

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 4.0)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.7); ax.axvline(0, color='k', lw=0.7)
ax.grid(True, alpha=0.2)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
ax.plot(0, 0, 'ko', ms=5, zorder=5)

v = np.array([3.0, 1.0])
u = np.array([1.5, 3.5])

# projection of u onto v
hat_u = (np.dot(u, v) / np.dot(v, v)) * v
resid = u - hat_u           # perpendicular component

# extend the v direction as a faint guide line
t = np.linspace(-0.2, 1.6, 200)
ax.plot(t*v[0], t*v[1], color='#1f77b4', lw=1.0, alpha=0.3, linestyle='--')

# main vectors from origin
draw_vec(ax, v,     '#1f77b4')          # v
draw_vec(ax, u,     '#d62728')          # u
draw_vec(ax, hat_u, '#2ca02c')          # projection

# residual: from hat_u to u (NOT from origin — it's the difference vector shown in place)
ax.annotate('', xy=u, xytext=hat_u,
            arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2.0,
                            mutation_scale=14, zorder=4))

# right-angle marker at hat_u
s = 0.18   # size of the square marker
perp_dir = resid / np.linalg.norm(resid)   # direction of residual (unit)
v_dir    = v    / np.linalg.norm(v)         # direction of v (unit)
corner   = hat_u + s*perp_dir + s*v_dir
ax.plot([hat_u[0] + s*perp_dir[0], corner[0], hat_u[0] + s*v_dir[0]],
        [hat_u[1] + s*perp_dir[1], corner[1], hat_u[1] + s*v_dir[1]],
        color='k', lw=1.2)

# labels
ax.text(v[0]+0.12,     v[1]+0.10,     '$v$',
        fontsize=14, color='#1f77b4')
ax.text(u[0]+0.12,     u[1]+0.06,     '$u$',
        fontsize=14, color='#d62728')
ax.text(hat_u[0]+0.08, hat_u[1]-0.28, r'$\hat{u}=\dfrac{u\cdot v}{\|v\|^2}\,v$',
        fontsize=12, color='#2ca02c', va='top')
ax.text(hat_u[0] + 0.5*resid[0] + 0.12,
        hat_u[1] + 0.5*resid[1],
        r'$u - \hat{u}$', fontsize=12, color='#ff7f0e')

ax.plot(*hat_u, 'o', color='#2ca02c', ms=7, zorder=5)

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
