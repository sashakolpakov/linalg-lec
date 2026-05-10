# Book Layout Specification

This file turns `BOOK_PLANNING.md` into a concrete modular book layout. It is a
layout plan only. It does not rewrite the existing notes, move files, or create
the proposed `book/` source tree.

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

## Proposed Top-Level Repository Layout

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
|   |   |-- notation.tex
|   |   `-- dependency-map.tex
|   |-- chapters/
|   |   |-- ch01-prologue-linear-game-of-life.tex
|   |   |-- ch02-vectors-data-linear-structure.tex
|   |   |-- ch03-vector-spaces-subspaces.tex
|   |   |-- ch04-span-independence-bases-dimension.tex
|   |   |-- ch05-matrices-linear-maps.tex
|   |   |-- ch06-coordinates-change-of-basis.tex
|   |   |-- ch07-image-kernel-rank-nullity.tex
|   |   |-- ch08-solving-linear-systems.tex
|   |   |-- ch09-least-squares-polynomial-regression.tex
|   |   |-- ch10-inner-product-geometry.tex
|   |   |-- ch11-projection-qr-four-subspaces.tex
|   |   |-- ch12-eigenvalues-dynamics.tex
|   |   |-- ch13-diagonalization-spectral-decomposition.tex
|   |   |-- ch14-psd-quadratic-forms.tex
|   |   |-- ch15-spectral-theorem-rayleigh-quotients.tex
|   |   |-- ch16-singular-value-decomposition.tex
|   |   |-- ch17-low-rank-pca-data-compression.tex
|   |   |-- ch18-images-convolution-dft.tex
|   |   `-- ch19-denoising-matrix-completion-low-rank-methods.tex
|   |-- exercises/
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
|   |   |-- ch17-exercises.tex
|   |   |-- ch18-exercises.tex
|   |   `-- ch19-exercises.tex
|   |-- hints/
|   |   |-- ch01-hints.tex
|   |   |-- ch02-hints.tex
|   |   |-- ...
|   |   `-- ch19-hints.tex
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
|       `-- partV-svd-data-low-rank.tex
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
\input{frontmatter/notation}
\input{frontmatter/dependency-map}
\tableofcontents

\mainmatter

\input{parts/partI-vectors-spaces-coordinates}
\include{chapters/ch01-prologue-linear-game-of-life}
\include{chapters/ch02-vectors-data-linear-structure}
\include{chapters/ch03-vector-spaces-subspaces}
\include{chapters/ch04-span-independence-bases-dimension}

\input{parts/partII-maps-rank-systems}
\include{chapters/ch05-matrices-linear-maps}
\include{chapters/ch06-coordinates-change-of-basis}
\include{chapters/ch07-image-kernel-rank-nullity}
\include{chapters/ch08-solving-linear-systems}

\input{parts/partIII-geometry-least-squares}
\include{chapters/ch09-least-squares-polynomial-regression}
\include{chapters/ch10-inner-product-geometry}
\include{chapters/ch11-projection-qr-four-subspaces}

\input{parts/partIV-spectral-thinking}
\include{chapters/ch12-eigenvalues-dynamics}
\include{chapters/ch13-diagonalization-spectral-decomposition}
\include{chapters/ch14-psd-quadratic-forms}
\include{chapters/ch15-spectral-theorem-rayleigh-quotients}

\input{parts/partV-svd-data-low-rank}
\include{chapters/ch16-singular-value-decomposition}
\include{chapters/ch17-low-rank-pca-data-compression}
\include{chapters/ch18-images-convolution-dft}
\include{chapters/ch19-denoising-matrix-completion-low-rank-methods}

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

\input{hints/ch01-hints}
\input{hints/ch02-hints}
\input{hints/ch03-hints}
% ...
\input{hints/ch19-hints}
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

### Part I: Vectors, Spaces, and Coordinates

#### Chapter 1: Prologue: A Linear Game of Life

File:

```text
book/chapters/ch01-prologue-linear-game-of-life.tex
book/exercises/ch01-exercises.tex
book/hints/ch01-hints.tex
```

Source material:

- `baby_intro/`
- selected material from `intro/`

Purpose:

- motivate linear maps, eigenmodes, stability, and Fourier thinking
- avoid requiring students to understand the full machinery yet
- create curiosity, not technical burden

Sections:

1. A discrete world of states
2. A linear transfer rule
3. What patterns persist?
4. A preview of eigenvectors
5. What the course will explain

Exercises:

- mostly conceptual and exploratory
- very light computation
- no advanced Fourier assumptions

#### Chapter 2: Vectors, Data, and Linear Structure

Files:

```text
book/chapters/ch02-vectors-data-linear-structure.tex
book/exercises/ch02-exercises.tex
book/hints/ch02-hints.tex
```

Source material:

- Course Philosophy
- early Vector Spaces material
- examples of signals, images, polynomials

Core goals:

- vector as an element of a structured space
- scalars and fields
- data objects as vectors
- productive language philosophy

Sections:

1. Math as a productive language
2. Scalars and fields
3. Vectors as structured objects
4. Examples: coordinates, polynomials, signals, images
5. Python: arrays as vector representatives

Related labs:

- Lab 1

#### Chapter 3: Vector Spaces and Subspaces

Files:

```text
book/chapters/ch03-vector-spaces-subspaces.tex
book/exercises/ch03-exercises.tex
book/hints/ch03-hints.tex
```

Source material:

- vector space definition
- subspace definition and subspace test
- examples/non-examples
- direct sums, lightly

Core goals:

- vector-space axioms
- subspace test
- examples and non-examples
- direct sums as optional enrichment

Sections:

1. Vector-space axioms
2. Formal consequences of the axioms
3. Subspaces
4. The subspace test
5. Sums and direct sums
6. Python: stochastic axiom checks and subspace tests

Related labs:

- Lab 1

#### Chapter 4: Span, Independence, Bases, and Dimension

Files:

```text
book/chapters/ch04-span-independence-bases-dimension.tex
book/exercises/ch04-exercises.tex
book/hints/ch04-hints.tex
```

Source material:

- Span and Linear Independence
- Bases and Dimension
- coordinates in a basis

Core goals:

- linear combinations and span
- linear independence
- bases as minimal spanning/maximal independent lists
- dimension and coordinates

Sections:

1. Linear combinations and span
2. Linear dependence and redundancy
3. Bases
4. Coordinates
5. Dimension
6. Python: rank as span/independence test

Related labs:

- Lab 1
- Lab 2, lightly

### Part II: Linear Maps, Matrices, Rank, and Systems

#### Chapter 5: Matrices and Linear Maps

Files:

```text
book/chapters/ch05-matrices-linear-maps.tex
book/exercises/ch05-exercises.tex
book/hints/ch05-hints.tex
```

Source material:

- Matrices
- Linear Maps
- matrix-vector product
- matrix-matrix multiplication
- differentiation/integration examples

Core goals:

- matrices as linear transformations
- columns as images of basis vectors
- composition as multiplication
- maps between abstract spaces and coordinate spaces

Sections:

1. Matrices as arrays and maps
2. Matrix-vector multiplication
3. Matrix-matrix multiplication
4. Linear maps
5. Matrix representation of a linear map
6. Composition equals multiplication
7. Python: constructing matrices from maps

Related labs:

- Lab 2

#### Chapter 6: Coordinates and Change of Basis

Files:

```text
book/chapters/ch06-coordinates-change-of-basis.tex
book/exercises/ch06-exercises.tex
book/hints/ch06-hints.tex
```

Source material:

- coordinates in a basis
- Structural Properties: Change of Basis
- robot demo

Core goals:

- coordinates as descriptions, not objects
- change-of-basis matrices
- `A' = P^{-1} A P`
- basis choice as interpretability and conditioning

