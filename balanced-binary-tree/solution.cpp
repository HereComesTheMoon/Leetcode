/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

int check(TreeNode* node) {
    if (node == nullptr) {
        return 0;
    }

    int l = check(node->left);
    int r = check(node->right);

    if (abs(l - r) > 1) throw -1;

    return 1 + max(l, r);
}

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        try {
            check(root);
        }

        catch (int e) {
            return false;
        }

        return true;
    }
};
