class KthLargest {
public:
    vector<int> v;
    priority_queue<int, vector<int>, greater<int>> pq;
    int num;
    
    KthLargest(int k, vector<int>& nums) {
        num = k;
        sort(nums.begin(), nums.end());
        int i = 0;
        while (i < num && !nums.empty()) {
            ++i;
            v.push_back(nums.back());
            nums.pop_back();
        }
        pq = priority_queue<int, vector<int>, greater<int>>(v.begin(), v.end());
    }
    
    int add(int val) {
        if (uint(num - 1) == pq.size()) {
            pq.push(val);
            return pq.top();
        }
        assert(pq.size() >= uint(num));
        if (val < pq.top()) return pq.top();
        pq.push(val);
        pq.pop();
        cout << pq.top() << endl;
        return pq.top();
    }
};