Sections:

1. Coordinates revisited
2. Change-of-basis matrices
3. Same vector, different coordinates
4. Same map, different matrix
5. Similar matrices
6. Demo: robot-arm trajectory basis
7. Python: coordinate conversion

Related labs:

- Lab 8
- Robot demo

#### Chapter 7: Image, Kernel, and Rank-Nullity

Files:

```text
book/chapters/ch07-image-kernel-rank-nullity.tex
book/exercises/ch07-exercises.tex
book/hints/ch07-hints.tex
```

Source material:

- Column Space, Null Space, and Rank-Nullity
- image/kernel algorithms
- rank and dimension

Core goals:

- image and kernel as subspaces
- rank and nullity
- rank-nullity theorem
- column operations and basis extraction

Sections:

1. Image and kernel
2. Kernel as relations among columns
3. Column operations and image bases
4. Rank and nullity
5. Rank-nullity
6. Numerical rank and tolerance
7. Python: image/kernel with NumPy/SciPy comparison

Related labs:

- Lab 3

#### Chapter 8: Solving Linear Systems

Files:

```text
book/chapters/ch08-solving-linear-systems.tex
book/exercises/ch08-exercises.tex
book/hints/ch08-hints.tex
```

Source material:

- solving `Ax=b`
- three/four cases
- matrix inverse
- least-norm solution as forward pointer
- Hamming code as optional project

