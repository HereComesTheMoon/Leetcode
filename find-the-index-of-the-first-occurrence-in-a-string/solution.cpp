class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        for(size_t i = 0; i < haystack.length(); ++i) {
            if (needle == haystack.substr(i, needle.length())) {
                return i;
            }
        }
        return -1;
    }
};

