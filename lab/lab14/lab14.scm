(define (split-at lst n)
  (if (> n (length lst))
      (list lst)
      (if (= n 0)
          (cons nil lst)
          (cons
               (append (car (split-at lst (- n 1))) (list (car (cdr (split-at lst (- n 1))))))
               (cdr (cdr (split-at lst (- n 1))))
               )
          )
    )
)


(define (compose-all funcs)
  (define (helper x)
      (if (null? funcs)
          x
          ((compose-all (cdr funcs)) ((car funcs) x))
          )
      )
  helper
)

