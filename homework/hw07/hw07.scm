(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1)
    ((> num 1) 1)
    (else 0))
)


(define (square x) (* x x))

(define (pow b n)
        (cond ((= n 0) 1)
              ((even? n) (square (pow b (/ n 2))))
              ((odd? n) (* b (pow b (- n 1))))
        )
)


(define (unique s)
  'YOUR-CODE-HERE
)


(define (replicate x n)
  'YOUR-CODE-HERE
  (define (helper x n lst )
    (if (= n 0)
      lst
      (helper x (- n 1)  (append lst (cons x nil))) )
  )
  (helper x n '())
  )


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (define (helper current sum)
    (if (> current n)
      sum 
      (helper (+ current 1) (combiner sum (term current)))
    )
  )
  (combiner start (helper 2 (term 1)))
  
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper current sum)
    (if (> current n)
      sum 
      (helper (+ current 1) (combiner sum (term current)))
    )
  )
  (combiner start (helper 2 (term 1)))
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)

