#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);
struct ListNode* buildList(int* arr, size_t len);
void printList(struct ListNode* head);

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

    while (list2) {
        while (list1 && list1->val <= list2->val) {
            current->next = list1;
            current = current->next;
            list1 = list1->next;
        }
        if (!list1) { // This ensures that we don't go through entire list2.
            current->next = list2;
            break;
        }
        current->next = list2;
        current = current->next;
        list2 = list2->next;
    }
    if (list1) {
        current->next = list1;
    }
    return head;

}
