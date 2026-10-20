class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++){
            if (numMap.containsKey(nums[i])) {
                return true;
            } else {
                numMap.put(nums[i], 1);
            }
        }
        return false;
    }
}