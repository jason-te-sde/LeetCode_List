class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        l=0
        r=0
        maxf=0
        maxi=0
        while r<len(s):
            dict1[s[r]]=dict1.get(s[r],0)+1
            maxf=max(maxf,dict1[s[r]])

            if r-l+1 - maxf >k:
                dict1[s[l]]-=1
                l+=1
            if r-l+1 -maxf<=k:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi 