#!/usr/bin/env bash
# Regenerate all intro figures as PNG.
set -e
cd "$(dirname "$0")"
for f in fig_glider.py fig_blip.py fig_blip_growth.py fig_stripes.py \
          fig_amplification_map.py fig_diagonal_compare.py fig_perturbation.py; do
    echo "Running $f ..."
    python "$f"
done
echo "All figures done."
