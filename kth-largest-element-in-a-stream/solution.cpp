class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    uint num;
    
    KthLargest(int k, vector<int>& nums) {
        num = uint(k);
        for (const auto& val: nums) {
            pq.push(val);
            if (num < pq.size()) pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        if (num < pq.size()) pq.pop();
        return pq.top();
    }
};