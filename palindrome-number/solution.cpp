class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 10) {
            return 0 <= x;
        }

        int len = std::log10(x);
        while (len > 0) {
            int highest = x / int(std::pow(10, len));
            if (x % 10 != highest) {
                return false;
            }
            x = (x - highest * int(std::pow(10, len))) / 10;
            --len;
            --len;
        }

        return true;
    }
};

