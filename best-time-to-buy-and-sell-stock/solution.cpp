class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int min = prices[0];
        int profit = 0;

        for(auto e: prices) {
            profit = ( e - min > profit ? e - min : profit );
            min = (e < min ? e : min );
        }
        return profit;
    }
};
