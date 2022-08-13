class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        ++digits.back();
        for (int i = digits.size() - 1; 0 < i; --i) {
            if (digits[i] == 10) {
                digits[i] = 0;
                digits[i-1] = digits[i-1] + 1;
            } else {
                break;
            }
        }
        if (digits[0] == 10) {
            digits[0] = 0;
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
