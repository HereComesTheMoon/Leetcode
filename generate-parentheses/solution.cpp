class Solution {
public:
    std::vector<std::string> generateParenthesis(int n) {
        if (n == 0) return std::vector<std::string>{""};
        std::vector<std::string> res;
        for (int k = 0; k < n; ++k) {
            for (const auto &s : this->generateParenthesis(k)) {
                for (const auto &t : this->generateParenthesis(n-1-k)) {
                    res.push_back("(" + s + ")" + t);
                }
            }
        }
        return res;
    }
};