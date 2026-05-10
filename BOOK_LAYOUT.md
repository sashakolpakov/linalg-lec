# Book Layout Specification

This file turns `BOOK_PLANNING.md` into a concrete modular book layout. It is
the current layout contract for the `book/` source tree.

Working title:

> Linear Algebra: Mathematics, Computation, and Data

Subtitle:

> An introduction primed for AI, machine learning, and scientific computing.

Core identity:

- first course in linear algebra
- computation-aware from the beginning
- primed for AI/ML through examples and habits
- not a specialized book on the algebra of AI/ML systems

## Design Principles

1. Keep the central theorem spine introductory and honest:
   vector spaces, maps, matrices, rank, least squares, inner products,
   eigenvalues, PSD matrices, spectral theorem, SVD, and low-rank structure.
2. Use AI/ML-facing examples as motivation and application, not as the
   organizing sequence of theorems.
3. Keep advanced algebraic complements as appendices unless they directly
   serve the core computation/data story.
4. Make proof, hand computation, and Python/NumPy work visible and separate.
5. Keep ordinary exercises solvable by prepared freshmen and sophomores.
6. Put hints at the end of the book, keyed by exercise ID.
7. Make every chapter independently editable as a `.tex` file.
8. Keep one common master `.tex` file for full compilation.

## Current Book Source and Target Course Layout

The `book/` entries below describe the current modular source. The later
`assets/`, `labs/`, `assignments/`, and `instructor/` entries describe the
target course-support layout.

```text
.
|-- book/
|   |-- main.tex
|   |-- latexmkrc
|   |-- preamble/
|   |   |-- packages.tex
|   |   |-- theorem-envs.tex
|   |   |-- macros.tex
|   |   |-- listings.tex
|   |   |-- boxes.tex
|   |   `-- metadata.tex
|   |-- frontmatter/
|   |   |-- titlepage.tex
|   |   |-- copyright.tex
|   |   |-- preface.tex
|   |   |-- how-to-use-this-book.tex
|   |   |-- prologue-linear-game-of-life.tex
|   |   |-- notation.tex
|   |   `-- dependency-map.tex
|   |-- chapters/
|   |   |-- ch01-vectors-data-linear-structure.tex
|   |   |-- ch02-vector-spaces-subspaces.tex
|   |   |-- ch03-span-independence-bases-coordinates.tex
|   |   |-- ch04-matrices-linear-maps.tex
|   |   |-- ch05-image-kernel-rank-nullity.tex
|   |   |-- ch06-solving-linear-systems.tex
|   |   |-- ch07-inner-product-geometry.tex
|   |   |-- ch08-projection-least-squares.tex
|   |   |-- ch09-regression-qr-numerical-stability.tex
|   |   |-- ch10-change-basis-similarity.tex
|   |   |-- ch11-eigenvalues-dynamics.tex
|   |   |-- ch12-symmetric-psd-matrices.tex
|   |   |-- ch13-spectral-theorem-rayleigh-quotients.tex
|   |   |-- ch14-svd-pca-low-rank.tex
|   |   |-- ch15-images-convolution-dft.tex
|   |   |-- ch16-denoising-matrix-completion.tex
|   |   `-- ch17-coding-theory-hamming-project.tex
|   |-- exercises/
|   |   |-- prologue-exercises.tex
|   |   |-- ch01-exercises.tex
|   |   |-- ch02-exercises.tex
|   |   |-- ch03-exercises.tex
|   |   |-- ch04-exercises.tex
|   |   |-- ch05-exercises.tex
|   |   |-- ch06-exercises.tex
|   |   |-- ch07-exercises.tex
|   |   |-- ch08-exercises.tex
|   |   |-- ch09-exercises.tex
|   |   |-- ch10-exercises.tex
|   |   |-- ch11-exercises.tex
|   |   |-- ch12-exercises.tex
|   |   |-- ch13-exercises.tex
|   |   |-- ch14-exercises.tex
|   |   |-- ch15-exercises.tex
|   |   |-- ch16-exercises.tex
|   |   `-- ch17-exercises.tex
|   |-- hints/
|   |   |-- prologue-hints.tex
|   |   |-- ch01-hints.tex
|   |   |-- ...
|   |   |-- ch16-hints.tex
|   |   `-- ch17-hints.tex
|   |-- appendices/
|   |   |-- appA-determinants-volume-orientation.tex
|   |   |-- appB-tensor-products-kronecker-products.tex
|   |   |-- appC-alternating-forms-exterior-algebra.tex
|   |   |-- appD-background-proofs.tex
|   |   `-- appE-python-numpy-reference.tex
|   |-- backmatter/
|   |   |-- hints-for-selected-exercises.tex
|   |   |-- glossary.tex
|   |   |-- index-terms.tex
|   |   `-- bibliography.tex
|   `-- parts/
|       |-- partI-vectors-spaces-coordinates.tex
|       |-- partII-maps-rank-systems.tex
|       |-- partIII-geometry-least-squares.tex
|       |-- partIV-spectral-thinking.tex
|       |-- partV-svd-data-low-rank.tex
|       `-- partVI-optional-applications-projects.tex
|-- assets/
|   |-- figures/
|   |   |-- source/
|   |   `-- generated/
|   |-- data/
|   `-- code/
|-- labs/
|   |-- student/
|   |-- solutions/
|   |-- shared/
|   |-- LABS.md
|   `-- labs_all.tex
|-- assignments/
|   |-- hw00-python-numpy-warmup.tex
|   |-- hw01-vector-spaces.tex
|   |-- ...
|   `-- final-projects.tex
|-- instructor/
|   |-- solutions/
|   `-- rubrics/
|-- scripts/
|   |-- build_book.sh
|   |-- build_figures.sh
|   |-- build_labs.sh
|   `-- execute_notebooks.sh
`-- README.md
```

