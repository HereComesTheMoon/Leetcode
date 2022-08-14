class Solution {
public:
    std::string longestPalindrome(const std::string s) {
        std::string longest = {s[0]};

        std::function<int(int, int)> biggestPalindrome = [&s](int a, int b){
            while (0 <= a && b < int(s.size()) && s[a] == s[b]) {
                --a;
                ++b;
            }
            return b - a - 2;
        };

        for (int i = 1; i < int(s.size()); ++i) {
            int size = biggestPalindrome(i, i);
            if (size > int(longest.size())) {
                longest = s.substr(i - size/2, size+1);
            }
        }

        for (int i = 0; i < int(s.size()); ++i) {
            int size = biggestPalindrome(i, i+1);
            if (size >= int(longest.size())) {
                longest = s.substr(i - size/2, size+1);
            }
        }
                
        return longest;
    }
};
