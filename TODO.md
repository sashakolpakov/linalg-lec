# Linear Algebra Notes — Progress

## Status: ALL 44 PAGES DONE.

---

## Done

| Pages | Content |
|-------|---------|
| 1 | Course philosophy: math as productive language, two-legs principle, linearity remark |
| 2 | Field basics (Z_2 example), vector space definition with all 8 axioms + quantifiers |
| 3 | Examples of vector spaces (F^n, {0}, function spaces, RGB exercise, P_n + isomorphism, exercise on deg-exactly-n) |
| 4 | Formal proofs philosophy (universality), Props 1.1.1–1.1.5 all proved with axiom annotations |
| 5 | Subspace definition, subspace test (one condition), trivial/non-trivial subspaces, affine non-example |
| 6 | Subspace examples (P_1 ≤ P_3, homogeneous vs inhomogeneous), sum of subspaces + Prop 1.2.1, direct sum + 3 equivalent characterizations |
| 7 | Props 1.2.2–1.2.3, §1.3 span = smallest containing subspace (proved), concrete span examples, Python (rank check) |
| 8 | Linear dependence ↔ one vector redundant (proved), basis via direct sum, coordinates remark, 4 equivalent characterizations of basis (proved), Python (coordinates) |
| 9 | Basis wrap-up remark, §1.9 matrices: digital image motivation, low-rank/SVD forward pointer, Python (rank-k approx) |
| 10 | Matrix definition, F^{m×n} is a vector space (proved via vec + standard units E_{ij}, dim=mn), transpose properties (proved), matrix-vector product as column linear combination |
| 11 | Matrix-matrix mult: 3 views (row, column, outer product) all proved, remark on why mult is defined this way, §1.5 linear transformations: hierarchy (set map → linear map → matrix) |
| 12 | Domain/codomain, linearity verified for Ax, differentiation D on P_n (matrix of D explicit), integration exercise J(p)(x)=∫₀¹ xp(xt)dt (D∘J=id, FTC exercise), proposition: linear map determined by basis |
| 13 | M_T = [T(e_1)\|…\|T(e_n)] proposition, L(V,W) is a vector space (proved), Theorem: composition = matrix mult (proved), associativity corollary |
| 14 | Summary (Av = linear map, BA = composition), roadmap: 3 open questions → change of basis, rank-nullity, eigenvalues/SVD |
| 15 | §1.6: im A and ker A definitions, Prop 1.6.1 (both are subspaces, proved), Python (kernel = space of linear relations) |
| 16 | Column operations preserving im A, echelon algorithm, example A=[[4,1,6,4],[2,0,1,7],[2,1,2,0]], Python (QR with column pivoting) |
| 17 | Combined algorithm [A;I] → [pivots\|0; t\|ker A], proof, example, Gauss-Jordan connection, Python (scipy orth/null_space + forward ref to §3) |
| 18 | Block diagram, Theorem 1.6.1 stated, rank definition, Python (rank is basis-independent), Steinitz remark |
| 19 | Rank sandwich proof, Theorem 1.6.2 (dim well-defined), Corollary 1.6.3: Rank-Nullity + Im-Ker Theorem (both forms), Python |
| 20 | Coordinate-finding algorithm [B\|v;I\|0], solving Ax=b, remarks on uniqueness and b∉im A, Python (lstsq) |
| 21 | 2×2 table (trivial/non-trivial kernel × b in/not in im A), matrix inverse AB=BA=I, invertibility via Im-Ker, Python (all 3 cases) |
| 22 | Polynomial regression setup: P_d ≅ ℝ^{d+1}, two failure modes, system of equations, Python (overdetermination) |
| 23 | β, X (Vandermonde), y, normal equations X^TX β = X^T y, Python (X^TX and lstsq comparison) |
| 24 | Inner products §2.1: bridge from regression, definition with 3 axioms, Python (axiom verification) |
| 25 | Examples (Euclidean, weighted, P_n), proof of positivity for P_n, Prop 3.1.1, Python (scipy.integrate) |
| 26 | Derived properties, norm definition, Prop 3.1.2, orthogonality, Pythagorean theorem, projection formula, Python |
| 27 | Prop 3.1.4, Cauchy-Schwarz (discriminant proof), Triangle Inequality, Parallelogram exercise, orthogonal complement |
| 28 | Normal equations solvability: geometric proof (projection) + algebraic proof (ker(X^TX)=ker(X)), hat matrix H |
| 29 | Lemma (⟨a,b⟩=0 ∀b → a=0), invertibility of X^TX, Vandermonde full rank remark, Python |
| 30 | Im-Ker full proof setup: row rank = col rank, two forms, basis extension, Python |
| 31 | Proof conclusion: V₂=span{u_j}, V=V₁⊕V₂, L(u_j) lin. indep., first isomorphism theorem remark |
| 32 | Row space + orthogonal complements: ℝ^m = row(A)⊕ker(A), four fundamental subspaces, Python |
| 33 | Theorem 3.1.9 (named), §4 Structural Properties, §4.1 Change of Basis setup, similar matrices, Python |
| 34 | A' = P^{-1}AP derivation, both equivalent forms, P always invertible remark, Python |
| 35 | §4.2 Eigenvalues: definition, example, Prop (λ eigenvalue ↔ L-λI not invertible), Python |
| 36 | Block structure via eigenbasis, Prop 4.2.1 (proved), Corollary (distinct → diagonalizable), invariant subspaces remark, Python |
| 37 | Prop 4.2.1 alternate proof, partial diagonalization theorem (k eigenvectors + r complement → block upper-triangular), k=n/k<n/k=0 cases, Python |
| 38 | Def diagonalizable (P^{-1}AP=Λ, not necessarily distinct), Prop 4.2.2, similar matrices, Abel-Ruffini remark on char. poly, Python |
| 39 | Open questions roadmap: which matrices are diagonalizable / how to find eigenvalues / existence; transition to spectral theorem |
| 40 | §4.3 PSD: def via A=B^TB, two definitions compared, quadratic form f(x)=‖Bx‖², ker B = ker A proof, Python (3 characterizations) |
| 41 | Invariant subspace definition + restriction, ker A is A-invariant, symmetric A → U^⊥ A-invariant (proved), spectral theorem inductive sketch, Python |
| 42 | Spectral theorem proof: constrained max on unit sphere, compactness argument, g(t) fraction formula, maximizer is eigenvector proposition |
| 43 | g'(0)=0 computation (exercise), double-complement conclusion Av∈⟨v⟩^{⊥⊥}=⟨v⟩, λ≥0 corollary, Spectral Theorem (Thm) stated |
| 44 | Eigenspace definition (E_λ = ker(A-λI), geometric multiplicity), Theorem 4.3.1 (P^TAP=Λ, P orthogonal), P^T vs P^{-1} remark, SVD forward pointer, Python |

