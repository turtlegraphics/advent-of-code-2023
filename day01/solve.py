#
# Advent of Code 2023
# Bryan Clair
#
# Day 01
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

import re

digits = {"one":1,"two":2,"three":3,"four":4,"five":5,
          "six":6,"seven":7,"eight":8,"nine":9}
for i in range(9):
    digits["123456789"[i]] = i+1

digx = '|'.join(digits.keys())

sum1 = 0
sum2 = 0
for line in inputlines:
    nums = re.findall(r'[0-9]',line)
    sum1 += int(nums[0])*10+int(nums[-1])

    # ugh. second try after wrong answer.
    # you can't use findall because the last
    # digit word may be partially chewed by the previous digit word.
    first = re.search(digx, line)[0]
    last  = re.search('.*('+digx+')', line).group(1) # hack to find last one!
    sum2 += digits[first]*10+digits[last]
    
print('part 1:',sum1)
print('part 2:',sum2)

    
