#include<stdlib.h>
#include<stdbool.h>

/*
struct Iterator {
    // Returns true if the iteration has more elements.
    bool (*hasNext)();

     // Returns the next element in the iteration.
    int (*next)();
};
*/

struct PeekingIterator {
    struct Iterator *iterator;
    bool hasPeeked;
    int top;
};

struct PeekingIterator* Constructor(struct Iterator* iter) {
    struct PeekingIterator* piter = malloc(sizeof(struct PeekingIterator));
    piter->iterator = iter;
    piter->hasPeeked = false;
    return piter;
}

int peek(struct PeekingIterator* obj) {
    if (obj->hasPeeked) return obj->top;
    obj->hasPeeked = true;
    obj->top = obj->iterator->next();
    return obj->top;
}

int next(struct PeekingIterator* obj) {
    if (obj->hasPeeked) {
        obj->hasPeeked = false;
        return obj->top;
    } else {
        return obj->iterator->next();
    }
}

bool hasNext(struct PeekingIterator* obj) {
    if (obj->hasPeeked) return true;
    return obj->iterator->hasNext();
}

/**
 * Your PeekingIterator struct will be instantiated and called as such:
 * PeekingIterator* obj = peekingIteratorCreate(arr, arrSize);
 * int param_1 = peek(obj);
 * int param_2 = next(obj);
 * bool param_3 = hasNext(obj);
 * peekingIteratorFree(obj);
*/

