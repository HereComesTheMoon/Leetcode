(define/contract (asteroid-collision asteroids)
  (-> (listof exact-integer?) (listof exact-integer?))
	(let loop 
	  (
	    [head empty]
	    [tail asteroids]
	  )
	  (if (empty? tail)
		(reverse head)
		(if (or (empty? head) (negative? (car head)))
          (loop (append (list (car tail)) head) (cdr tail))
		  (if (negative? (car tail))
			(cond
			  [(= (abs (car head)) (abs (car tail))) (loop (cdr head) (cdr tail))]
			  [(< (car head) (abs (car tail))) (loop (cdr head) tail)]
			  [else (loop head (cdr tail))]
			)
			(loop (append (list (car tail)) head) (cdr tail))
		  )
		)
	  )

	)
  )
