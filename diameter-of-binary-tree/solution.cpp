pair<int, int> rec(TreeNode* root) {
    if (root->left == nullptr && root->right == nullptr)
        return {1, 0};
    if (root->left == nullptr) {
        auto [depth, diam] = rec(root->right);
        return {depth + 1, max(diam, depth)};
    }
    if (root->right == nullptr) {
        auto [depth, diam] = rec(root->left);
        return {depth + 1, max(diam, depth)};
    }
    auto [depthl, diaml] = rec(root->left);
    auto [depthr, diamr] = rec(root->right);
    auto diam_max = max(diaml, diamr);
    return {1 + max(depthl, depthr), max(diam_max, depthl + depthr)};
}


class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return -1;
        return rec(root).second;
    }
};