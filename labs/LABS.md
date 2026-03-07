# Linear Algebra Labs — UATX

12 computational labs, designed for an 11-week course. Each lab runs entirely in Google Colab (no local setup required).

> **Note:** replace `YOUR_GITHUB_USER/YOUR_REPO` in the links below with your actual GitHub username and repository name after pushing.

---

## Lab 01 — Vector Spaces in Python
**Week 2 · Prerequisites: §1.1–§1.2 (pages 1–6)**

Turn the abstract vector-space axioms into Python: stochastic axiom checker, subspace criterion, span visualisation in 2D and 3D, and the isomorphism $P_2 \cong \mathbb{R}^3$. Extension: direct-sum test.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab01_vector_spaces.ipynb)

---

## Lab 02 — Linear Maps and Their Matrices
**Week 3 · Prerequisites: §1.5 (pages 11–14)**

Build differentiation $D$ and integration $J$ as explicit matrices on $P_n$ and verify $DJ = I$. Implement `matrix_of_T(T, basis)` for arbitrary linear maps; compute matrices of reflection, rotation, and projection; verify $M_{S \circ T} = M_S M_T$.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab02_linear_maps.ipynb)

---

## Lab 03 — Image, Kernel, and Gaussian Elimination
**Weeks 4–5 · Prerequisites: §1.6 (pages 15–21)**

Column-reduce $[A \mid I_n]$ to simultaneously extract bases for $\mathrm{im}(A)$ and $\ker(A)$. Solve $Ax = b$ in all three cases (unique / infinitely many / no solution). Explore the Hilbert matrix: exact arithmetic keeps full rank; floating-point collapses for $n \geq 13$.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab03_im_ker_gaussian.ipynb)

---

## Lab 04 — Solving $Ax = b$: The Four Cases
**Week 5 · Prerequisites: §1.6 (pages 20–21)**

Construct matrices realising all four solvability cases (unique / infinitely many / no solution). Extract and parameterise the full solution set $x_0 + \ker(A)$. Compute and verify the least-norm solution $x^* \in \mathrm{row}(A)$. Visualise solution sets as lines and planes.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab04_solving_axb.ipynb)

---

## Lab 05 — Polynomial Regression
**Weeks 5–6 · Prerequisites: pages 22–23, §2.1**

Fit polynomials to noisy data via the Vandermonde matrix and normal equations. Observe underfitting and overfitting as degree increases. Use a validation set to select the optimal degree; connect explosion of validation error to ill-conditioning of the Vandermonde matrix.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab05_polynomial_regression.ipynb)

---

## Lab 06 — Inner Products, Norms, and Gram–Schmidt
**Week 7 · Prerequisites: §2.1 / §3.1 (pages 24–29)**

Implement classical and modified Gram–Schmidt; verify $A = QR$ and $Q^\top Q = I$. Apply GS to $\{1, x, x^2, x^3\}$ under the $L^2[-1,1]$ inner product to recover Legendre polynomials. Solve polynomial regression via QR (more stable than normal equations). Verify the Cauchy–Schwarz inequality numerically.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab06_gram_schmidt.ipynb)

---

## Lab 07 — The Four Fundamental Subspaces
**Weeks 7–8 · Prerequisites: pages 30–32**

Compute orthonormal bases for $\mathrm{col}(A)$, $\ker(A)$, $\mathrm{row}(A)$, and $\ker(A^\top)$; verify dimensions satisfy rank–nullity. Confirm orthogonality relations $\mathrm{row}(A) \perp \ker(A)$ and $\mathrm{col}(A) \perp \ker(A^\top)$. Decompose a vector into its column-space and left-null-space components. Visualise all four subspaces for a rank-2 matrix in $\mathbb{R}^3$.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab07_four_subspaces.ipynb)

---

## Lab 08 — Change of Basis
**Week 8 · Prerequisites: §4.1 (pages 33–34)**

Implement `coords(v, B)` for arbitrary bases; convert vectors back and forth. Compute the change-of-basis transform $A' = P^{-1}AP$ and verify it represents the same map. Diagonalise a matrix via its eigenbasis: $P^{-1}AP = \Lambda$. Use $A^k = P\Lambda^k P^{-1}$ to compute matrix powers and derive the Binet formula for the Fibonacci sequence.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab08_change_of_basis.ipynb)

---

## Lab 09 — Eigenvalues via Rayleigh Quotients
**Week 9 · Prerequisites: §4.2 (pages 35–38)**

Minimise the Rayleigh quotient $R(x) = x^\top Ax / x^\top x$ by gradient descent on the unit sphere to find $\lambda_{\min}$. Recover the full spectrum by successive deflation (projecting out found eigenvectors). Plot convergence $|R(x_t) - \lambda_{\min}|$ for different learning rates. Compare timing against `numpy.linalg.eigh` on a $100 \times 100$ matrix.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab09_rayleigh_quotients.ipynb)

---

## Lab 10 — SVD: Geometry and Image Compression
**Week 10 · Prerequisites: §4.3 (page 44), Spectral Theorem**

Visualise $A = U\Sigma V^\top$ mapping the unit circle to an ellipse. Plot Frobenius reconstruction error vs rank $k$ (Eckart–Young theorem). Compress real grayscale images at ranks 5, 20, 60; plot singular-value histograms. Find the minimum rank $k^*$ for 95% energy retention and report the compression ratio.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab10_svd.ipynb)

---

## Lab 11 — Image Processing as Linear Algebra
**Weeks 10–11 · Prerequisites: §4.3, Lab 10**

Every image filter is a linear map. Build the Toeplitz matrix for 1D convolution and verify it matches `scipy.ndimage.convolve`. Apply blur, sharpen, Sobel, and Laplacian kernels to a real image; verify linearity numerically. Compute the SVD of blur and derivative Toeplitz matrices and interpret singular-value decay. Extension: deconvolution via pseudoinverse and the noise-amplification problem.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab11_image_processing.ipynb)

---

## Lab 12 — Matrix Denoising via SVD
**Week 11 · Prerequisites: §4.3, Lab 10**

Observe a rank-3 signal corrupted by Gaussian noise; read off the signal in the singular-value spectrum. Truncate SVD at ranks $k = 1,\ldots,7$ and find the optimal $k$ by recovery error. Implement rank estimation via the Marchenko–Pastur threshold and the elbow method; compare across noise levels. Denoise a real image and measure PSNR before and after.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USER/YOUR_REPO/blob/main/labs/lab12_denoising.ipynb)

---

## Dependencies

All labs require only standard scientific Python:

```
numpy  scipy  matplotlib  imageio  sympy
```

These are all pre-installed in Google Colab. No additional setup is needed.
