/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        int val = head->val;
        ListNode* last = head;
        ListNode* now = head->next;

        while (now != nullptr) {
            if (now->val == val) {
                last->next = now->next;
            } else {
                val = now->val;
                last = now;
            }
            now = now->next;
        }
        return head;
    }
};
