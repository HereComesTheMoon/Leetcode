; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (all-possible-fbt n)
  (-> exact-integer? (listof (or/c tree-node? #f)))
  (if (= n 1)
    (list (tree-node 0 #f #f))
    (flatten
      (for/list ([k (in-range 1 (- n 1))])
        (map
          (lambda (vals) (apply tree-node vals))
          (cartesian-product
            (list 0)
            (all-possible-fbt k)
            (all-possible-fbt (- n (+ k 1)))
          )
        )
      )
    )
  )
)