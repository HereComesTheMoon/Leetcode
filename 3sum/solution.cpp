class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        std::vector<std::vector<int>> res;

        int lastFirst = nums[0]-1;
        for( size_t i = 0; i < nums.size(); ++i ) {
            if( nums[i] == lastFirst ) {
                continue;
            }
            lastFirst = nums[i];
            
            std::map<int, int> seen; // map[value_which_is_needed, second_value]
            int lastResLastValue = nums[i] - 1;
            for( size_t j = i + 1; j < nums.size(); ++j ) {
                if( nums[j] == lastResLastValue ) {
                    continue;
                }

                auto it = seen.find(nums[j]);
                if( it == seen.end() ) {
                    seen[-nums[i]-nums[j]] = nums[j];
                    continue;
                }
                res.push_back({nums[i], seen[nums[j]], nums[j]});
                lastResLastValue = nums[j];
            }
        }
        return res;
    }
};
