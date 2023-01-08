struct Edge {
    int px;
    int py;
    int qx;
    int qy;
    int dist;
};

int l1_dist(int px, int py, int qx, int qy) {
    return abs(px - qx) + abs(py - qy);
}

class DisjointSet {
    map<pair<int, int>, pair<int, int>> s;
    map<pair<int, int>, int> size;

public:
    void push(int x, int y) {
        s[{x, y}] = {x, y};
        size[{x, y}] = 1;
    }

    pair<int, int> find_rep(int x, int y) {
        auto [xx, yy] = s.at({x, y});
        while (xx != x || yy != y) {
            auto par = s.at({xx, yy});
            s[{x, y}] = par;
            x = xx;
            y = yy;
            xx = par.first;
            yy = par.second;
        }
        return {xx, yy};
    }

    pair<int, int> merge(int px, int py, int qx, int qy) {
        auto p = find_rep(px, py);
        auto q = find_rep(qx, qy);
        if (size[p] < size[q]) {
            s[p] = q;
            size[q] += size[p];
            return q;
        } else {
            s[q] = p;
            size[p] += size[q];
            return p;
        }
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        auto cmp = [](Edge l, Edge r) { 
            return l.dist > r.dist; // > for min priority_queue
        };
        vector<Edge> v;
        priority_queue pq(v.begin(), v.end(), cmp);
        DisjointSet ds;
        
        for (size_t i = 0; i < points.size(); ++i) {
            auto px = points[i][0];
            auto py = points[i][1];
            ds.push(px, py);
            for (size_t j = i + 1; j < points.size(); ++j) {
                auto qx = points[j][0];
                auto qy = points[j][1];
                pq.push(Edge { px, py, qx, qy, l1_dist(px, py, qx, qy) }); 
            }
        }

        int min_cost = 0;
        uint connected = 1;
        while (connected < points.size()) {
            Edge e = pq.top();
            pq.pop();
            if (ds.find_rep(e.px, e.py) == ds.find_rep(e.qx, e.qy)) continue;
            min_cost += e.dist;
            ds.merge(e.px, e.py, e.qx, e.qy);
            ++connected;
        }

        return min_cost;
    }
};