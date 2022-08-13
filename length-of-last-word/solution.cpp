class Solution {
public:
    int lengthOfLastWord(std::string s) {
        auto it = --s.end();
        int count = 0;
        while (*it == ' ') {
            --it;
        }
        while (s.begin() <= it && *it != ' ') {
            ++count;
            --it;
        }

        return count;
    }
};
