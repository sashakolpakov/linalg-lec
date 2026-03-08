"""
fig10: Eckart-Young theorem.
Left:  singular value spectrum — bars coloured blue (kept, k≤2) vs grey (discarded).
Right: Frobenius approximation error ||A - A_k||_F vs rank k.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
# build a rank-rich 6×8 matrix with a controlled spectrum
n = 6
# prescribe singular values with a nice decay
sv_true = np.array([5.0, 3.4, 2.1, 1.1, 0.5, 0.2])
U0, _ = np.linalg.qr(rng.standard_normal((6, 6)))
Vt0, _ = np.linalg.qr(rng.standard_normal((8, 8)))
A = U0 @ np.pad(np.diag(sv_true), ((0,0),(0,2))) @ Vt0

U, s, Vt = np.linalg.svd(A, full_matrices=False)  # s sorted descending

k_show = 2   # highlight keeping the first k_show+1 singular values (0-indexed: 0..k_show)

# Frobenius error vs rank k: err(k) = sqrt(sum s[k:]^2)
ks = np.arange(n + 1)
errors = np.array([np.sqrt(np.sum(s[k:]**2)) for k in ks])

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5))

# ── LEFT: singular value spectrum ─────────────────────────────────────────────
bar_colors = ['#1f77b4' if i <= k_show else '#aec7e8' for i in range(n)]
axL.bar(np.arange(1, n+1), s, color=bar_colors, edgecolor='white', linewidth=0.8, zorder=3)
# dividing line between kept and discarded
axL.axvline(k_show + 1.5, color='#d62728', lw=1.5, linestyle='--', zorder=4)
# bracket / label for kept region
axL.annotate('', xy=(0.55, max(s)*0.72), xytext=(k_show+1.45, max(s)*0.72),
             arrowprops=dict(arrowstyle='<->', color='#1f77b4', lw=1.4))
axL.text((k_show+1)/2 + 0.5, max(s)*0.76, f'$k={k_show+1}$ kept',
         fontsize=11, color='#1f77b4', ha='center')

axL.set_xticks(np.arange(1, n+1))
axL.set_xticklabels([f'$\\sigma_{i}$' for i in range(1, n+1)], fontsize=12)
axL.set_ylabel('singular value', fontsize=11)
axL.set_ylim(0, max(s)*1.15)
axL.grid(axis='y', alpha=0.25)
axL.set_axisbelow(True)

# ── RIGHT: Frobenius error vs rank ────────────────────────────────────────────
axR.step(ks, errors, where='post', color='#ff7f0e', lw=2.2, zorder=3)
axR.plot(ks, errors, 'o', color='#ff7f0e', ms=6, zorder=4)

# mark the k=k_show+1 point
k_marked = k_show + 1
axR.plot(k_marked, errors[k_marked], 'o', color='#d62728', ms=9, zorder=5)
axR.axvline(k_marked, color='#d62728', lw=1.5, linestyle='--', zorder=2, alpha=0.7)

axR.set_xlabel('rank $k$', fontsize=12)
axR.set_ylabel(r'$\|A - A_k\|_F$', fontsize=12)
axR.set_xticks(ks)
axR.set_xlim(-0.3, n + 0.3)
axR.set_ylim(0, errors[0] * 1.1)
axR.grid(alpha=0.25)
axR.set_axisbelow(True)

plt.tight_layout()
plt.savefig(str(__import__('pathlib').Path(__file__).with_suffix('.png')),
            dpi=150, bbox_inches='tight')
plt.close()
print('saved')
