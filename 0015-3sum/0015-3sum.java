class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Time Complexity: O(n^2)
        // Space Complexity: O(n)
        /*
            1. sort arrays
            2. fixed an element i, use double pointers scan
            left and right.
            3. when the sum is 0, save into results, else move
            pointers and skip the duplicates.
            4. if sum < 0, move the left pointer right,
            if sum > 0, move the right pointer left.
        */
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1, right = nums.length - 1;

            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while(left < right && nums[left] == nums[left - 1]) left++;
                    while(left < right && nums[right] == nums[right + 1]) right--;
                } else if(sum < 0){
                    left++;
                } else {
                    right--;
                }
            }
        }

        return res;
    }
}