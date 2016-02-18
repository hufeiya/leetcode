class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroItr = -1;
        for(int i = 0;i < nums.size();i++){
            if(nums[i] == 0 && zeroItr == -1){
                zeroItr = i;
            }
            else if(nums[i] != 0 && zeroItr != -1){
                nums[zeroItr] = nums[i];
                nums[i] = 0;
                zeroItr ++;
            }
        }
    }
};
