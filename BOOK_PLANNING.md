# Book Planning: Linear Algebra Primed for AI/ML

This file contains suggestions only. No course notes, notebooks, figures, or
build files were rewritten as part of this analysis.

## Executive Direction

The strongest version of this project is not "Linear Algebra for AI/ML" in the
sense of deriving modern machine-learning architectures. It should be an
introductory linear algebra book whose examples, instincts, computational
habits, and applications prepare students to recognize and use linear algebra in
AI/ML later.

That distinction matters. The core should still be a serious first course in
linear algebra: vector spaces, subspaces, bases, linear maps, matrices, rank,
least squares, inner products, eigenvalues, spectral theorem, SVD, and selected
applications. AI/ML should shape the examples and problem choices, not replace
the spine of the subject.

My recommendation: make the book identity:

> Linear Algebra: Mathematics, Computation, and Data

or:

> Linear Algebra for Mathematical Computing

with a subtitle like:

> An introduction primed for AI, machine learning, and scientific computing.

## Current Repository Inventory

The repo currently contains these major assets:

- `linear_algebra_notes.tex`: one monolithic LaTeX article, 5467 lines, 21
  top-level sections, 47 Python listings, 12 included figures, and a full
  theorem/proof style.
- `linear_algebra_notes.pdf`: compiled main notes.
- `labs/`: 12 Jupyter notebooks plus `LABS.md` and `labs_all.tex`/PDF.
- `intro/`: a longer "Linear Game of Life" intro in both `.tex` and `.ipynb`,
  with generated figures.
- `baby_intro/`: a simplified first-lecture version using the intro figures.
- `robot_demo/`: a small interactive notebook on basis choice for robot-arm
  trajectories.
- `figures/`: source scripts and PNGs for the main notes.
- `.github/workflows/build.yml`: builds the main PDF and regenerates main
  figures.
- `README.md` and `TODO.md`: useful but now partially stale project summaries.

## High-Level Assessment

### What is already strong

- The notes have a clear philosophy: proofs and computation are paired rather
  than treated as separate worlds.
- The course already has a good applied arc: images, polynomial regression,
  least squares, Gram-Schmidt/QR, Rayleigh quotients, SVD, PCA, denoising, and
  image processing.
- The labs are topic-aligned with the lecture sequence and are Colab-friendly.
- The intro material is distinctive. The linearized Game of Life / Fourier /
  eigenmode story is a real book-opening hook if placed carefully.
- The notes avoid the common determinant-first trap and instead build toward
  structure, computation, and spectral methods.
- There is enough raw material for a serious book, not just lecture notes.

### Main risks

- The main notes are still shaped like accumulated lecture notes, not a book.
  They need chapter architecture, exercise architecture, summaries, reading
  flow, and consistent front/back matter.
- The scope expands after SVD into DFT, trace, determinants, tensor products,
  and exterior algebra. These are valuable, but if all remain in the core path,
  the book identity may drift from "intro linear algebra primed for AI/ML" into
  "broad algebra add-ons after linear algebra."
- Exercises are far too sparse for a book. I found only a small number of
  formal `exercise` environments and a few propositions marked `Homework`.
- The labs currently read more like solved guided notebooks than assignable
  homework notebooks. They need student/instructor variants, deliverables, and
  rubrics.
- Some metadata is stale or inconsistent:
  - `README.md` says "10-week course" and "through SVD and spectral theorem."
  - `labs/LABS.md` says "11-week course."
  - `labs/labs_all.tex` says Spring 2025 and marks several notebooks "to build,"
    even though all 12 notebooks exist.
  - `labs/labs_all.tex` refers to `lab11_edge_detection.ipynb`, while the repo
    has `lab11_image_processing.ipynb`.
  - The title page in the notes says Spring 2026.
- The build workflow only builds the main notes, not the lab PDF, intros, or
  notebooks.

## Recommended Book Spine

The current material wants to be reorganized into parts. A good book structure
would be:

### Front Matter

1. Preface: what the book is and is not.
2. How to use the book: proofs, Python, labs, exercises.
3. Notation and computational conventions.
4. Optional prologue: "A Linear Game of Life" or the shorter `baby_intro/`
   version.

The preface should explicitly state:

- This is an introductory linear algebra text.
- It is computation-aware from the first chapter.
- It prepares students for AI/ML by building the right linear algebra habits:
  data as vectors, models as maps, features as coordinates, learning as
  approximation, dimension reduction as projection, and low-rank structure as
  compression.
- It is not trying to teach neural networks, transformers, backpropagation, or
  modern ML theory.

### Part I: Vectors, Spaces, and Coordinates

Suggested chapters:

1. Vectors as mathematical objects and data objects
2. Vector spaces and subspaces
3. Span, linear independence, bases, and dimension
4. Coordinates and change of representation

Current source material:

- `linear_algebra_notes.tex`: Course Philosophy through Bases and Dimension.
- `baby_intro/`: possible motivational opener.
- `robot_demo/`: useful as an early change-of-basis demo or project.
- Labs 1 and 2.

AI/ML priming:

- Vectors as feature records, signals, images, and coefficients.
- Coordinates as representation choice.
- Basis choice as an interpretability and conditioning issue.
- Direct sums as separating independent sources of variation.

Do not overload this part with ML terminology. Students should first learn that
"data can be vectors" and "changing basis changes the description, not the
object."

### Part II: Linear Maps, Matrices, Rank, and Systems

Suggested chapters:

5. Matrices as linear maps
6. Image, kernel, and rank-nullity
7. Solving `Ax=b`: existence, uniqueness, and geometry
8. Applications of image/kernel: coding theory and constraints

Current source material:

- Matrices
- Linear Maps
- Column Space, Null Space, and Rank-Nullity
- Hamming(7,4) error-correcting code
- Labs 3 and 4

AI/ML priming:

- Feature maps and design matrices.
- Constraints, null spaces, identifiability, and non-uniqueness.
- Rank as information content.
- Underdetermined and overdetermined systems.

Recommendation:

- Keep Hamming codes as an optional application or end-of-part project. It is
  excellent for image/kernel over finite fields, but it is not central to the
  AI/ML-oriented path.

### Part III: Geometry, Orthogonality, and Least Squares

Suggested chapters:

9. Inner products, norms, and angles
10. Orthogonal projection and least squares
11. QR, Gram-Schmidt, and the four fundamental subspaces
12. Regression, validation, and conditioning

Current source material:

- Polynomial Regression
- Inner Products and Norms
- Im-Ker Theorem: Full Proof
- Four fundamental subspaces material
- Labs 5, 6, and 7

AI/ML priming:

- Least squares as the first learning problem.
- Residuals as orthogonal projection errors.
- Normal equations vs QR as a stability lesson.
- Train/validation split as model selection, not just curve fitting.
- Feature scaling and ill-conditioning.
- Cosine similarity and embeddings as an inner-product application.

