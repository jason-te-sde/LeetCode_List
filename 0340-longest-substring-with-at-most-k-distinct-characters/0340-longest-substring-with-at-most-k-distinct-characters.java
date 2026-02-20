class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        //  Time Complexity: O(n)
        //  Space Complexity: O(k)
        /*  1. use HashMap to record the number of occurrences  
            of characters in the window.
            2. When meets a new character, expend the window.
            3. when the number of characters in the window
            exceeds k, shirink the window <= k.
            4. Update maximum length for each loop.
        */
        if(s == null || s.length() == 0 || k == 0) return 0;

        Map<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;

        for(int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            map.put(c, map.getOrDefault(c, 0) + 1);

            while(map.size() > k) {
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);
                
                if(map.get(leftChar) == 0){
                    map.remove(leftChar);
                }

                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
        
    }
}