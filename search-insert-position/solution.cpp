class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        if (target <= nums[0]) {
            return 0;
        }
        int a = 0;
        int b = nums.size();
        int d = (b + a) / 2;
        while (a < b) {
            if (nums[d] < target) {
                a = d + 1;
            } else {
                b = d - 1;
                if (nums[d] == target || nums[d-1] < target) {
                    return d;
                }
            }
            d = (b + a) / 2;
        }

        return d;
    }
};