Recommendation:

- Polynomial regression should become the first major "learning" chapter, but
  frame it as approximation/projection first and ML terminology second.
- Add ridge regression as an optional box or exercise after normal equations,
  not as a core theorem.

### Part IV: Spectral Thinking

Suggested chapters:

13. Change of basis and similarity
14. Eigenvalues, eigenvectors, and dynamics
15. Positive semidefinite matrices
16. The spectral theorem
17. Rayleigh quotients and optimization

Current source material:

- Structural Properties of Linear Transformations
- Eigenvalues and Diagonalization
- Positive Semidefinite Matrices
- Trace, if integrated into PSD/spectral material
- Lab 8 and Lab 9
- `intro/` Game of Life material, selectively

AI/ML priming:

- Eigenvectors as stable directions of a transformation.
- PSD matrices as covariance, Gram matrices, and quadratic losses.
- Rayleigh quotient as a controlled introduction to optimization on a sphere.
- Spectral decomposition as changing to coordinates where the system decouples.

Recommendation:

- Integrate `Trace` into the spectral/PSD chapter rather than leaving it as a
  tiny standalone section. Trace naturally belongs with eigenvalue sums,
  covariance, variance explained, and Frobenius norm identities.
- The Game of Life intro should be either a prologue or an opening case study
  for spectral thinking, not a prerequisite-heavy detour in the middle.

### Part V: SVD, Data Matrices, and Low-Rank Structure

Suggested chapters:

18. Singular value decomposition
19. Low-rank approximation and Eckart-Young
20. PCA and dimensionality reduction
21. Image compression and denoising
22. Convolution, DFT, and image filters

Current source material:

- Singular Value Decomposition
- SVD applications: image compression, PCA
- The Discrete Fourier Transform
- Labs 10, 11, and 12

AI/ML priming:

- Data matrices and low-rank structure.
- PCA as variance-maximizing coordinates.
- SVD as compression, denoising, and representation learning intuition.
- Convolution as a linear map.
- DFT as diagonalization of convolution/circulant operators.
- LoRA only as an optional "why low rank matters in modern ML" box after SVD.

Recommendation:

- Move DFT/convolution after diagonalization or after SVD as an application
  chapter. It is valuable, especially for images and signal processing, but it
  should not interrupt the core path to spectral theorem and SVD.
- Keep Marchenko-Pastur in Lab 12 as an extension unless the target audience is
  mathematically mature. The main denoising story can work with elbow heuristics
  and controlled synthetic examples.

### Appendices / Advanced Complements

Suggested appendices:

A. Determinants, volume, and orientation
B. Tensor products and Kronecker products
C. Alternating forms and exterior algebra
D. Extra proof details and background theorems
E. NumPy/SciPy quick reference
F. Hints for selected exercises

Current source material:

- Determinants (Geometric Approach)
- Tensor Products
- Alternating Forms and the Exterior Algebra

Recommendation:

- Do not keep tensors and exterior algebra in the core introductory route.
  They are mathematically good, but they will pull the book away from the
  intended audience and identity.
- Tensor products can be a short optional bridge to data arrays, Kronecker
  products, separable filters, and multi-index features. Exterior algebra
  should be an appendix or separate enrichment note.

## Suggested Chapter Map

This is a possible final table of contents.

1. Prologue: A Linear Game of Life
2. Vectors, data, and linear structure
3. Vector spaces and subspaces
4. Span, independence, bases, and dimension
5. Matrices and linear maps
6. Coordinates and change of basis
7. Image, kernel, and rank-nullity
8. Solving linear systems
9. Least squares and polynomial regression
10. Inner product geometry
11. Orthogonal projection, QR, and the four subspaces
12. Eigenvalues, eigenvectors, and dynamics
13. Diagonalization and spectral decomposition
14. PSD matrices and quadratic forms
15. The spectral theorem and Rayleigh quotients
16. The SVD
17. Low-rank approximation, PCA, and data compression
18. Images, convolution, and the DFT
19. Denoising, matrix completion, and optional modern low-rank methods
20. Mathematical complements: determinants, tensors, exterior algebra
21. Hints for Selected Exercises

For a shorter course edition, chapters 18-20 can become optional modules.

## Exercise Architecture

The book needs a real exercise system. Right now, exercises exist, but they are
not structurally enough for homework, self-study, or instructor adoption.

Each chapter should have 30-50 exercises organized first by theme, then by
difficulty. The three core exercise tracks should be:

1. Theory exercises
2. Hand/computation exercises
3. Python/NumPy programming exercises

This partition is pedagogically important. The goal is not to make students do
large arithmetic by hand. The goal is to build the small-scale mechanical
intuition that lets them see what an algorithm or theorem is doing before
delegating the work to a computer.

### Accessibility and Complexity Guardrails

The default exercise target should be freshmen and sophomores in a first
serious linear algebra course. Exercises can be thoughtful and occasionally
challenging, but they should not be overspecialized, overcomplicated, or
dependent on background the course has not built.

Core rule:

> Most exercises should be solvable by a prepared freshman or sophomore using
> the current chapter, previous chapters, basic algebra, and basic Python/NumPy.

This means:

- avoid specialized ML jargon unless the problem defines it completely
- avoid long chains of prerequisites from analysis, abstract algebra,
  probability, optimization, or advanced CS
- avoid problems whose real difficulty is decoding notation
- avoid multi-page calculations unless the point is explicitly cumulative
- avoid "research taste" problems in ordinary homework
- avoid advanced applications that require knowing neural networks,
  transformers, convex optimization, measure theory, or statistics beyond the
  explanation given in the book
- keep most matrices small and structured
- keep most proofs one to eight meaningful lines
- reserve genuinely difficult problems for clearly labeled `Challenge`
  sections

The AI/ML priming should appear through accessible contexts:

- feature vectors
- images as arrays
- regression as approximation
- covariance and Gram matrices
- low-rank structure
- cosine similarity
- compression and denoising

It should not require students to already know machine learning.

### Difficulty Calibration

Suggested difficulty distribution per chapter:

- 50-60 percent A-level: direct fluency and basic theorem use
- 25-35 percent B-level: standard homework problems requiring synthesis
- 10-15 percent C-level: more interesting proof/application problems
- 0-5 percent D-level: optional challenge problems

Difficulty labels should mean:

- A: a student can solve it shortly after reading the relevant section
- B: a normal homework problem, usually combining two ideas
- C: a harder problem that may require a hint, a clever example, or a longer
  explanation
- D: optional challenge, enrichment, or unusually elegant problem

No ordinary homework should be built mostly from C/D problems. The book should
earn student confidence before asking for sophistication.

