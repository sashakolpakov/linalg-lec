# Linear Algebra Labs — UATX

12 computational labs, designed for an 11-week course. Each lab runs entirely in Google Colab (no local setup required).

---

## Lab 01 — Vector Spaces in Python
**Week 1**

Turn the abstract vector-space axioms into Python: stochastic axiom checker, subspace criterion, span visualisation in 2D and 3D, and the isomorphism $P_2 \cong \mathbb{R}^3$. Extension: direct-sum test.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab01_vector_spaces.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 02 — Linear Maps and Their Matrices
**Week 2**

Build differentiation $D$ and integration $J$ as explicit matrices on $P_n$ and verify $DJ = I$. Implement `matrix_of_T(T, basis)` for arbitrary linear maps; compute matrices of reflection, rotation, and projection; verify $M_{S \circ T} = M_S M_T$.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab02_linear_maps.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 03 — Image, Kernel, and Gaussian Elimination
**Weeks 3–4**

Column-reduce $[A \mid I_n]$ to simultaneously extract bases for $\mathrm{im}(A)$ and $\ker(A)$. Solve $Ax = b$ in all three cases (unique / infinitely many / no solution). Explore the Hilbert matrix: exact arithmetic keeps full rank; floating-point collapses for $n \geq 13$.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab03_im_ker_gaussian.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 04 — Solving $Ax = b$: The Four Cases
**Week 4**

Construct matrices realising all four solvability cases (unique / infinitely many / no solution). Extract and parameterise the full solution set $x_0 + \ker(A)$. Compute and verify the least-norm solution $x^* \in \mathrm{row}(A)$. Visualise solution sets as lines and planes.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab04_solving_axb.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 05 — Polynomial Regression
**Weeks 4–5**

Fit polynomials to noisy data via the Vandermonde matrix and normal equations. Observe underfitting and overfitting as degree increases. Use a validation set to select the optimal degree; connect explosion of validation error to ill-conditioning of the Vandermonde matrix.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab05_polynomial_regression.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 06 — Inner Products, Norms, and Gram–Schmidt
**Week 6**

Implement classical and modified Gram–Schmidt; verify $A = QR$ and $Q^\top Q = I$. Apply GS to $\{1, x, x^2, x^3\}$ under the $L^2[-1,1]$ inner product to recover Legendre polynomials. Solve polynomial regression via QR (more stable than normal equations). Verify the Cauchy–Schwarz inequality numerically.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab06_gram_schmidt.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 07 — The Four Fundamental Subspaces
**Weeks 6–7**

Compute orthonormal bases for $\mathrm{col}(A)$, $\ker(A)$, $\mathrm{row}(A)$, and $\ker(A^\top)$; verify dimensions satisfy rank–nullity. Confirm orthogonality relations $\mathrm{row}(A) \perp \ker(A)$ and $\mathrm{col}(A) \perp \ker(A^\top)$. Decompose a vector into its column-space and left-null-space components. Visualise all four subspaces for a rank-2 matrix in $\mathbb{R}^3$.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab07_four_subspaces.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 08 — Change of Basis
**Week 7**

Implement `coords(v, B)` for arbitrary bases; convert vectors back and forth. Compute the change-of-basis transform $A' = P^{-1}AP$ and verify it represents the same map. Diagonalise a matrix via its eigenbasis: $P^{-1}AP = \Lambda$. Use $A^k = P\Lambda^k P^{-1}$ to compute matrix powers and derive the Binet formula for the Fibonacci sequence.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab08_change_of_basis.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 09 — Eigenvalues via Rayleigh Quotients
**Week 8**

Minimise the Rayleigh quotient $R(x) = x^\top Ax / x^\top x$ by gradient descent on the unit sphere to find $\lambda_{\min}$. Recover the full spectrum by successive deflation (projecting out found eigenvectors). Plot convergence $|R(x_t) - \lambda_{\min}|$ for different learning rates. Compare timing against `numpy.linalg.eigh` on a $100 \times 100$ matrix.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab09_rayleigh_quotients.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 10 — SVD: Geometry and Image Compression
**Week 9**

Visualise $A = U\Sigma V^\top$ mapping the unit circle to an ellipse. Plot Frobenius reconstruction error vs rank $k$ (Eckart–Young theorem). Compress real grayscale images at ranks 5, 20, 60; plot singular-value histograms. Find the minimum rank $k^*$ for 95% energy retention and report the compression ratio.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab10_svd.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 11 — Image Processing as Linear Algebra
**Weeks 9–10**

Every image filter is a linear map. Build the Toeplitz matrix for 1D convolution and verify it matches `scipy.ndimage.convolve`. Apply blur, sharpen, Sobel, and Laplacian kernels to a real image; verify linearity numerically. Compute the SVD of blur and derivative Toeplitz matrices and interpret singular-value decay. Extension: deconvolution via pseudoinverse and the noise-amplification problem.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab11_image_processing.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Lab 12 — Matrix Denoising via SVD
**Week 10**

Observe a rank-3 signal corrupted by Gaussian noise; read off the signal in the singular-value spectrum. Truncate SVD at ranks $k = 1,\ldots,7$ and find the optimal $k$ by recovery error. Implement rank estimation via the Marchenko–Pastur threshold and the elbow method; compare across noise levels. Denoise a real image and measure PSNR before and after.

<a href="https://colab.research.google.com/github/sashakolpakov/linalg-lec/blob/main/labs/lab12_denoising.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Dependencies

All labs require only standard scientific Python:

```
numpy  scipy  matplotlib  imageio  sympy
```

These are all pre-installed in Google Colab. No additional setup is needed.