## Compilation Model

Use a LaTeX-first workflow initially. The migration target is a clean PDF book
with a single `book/main.tex` entry point.

Recommended command:

```text
latexmk -pdf -interaction=nonstopmode book/main.tex
```

The master file should use `\include{...}` for chapters and appendices so
individual chapters can be compiled selectively using `\includeonly`.

## Master File: `book/main.tex`

Proposed structure:

```tex
\documentclass[11pt,oneside]{book}

\input{preamble/packages}
\input{preamble/metadata}
\input{preamble/theorem-envs}
\input{preamble/macros}
\input{preamble/listings}
\input{preamble/boxes}

\begin{document}

\frontmatter
\input{frontmatter/titlepage}
\input{frontmatter/copyright}
\input{frontmatter/preface}
\input{frontmatter/how-to-use-this-book}
\input{frontmatter/prologue-linear-game-of-life}
\input{frontmatter/notation}
\input{frontmatter/dependency-map}
\tableofcontents

\mainmatter

\input{parts/partI-vectors-spaces-coordinates}
\include{chapters/ch01-vectors-data-linear-structure}
\include{chapters/ch02-vector-spaces-subspaces}
\include{chapters/ch03-span-independence-bases-coordinates}

\input{parts/partII-maps-rank-systems}
\include{chapters/ch04-matrices-linear-maps}
\include{chapters/ch05-image-kernel-rank-nullity}
\include{chapters/ch06-solving-linear-systems}

\input{parts/partIII-geometry-least-squares}
\include{chapters/ch07-inner-product-geometry}
\include{chapters/ch08-projection-least-squares}
\include{chapters/ch09-regression-qr-numerical-stability}
\include{chapters/ch10-change-basis-similarity}

\input{parts/partIV-spectral-thinking}
\include{chapters/ch11-eigenvalues-dynamics}
\include{chapters/ch12-symmetric-psd-matrices}
\include{chapters/ch13-spectral-theorem-rayleigh-quotients}

\input{parts/partV-svd-data-low-rank}
\include{chapters/ch14-svd-pca-low-rank}

\input{parts/partVI-optional-applications-projects}
\include{chapters/ch15-images-convolution-dft}
\include{chapters/ch16-denoising-matrix-completion}
\include{chapters/ch17-coding-theory-hamming-project}

\appendix
\include{appendices/appA-determinants-volume-orientation}
\include{appendices/appB-tensor-products-kronecker-products}
\include{appendices/appC-alternating-forms-exterior-algebra}
\include{appendices/appD-background-proofs}
\include{appendices/appE-python-numpy-reference}

\backmatter
\include{backmatter/hints-for-selected-exercises}
\include{backmatter/glossary}
\include{backmatter/bibliography}

\end{document}
```