Core goals:

- solvability as `b in im(A)`
- uniqueness as `ker(A) = {0}`
- solution sets as `x0 + ker(A)`
- inverse matrices
- underdetermined/overdetermined intuition

Sections:

1. The equation `Ax=b`
2. Existence
3. Uniqueness
4. Solution sets
5. Invertibility
6. Least-norm solution as a preview
7. Optional project: Hamming(7,4)
8. Python: classifying systems

Related labs:

- Lab 4
- optional Hamming project

### Part III: Geometry, Orthogonality, and Least Squares

#### Chapter 9: Least Squares and Polynomial Regression

Files:

```text
book/chapters/ch09-least-squares-polynomial-regression.tex
book/exercises/ch09-exercises.tex
book/hints/ch09-hints.tex
```

Source material:

- Polynomial Regression
- normal equations
- bridge to inner products

Core goals:

- inconsistent systems
- design matrices
- polynomial features
- least squares as approximation
- normal equations as a first derivation
- validation and overfitting, lightly

Sections:

1. Exact fitting and why it fails
2. Polynomial regression setup
3. Vandermonde matrices
4. Least-squares objective
5. Normal equations
6. Train/validation split
7. Conditioning warning
8. Python: fitting and validation

Related labs:

- Lab 5

#### Chapter 10: Inner Product Geometry

Files:

```text
book/chapters/ch10-inner-product-geometry.tex
book/exercises/ch10-exercises.tex
book/hints/ch10-hints.tex
```

Source material:

- Inner Products and Norms
- Cauchy-Schwarz
- triangle inequality
- projections

Core goals:

- inner products
- norms and distances
- orthogonality
- Cauchy-Schwarz
- projections onto lines
- cosine similarity as accessible data example

Sections:

1. Inner products
2. Norms and distances
3. Orthogonality
4. Projection onto a line
5. Cauchy-Schwarz
6. Triangle inequality
7. Cosine similarity
8. Python: projections and inner products

Related labs:

- Lab 6

#### Chapter 11: Orthogonal Projection, QR, and the Four Subspaces

Files:

```text
book/chapters/ch11-projection-qr-four-subspaces.tex
book/exercises/ch11-exercises.tex
book/hints/ch11-hints.tex
```

Source material:

- normal equations derivation
- Gram-Schmidt
- row rank equals column rank
- four fundamental subspaces

Core goals:

- projection onto a subspace
- least squares as projection
- Gram-Schmidt and QR
- stability of QR vs normal equations
- four fundamental subspaces

Sections:

1. Orthogonal complements
2. Projection onto a subspace
3. Least squares revisited
4. Gram-Schmidt
5. QR decomposition
6. Four fundamental subspaces
7. Numerical stability
8. Python: Gram-Schmidt vs `np.linalg.qr`

Related labs:

- Lab 6
- Lab 7

### Part IV: Spectral Thinking

#### Chapter 12: Eigenvalues, Eigenvectors, and Dynamics

Files:

