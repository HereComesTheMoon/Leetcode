class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        vector<int> seq;
        for (const auto& val : nums) {
            auto it = lower_bound(seq.begin(), seq.end(), val);
            if (it == seq.end()) {
                seq.push_back(val);
            } else {
                *it = val;
            }
        }
        return seq.size();
    }
};