## Preamble Files

### `book/preamble/packages.tex`

Purpose: all package imports and low-level package configuration.

Suggested contents:

```tex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}

\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{listings}
\usepackage{hyperref}
\usepackage[nameinlink,noabbrev]{cleveref}
\usepackage[most]{tcolorbox}
```

Keep this file boring. Do not put custom commands here unless a package
requires immediate configuration.

### `book/preamble/metadata.tex`

Purpose: title, author, term-independent metadata, PDF metadata.

Suggested contents:

```tex
\newcommand{\BookTitle}{Linear Algebra: Mathematics, Computation, and Data}
\newcommand{\BookSubtitle}{An introduction primed for AI, machine learning, and scientific computing}
\newcommand{\BookAuthor}{Sasha Kolpakov}

\hypersetup{
  colorlinks=true,
  linkcolor=blue!55!black,
  citecolor=blue!55!black,
  urlcolor=blue!55!black,
  pdftitle={\BookTitle},
  pdfauthor={\BookAuthor}
}
```

Avoid semester labels such as Spring 2025 or Spring 2026 in source-level book
metadata. Put course-offering dates in course-specific wrappers if needed.

### `book/preamble/theorem-envs.tex`

Purpose: definitions, theorems, exercises, examples.

Suggested contents:

```tex
\theoremstyle{definition}
\newtheorem{definition}{Definition}[chapter]
\newtheorem{example}{Example}[chapter]
\newtheorem{remark}{Remark}[chapter]
\newtheorem{exercise}{Exercise}[chapter]

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{proposition}{Proposition}[chapter]
\newtheorem{lemma}{Lemma}[chapter]
\newtheorem{corollary}{Corollary}[chapter]
```

Exercise metadata can start as comments near each exercise. Do not overbuild
the macro system before the exercise bank exists.

### `book/preamble/macros.tex`

Purpose: mathematical notation and course-wide commands.

Suggested contents:

```tex
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\Z}{\mathbb{Z}}

\newcommand{\im}{\operatorname{im}}
\newcommand{\rank}{\operatorname{rank}}
\newcommand{\nullity}{\operatorname{nullity}}
\newcommand{\Span}{\operatorname{span}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\diag}{\operatorname{diag}}
\newcommand{\proj}{\operatorname{proj}}
\newcommand{\dist}{\operatorname{dist}}

\newcommand{\mat}[1]{\begin{bmatrix}#1\end{bmatrix}}
```

Keep naming consistent. Choose `image/kernel` or `column space/null space`
terminology deliberately and document synonyms in the notation section.

### `book/preamble/listings.tex`

Purpose: Python listing style.

Suggested contents:

```tex
\lstset{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue!70!black},
  commentstyle=\color{gray!70},
  stringstyle=\color{green!40!black},
  showstringspaces=false,
  frame=single,
  breaklines=true,
  columns=fullflexible
}
```

For chapter exercises, keep Python examples limited to basic Python and NumPy
unless a lab explicitly uses more.

### `book/preamble/boxes.tex`

Purpose: recurring pedagogical boxes.

Suggested box types:

- `aimlbox`: accessible AI/ML priming notes
- `computebox`: computational interpretation
- `warningbox`: numerical or conceptual warning
- `labbox`: points to a related lab
- `historybox`: optional historical/context note

Example:

```tex
\newtcolorbox{aimlbox}{
  colback=blue!3,
  colframe=blue!50!black,
  title=Why this matters for data,
  sharp corners
}

\newtcolorbox{warningbox}{
  colback=orange!5,
  colframe=orange!70!black,
  title=Warning,
  sharp corners
}
```

Do not use boxes to introduce material that should be in the main exposition.
Boxes should clarify, motivate, or warn.

