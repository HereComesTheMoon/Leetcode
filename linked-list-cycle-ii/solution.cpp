/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode* detectCycle(ListNode* head) {
        std::set<ListNode*> seen;
        seen.insert(nullptr);
        while (seen.find(head) == seen.end()) {
            seen.insert(head);
            head = head->next;
        }
        return head;
    }
};


