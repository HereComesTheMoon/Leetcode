#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool isPalindrome(struct ListNode* head);

bool isPalindrome(struct ListNode* head){
    // Idea: 1. Find middle of linked list.
    // 2. Reverse first half of linked list.
    // 3. Starting from middle, check if palindrome by going through both halves one element at a time, and fix list.
    int len = 0;
    struct ListNode* n = head;
    while (n != NULL) {
        ++len;
        n = n->next;
    }
    // Now len is the length of the list.
    if (len <= 1) return true;

    int halfLen = len/2;
    n = head;
    struct ListNode* temp_last = NULL;
    struct ListNode* temp_next = head;
    for(int k = 0; k < halfLen; ++k) {
        temp_next = n->next;
        n->next = temp_last;
        temp_last = n;
        n = temp_next;
    }

    // At this point temp_next == n
    // Now our linked list is split into two in the exact middle, with temp_last and n as their heads.
    // Now move n by one if len odd, and then compare one by one, and repair the list in the process.
    // Use n, m to iterate, and use temp_last, temp_next to fix the first half of the list.

    if (len % 2) {
        n = n->next;
    }

    struct ListNode* m = temp_last;
    temp_last = temp_next;
    for (int k = 0; k < halfLen-1; ++k) {
        if (m->val != n->val) {
            return false;
        }
        n = n->next;

        temp_next = m->next;
        m->next = temp_last;
        temp_last = m;
        m = temp_next;
    }
    if (m->val != n->val) return false;
    return true;
}