## Standard Chapter File Template

Every chapter file should follow the same skeleton:

```tex
% ============================================================
\chapter{Chapter Title}
\label{ch:chapter-label}
% ============================================================

\section*{Chapter Preview}
\addcontentsline{toc}{section}{Chapter Preview}

Short motivation, prerequisites, and the one or two core questions.

\section{Main Section}

Definitions, examples, theorems, proofs, and small computations.

\begin{computebox}
Computational interpretation or algorithmic warning.
\end{computebox}

\section{Python: Core Experiment}

\begin{lstlisting}
import numpy as np
\end{lstlisting}

\section*{Chapter Summary}
\addcontentsline{toc}{section}{Chapter Summary}

Bullets summarizing definitions, theorems, algorithms, and where they are used.

\section*{Where This Appears Later}
\addcontentsline{toc}{section}{Where This Appears Later}

Short forward links to future chapters/labs.

\input{exercises/chXX-exercises}
```

Do not put full lab material into chapters. Chapters should include small
Python experiments; labs should remain larger investigations.

## Exercise File Template

Every `book/exercises/chXX-exercises.tex` file should follow the three-track
layout:

```tex
\section*{Exercises}
\addcontentsline{toc}{section}{Exercises}

\subsection*{A. Theory}

% id: 3.A1
% track: theory
% difficulty: A
% tags: definition, subspace
% hint: no
\begin{exercise}
...
\end{exercise}

\subsection*{B. By Hand}

% id: 3.B1
% track: by-hand
% difficulty: A
% tags: compute, subspace
% hint: yes
% hint text:
% Start by checking whether the zero vector belongs to the set.
\begin{exercise}
...
\end{exercise}

\subsection*{C. Python / NumPy}

% id: 3.C1
% track: python
% difficulty: B
% tags: python, numpy, algorithm
% hint: yes
% dependencies: Python, NumPy
\begin{exercise}
Use only basic Python and NumPy.
...
\end{exercise}

\subsection*{D. Cumulative / Challenge}

% id: 3.D1
% track: challenge
% difficulty: C
% tags: proof, synthesis
% hint: yes
\begin{exercise}
...
\end{exercise}
```

Exercise design constraints:

- ordinary exercises target prepared freshmen and sophomores
- C/D problems must be visibly harder
- most computations should use small structured examples
- Python exercises should be short and use basic Python plus NumPy
- all C/D problems and most B-level problems should have hints

## Hints Layout

Hints are collected at the end of the book rather than placed immediately after
the exercises.

### Per-Chapter Hint Source

Each `book/hints/chXX-hints.tex` file:

```tex
\section*{Chapter 3}

\paragraph{3.A5.}
Use the definition of subspace directly. Check closure under arbitrary linear
combinations, not just addition.

\paragraph{3.B4.}
Put the candidate basis vectors in the columns of a matrix and solve for the
coordinate vector.

\paragraph{3.C2.}
Check the shapes first: if `A` is `m x n` and `x` is length `n`, then `A @ x`
has length `m`.
```

### Backmatter Hints File

`book/backmatter/hints-for-selected-exercises.tex`:

```tex
\chapter{Hints for Selected Exercises}
\label{ch:hints}

\input{hints/prologue-hints}
\input{hints/ch01-hints}
\input{hints/ch02-hints}
% ...
\input{hints/ch16-hints}
\input{hints/ch17-hints}
```

Hints should:

- give a first move, not a full solution
- point to the relevant definition or theorem
- identify a useful representation
- warn about common traps
- for Python, mention shapes or relevant NumPy routines without giving full
  code

## Part and Chapter Layout

### Front Matter

#### `frontmatter/titlepage.tex`

Book title, subtitle, author, institution if desired. No term-specific course
date.

#### `frontmatter/preface.tex`

Must explicitly state:

- this is an introductory linear algebra book
- it is computation-aware
- it is primed for AI/ML, not a specialized AI/ML algebra text
- proofs and computation both matter
- students should expect theory, by-hand work, Python, and labs

#### `frontmatter/how-to-use-this-book.tex`

Explain:

