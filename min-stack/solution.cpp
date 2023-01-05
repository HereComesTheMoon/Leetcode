class MinStack {
vector<int> stack;
vector<int> mins;

public:
    MinStack() {}
    
    void push(int val) {
        stack.emplace_back(val);
        if (mins.empty()) {
            mins.emplace_back(val);
        } else if (val <= mins.back()) {
            mins.emplace_back(val);
        }
    }
    
    void pop() {
        if (stack.back() == mins.back()) {
            mins.pop_back();
        }
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return mins.back();
    }
};
