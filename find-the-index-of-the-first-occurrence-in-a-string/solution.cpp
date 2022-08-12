class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        if (haystack.length() < needle.length()) {
            return -1;
        }
        const size_t upper = haystack.length() - needle.length() + 1;
        for(size_t i = 0; i < upper; ++i) {
            for (size_t j = 0; j < needle.length(); ++j) {
                if (haystack[i+j] != needle[j]) {
                    goto BREAK_NESTED;
                }
            }
            return i;
BREAK_NESTED:
            ;
        }
        return -1;
    }
};