- chapter structure
- three exercise tracks
- how hints work
- what Python background is assumed
- relationship between short Python exercises and labs
- recommended 10-12 week course path

#### `frontmatter/notation.tex`

Define recurring symbols:

- fields: `\F`, `\R`, `\C`
- spaces: `\R^n`, `\F^{m x n}`, polynomial spaces
- maps: `T: V -> W`
- matrices: `A`, `B`, `X`
- image/kernel/rank/nullity
- inner product, norm, orthogonal complement
- eigenvalues/eigenvectors
- SVD notation

#### `frontmatter/dependency-map.tex`

One-page map showing:

- which chapters are required for which labs
- optional appendices
- short vs long course pathways

## Main Chapters

### Front Matter Prologue

#### Prologue: A Linear Game of Life

Files:

```text
book/frontmatter/prologue-linear-game-of-life.tex
book/exercises/prologue-exercises.tex
book/hints/prologue-hints.tex
```

Purpose:

- motivate linear maps, eigenmodes, stability, and Fourier thinking
- avoid requiring students to understand the full machinery yet
- create curiosity, not technical burden

### Part I: Vectors, Spaces, and Coordinates

#### Chapter 1: Vectors, Data, and Linear Structure

Files:

```text
book/chapters/ch01-vectors-data-linear-structure.tex
book/exercises/ch01-exercises.tex
book/hints/ch01-hints.tex
```

Core goals: vectors as structured objects, scalars and fields, data objects as vectors, and Python arrays as representatives.

#### Chapter 2: Vector Spaces and Subspaces

Files:

```text
book/chapters/ch02-vector-spaces-subspaces.tex
book/exercises/ch02-exercises.tex
book/hints/ch02-hints.tex
```

Core goals: vector-space axioms, subspace test, examples and non-examples, and direct sums as optional enrichment.

#### Chapter 3: Span, Independence, Bases, and Coordinates

Files:

```text
book/chapters/ch03-span-independence-bases-coordinates.tex
book/exercises/ch03-exercises.tex
book/hints/ch03-hints.tex
```

Core goals: linear combinations, span, independence, bases, dimension, and basic coordinates.

### Part II: Linear Maps, Matrices, Rank, and Systems

#### Chapter 4: Matrices and Linear Maps

Files:

```text
book/chapters/ch04-matrices-linear-maps.tex
book/exercises/ch04-exercises.tex
book/hints/ch04-hints.tex
```

Core goals: matrices as linear transformations, columns as images of basis vectors, composition as multiplication, and matrix representation of maps.

#### Chapter 5: Image, Kernel, Rank, and Rank-Nullity

Files:

```text
book/chapters/ch05-image-kernel-rank-nullity.tex
book/exercises/ch05-exercises.tex
book/hints/ch05-hints.tex
```

Core goals: image and kernel as subspaces, rank and nullity, rank-nullity, and numerical rank.

#### Chapter 6: Solving Linear Systems

Files:

```text
book/chapters/ch06-solving-linear-systems.tex
book/exercises/ch06-exercises.tex
book/hints/ch06-hints.tex
```

Core goals: existence, uniqueness, solution sets, inverse matrices, and the least-squares preview.

### Part III: Geometry, Least Squares, and Coordinates

#### Chapter 7: Inner Product Geometry

Files:

```text
book/chapters/ch07-inner-product-geometry.tex
book/exercises/ch07-exercises.tex
book/hints/ch07-hints.tex
```

Core goals: inner products, norms, distances, orthogonality, Cauchy-Schwarz, line projections, and cosine similarity.

#### Chapter 8: Orthogonal Projection and Least Squares

Files:

```text
book/chapters/ch08-projection-least-squares.tex
book/exercises/ch08-exercises.tex
book/hints/ch08-hints.tex
```

Core goals: projection onto subspaces, residual orthogonality, normal equations, and four-subspace intuition.

#### Chapter 9: Regression, QR, and Numerical Stability

Files:

```text
book/chapters/ch09-regression-qr-numerical-stability.tex
book/exercises/ch09-exercises.tex
book/hints/ch09-hints.tex
```

