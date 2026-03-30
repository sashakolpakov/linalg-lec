"""
fig_diagonal_compare: Side-by-side of anti vs main-diagonal modes at K=1,2,4 on N=32.
Shows how |lambda| varies with K for main-diagonal but stays 2.0 for anti-diagonal.
At K=4: main-diagonal eigenvalue |p-q|=0.4 < 1, mode fully decays after T steps.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

N = 32
p, q = 1.2, 0.8
m_idx, n_idx = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')

def wave(k, direction='anti'):
    phase = 2 * np.pi * k * ((m_idx - n_idx) if direction == 'anti'
                              else (m_idx + n_idx)) / N
    return np.cos(phase)

def predict_fft(u0, t):
    Uhat = np.fft.fft2(u0)
    k1 = 2 * np.pi * np.fft.fftfreq(N)
    K1, K2 = np.meshgrid(k1, k1, indexing='ij')
    lam = p * np.exp(1j*(K1+K2)) + q * np.exp(-1j*(K1+K2))
    return np.real(np.fft.ifft2(Uhat * (lam ** t)))

def lam_main(K):
    k = 2 * np.pi * K / N
    return float(np.sqrt(p**2 + q**2 + 2*p*q*np.cos(4*k)))

K_vals = [1, 2, 4]
T = 15

fig, axes = plt.subplots(len(K_vals), 4, figsize=(13, 9))
opts = dict(cmap='seismic', vmin=-1, vmax=1, origin='lower', interpolation='nearest')

for row, K in enumerate(K_vals):
    lm = lam_main(K)
    u_a0 = wave(K, 'anti')
    u_m0 = wave(K, 'main')
    u_aT = predict_fft(u_a0, T)
    u_mT = predict_fft(u_m0, T)

    peak_a = float(np.max(np.abs(u_aT)))  # = 2^T
    peak_m = float(np.max(np.abs(u_mT)))  # = lm^T

    axes[row, 0].imshow(u_a0, **opts)
    axes[row, 0].set_title(f'anti-diag $K={K}$,  $t=0$', fontsize=9)

    # Show anti-diag at t=T normalised (it's just scaled up)
    axes[row, 1].imshow(u_aT / (peak_a + 1e-30), **opts)
    axes[row, 1].set_title(
        f'anti-diag $K={K}$,  $t={T}$\n'
        f'amp $\\times{peak_a:.1e}$  (shape unchanged)', fontsize=8)

    axes[row, 2].imshow(u_m0, **opts)
    axes[row, 2].set_title(
        f'main-diag $K={K}$,  $t=0$\n$|\\lambda|={lm:.2f}$', fontsize=9)

    # Show main-diag at t=T with same normalisation as t=0 to reveal decay/growth
    norm_factor = 1.0  # keep original scale (vmin/vmax=±1 clips/dims)
    axes[row, 3].imshow(u_mT / norm_factor, **opts)
    amp_label = f'{peak_m:.2e}' if peak_m < 0.1 else f'{peak_m:.2f}'
    axes[row, 3].set_title(
        f'main-diag $K={K}$,  $t={T}$\n'
        f'amp $\\times{amp_label}$', fontsize=8)

    for ax in axes[row]:
        ax.axis('off')

fig.suptitle(
    f'Anti-diagonal $|\\lambda|=2.0$ for all $K$; '
    f'main-diagonal $|\\lambda|$ depends on $K$  ($N={N}$, $t={T}$)',
    fontsize=11)
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix('.png'), dpi=150, bbox_inches='tight')
plt.close()
print('saved', Path(__file__).with_suffix('.png'))
