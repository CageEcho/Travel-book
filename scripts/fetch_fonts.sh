#!/usr/bin/env bash
# Download the open-source (SIL OFL) fonts the book uses into fonts/.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p fonts
B=https://raw.githubusercontent.com/google/fonts/main/ofl
for p in "longcang/LongCang-Regular.ttf" "notosanssc/NotoSansSC%5Bwght%5D.ttf" "notoserifsc/NotoSerifSC%5Bwght%5D.ttf" \
         "caveat/Caveat%5Bwght%5D.ttf" "pinyonscript/PinyonScript-Regular.ttf" \
         "ibmplexmono/IBMPlexMono-Regular.ttf" "ibmplexmono/IBMPlexMono-Medium.ttf"; do
  n=$(basename "$p" | sed 's/%5B/[/;s/%5D/]/')
  [ -f "fonts/$n" ] || { echo "downloading $n"; curl -sfL -o "fonts/$n" "$B/$p"; }
done
echo "fonts ready"
