; combiner: a function of two arguments
; start: a number with which to start combining
; n: the number of natural numbers to combine
; term: a function of one argument that computes the nth term of a sequence
(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (if (> n 0)
      (accumulate-tail combiner (combiner start (term n)) (- n 1) term)
      start
  )
  ;(define (accumulate-result combiner start n term result)
  ;  (if (= n 0)
  ;    result
  ;    (accumulate-result combiner start (- n 1) term (combiner (term n) result))
  ;  ) 
  ;)

  ;(accumulate-result combiner start n term start)
)

; (list-of (* x x) for x in '(3 4 5) if (odd? x))
(define-macro (list-of expr for var in seq if filter-fn)
  (list 'map (list 'lambda (list var) expr) (list 'filter (list 'lambda (list var) filter-fn) seq))
)