### Specialization Guardrails

Application problems should be broad and reusable. Prefer:

- "data matrix" over a narrow industrial scenario
- "image" over a specialized computer-vision pipeline
- "low-rank approximation" over a detailed modern model architecture
- "feature vector" over a domain-specific embedding model
- "covariance/Gram matrix" over an advanced probabilistic model

When a modern example is included, it should be self-contained and optional.
For example, a LoRA exercise should mainly ask for parameter counting and rank
intuition, not training dynamics or language-model architecture.

### Exercise Acceptance Checklist

Before adding an exercise to the main book, check:

- Can a prepared freshman or sophomore understand the statement?
- Are all nonstandard terms defined in the problem or earlier in the book?
- Is the exercise testing linear algebra rather than hidden background
  knowledge?
- Is the computation small enough to reveal structure without becoming a grind?
- Is the expected solution path reasonably short?
- If the exercise is hard, is it labeled `Challenge` or difficulty C/D?
- If the exercise is C/D, is there a hint at the end of the book?
- If the exercise uses Python, can it be done with basic Python and NumPy?
- If the exercise uses an AI/ML-flavored context, can it be solved without
  prior ML knowledge?
- Does the exercise ask for interpretation, not just manipulation?

Reject or revise an exercise if:

- it requires a long digression to state correctly
- it is mainly hard because the numbers are ugly
- it depends on specialized knowledge not taught in the book
- it is a disguised advanced topic
- it would take a normal student much longer than its pedagogical value
  justifies
- its only connection to AI/ML is branding

### Track 1: Theory Exercises

Theory exercises should train proof, structure, and conceptual transfer.

Subtypes:

- definitions and counterexamples
- short proof exercises
- theorem-application exercises
- "repair the false statement" exercises
- proof-completion exercises
- challenge proofs
- conceptual comparison questions

The theory track should include some genuinely interesting and challenging
problems, not only routine verification. These are where stronger students can
see the subject as a living structure rather than a list of procedures.

Examples:

- Prove that every kernel is a subspace, then find a subspace that is not
  obviously presented as a kernel and represent it as one.
- Give two non-isomorphic-looking vector spaces and construct an explicit
  isomorphism between them.
- Find the precise false step in an incorrect proof that an affine plane is a
  subspace.
- Prove that a Gram matrix is PSD, then explain why this matters for covariance
  matrices.
- Show that if a symmetric matrix has only positive eigenvalues, then its
  quadratic form is strictly positive away from zero.

### Track 2: Hand / Mechanical Computation Exercises

Hand computation exercises should be small, deliberate, and instructive. They
are not meant to reward stamina or arithmetic endurance. They should give
students "small motorics" for the subject: the mental feel of elimination,
projection, basis change, diagonalization, and SVD-scale reasoning.

Design rule:

- use small matrices, usually `2 x 2`, `3 x 3`, or carefully chosen `4 x 4`
- choose numbers that expose structure
- avoid ugly arithmetic unless the ugliness is itself the lesson
- ask for interpretation after computation
- make students predict before computing when possible

Subtypes:

- compute one step of an algorithm and explain what changed
- complete a partially worked calculation
- compare two methods on the same small example
- hand-check a theorem on a small matrix
- classify outcomes without fully solving
- draw the geometry of a computation
- estimate rank, dimension, or stability from structure

Examples:

- Perform two steps of Gaussian elimination and identify the pivot columns.
- Compute a basis for `ker(A)` for a `3 x 4` matrix with simple dependencies.
- Find coordinates of a vector in a nonstandard basis.
- Project a vector onto a line and interpret the residual geometrically.
- Run Gram-Schmidt on two or three small vectors, then identify where
  orthogonality appears.
- Diagonalize a `2 x 2` matrix with visible eigenvectors and use it to compute
  `A^5`.
- Compute a rank-one approximation from a simplified SVD already given.

Important framing:

Hand computation is not included because it is efficient. It is included
because students need to feel what the procedures do at small scale before they
trust or understand large-scale computation.

### Track 3: Basic Python / NumPy Programming Exercises

Python exercises should use only basic Python plus NumPy unless a chapter
explicitly needs a small amount of plotting. They should complement, not
duplicate, the labs.

Purpose:

- show how fast computers are at the same operations students saw by hand
- make students implement core algorithms from the ground up once
- compare naive implementations to NumPy/SciPy-backed routines
- reveal where BLAS/LAPACK-level routines enter the story
- build numerical caution: tolerances, conditioning, and floating-point error

Recommended constraint:

- core exercises: `python` + `numpy`
- optional visualization: `matplotlib`
- full labs may use `scipy`, `imageio`, and richer plotting
- do not require heavy ML frameworks

Subtypes:

- implement the algorithm directly
- call the NumPy routine and compare
- test a theorem numerically
- generate counterexamples
- benchmark naive vs library-backed computation
- explore floating-point failure modes
- reproduce a small hand computation at scale

Examples:

- Implement matrix-vector multiplication using loops, then compare with `A @ x`.
- Implement Gaussian elimination for small matrices, then compare with
  `np.linalg.solve`.
- Implement classical Gram-Schmidt, compare with `np.linalg.qr`, and test
  `Q.T @ Q`.
- Implement least squares through normal equations, compare with
  `np.linalg.lstsq`, and observe conditioning issues.
- Generate matrices with controlled rank and verify rank-nullity numerically.
- Implement power iteration for a symmetric matrix and compare with
  `np.linalg.eigh`.
- Build a rank-`k` SVD approximation using `np.linalg.svd` and verify the
  Frobenius error formula.

### Recommended Per-Chapter Exercise Mix

For a normal chapter:

- 8-12 theory exercises
- 8-12 hand/mechanical computation exercises
- 6-10 Python/NumPy exercises
- 2-4 cumulative or challenge exercises

For application-heavy chapters:

- fewer formal proofs
- more interpretation and Python
- at least a few hand examples to anchor the algorithms

For proof-heavy chapters:

- more theory
- enough hand examples to keep the abstractions grounded
- short Python checks where appropriate, but not as substitutes for proof

### Assignment Design Using the Three Tracks

Each homework should usually include:

- 2-3 theory problems
- 2-3 hand computation problems
- 1 Python/NumPy problem
- optionally 1 challenge problem

The Python problem should often be a continuation of a hand problem:

1. do the small case by hand
2. implement the algorithm
3. compare with NumPy
4. explain any numerical discrepancy

This structure teaches the full pipeline:

> theorem -> small mechanical example -> algorithm -> library routine ->
> interpretation.

### Hints at the End of the Book

The book should include a final "Hints for Selected Exercises" section. Hints
should help students get unstuck without turning the back matter into a full
solution manual.

Recommended placement:

