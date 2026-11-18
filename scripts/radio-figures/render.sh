#!/bin/sh
# Rasterizes figures to PNG (macOS QuickLook) for visual checks:
#   scripts/radio-figures/render.sh <outdir> <svg>...   ->  <outdir>/<name>.svg.png
out="$1"; shift; mkdir -p "$out"
qlmanage -t -s 640 -o "$out" "$@" >/dev/null 2>&1
