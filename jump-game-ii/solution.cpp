class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.empty()) return -1;
        vector<int> jumps(nums.size(), numeric_limits<int>::max());
        jumps.at(0) = 0;
        size_t lower = 0;
        size_t upper = 1;
        for (size_t i = 0; i < nums.size(); ++i) {
            auto val = nums[i];
            upper = min(i + 1 + val, nums.size());
            for (size_t j = lower + 1; j < upper; ++j) {
                jumps[j] = min(jumps[i] + 1, jumps[j]);
            }
            lower = upper - 1;
            if (upper == nums.size()) return jumps.back();
        }
        return -1;
    }
};