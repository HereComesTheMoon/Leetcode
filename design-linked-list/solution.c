#include<stdlib.h>
#include<stdbool.h>
#include<stdio.h>

typedef struct Node Node;

typedef struct {
    Node* head;
    Node* tail;
} MyLinkedList;

struct Node {
    int val;
    Node* next;
    Node* prev;
};

MyLinkedList* myLinkedListCreate() {
    MyLinkedList* mll = malloc(sizeof(MyLinkedList));
    mll->head = NULL;
    mll->tail = NULL;
    return mll;
}

Node* myLinkedListGetNodeAtIndex(MyLinkedList* obj, int index) {
    Node* n = obj->head;
    int i = 0;
    while(n != NULL && i != index) {
        n = n->next;
        ++i;
    }
    return n;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    Node* n = myLinkedListGetNodeAtIndex(obj, index);
    if (n != NULL) {
        return n->val;
    }
    return -1;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    Node* n = malloc(sizeof(Node));
    n->val = val;
    n->next = obj->head;
    n->prev = NULL;
    if (obj->head != NULL) {
        obj->head->prev = n;
    } else {
        obj->tail = n;
    }
    obj->head = n;
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    Node* n = malloc(sizeof(Node));
    n->val = val;
    n->prev = obj->tail;
    n->next = NULL;
    if (obj->tail != NULL) {
        obj->tail->next = n;
    } else {
        obj->head = n;
    }
    obj->tail = n;
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index == 0) {
        myLinkedListAddAtHead(obj, val);
        return;
    }

    Node* n = myLinkedListGetNodeAtIndex(obj, index-1);

    if (n == NULL) return;
    Node* new = malloc(sizeof(Node));
    new->val = val;
    new->next = n->next;
    new->prev = n;
    if (n->next != NULL) {
        n->next->prev = new;
    } else {
        obj->tail = new;
    }

    n->next = new;
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    Node* n = myLinkedListGetNodeAtIndex(obj, index);
    if (n == NULL) return;
    if (n->next == NULL) {
        obj->tail = n->prev;
    } else {
        n->next->prev = n->prev;
    }
    if (n->prev == NULL) {
        obj->head = n->next;
    } else {
        n->prev->next = n->next;
    }
    free(n);
}

void myLinkedListFree(MyLinkedList* obj) {
    Node* n = obj->head;
    if (n == NULL) {
        free(obj);
        return;
    }
    n = n->next;
    while (n != NULL) {
        free(n->prev);
        n = n->next;
    }
    free(n);
    free(obj);
}

void myLinkedListPrint(MyLinkedList* obj) {
    Node* n = obj->head;

    printf("[ ");
    while (n != NULL) {
        printf("%d, ", n-> val);
        Node* m = n->next;
        if (m != NULL) {
            if (m->prev != n) {
            }
        }
        n = n->next;
    }
    printf("]. Head: %p, Tail: %p\n", obj->head, obj->tail);
}

void printNode(Node* n) {
    printf("%p -> %p -> %p\n", n->prev, n, n->next);
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/