```text
book/chapters/ch12-eigenvalues-dynamics.tex
book/exercises/ch12-exercises.tex
book/hints/ch12-hints.tex
```

Source material:

- Eigenvalues and Diagonalization, first half
- linear dynamics examples
- selective Game of Life callback

Core goals:

- eigenvectors as stable directions
- eigenvalues as scaling factors
- powers of matrices
- qualitative dynamics

Sections:

1. Eigenvectors and eigenvalues
2. Geometric interpretation
3. Eigenvalues and invertibility
4. Powers and dynamics
5. Distinct eigenvalues and independence
6. Python: trajectories under repeated multiplication

Related labs:

- Lab 9, first half

#### Chapter 13: Diagonalization and Spectral Decomposition

Files:

```text
book/chapters/ch13-diagonalization-spectral-decomposition.tex
book/exercises/ch13-exercises.tex
book/hints/ch13-hints.tex
```

Source material:

- diagonalizable matrices
- partial diagonalization
- similar matrices
- block structure

Core goals:

- diagonalization as a change of basis
- `A = P Lambda P^{-1}`
- when diagonalization succeeds or fails
- partial diagonalization

Sections:

1. Eigenbases
2. Diagonalization
3. Similarity
4. Repeated eigenvalues and failure modes
5. Partial diagonalization
6. Python: diagonalization and matrix powers

Related labs:

- Lab 8
- Lab 9

#### Chapter 14: PSD Matrices and Quadratic Forms

Files:

```text
book/chapters/ch14-psd-quadratic-forms.tex
book/exercises/ch14-exercises.tex
book/hints/ch14-hints.tex
```

Source material:

- Positive Semidefinite Matrices
- trace material, partly
- covariance/Gram matrix examples

Core goals:

- PSD via quadratic forms and `B^T B`
- Gram matrices
- covariance matrices
- quadratic forms as bowls
- trace as sum of diagonal/eigenvalues where appropriate

Sections:

1. Quadratic forms
2. PSD matrices
3. Factorizations `B^T B`
4. Gram matrices
5. Covariance matrices
6. Trace and total variance
7. Python: checking PSD numerically

Related labs:

- Lab 9
- Lab 10, lightly

#### Chapter 15: The Spectral Theorem and Rayleigh Quotients

Files:

```text
book/chapters/ch15-spectral-theorem-rayleigh-quotients.tex
book/exercises/ch15-exercises.tex
book/hints/ch15-hints.tex
```

Source material:

- spectral theorem proof
- invariant subspaces
- Rayleigh quotients

Core goals:

- symmetric matrices have orthonormal eigenbases
- spectral decomposition
- Rayleigh quotient
- optimization interpretation
- stability and numerical eigenvalue computation

Sections:

1. Symmetry and orthogonality
2. Invariant subspaces
3. Spectral theorem
4. PSD spectral theorem
5. Rayleigh quotient
6. Computing extreme eigenvalues
7. Python: Rayleigh quotient experiments

Related labs:

- Lab 9

### Part V: SVD, Data Matrices, and Low-Rank Structure

#### Chapter 16: Singular Value Decomposition

Files:

```text
book/chapters/ch16-singular-value-decomposition.tex
book/exercises/ch16-exercises.tex
book/hints/ch16-hints.tex
```

Source material:

- Singular Value Decomposition
- four fundamental subspaces via SVD
- SVD geometry

Core goals:

- SVD for rectangular matrices
- singular values and singular vectors
- geometry of unit sphere to ellipsoid
- subspaces from SVD

Sections:

1. Why eigenvalues are not enough
2. `A^T A` and right singular vectors
3. Left singular vectors
4. Assembling the SVD
5. Geometry
6. Four subspaces via SVD
7. Python: reconstructing a matrix from SVD

Related labs:

- Lab 10

#### Chapter 17: Low-Rank Approximation, PCA, and Data Compression

Files:

```text
book/chapters/ch17-low-rank-pca-data-compression.tex
book/exercises/ch17-exercises.tex
book/hints/ch17-hints.tex
```

Source material:

