/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Solving this problem to this point took approximately 27 minutes.

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (!list1) return list2;
    if (!list2) return list1;

    struct ListNode* head;
    if (list1->val <= list2->val) {
        head = list1;
        list1 = list1->next;
    } else {
        head = list2;
        list2 = list2->next;
    }

    struct ListNode* current = head;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            current->next = list1;
            current = current->next;
            list1 = list1->next;
        } else {
            current->next = list2;
            current = current->next;
            list2 = list2->next;
        }
    }

    if (list1) {
        current->next = list1;
    } else if (list2) {
        current->next = list2;
    }

    return head;
}