- printed book/PDF: after appendices, before any full solution material
- web version: collapsible hint blocks or a separate hints page
- instructor version: hints plus full solutions, kept separate

Recommended hint coverage:

- most B-level exercises
- all C-level exercises
- all D-level challenge exercises
- selected A-level exercises only when the first step is commonly confusing

Recommended hint style:

- give the first useful move, not the whole solution
- point to a theorem or definition
- suggest a smaller example
- identify the right representation or basis
- warn about a common trap
- for Python problems, name the relevant array shapes or NumPy function, but
  do not provide full code unless the goal is debugging

Avoid:

- full worked solutions in the hint section
- hints that introduce new theory not in the chapter
- hints that make the exercise statement dependent on reading the hint
- long hints that are harder to parse than the problem

Example hint forms:

```text
Hint for 3.B7. Start by writing the three vectors as columns of a matrix.
The question is about pivot columns, not about solving a system with a
particular right-hand side.

Hint for 6.C4. Check the shape of `Q.T @ Q`. If the columns of `Q` are
orthonormal, what matrix should this be close to?

Hint for 10.A9. Use the fact that `B.T @ B` has quadratic form
`x.T @ B.T @ B @ x = ||Bx||^2`.
```

Hints should be numbered by exercise ID, not by page number, so they survive
format changes.

### Exercise Labels

Recommended visible labels:

- `Theory`
- `By Hand`
- `Python`
- `Challenge`

Recommended metadata tags:

- `proof`
- `compute`
- `concept`
- `python`
- `numpy`
- `data`
- `geometry`
- `algorithm`
- `conditioning`
- `application`
- `challenge`
- `hinted`

Suggested difficulty labels:

- A: routine fluency
- B: standard homework
- C: proof/application synthesis
- D: challenge or extension

The labels should help instructors assemble balanced homework quickly.

Recommended exercise IDs:

- `3.A1`: chapter 3, Theory, problem 1
- `3.B4`: chapter 3, By Hand, problem 4
- `3.C2`: chapter 3, Python, problem 2
- `3.D1`: chapter 3, Challenge/Cumulative, problem 1

The hints section should use these IDs directly:

```text
Hints for Chapter 3

3.A5. ...
3.B4. ...
3.C2. ...
```

### Chapter Exercise Section Template

Each chapter should end with a predictable exercise section. Suggested layout:

```text
Exercises

A. Theory
   A1. Definitions and counterexamples
   A2. Proofs and theorem use
   A3. Conceptual synthesis
   A4. Challenge theory

B. By Hand
   B1. Small computations
   B2. Algorithm walk-throughs
   B3. Geometry and interpretation
   B4. Checks against theorems

C. Python / NumPy
   C1. Implement the algorithm
   C2. Compare with NumPy
   C3. Numerical experiments
   C4. Scaling and stability

D. Cumulative / Projects
   D1. Mixed proof-computation problems
   D2. Short applied projects
   D3. Optional challenge problems
```

Do not hide the partition. Students should know which intellectual muscle an
exercise is meant to train. This also helps instructors build balanced
assignments without rereading every problem.

### The Hand-Work Principle

The hand-computation track should be governed by this principle:

> The purpose of hand calculation is mechanical intuition, not arithmetic
> burden.

This means:

- ask for one or two meaningful elimination steps, not a page of row reduction
- choose matrices where the theorem is visible
- give partially completed computations when the interesting part is the
  interpretation
- include "predict first" questions before calculation
- include "what changed?" questions after each algorithmic step
- allow exact arithmetic with simple fractions only when the fractions teach
  something
- prefer rank-one, diagonal, triangular, orthogonal, projection, and block
  examples when introducing new theorems

Good hand examples should make students say: "I see what the algorithm is
doing." They should not make students say: "I survived the arithmetic."

### The Python-Work Principle

The Python track should be governed by this principle:

> Implement once to understand, then compare with the professional routine.

For each major algorithm, the book should normally include this progression:

1. a small hand example
2. a direct NumPy implementation from the definition
3. a call to the appropriate `np.linalg` routine
4. a comparison of answers, speed, or numerical behavior
5. a short explanation of why production code uses the library routine

Examples of the implementation-then-compare pattern:

- loop-based matrix-vector multiplication vs `A @ x`
- manual Gaussian elimination vs `np.linalg.solve`
- normal equations vs `np.linalg.lstsq`
- classical Gram-Schmidt vs `np.linalg.qr`
- power iteration vs `np.linalg.eigh`
- rank-`k` reconstruction from `np.linalg.svd`

This keeps the programming exercises small enough for regular homework while
still showing students that NumPy inherits serious numerical linear algebra
from BLAS/LAPACK.

### Boundary Between Python Exercises and Labs

Short Python exercises and labs should not be the same thing.

Python exercises:

- are local to a chapter
- should usually take 15-45 minutes
- use basic Python and NumPy
- test one concept or one algorithm
- can be assigned inside ordinary homework
- should be possible in a plain `.py` file or one notebook cell sequence

Labs:

- are larger guided investigations
- may use plotting, images, `scipy`, `imageio`, and richer notebooks
- should have deliverables and reflection questions
- may combine several chapters
- should feel like a computational experiment, not just a code exercise

Example distinction:

- Python exercise: implement projection onto a line and compare with the matrix
  formula.
- Lab: use projections and least squares to fit several models, compare
  validation error, and discuss overfitting.

### Assignment Patterns

The most effective homework problems should chain the tracks. Suggested
patterns:

#### Pattern 1: Theorem, Small Case, Code

1. Prove or state the relevant theorem.
2. Work a `2 x 2` or `3 x 3` case by hand.
3. Implement the algorithm in NumPy.
4. Compare with a library routine.
5. Explain what the theorem predicted and what the computation confirmed.

Good for:

- rank-nullity
- least squares
- Gram-Schmidt
- diagonalization
- SVD reconstruction error

#### Pattern 2: Counterexample, Repair, Experiment

1. Give a false statement.
2. Find a small counterexample by hand.
3. Repair the statement by adding the missing hypothesis.
4. Generate random examples in Python to test the repaired version.

Good for:

- subspace tests
- diagonalizability
- orthogonality
- PSD equivalences
- numerical rank

#### Pattern 3: Algorithm Walk-Through

1. Do one or two algorithm steps by hand.
2. Identify the invariant preserved by those steps.
3. Finish the computation with NumPy.
4. Interpret the output geometrically.

Good for:

- elimination
- column reduction
- Gram-Schmidt
- QR
- power iteration

#### Pattern 4: Exact vs Floating Point

1. Analyze a small exact example.
2. Run the same example in floating point.
3. Perturb the input.
4. Explain the role of condition number, tolerance, or rounding.

Good for:

- Hilbert matrices
- Vandermonde regression
- nearly dependent bases
- normal equations
- small singular values