---

## Lab ideas

Existing notebooks in the repo that can become structured labs:

| File | Topic | Key ideas |
|------|-------|-----------|
| `polynomial_regression.ipynb` | Practice 1 (already in notes) | Vandermonde matrix, normal equations, overfitting vs degree |
| `im-ker-Gaussian.ipynb` | Im/Ker algorithm + numerical rank | Column reduction implementation; **Hilbert matrix** — theoretically invertible but numerically rank-12 at n=20 (extreme condition number); gap between exact and floating-point rank |
| `Rayleigh_quotients.ipynb` | Eigenvalue computation without determinants | Rayleigh quotient $R(x)=x^TAx/x^Tx$; gradient descent on unit sphere finds min/max eigenvalue; deflation (project out found eigenvectors) to get the rest — the *practical* alternative to $\det(A-\lambda I)=0$ |
| `svd_tutorial.ipynb` | SVD geometry + image compression | Unit circle → ellipse picture; Frobenius error vs rank $k$ plot; singular value histograms and energy-per-decile for real images (astronaut, chelsea, coffee, camera) |
| `edge_detection.ipynb` | Image processing as linear algebra | Convolution = linear map on image matrices; finite-difference gradient (Sobel); Laplacian; diffusion PDE $X \leftarrow X + \alpha\Delta X + \beta(X-\bar X)$; Canny / Felzenszwalb segmentation |

### Additional lab ideas (not yet in notebooks)

| Lab | Description |
|-----|-------------|
| Denoising | $M = A_{\text{signal}} + E$; SVD truncation; elbow plot to pick rank; Marchenko–Pastur threshold $\sigma(\sqrt{m}+\sqrt{n})$ |
| LoRA | Simulate low-rank weight updates $\Delta W = AB^T$; show $r(m+n)$ vs $mn$ parameter count; connect to Eckart–Young |

---

## Post-completion: interactive website

**When all pages are done**, build a public course site combining the notes with live Python.

**Stack:**
- **Quarto** → compiles `notes.qmd` to a beautiful HTML site (math via MathJax) + PDF
- **GitHub Pages** → hosts the site, auto-deploys on push via GitHub Actions
- **Google Colab** → each Python example has an "Open in Colab" button (all students have access)

**Structure:**
```
/
├── notes.qmd              ← single source: LaTeX math + prose + code
├── _quarto.yml            ← build config (HTML + PDF targets)
├── .github/workflows/
│   └── deploy.yml         ← build + deploy to gh-pages on push
└── notebooks/
    └── chapterN.ipynb     ← one notebook per chapter, linked from notes
```

**Student experience:** open URL → read typeset notes in browser → click "Open in Colab" next to any code block → run and edit live, zero install.

**Instructor experience:** edit `notes.qmd`, push → site rebuilds automatically.
