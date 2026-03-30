"""
fig_blip_growth: Growth of a single-cell blip under the diagonal transfer rule.
Left:  L1 norm grows exactly as (p+q)^t = 2^t  (binomial theorem).
Right: peak value grows as (p+q)^t / sqrt(t)  (local CLT for the binomial peak).
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

N = 64
p, q = 1.2, 0.8

def step(u):
    return p * np.roll(np.roll(u, -1, axis=0), -1, axis=1) \
         + q * np.roll(np.roll(u, +1, axis=0), +1, axis=1)

u0 = np.zeros((N, N))
u0[N//2, N//2] = 1.0

T = 20
u = u0.copy()
energies = [float(np.sum(np.abs(u)))]
max_vals  = [float(np.max(np.abs(u)))]
for _ in range(T):
    u = step(u)
    energies.append(float(np.sum(np.abs(u))))
    max_vals.append(float(np.max(np.abs(u))))

t_arr = np.arange(T + 1)

# Exact prediction for the binomial peak  C(t, j*) p^{j*} q^{t-j*}
# Local CLT approximation:  (p+q)^t / sqrt(2 pi t pq / (p+q)^2)
def peak_theory(t):
    if t == 0:
        return 1.0
    return (p + q)**t / np.sqrt(2 * np.pi * t * p * q / (p + q)**2)

peak_pred = np.array([peak_theory(t) for t in t_arr])

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

ax = axes[0]
ax.semilogy(t_arr, energies, 'b-o', ms=4, label=r'$\|u(t)\|_1$')
ax.semilogy(t_arr, (p + q)**t_arr, 'r--', lw=2, label=r'$(p+q)^t = 2^t$')
ax.set(xlabel='$t$', ylabel=r'$\|u(t)\|_1$  (log scale)',
       title=r'Total $|\mathrm{activity}|$ grows as $(p+q)^t$')
ax.legend(); ax.grid(True, which='both', alpha=0.3)

ax = axes[1]
ax.semilogy(t_arr, max_vals,  'g-o', ms=4, label=r'$\max|u(t)|$')
ax.semilogy(t_arr, peak_pred, 'r--', lw=2,
            label=r'$(p{+}q)^t / \sqrt{2\pi t\,pq/(p{+}q)^2}$')
ax.set(xlabel='$t$', ylabel=r'$\max|u(t)|$  (log scale)',
       title=r'Peak $\sim (p+q)^t/\sqrt{t}$  (binomial peak, local CLT)')
ax.legend(fontsize=8); ax.grid(True, which='both', alpha=0.3)

fig.suptitle("Growth of a single-cell blip  ($p=1.2,\\ q=0.8$)", fontsize=13)
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