### Older Type List, Recast Under the Three Tracks

The earlier exercise categories still apply, but they should sit under the
three-track partition:

1. Reading checks
2. Conceptual questions
3. Hand computations
4. Proof exercises
5. Computational exercises
6. AI/ML-primed applications
7. Challenge problems
8. Cumulative review problems

### Example Exercise Families to Add

#### Vector spaces and subspaces

- Decide whether sets of signals, images, polynomials, and feature vectors are
  subspaces.
- Show that zero-mean signals form a subspace.
- Show that probability vectors do not form a vector space over `R`, but the
  affine hyperplane sum = 1 has a useful geometry.
- Give two different bases for the same space and translate coordinates.
- Explain why "degree exactly n" polynomials are not a subspace.

#### Bases and coordinates

- Compute coordinates in a nonstandard basis.
- Compare monomial basis vs a physically meaningful basis using the robot-arm
  demo.
- Find a basis that makes a simple transformation easier to interpret.
- Explain why basis choice matters for numerical conditioning.

#### Linear maps and matrices

- Build matrices for differentiation, integration, projection, rotation, and
  simple image filters.
- Given a rule on basis vectors, construct the full map.
- Determine whether a described transformation is linear.
- Interpret matrix multiplication as composition in concrete settings.

#### Image/kernel/rank

- Compute image and kernel bases by hand for small matrices.
- Interpret nontrivial kernel as non-identifiability.
- Construct matrices with prescribed rank and nullity.
- Relate rank to the number of independent features in a data matrix.

#### Solving systems

- Classify systems as no solution, unique solution, or infinitely many
  solutions.
- Parameterize solution sets as `x0 + ker(A)`.
- Find the least-norm solution in an underdetermined case.
- Explain why inconsistent systems lead naturally to least squares.

#### Least squares and regression

- Derive normal equations geometrically.
- Fit low-degree polynomials by hand for small data sets.
- Compare normal equations and QR numerically.
- Add validation-set problems: choose degree from train/validation error.
- Include conditioning examples with Vandermonde matrices.
- Add optional ridge regression: solve `(X^T X + lambda I) beta = X^T y`.

#### Inner products and orthogonality

- Prove Cauchy-Schwarz in several settings.
- Compute projections under weighted inner products.
- Interpret cosine similarity for vectors representing documents or embeddings.
- Show how orthogonality depends on the inner product.

#### Eigenvalues and spectral methods

- Compute eigenvalues/eigenvectors for small matrices by hand.
- Interpret eigenvectors as stable directions.
- Analyze powers `A^k` using diagonalization.
- Connect stochastic matrices or simple Markov chains to eigenvectors.
- Use Rayleigh quotient exercises for symmetric matrices.

#### PSD and spectral theorem

- Identify PSD matrices from factorizations, eigenvalues, and quadratic forms.
- Prove Gram matrices are PSD.
- Interpret covariance matrices as PSD.
- Relate PSD quadratic forms to convex bowls in least squares.

#### SVD and PCA

- Compute SVD for small diagonal or rank-one matrices.
- Use singular values to compute Frobenius reconstruction error.
- Prove or apply the Eckart-Young error formula in small cases.
- Perform PCA on a small centered data matrix.
- Interpret variance explained.
- Use SVD to identify low-rank signal plus noise.

#### DFT and convolution

- Build circulant matrices and diagonalize them with Fourier vectors.
- Verify convolution as matrix multiplication.
- Compare spatial convolution with frequency-domain multiplication.
- Analyze simple blur, sharpen, and derivative filters.

#### Optional modern ML boxes

- Low-rank adapters: parameter count of `Delta W = AB^T`.
- Embeddings: cosine similarity and projection.
- PCA as representation learning without labels.
- Collaborative filtering as low-rank matrix completion.
- Neural network linear layers as matrix maps.

These should be boxes or exercises, not the main theorem spine.

### Topic-by-Topic Three-Track Examples

The following is a more operational template for turning each chapter into
assignable work.

#### Vector spaces and subspaces

Theory:

- Prove that the solution set of a homogeneous linear system is a subspace.
- Find and repair a false proof that an affine line is a subspace.
- Construct a vector space whose vectors are not arrows or coordinate lists.
- Prove that "degree at most `n`" polynomials form a vector space, while
  "degree exactly `n`" polynomials do not.

By Hand:

- Test five small sets in `R^2` or `R^3` for the subspace property.
- Draw examples of a line through the origin, an affine line, a plane, and a
  union of two axes.
- For two small subspaces, compute their sum and intersection.

Python:

- Write a simple stochastic subspace tester using a membership function.
- Generate random linear combinations of two vectors and plot or inspect their
  span.
- Represent polynomials by coefficient arrays and verify addition/scalar
  multiplication numerically.

#### Span, independence, bases, and dimension

Theory:

- Prove that a linearly dependent list contains a redundant vector.
- Prove that coordinates in a basis are unique.
- Explain why dimension is an invariant of the vector space, not the chosen
  basis.

By Hand:

- Decide whether three vectors in `R^3` form a basis.
- Find coordinates of a vector in a nonstandard basis.
- Remove redundant vectors from a spanning list.

Python:

- Use `np.linalg.matrix_rank` to test independence.
- Solve `Bx = v` for coordinates in a basis.
- Generate nearly dependent vectors and compare exact intuition with numerical
  rank.

#### Linear maps and matrices

Theory:

- Prove that a linear map is determined by its values on a basis.
- Give examples of transformations that fail additivity or homogeneity.
- Prove that matrix multiplication represents composition.

By Hand:

- Build the matrix of a map from its action on basis vectors.
- Compute the matrix for a projection, reflection, or rotation in `R^2`.
- Compose two simple maps and compare with multiplying their matrices.

Python:

- Implement `matrix_of_T(T, basis)` for maps on `R^n`.
- Build differentiation and integration matrices for polynomial coefficient
  vectors.
- Compare manual composition with `B @ A`.

#### Image, kernel, rank, and systems

Theory:

- Prove rank-nullity in a small special case.
- Explain why nontrivial kernel means non-unique solutions.
- Prove that `b in im(A)` is the condition for solvability of `Ax=b`.

By Hand:

- Row-reduce a small matrix and identify pivot columns.
- Compute a basis for the kernel of a `2 x 3` or `3 x 4` matrix.
- Classify `Ax=b` as no solution, unique solution, or infinitely many
  solutions.

Python:

- Implement a minimal row-reduction routine for small matrices.
- Compare computed ranks with `np.linalg.matrix_rank`.
- Generate matrices of prescribed rank using products `U @ V`.

#### Least squares and regression

Theory:

- Derive the normal equations from orthogonality of the residual.
- Prove that the least-squares residual is orthogonal to the column space.
- Explain why full column rank gives a unique least-squares solution.

