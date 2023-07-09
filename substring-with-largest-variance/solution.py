class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = list(set(s))
		
		# Loop through each pari of (c1, c2)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
                        max_diff = max(last_c1_diff, max_diff)
						
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res