Core goals: design matrices, polynomial features, QR-based least squares, conditioning warnings, validation, underfitting, and overfitting.

#### Chapter 10: Change of Basis and Similarity

Files:

```text
book/chapters/ch10-change-basis-similarity.tex
book/exercises/ch10-exercises.tex
book/hints/ch10-hints.tex
```

Core goals: change-of-basis matrices, similar matrices, diagonalization as a coordinate choice, interpretability, conditioning, and the robot-arm demo.

### Part IV: Spectral Thinking

#### Chapter 11: Eigenvalues, Eigenvectors, and Dynamics

Files:

```text
book/chapters/ch11-eigenvalues-dynamics.tex
book/exercises/ch11-exercises.tex
book/hints/ch11-hints.tex
```

Core goals: preserved directions, eigenvalues as scaling factors, powers of matrices, and qualitative dynamics.

#### Chapter 12: Symmetric and PSD Matrices

Files:

```text
book/chapters/ch12-symmetric-psd-matrices.tex
book/exercises/ch12-exercises.tex
book/hints/ch12-hints.tex
```

Core goals: quadratic forms, PSD matrices, Gram matrices, covariance matrices, and trace as total variance.

#### Chapter 13: The Spectral Theorem and Rayleigh Quotients

Files:

```text
book/chapters/ch13-spectral-theorem-rayleigh-quotients.tex
book/exercises/ch13-exercises.tex
book/hints/ch13-hints.tex
```

Core goals: orthonormal eigenbases for symmetric matrices, spectral decomposition, Rayleigh quotients, and eigenvalue optimization.

### Part V: SVD, Data Matrices, and Low-Rank Structure

#### Chapter 14: The SVD, PCA, and Low-Rank Approximation

Files:

```text
book/chapters/ch14-svd-pca-low-rank.tex
book/exercises/ch14-exercises.tex
book/hints/ch14-hints.tex
```

Core goals: SVD for rectangular matrices, singular values and vectors, geometry, Eckart-Young, PCA, variance explained, and compression.

### Part VI: Optional Applications and Projects

#### Chapter 15: Images, Convolution, and the DFT

Files:

```text
book/chapters/ch15-images-convolution-dft.tex
book/exercises/ch15-exercises.tex
book/hints/ch15-hints.tex
```

Purpose: optional signal/image module using convolution, circulant matrices, and the DFT as a change of basis.

#### Chapter 16: Denoising and Matrix Completion

Files:

```text
book/chapters/ch16-denoising-matrix-completion.tex
book/exercises/ch16-exercises.tex
book/hints/ch16-hints.tex
```

Purpose: optional low-rank application module covering singular-value threshold intuition, denoising by truncation, and matrix completion.

#### Chapter 17: Coding Theory and the Hamming Code

Files:

```text
book/chapters/ch17-coding-theory-hamming-project.tex
book/exercises/ch17-exercises.tex
book/hints/ch17-hints.tex
```

Purpose: optional project using subspaces, parity-check matrices, null spaces, and syndromes without requiring abstract algebra.

## Appendices

### Appendix A: Determinants, Volume, and Orientation

File:

```text
book/appendices/appA-determinants-volume-orientation.tex
```

Source material:

- Determinants (Geometric Approach)

Purpose:

- keep determinants available without making them central
- connect volume, orientation, invertibility, and SVD product formula

### Appendix B: Tensor Products and Kronecker Products

File:

```text
book/appendices/appB-tensor-products-kronecker-products.tex
```

Source material:

- Tensor Products

Purpose:

- optional enrichment
- Kronecker products for separable structure, image filters, and data arrays

### Appendix C: Alternating Forms and Exterior Algebra

File:

```text
book/appendices/appC-alternating-forms-exterior-algebra.tex
```

Source material:

- Alternating Forms and the Exterior Algebra

Purpose:

- mathematically valuable advanced complement
- not part of the main freshman/sophomore route

### Appendix D: Background Proofs

File:

```text
book/appendices/appD-background-proofs.tex
```

Possible contents:

- Steinitz exchange lemma
- dimension well-definedness
- compactness notes for spectral theorem
- optional proof details that would interrupt the main flow

