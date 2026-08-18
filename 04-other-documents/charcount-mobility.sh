#!/bin/sh
f="$(dirname "$0")/statement-of-mobility-draft.md"
n=$(sed -e '1,/^## Statement of mobility$/d' -e 's/\[\[[^]]*\]\]//g' -e 's/[*_`#|-]//g' "$f" | tr -s ' \n' ' ' | wc -c)
w=$(sed -e '1,/^## Statement of mobility$/d' -e 's/\[\[[^]]*\]\]//g' "$f" | wc -w)
printf 'statement of mobility: %d characters, %d words\n' "$n" "$w"