By Hand:

- Fit a line to three small points using normal equations.
- Compute a projection onto the column space of a `3 x 2` matrix.
- Compare exact solution, inconsistent system, and least-squares solution.

Python:

- Implement polynomial feature matrices with NumPy.
- Solve least squares using normal equations and compare with
  `np.linalg.lstsq`.
- Demonstrate overfitting with a small train/validation split.
- Show how Vandermonde conditioning changes with degree.

#### Inner products, projections, and QR

Theory:

- Prove Cauchy-Schwarz or use it to prove the triangle inequality.
- Show that orthogonality depends on the chosen inner product.
- Prove that Gram-Schmidt produces an orthogonal list when no zero vector is
  created.

By Hand:

- Project a vector onto a line.
- Compute an orthogonal basis from two or three simple vectors.
- Check `Q^T Q = I` for a small matrix.

Python:

- Implement classical Gram-Schmidt.
- Compare with `np.linalg.qr`.
- Create nearly dependent vectors and measure loss of orthogonality.
- Solve a least-squares problem with QR and compare with normal equations.

#### Eigenvalues, diagonalization, and dynamics

Theory:

- Prove that eigenvectors with distinct eigenvalues are linearly independent.
- Explain why diagonalization makes powers of a matrix easy.
- Give a matrix that has repeated eigenvalues but is not diagonalizable.

By Hand:

- Find eigenvalues and eigenvectors of a simple `2 x 2` matrix.
- Diagonalize a small matrix and compute `A^k`.
- Draw the action of a diagonal matrix and a similar matrix on basis vectors.

Python:

- Use `np.linalg.eig` or `np.linalg.eigh` and interpret the output.
- Implement power iteration.
- Compare symmetric and nonsymmetric examples.
- Simulate `x_{t+1} = A x_t` and explain the long-term behavior.

#### PSD matrices, spectral theorem, and Rayleigh quotients

Theory:

- Prove that `B.T @ B` is PSD.
- Prove that a symmetric matrix with nonnegative eigenvalues is PSD.
- Explain the relationship between covariance matrices and PSD matrices.

By Hand:

- Test PSD-ness of small diagonal and `2 x 2` matrices.
- Compute a quadratic form and sketch its level sets.
- Evaluate a Rayleigh quotient on several vectors.

Python:

- Generate Gram matrices and check eigenvalues with `np.linalg.eigvalsh`.
- Numerically minimize or maximize the Rayleigh quotient on the unit circle.
- Compare gradient-style iteration with `np.linalg.eigh`.

#### SVD, PCA, and low-rank approximation

Theory:

- Explain why SVD exists for rectangular matrices while diagonalization need
  not.
- Use Eckart-Young to justify best rank-`k` approximation.
- Prove the Frobenius error formula when the SVD is given.

By Hand:

- Compute SVD for a diagonal or rank-one matrix.
- Build a rank-one reconstruction from a provided singular triplet.
- Compute variance explained from a short list of singular values.

Python:

- Use `np.linalg.svd` to reconstruct a matrix.
- Compute rank-`k` approximations and Frobenius errors.
- Implement PCA by centering a data matrix and taking the SVD.
- Compare storage cost for low-rank image approximations.

#### DFT, convolution, and image filters

Theory:

- Prove that circulant convolution operators are diagonalized by Fourier
  vectors in a small finite case.
- Explain why convolution is linear but thresholding is not.
- Connect eigenvalues of a circulant matrix to the DFT of its kernel.

By Hand:

- Build a `4 x 4` circulant matrix from a short kernel.
- Apply a simple blur or difference filter to a tiny signal.
- Compute a tiny DFT by hand for a sparse vector.

Python:

- Implement 1D circular convolution directly and compare with FFT-based
  multiplication.
- Build Toeplitz or circulant convolution matrices.
- Apply simple filters to small arrays before using real images in labs.

## Homework Sequence

For a 10-12 week course, use roughly this sequence:

- HW0: Python/NumPy warmup, vectors, plotting, notation.
- HW1: vector spaces, subspaces, examples/non-examples.
- HW2: span, independence, bases, coordinates.
- HW3: matrices, linear maps, composition.
- HW4: image, kernel, rank-nullity, solving `Ax=b`.
- HW5: least squares and polynomial regression.
- HW6: inner products, projections, Gram-Schmidt, QR.
- HW7: four fundamental subspaces and orthogonal decompositions.
- HW8: change of basis, eigenvalues, diagonalization.
- HW9: PSD matrices, spectral theorem, Rayleigh quotients.
- HW10: SVD, low-rank approximation, PCA.
- HW11: image processing, DFT/convolution, denoising.
- Final project: choose one of PCA, image compression, denoising, Hamming code,
  robot-arm basis design, or low-rank recommendation.

For a book, every homework should pull from a larger exercise bank. Do not make
the homework the only exercises.

Each homework should also preserve the three-track balance:

```text
Homework N

Part A. Theory
  2-3 problems: proof, counterexample, theorem use, conceptual synthesis.

Part B. By Hand
  2-3 problems: small computations, algorithm walk-throughs, geometric
  interpretation.

Part C. Python / NumPy
  1 problem: implement a core algorithm or numerical experiment using basic
  Python and NumPy.

Part D. Challenge / Extension
  0-1 problem: optional or extra-credit, often more theoretical or more
  applied.
```

The Python problem should usually be connected to a hand problem from the same
homework. For example:

- HW4 by hand: compute `ker(A)` for a small matrix.
- HW4 Python: generate rank-deficient matrices and verify rank-nullity with
  `np.linalg.matrix_rank`.

or:

- HW6 by hand: run Gram-Schmidt on three simple vectors.
- HW6 Python: implement Gram-Schmidt and compare with `np.linalg.qr`.

or:

- HW10 by hand: compute the rank-one approximation from a provided SVD.
- HW10 Python: use `np.linalg.svd` to compute rank-`k` errors for larger
  matrices.

This makes the homework sequence teach scale:

1. understand the theorem
2. feel the small mechanical computation
3. implement the algorithm
4. compare with the optimized numerical routine
5. interpret what changed when the scale increased

## Lab Strategy

The labs are one of the strongest assets, but they need a publishing model.

Recommended versions:

- `labs/student/`: notebooks with prompts, starter code, TODO cells, and
  deliverables.
- `labs/solutions/`: complete instructor notebooks.
- `labs/shared/`: helper utilities, plotting functions, small datasets.
- `labs/LABS.md`: public index with Colab links.
- `labs/labs_all.tex`: lab manual built from the student-facing descriptions.

Current notebooks appear to be full guided solutions. That is fine for internal
development, but not enough for homework. Student versions should require real
work.

Each lab should have:

- prerequisites
- learning objectives
- required deliverables
- checkpoint questions
- coding tasks
- reflection questions
- optional extensions
- a short rubric

Labs should explicitly build on the shorter Python exercises but should not
replace them. The relationship should be:

```text
By-hand exercise:
  Work a tiny case until the algorithm is visible.

Python exercise:
  Implement the core operation in basic Python/NumPy and compare with NumPy.

Lab:
  Use the same idea in a richer computational setting with real data,
  visualization, interpretation, and a written deliverable.
```

Example:

- By hand: project a vector onto a line.
- Python exercise: implement projection onto a column space using
  `A @ np.linalg.solve(A.T @ A, A.T @ b)` and compare with `np.linalg.lstsq`.
- Lab: fit polynomial models, evaluate validation error, and explain
  overfitting.

Another example:

- By hand: compute one step of Gram-Schmidt.
- Python exercise: implement Gram-Schmidt and test `Q.T @ Q`.
- Lab: compare classical Gram-Schmidt, modified Gram-Schmidt, and QR on nearly
  dependent vectors.

Another example:

- By hand: build a rank-one approximation from a provided SVD.
- Python exercise: use `np.linalg.svd` to reconstruct rank-`k` approximations.
- Lab: compress and denoise images, then report storage and quality metrics.

### Lab-by-Lab Suggestions

#### Lab 1: Vector spaces in Python

Keep the stochastic axiom checker, but add a conceptual warning:

- Numerical testing can find counterexamples.
- Numerical testing does not prove an axiom universally.

Add deliverables asking students to produce one genuine proof and one numerical
counterexample.

#### Lab 2: Linear maps and matrices

Good fit for differentiation/integration and matrix representation. Add a
student task where they define a transformation in words, test linearity, and
construct its matrix if linear.

#### Lab 3: Image, kernel, Gaussian elimination

The Hilbert matrix rank-collapse topic is excellent. It should become the first
explicit "exact math vs floating-point computation" warning.

Add conditioning questions:

- What changes when the same matrix is treated exactly vs in float64?
- Why is numerical rank tolerance-dependent?

#### Lab 4: Solving `Ax=b`

Good place to separate existence, uniqueness, and minimum norm. Add a problem
where multiple students get different solutions and must explain why all are
correct.

#### Lab 5: Polynomial regression

This is the first ML-flavored lab. Add:

- train/validation split
- feature scaling
- ridge extension
- comparison of `np.linalg.lstsq`, normal equations, and QR

#### Lab 6: Gram-Schmidt

Add a near-linear-dependence example to show classical Gram-Schmidt instability
and modified Gram-Schmidt improvement.

#### Lab 7: Four fundamental subspaces

Turn this into a decomposition lab: every vector in the domain/codomain gets
split into meaningful pieces. This is a good place for diagrams and short proof
questions.

#### Lab 8: Change of basis

Connect directly to `robot_demo/`. Basis choice should feel useful, not
formalistic. Students should see that the same object can be simple or ugly
depending on coordinates.

#### Lab 9: Rayleigh quotients

Good spectral optimization lab. Add a derivation checkpoint for the gradient
and a conceptual question about why symmetric matrices are special.

#### Lab 10: SVD

Strong lab. Add a deliverable where students must explain the storage formula
and identify when low-rank compression is worse than storing the original.

#### Lab 11: Image processing

Fix the naming inconsistency later: docs mention `lab11_edge_detection.ipynb`
but the repo has `lab11_image_processing.ipynb`.

This lab should explicitly distinguish:

- linear filters
- nonlinear post-processing, such as gradient magnitude
- deconvolution as an ill-posed inverse problem

#### Lab 12: Denoising

Keep Marchenko-Pastur as an extension or advanced section. For main homework,
focus on:

- controlled low-rank signal
- singular value elbow
- reconstruction error
- image PSNR before/after denoising

## Repository Restructuring Proposal

No files were moved now. This is a suggested future structure.

```text
.
├── book/
│   ├── main.tex
│   ├── preamble/
│   ├── frontmatter/
│   ├── chapters/
│   │   ├── ch01-prologue.tex
│   │   ├── ch02-vector-spaces.tex
│   │   ├── ...
│   ├── appendices/
│   └── exercises/
│       ├── ch02-exercises.tex
│       ├── ch03-exercises.tex
│       └── ...
├── labs/
│   ├── student/
│   ├── solutions/
│   ├── shared/
│   ├── LABS.md
│   └── labs_all.tex
├── demos/
│   └── robot_arm_basis/
├── assets/
│   ├── figures/
│   │   ├── source/
│   │   └── generated/
│   └── data/
├── assignments/
│   ├── hw01.tex
│   ├── hw02.tex
│   └── ...
├── instructor/
│   ├── solutions/
│   └── rubrics/
├── scripts/
│   ├── build_figures.sh
│   ├── execute_notebooks.sh
│   └── build_book.sh
└── README.md
```

Notes:

- If instructor solutions should not be public, keep them out of the repo or in
  a private repo. Do not rely only on `.gitignore` for sensitive material.
- The current `linear_algebra_notes.tex` can first be split mechanically by
  chapter before doing any prose rewrite.
- Figure source and generated PNGs should be separated eventually.
- `intro/` and `baby_intro/` should become either frontmatter modules or
  `demos/linear_game_of_life/`.

## Build and Publishing Suggestions

### Conservative LaTeX path

Use a LaTeX `book` or `memoir` class, split chapters into files, and keep labs
as notebooks.

Advantages:

- Lowest migration risk.
- Preserves current theorem/proof machinery.
- Best for a polished PDF book.

Add later:

- `cleveref` for references.
- `subfiles` or simple `\input` chapter files.
- theorem numbering by chapter.
- exercise numbering by chapter.
- an index/glossary.

### Quarto/Jupyter Book path

Use Quarto Book if the web version and notebooks are first-class deliverables.

Advantages:

- Strong HTML output.
- Easier to integrate notebooks and executable code.
- Good for "read in browser, open in Colab" workflow.

Risk:

- Migration cost is real. Math-heavy proof text and custom theorem environments
  need careful conversion.

Recommendation:

- First modularize the current LaTeX source and stabilize the table of
  contents.
- Then prototype one chapter in Quarto before committing to a full migration.

## CI / Quality Control Suggestions

Current CI builds only the main notes PDF. Future CI should:

- regenerate all main figures
- compile the book PDF
- compile the lab manual PDF
- compile intro/baby intro PDFs if retained
- execute notebooks with a timeout
- fail on notebooks with broken imports or stale outputs
- optionally strip outputs from student notebooks
- upload PDFs as artifacts

Suggested future dependency files:

- `requirements.txt` or `environment.yml`
- pinned minimal versions for `numpy`, `scipy`, `matplotlib`, `imageio`,
  `sympy`, `jupyter`, and `nbclient`

