class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // 1. add non-overlapping intervals
        // 2. merge overlapping interval
        // 3. add rest intervals
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        List<int[]> res = new ArrayList<>();
        int i = 0;
        
        // 1. add non-overlapping intervals
        while(i < intervals.length && intervals[i][1] < newInterval[0]){
            res.add(intervals[i]);
            i++;
        }

        // 2. merge overlapping interval
        while(i < intervals.length && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
            i++;
        }
        res.add(newInterval);

        while(i < intervals.length){
            res.add(intervals[i]);
            i++;
        }

        return res.toArray(new int[res.size()][]);
    }
}