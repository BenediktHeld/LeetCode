public class SearchInsertPostion35 {
    public int searchInsert(int[] nums, int target) {
        int CurrentPos = 0;
        int current = nums[CurrentPos];

        while (true){
            if (current == target){
                return CurrentPos;
            }else if(current > target){
                return CurrentPos;
            }else if(CurrentPos < nums.length-1){
                CurrentPos = CurrentPos + 1;
                current = nums[CurrentPos];
            }
            else{return nums.length;}
        }
    }
}
