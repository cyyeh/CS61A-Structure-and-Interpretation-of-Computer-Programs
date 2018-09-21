;; Scheme ;;

; Q2
(define (over-or-under x y)
  (cond (< x y) -1
        (= x y) 0
        else 1)
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q3
(define (filter f lst)
  (cond ((equal? nil lst) '())
        ((equal? #t (f (car lst))) (append (list(car lst)) (list(filter f (cdr lst)))))
        (else (append list() (list(filter f (cdr lst))))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q4
(define (make-adder num)
  (lambda (x) (+ num x))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13