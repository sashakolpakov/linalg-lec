"""
fig03: Span in R^2.
Left:  two collinear vectors — span is just a line.
Right: two independent vectors — span fills all of R^2.
"""
import numpy as np
import matplotlib.pyplot as plt

def draw_vec(ax, tip, col, lw=2.2):
    ax.annotate('', xy=tip, xytext=(0,0),
                arrowprops=dict(arrowstyle='->', color=col,
                                lw=lw, mutation_scale=14, zorder=4))

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5))

for ax in (axL, axR):
    ax.set_xlim(-3, 3); ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axhline(0, color='k', lw=0.7)
    ax.axvline(0, color='k', lw=0.7)
    ax.grid(True, alpha=0.2)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12, rotation=0, labelpad=10)
    ax.plot(0, 0, 'ko', ms=5, zorder=5)

# ── LEFT: dependent vectors, span = line ─────────────────────────────────────
v1 = np.array([1.5,  1.0])
v2 = np.array([-2.4, -1.6])   # = (8/5)*(-1.5, -1.0), same direction

t = np.linspace(-3, 3, 200)
slope = v1[1]/v1[0]
axL.plot(t, slope*t, color='gray', lw=1.5, linestyle='--', alpha=0.6,
         label=r'$\mathrm{span}\{v_1,v_2\}$')

draw_vec(axL, v1,  '#1f77b4')
draw_vec(axL, v2,  '#d62728')

axL.text(v1[0]+0.12, v1[1]+0.12, '$v_1$', fontsize=13, color='#1f77b4')
axL.text(v2[0]-0.35, v2[1]-0.22, '$v_2$', fontsize=13, color='#d62728')
axL.text(2.2, -2.2, r'$\mathrm{span} = $ line', fontsize=11, color='gray',
         ha='right')

# ── RIGHT: independent vectors, span = R^2 ───────────────────────────────────
u1 = np.array([2.0,  0.5])
u2 = np.array([0.3,  2.0])

# shade the whole plane to show span = R^2
axR.fill_between([-3,3], -2.5, 2.5, color='#2ca02c', alpha=0.07)

draw_vec(axR, u1, '#1f77b4')
draw_vec(axR, u2, '#d62728')

# show a few linear combinations as dots
rng = np.random.default_rng(0)
for a, b in rng.uniform(-1.2, 1.2, (18, 2)):
    pt = a*u1 + b*u2
    if abs(pt[0]) < 2.8 and abs(pt[1]) < 2.3:
        axR.plot(*pt, '.', color='#2ca02c', ms=5, alpha=0.5, zorder=2)

axR.text(u1[0]+0.12, u1[1]+0.12, '$u_1$', fontsize=13, color='#1f77b4')
axR.text(u2[0]+0.12, u2[1]+0.10, '$u_2$', fontsize=13, color='#d62728')
axR.text(1.5, -2.1, r'$\mathrm{span} = \mathbb{R}^2$', fontsize=11,
         color='#2ca02c')

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