- Eckart-Young
- image compression
- PCA
- LoRA as optional box

Core goals:

- low-rank approximation
- Eckart-Young
- Frobenius error formula
- PCA
- variance explained
- compression

Sections:

1. Outer-product expansion
2. Rank-`k` approximation
3. Eckart-Young
4. Image compression
5. PCA
6. Optional box: low-rank adapters
7. Python: PCA and rank-`k` reconstruction

Related labs:

- Lab 10
- Lab 12, lightly

#### Chapter 18: Images, Convolution, and the DFT

Files:

```text
book/chapters/ch18-images-convolution-dft.tex
book/exercises/ch18-exercises.tex
book/hints/ch18-hints.tex
```

Source material:

- The Discrete Fourier Transform
- image processing lab
- intro Fourier material, selectively

Core goals:

- images as matrices/vectors
- convolution as a linear map
- circulant matrices
- Fourier basis
- DFT diagonalizes convolution
- filters and frequency response

Sections:

1. Images as arrays and vectors
2. Linear filters
3. Convolution matrices
4. Circulant matrices
5. DFT as diagonalization
6. The convolution theorem
7. Python: tiny filters and FFT comparison

Related labs:

- Lab 11

#### Chapter 19: Denoising, Matrix Completion, and Modern Low-Rank Methods

Files:

```text
book/chapters/ch19-denoising-matrix-completion-low-rank-methods.tex
book/exercises/ch19-exercises.tex
book/hints/ch19-hints.tex
```

Source material:

- SVD denoising lab
- low-rank applications from SVD notes
- optional collaborative filtering
- optional LoRA continuation

Core goals:

- signal plus noise model
- singular-value threshold intuition
- denoising by truncation
- matrix completion as optional project
- modern low-rank ideas without ML architecture burden

Sections:

1. Low-rank signal plus noise
2. Singular value spectra
3. Choosing a rank
4. Denoising by truncation
5. Matrix completion as a low-rank problem
6. Optional modern low-rank methods
7. Python: denoising toy matrices

Related labs:

- Lab 12

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
|-- Course Philosophy                         -> ch02, preface
|-- Vector Spaces                             -> ch02, ch03
|-- Subspaces                                 -> ch03
|-- Span and Linear Independence              -> ch04
|-- Bases and Dimension                       -> ch04, ch06
|-- Matrices                                  -> ch05
|-- Linear Maps                               -> ch05
|-- Column Space, Null Space, Rank-Nullity    -> ch07
|-- Hamming(7,4)                              -> ch08 optional project
|-- Polynomial Regression                     -> ch09
|-- Inner Products and Norms                  -> ch10
|-- Im-Ker Theorem Full Proof                 -> ch07, ch11, appD
|-- Structural Properties                     -> ch06, ch13
|-- Eigenvalues and Diagonalization           -> ch12, ch13
|-- Discrete Fourier Transform                -> ch18
|-- Positive Semidefinite Matrices            -> ch14, ch15
|-- Trace                                     -> ch14, ch17
|-- Singular Value Decomposition              -> ch16, ch17
|-- Determinants                              -> appA
|-- Tensor Products                           -> appB
|-- Alternating Forms                         -> appC

intro/intro.tex and intro/intro.ipynb          -> ch01, ch18 optional case study
baby_intro/baby_intro.tex and .ipynb           -> ch01 short prologue
robot_demo/demo_robot_arm_basis.ipynb          -> ch06 demo/project
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
Lab 01 -> ch02, ch03, ch04
Lab 02 -> ch05, ch06
Lab 03 -> ch07
Lab 04 -> ch08
Lab 05 -> ch09
Lab 06 -> ch10, ch11
Lab 07 -> ch11
Lab 08 -> ch06, ch13
Lab 09 -> ch12, ch15
Lab 10 -> ch16, ch17
Lab 11 -> ch18
Lab 12 -> ch19
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
ch09-least-squares-polynomial-regression.tex
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
book/chapters/ch02-vectors-data-linear-structure.tex
book/exercises/ch02-exercises.tex
book/hints/ch02-hints.tex
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