### Appendix E: Python and NumPy Reference

File:

```text
book/appendices/appE-python-numpy-reference.tex
```

Possible contents:

- array creation
- shapes
- matrix-vector and matrix-matrix products
- slicing
- `np.linalg.solve`
- `np.linalg.lstsq`
- `np.linalg.qr`
- `np.linalg.eig`
- `np.linalg.eigh`
- `np.linalg.svd`
- random number generator basics

## Migration Map from Current Files

```text
linear_algebra_notes.tex
|-- Course Philosophy                         -> ch01, preface
|-- Vector Spaces                             -> ch01, ch02
|-- Subspaces                                 -> ch02
|-- Span and Linear Independence              -> ch03
|-- Bases and Dimension                       -> ch03, ch10
|-- Matrices                                  -> ch04
|-- Linear Maps                               -> ch04
|-- Column Space, Null Space, Rank-Nullity    -> ch05
|-- Hamming(7,4)                              -> ch17 optional project
|-- Polynomial Regression                     -> ch09
|-- Inner Products and Norms                  -> ch07
|-- Im-Ker Theorem Full Proof                 -> ch05, ch08, appD
|-- Structural Properties                     -> ch10, ch11
|-- Eigenvalues and Diagonalization           -> ch10, ch11, ch13
|-- Discrete Fourier Transform                -> ch15
|-- Positive Semidefinite Matrices            -> ch12, ch13
|-- Trace                                     -> ch12, ch14
|-- Singular Value Decomposition              -> ch14
|-- Determinants                              -> appA
|-- Tensor Products                           -> appB
|-- Alternating Forms                         -> appC

intro/intro.tex and intro/intro.ipynb          -> prologue, ch15 optional case study
baby_intro/baby_intro.tex and .ipynb           -> prologue
robot_demo/demo_robot_arm_basis.ipynb          -> ch10 demo/project
labs/*.ipynb                                  -> labs/student and labs/solutions
figures/*.py and figures/*.png                 -> assets/figures/source and generated
```

## Labs Integration

The book should reference labs using a standard box near the end of relevant
chapters:

```tex
\begin{labbox}
Related lab: Lab 6, Inner Products, Norms, and Gram-Schmidt. In the lab you
will implement classical Gram-Schmidt, compare it with NumPy's QR routine, and
test stability on nearly dependent vectors.
\end{labbox}
```

Suggested lab mapping:

```text
Lab 01 -> ch01, ch02, ch03
Lab 02 -> ch04, ch10
Lab 03 -> ch05
Lab 04 -> ch06
Lab 05 -> ch09
Lab 06 -> ch07, ch08, ch09
Lab 07 -> ch08
Lab 08 -> ch10, ch11
Lab 09 -> ch11, ch13
Lab 10 -> ch14
Lab 11 -> ch15
Lab 12 -> ch16
```

## Assignment Layout

Assignments should live outside the book source but use the same exercise IDs.

