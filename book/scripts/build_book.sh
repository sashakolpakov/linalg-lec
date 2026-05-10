#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
mkdir -p \
  book/build \
  book/build/book/chapters \
  book/build/book/appendices \
  book/build/book/backmatter
latexmk -r book/latexmkrc -pdf -interaction=nonstopmode -outdir=book/build book/main.tex
