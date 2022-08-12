class Solution {
public:
    bool isValid(std::string s) {
        std::vector<char> stack = {1};
        
        for (auto &c: s) {
            switch (c) {
            case '(':
                stack.push_back(c);
                break;
            case '[':
                stack.push_back(c);
                break;
            case '{':
                stack.push_back(c);
                break;
            case ')':
                if (stack.back() != '(') {
                    return false;
                }
                stack.pop_back();
                break;
            case ']':
                if (stack.back() != '[') {
                    return false;
                }
                stack.pop_back();
                break;
            case '}':
                if (stack.back() != '{') {
                    return false;
                }
                stack.pop_back();
                break;
            }
        }
        stack.pop_back();
        return stack.empty();
    }
};