```text
assignments/
|-- hw00-python-numpy-warmup.tex
|-- hw01-vector-spaces.tex
|-- hw02-span-bases-coordinates.tex
|-- hw03-matrices-linear-maps.tex
|-- hw04-rank-nullity-systems.tex
|-- hw05-least-squares-regression.tex
|-- hw06-inner-products-qr.tex
|-- hw07-four-subspaces.tex
|-- hw08-eigenvalues-diagonalization.tex
|-- hw09-psd-spectral-rayleigh.tex
|-- hw10-svd-pca.tex
|-- hw11-images-dft-denoising.tex
`-- final-projects.tex
```

Each homework:

```text
Part A. Theory
Part B. By Hand
Part C. Python / NumPy
Part D. Challenge / Extension
```

Use mostly A/B problems, with at most one C/D problem unless it is optional.

## Build Scripts

### `scripts/build_book.sh`

Purpose:

- regenerate figures if needed
- compile `book/main.tex`
- place PDF in a predictable output directory

Sketch:

```sh
#!/usr/bin/env bash
set -e
bash scripts/build_figures.sh
latexmk -pdf -interaction=nonstopmode book/main.tex
```

### `scripts/build_figures.sh`

Purpose:

- run figure scripts
- keep generated PNGs under `assets/figures/generated`

### `scripts/execute_notebooks.sh`

Purpose:

- execute student/solution notebooks in CI
- catch broken imports and stale assumptions

Do not make notebook execution a blocker for ordinary TeX compilation until
the lab split is stable.

## CI Layout

Future CI should have separate jobs:

1. build book PDF
2. build lab manual PDF
3. execute notebooks
4. check links and Colab paths
5. upload artifacts

Initial minimal CI:

```text
install TeX
install Python dependencies
generate figures
latexmk book/main.tex
upload book PDF
```

## Naming Conventions

Use lowercase file names with hyphens:

```text
ch09-regression-qr-numerical-stability.tex
appA-determinants-volume-orientation.tex
```

Use stable labels:

```tex
\label{ch:least-squares}
\label{sec:normal-equations}
\label{thm:rank-nullity}
\label{ex:9.B4}
```

Use exercise IDs:

```text
9.A1  theory
9.B1  by hand
9.C1  Python/NumPy
9.D1  challenge/cumulative
```

## Content Style Per Chapter

Recommended rhythm:

1. motivating question
2. definition/theorem
3. geometric interpretation
4. small by-hand example
5. Python/NumPy experiment
6. warning or AI/ML-facing box where appropriate
7. summary
8. exercises

Keep "why this matters for AI/ML" boxes:

- short
- self-contained
- accessible without prior ML
- subordinate to the linear algebra

Do not include:

- unintroduced ML jargon
- neural network architecture details
- long application detours
- exercises that require advanced probability/optimization

## Implementation Order

### Pass 0: Create the empty structure

- create `book/main.tex`
- create preamble files
- create empty chapter files with chapter titles
- create empty exercise files
- create empty hint files
- compile a skeleton PDF

### Pass 1: Mechanical split

- split `linear_algebra_notes.tex` into chapter files
- do not rewrite heavily yet
- preserve existing figures and code listings
- make labels compile

### Pass 2: Chapter shaping

- add chapter previews
- add chapter summaries
- add "where this appears later"
- move advanced material into appendices
- standardize terminology

### Pass 3: Exercise bank

- add three-track exercises chapter by chapter
- enforce accessibility guardrails
- add hints for selected exercises
- keep Python exercises basic NumPy

### Pass 4: Labs

- split solved notebooks into student and solution versions
- add deliverables and rubrics
- wire labs into chapters using `labbox`

### Pass 5: Course packaging

- build assignments from exercise IDs
- create a 10-week and 12-week route
- update README and CI

## Minimal Skeleton to Compile First

The first compilable skeleton should include:

```text
book/main.tex
book/preamble/packages.tex
book/preamble/metadata.tex
book/preamble/theorem-envs.tex
book/preamble/macros.tex
book/frontmatter/titlepage.tex
book/frontmatter/preface.tex
book/chapters/ch01-vectors-data-linear-structure.tex
book/exercises/ch01-exercises.tex
book/hints/ch01-hints.tex
book/backmatter/hints-for-selected-exercises.tex
```

Start with chapter 2 rather than chapter 1 if the prologue is still unsettled.
This gives a clean prototype for:

- theorem numbering
- code listings
- exercise sections
- hints
- cross-references
- figure paths

Once chapter 2 compiles cleanly, clone the pattern across the rest of the book.

## Open Decisions

1. Final title.
2. Whether the prologue is chapter 1 or frontmatter.
3. Whether `Hamming(7,4)` is a chapter section, project, or appendix item.
4. Whether DFT is core chapter 18 or optional module.
5. How many full solutions are public.
6. Whether to keep LaTeX-only or later prototype Quarto.
7. Whether exercises live only in `.tex` or eventually in YAML/Markdown.

Default recommendation:

- make the prologue chapter 1 for the book version
- keep Hamming as optional project
- keep DFT as chapter 18 but marked optional for short courses
- keep full solutions private/instructor-facing
- keep LaTeX first, then prototype Quarto after the chapter structure settles
