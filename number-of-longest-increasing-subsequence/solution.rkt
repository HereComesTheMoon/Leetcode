(define/contract (find-number-of-lis nums)
  (-> (listof exact-integer?) exact-integer?)
  (define nums_v (list->vector nums))
  (define n (length nums))
  (define len (make-vector n 1))
  (define count (make-vector n 1))
  (for ([i (in-range n)])
    (for ([j (in-range i)])
      (if (< (vector-ref nums_v j) (vector-ref nums_v i))
        (begin
          (if (< (vector-ref len i) (+ 1 (vector-ref len j)))
            (begin
              (vector-set! len i (+ 1 (vector-ref len j)))
              (vector-set! count i 0)
            )
            empty
          )
          (if (= (vector-ref len i) (+ 1 (vector-ref len j)))
            (vector-set! count i (+ (vector-ref count i) (vector-ref count j)))
            empty
          )
        )
        empty
      )
    )
  )  
  (let ([max_length (vector-argmax identity len)])
    (apply +
      (for/list (
        [x count]
        [l len]
        #:when ((lambda (y) (= y max_length)) l))
        x
      )
    )
  )
)