use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct SmallestInfiniteSet (BinaryHeap<Reverse<i32>>);


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SmallestInfiniteSet {

    fn new() -> Self {
        let mut heap = SmallestInfiniteSet(BinaryHeap::with_capacity(1000));
        for x in 1..=1001 {
            heap.0.push(Reverse(x));
        }
        heap
    }
    
    fn pop_smallest(&mut self) -> i32 {
        let x = self.0.pop().unwrap().0;
        while self.0.peek().unwrap().0 == x {
            self.0.pop();
        }
        x
    }
    
    fn add_back(&mut self, num: i32) {
        self.0.push(Reverse(num));
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet::new();
 * let ret_1: i32 = obj.pop_smallest();
 * obj.add_back(num);
 */