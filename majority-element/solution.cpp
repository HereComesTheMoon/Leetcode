class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        if( nums.size() == 1 ) {
            return nums[0];
        }
        std::map<int, size_t> count = {};
        for( auto x : nums ) {
            if ( count.find(x) != count.end() ) {
                count[x]++;
                if ( count[x] > nums.size()/2 ) {
                    return x;
                }
            } else {
                count[x] = 1;
            }
        }
        __builtin_unreachable();
    }
};
