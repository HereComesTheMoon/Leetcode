class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        std::mt19937 rng = std::mt19937{std::random_device{}()};
        std::uniform_int_distribution<std::mt19937::result_type> sample(0, nums.size() - 1);
        while ( true ) {
            int last = nums[sample(rng)];
            size_t count = 0;
            for ( auto e : nums ) {
                count += (e == last);
            }
            if ( count > nums.size()/2 ) {
                return last;
            }
        }
    }
};
