/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

void rec(map<Node*, Node*>& known, Node* node) {
    Node* new_node = new Node(node->val, {});
    known.insert({node, new_node});
    for (const auto& neighbor : node->neighbors) {
        if (known.find(neighbor) == known.end()) {
            rec(known, neighbor);
        }
        new_node->neighbors.emplace_back(known[neighbor]);
    }
}

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        map<Node*, Node*> known;
        rec(known, node);
        return known[node];
    }
};