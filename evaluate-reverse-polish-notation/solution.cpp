class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        for (const auto& s : tokens) {
            if (isdigit(s.back())) {
                stack.push(stoi(s));
                continue;
            }
            assert(stack.size() >= 2);
            auto a = stack.top();
            stack.pop();
            auto b = stack.top();
            stack.pop();
            switch (s.at(0)) {
            case '+':
                stack.push(b + a);
                break;
            case '-':
                stack.push(b - a);
                break;
            case '*':
                stack.push(b * a);
                break;
            case '/':
                stack.push(b / a);
                break;
            default:
                assert(false);
            }
        }
        return stack.top();
    }
};