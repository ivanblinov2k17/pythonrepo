import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    all_subs = re.sub(r'((\w)\2+)', r'\2', line)
    print(all_subs)
