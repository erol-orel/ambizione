#!/bin/sh
# Character count per narrative module against the assumed ~4,350 limit.
DIR="$(dirname "$0")"
printf '%-28s %8s %7s  %s\n' MODULE CHARS WORDS STATUS
for f in "$DIR"/module-*.md; do
    body=$(sed -e '/^> /d' -e 's/\[\[[^]]*\]\]//g' -e 's/^#.*//' -e 's/[*_`]//g' "$f")
    n=$(printf '%s' "$body" | tr -s ' \n' ' ' | wc -c)
    w=$(printf '%s' "$body" | wc -w)
    if [ "$n" -gt 4350 ]; then st="OVER by $((n-4350))"; else st="ok ($((4350-n)) left)"; fi
    printf '%-28s %8d %7d  %s\n' "$(basename "$f")" "$n" "$w" "$st"
done
