(define/contract (peak-index-in-mountain-array arr)
  (-> (listof exact-integer?) exact-integer?)
  (car 
    (foldl 
        (lambda (now acc) 
          (if (< (cdr acc) (cdr now))
            now
            acc))
        (cons 0 0)
        (for/list 
          ([i (in-range 100000)] [x arr])
          (cons i x))))
)
