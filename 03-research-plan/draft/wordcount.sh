#!/bin/sh
# Character budget check against the 60,000-character limit CONFIRMED by Guidelines 4.3
# (includes title, summary, footnotes, figures, tables; excludes bibliography).
# The mySNF counter is BINDING — verify there before submission; this is an estimate.
# Strips markdown syntax and [[…]] / [VERIFY] annotations for a closer estimate.
DIR="$(dirname "$0")"
total=0
printf '%-32s %8s %8s\n' FILE CHARS WORDS
for f in "$DIR"/0*.md; do
    n=$(sed -e 's/\[\[[^]]*\]\]//g' -e 's/`\[VERIFY\]`//g' -e 's/[#*`|_>-]//g' "$f" | tr -s ' ' | wc -c)
    w=$(sed -e 's/\[\[[^]]*\]\]//g' "$f" | wc -w)
    printf '%-32s %8d %8d\n' "$(basename "$f")" "$n" "$w"
    total=$((total + n))
done
printf '%-32s %8d\n' TOTAL "$total"
printf '\nLimit 60000 (confirmed; mySNF counter binding). Remaining: %d\n' $((60000 - total))
