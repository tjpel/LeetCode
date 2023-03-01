class Solution {
    public static int[] twoSum(int[] nums, int target) {
        for(int i = 1; i < nums.length; i++){
            for(int j = 0; j + i < nums.length; j++){
                if(nums[j] + nums[j + i] == target){
                    return new int[] {j, j + i};
                }
            }
        }
        return new int[] {};
    }

    public static void main(String[] args){
        int[] nums = {2, 7, 11, 15};
        for(int num : twoSum(nums, 9)){
            System.out.println(num);
        }
    }
}