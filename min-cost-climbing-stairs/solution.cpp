class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int a = 0;
        int b = 0;
        int temp;
        for (const auto& val : cost) {
            temp = b;
            b = val + min(a, b); 
            a = temp;
        }
        return min(a, b);
    }
};