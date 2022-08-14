class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        size_t walker = 0;
        size_t longest = 0;

        std::unordered_set<int> seen = {};



        for (size_t runner = 0; runner < s.length(); ++runner) {
            if (seen.count(s[runner])) {
                while ( s[walker] != s[runner] ) {
                    seen.erase(s[walker]);
                    ++walker; 
                }
                ++walker;
            } else {
                seen.insert(s[runner]);
            }
            longest = ( 1 + runner - walker > longest ? 1 + runner - walker : longest );
        }

        return longest;
    }
};