## Style and Pedagogy Guidelines

### Keep the proof/computation alternation

The book's voice should keep alternating:

1. definition/theorem
2. geometric interpretation
3. small hand example
4. Python experiment
5. exercise/application

That rhythm is already present and should become intentional book structure.

### Use "why ML people care" boxes sparingly

Good boxes:

- Why least squares is the first learning problem
- Why feature scaling matters
- Why covariance matrices are PSD
- Why PCA is a change of coordinates
- Why low rank matters
- Why convolution is linear
- Why LoRA is a low-rank constraint

Avoid boxes that require too much external ML machinery:

- attention mechanisms
- backpropagation
- full neural network training
- transformer architecture
- modern optimization theory

### Make applications cumulative

Use recurring data objects:

- a small image matrix
- a polynomial regression data set
- a signal on a grid
- a feature matrix
- a low-rank noisy matrix

Returning to the same objects makes students feel the accumulation of tools.

### Be explicit about numerical vs exact linear algebra

This is essential for AI/ML preparation. Add repeated warnings and exercises
around:

- floating-point rank
- conditioning
- normal equations squaring the condition number
- tolerance dependence
- exact symbolic vs numerical computation
- stability of algorithms

## Specific Current-Content Moves

These are suggestions for later editing, not actions taken now.

### Move or relabel

- Move `Determinants`, `Tensor Products`, and `Alternating Forms` into
  appendices or advanced complements.
- Move or integrate `Trace` into PSD/spectral/SVD material.
- Treat `Hamming(7,4)` as an optional project after image/kernel.
- Treat `DFT` as an application of diagonalization/convolution, likely after
  spectral material or near image processing.
- Use `baby_intro/` as the short prologue candidate.
- Use `intro/` as an expanded optional case study.
- Use `robot_demo/` as a change-of-basis project.

### Expand

- Add chapter summaries.
- Add "where this is used later" notes.
- Add exercises after every chapter.
- Add end-of-book hints for selected exercises.
- Add cumulative review sections after each part.
- Add a notation table.
- Add a dependency graph showing which chapters are required for which labs.
- Add a glossary of core terms: vector, scalar, subspace, span, basis, rank,
  kernel, image, orthogonal, projection, eigenvector, PSD, SVD.

### Standardize

- Choose either American or British spelling: diagonalization/diagonalisation.
- Standardize `image/kernel` vs `column space/null space` language.
- Standardize course duration references: 10-week, 11-week, or book-first.
- Standardize academic term references: Spring 2025 vs Spring 2026.
- Standardize lab filenames in docs.
- Standardize theorem numbering after chapterization.

## Suggested Exercise Source Format

For LaTeX, define an exercise macro with metadata:

```tex
\begin{exercise}[id=3.A5, track=theory, difficulty=B, tags={proof,subspace}, hint=yes]
...
\end{exercise}
```

or, if LaTeX key-value metadata becomes annoying, keep metadata in comments:

```tex
% id: 3.A5
% track: theory
% difficulty: B
% tags: proof, subspace
% hint: yes
\begin{exercise}
...
\end{exercise}
```

Hints can be stored near the exercise source as comments during drafting, then
rendered into a final end-of-book hints section:

```tex
% hint text:
% Try applying the subspace test directly. The key point is closure under
% arbitrary linear combinations, not just closure under addition.
```

For future automation, a YAML/Markdown exercise bank may be better:

```yaml
id: ch03-017
chapter: 3
display_id: 3.B7
track: by-hand
difficulty: B
tags: [basis, coordinates, compute]
hint: |
  Put the basis vectors into the columns of a matrix and solve Bc = v.
statement: |
  ...
solution: |
  ...
```

Recommended `track` values:

- `theory`
- `by-hand`
- `python`
- `challenge`
- `cumulative`

Recommendation:

- Keep the first version simple in LaTeX.
- Do not over-engineer exercise infrastructure before the exercise bank exists.
- Make the track visible in the rendered book, not just in metadata.
- Make difficulty visible for C/D problems; A/B can be visible or only
  instructor-facing.
- Mark exercises with available hints using a small visible marker, such as
  `Hint available`.
- Keep Python exercise dependencies explicit at the problem level. For example:
  "Use only Python and NumPy" or "You may use Matplotlib for plotting."
- Keep full solutions separate from hints. Hints belong in the student-facing
  book; full solutions belong in an instructor resource or separate solution
  manual.

## Proposed First Three Development Passes

### Pass 1: Editorial architecture

- Decide final chapter list.
- Move advanced material into appendices on paper.
- Split the monolithic notes into chapter files.
- Add chapter openings, summaries, and "AI/ML priming" boxes.
- Add an end-of-book placeholder for hints.
- Fix stale metadata in docs.

### Pass 2: Exercises and assignments

- Add 20-30 exercises per chapter for the first half of the book.
- Enforce the three-track exercise partition: Theory, By Hand, Python/NumPy.
- Check each exercise against the freshman/sophomore accessibility guardrails.
- Label C/D problems clearly so ordinary homework is not accidentally too hard.
- Write first-pass hints for all C/D problems and selected B problems.
- Create HW1-HW6 from the exercise bank.
- Add solutions for selected exercises.
- Add rubrics for computational assignments.

### Pass 3: Labs as assignments

- Split labs into student and solution versions.
- Add deliverables and checkpoint questions.
- Add notebook execution tests.
- Build a public lab index and instructor-facing solution index.

## Priority Recommendations

1. Preserve the core introductory linear algebra spine.
2. Move advanced algebraic material to appendices unless it directly serves the
   data/computation story.
3. Build a serious exercise bank before doing heavy prose polishing.
4. Split labs into student and solution versions before assigning them.
5. Use AI/ML as motivation and application, not as the organizing theorem
   sequence.
6. Make numerical stability a recurring theme.
7. Decide whether the final product is PDF-first LaTeX or web-first Quarto only
   after one prototype chapter.

## What Not To Do

- Do not turn the book into a tour of ML algorithms.
- Do not put neural networks at the center of the first course.
- Do not make every example "AI-branded."
- Do not leave tensor/exterior algebra in the main path unless the target
  audience changes.
- Do not ship solved notebooks as homework without student versions.
- Do not postpone exercises until after prose polish. Exercises will reveal
  where exposition is weak.

## Bottom Line

The current repo has enough material for a strong book, but the book needs a
clearer spine:

1. Linear structure
2. Coordinates and maps
3. Rank and systems
4. Geometry and least squares
5. Spectral structure
6. SVD and data matrices
7. Optional advanced complements

That spine naturally primes students for AI/ML without pretending to be an
AI/ML course. The best next investment is not more advanced topics. It is
chapter architecture, exercises, homework design, and student-ready labs.
