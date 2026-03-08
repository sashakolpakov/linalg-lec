#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"

for script in \
    fig01_vectors.py \
    fig02_subspace.py \
    fig03_span.py \
    fig04_projection.py \
    fig05_poly_regression.py \
    fig06_gram_schmidt.py \
    fig07_eigenvalues.py \
    fig08_psd_quadratic.py \
    fig09_svd_geometry.py \
    fig10_eckart_young.py \
    fig11_pca.py \
    fig12_determinant.py
do
    printf "  %s ... " "$script"
    python "$DIR/$script"
done

echo "all figures done."
