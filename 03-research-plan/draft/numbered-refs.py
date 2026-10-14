#!/usr/bin/env python3
"""Convert [Author Year] citations to numbered ones, in order of first appearance,
and renumber the bibliography accordingly. Run by assemble.sh on the assembled file."""
import re, sys
path = sys.argv[1]
txt = open(path, encoding='utf-8').read()
head, bib = txt.split('# Bibliography', 1)
entries = {}
for m in re.finditer(r'^- \*\*\[([^\]]+)\]\*\*\s*(.*?)(?=^- \*\*\[|\Z)', bib, re.S | re.M):
    entries[m.group(1)] = ' '.join(m.group(2).split())
order = []
def repl(m):
    inner = m.group(1)
    keys = [k.strip() for k in inner.split(';')]
    if not all(k in entries for k in keys):
        return m.group(0)
    nums = []
    for k in keys:
        if k not in order:
            order.append(k)
        nums.append(order.index(k) + 1)
    nums = sorted(set(nums))
    # compress runs of 3+ consecutive numbers into ranges
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f'{nums[i]}–{nums[j]}' if j - i >= 2 else ', '.join(str(n) for n in nums[i:j + 1]))
        i = j + 1
    return '[' + ', '.join(out) + ']'
head = re.sub(r'(?<!\!)\[([^\]\[]+)\]', repl, head)
missing = [k for k in entries if k not in order]
lines = ['# Bibliography', '']
for i, k in enumerate(order, 1):
    lines.append(f'{i}. {entries[k]}')
for k in missing:
    order.append(k); lines.append(f'{len(order)}. {entries[k]}')
open(path, 'w', encoding='utf-8').write(head + '\n'.join(lines) + '\n')
print(f'numbered references: {len(order)} entries, {len(missing)} uncited', file=sys.stderr)
