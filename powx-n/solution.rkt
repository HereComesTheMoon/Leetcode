(define/contract (my-pow x n)
  (-> flonum? exact-integer? number?)
    (expt x n)
  )