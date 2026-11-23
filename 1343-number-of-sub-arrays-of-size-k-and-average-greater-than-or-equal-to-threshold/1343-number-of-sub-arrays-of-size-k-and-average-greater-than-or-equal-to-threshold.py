class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        cur = 0
        res = 0
        for i, x in enumerate(arr):
            # 1. in
            cur += x
            
            left = i - k + 1
            if left < 0:
                continue
            
            # 2. update
            if cur >= threshold:
                res += 1
            
            # 3. out
            cur -= arr[left]
        
        return res