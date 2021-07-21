(defun dec->bin (n)
(if (and (> n -1) (< n 16))
	(aref bin n) nil))
	  
(defun display-board (board)
	(dotimes (x 4)
		(dotimes (y 4)
			(if (= y 3)
				(if (= 16 (aref board x y)) (format t "|        -       |~%") (format t "|   ~A   |~%" (dec->bin (aref board x y))))
				(if (= 16 (aref board x y)) (format t "|        -        ")   (format t "|   ~A    " (dec->bin (aref board x y))))))) 
			
	(format t "~%"))
	
(defun update-board (board coords figure)
	(setf (aref board (getf coords :x) (getf coords :y)) figure))
	
(defun update-figures (figures figure)
	(setf (aref figures figure) 16))
	
(defun valid-position-p (board coords)
	(if (and (< -1 (getf coords :x)) (> 4 (getf coords :x)) (< -1 (getf coords :y)) (> 4 (getf coords :y)))
	(and (equal 16 (aref board (getf coords :x) (getf coords :y))))))
	
(defun valid-figure-p (figures figure)
(if (or (> figure 15) (< figure 0) (= (aref figures figure) 16)) (return-from valid-figure-p nil)
	(return-from valid-figure-p t)))
	
(defun print-valid-figures (figures)
	(format t "The valid figures are ~%")
	(dotimes (i 16)
		(if (valid-figure-p figures (aref figures i)) (format t "~2d  ~A~%" (aref figures i) (dec->bin (aref figures i)))))
	(choose-figure figures 'c))
	
(defun choose-coords (board player)
	(if (equal player 'p) (format t "Please enter coordinates x and y: ") (format t "Oponent is selecting coordinates!~%"))
	(if (equal player 'c) 
	
		(let ((x (random 4 (make-random-state t))))
			(let ((y (random 4 (make-random-state t))))
			(let ((coords `(:x, x :y, y)))
		(if (valid-position-p board coords) (return-from choose-coords coords) (choose-coords board 'c)))))
		
		(let ((x (parse-integer (read-line) :junk-allowed t))) 
				(let ((y (parse-integer (read-line) :junk-allowed t)))				
				(let ((coords `(:x, x :y, y))) (if (valid-position-p board coords) (return-from choose-coords coords) (choose-coords board 'p)))))
		))
		
(defun choose-figure (figures player)
	(if (equal player 'c) (format t "Please enter figure number, 0-15 (or -1): ") (format t "Oponent is selecting a figure!~%"))
	(if (equal player 'c) 
		(let ((figure (parse-integer (read-line) :junk-allowed t)))
			(if (equal figure -1)(print-valid-figures figures) 
				(if (valid-figure-p figures figure) (return-from choose-figure figure) (choose-figure figures 'c))))
			
		(let ((figure (random 16 (make-random-state t))))
		(if (valid-figure-p figures figure) (return-from choose-figure (napisi figure)) (choose-figure figures 'p)))))

(defun napisi (figure)
	(format t "The figure selected is ~d ~A.~%" figure (dec->bin figure)) 
	(return-from napisi figure))
	
(defun one-turn (board figures player)
	(let ((figure (choose-figure figures player)))
		(let ((coords (choose-coords board player))) (end-turn board coords figures figure player))))

(defun end-turn (board coords figures figure player)
	(update-board board coords figure)
	(update-figures figures figure))

(defun game-over-p (board)
	(flet ((draw-p (board)
			(let ((counter 0)) 
				(dotimes (x 4)
					(dotimes (y 4)
						(when (equal 16 (aref board x y)) (incf counter))))
			(= 0 counter))))		

	(dotimes (i 4)
		(dotimes (j 4)
			(cond
				;rows
				((and  
					(if (and (not (= (aref board i 0) 16)) (not (= (aref board i 1) 16))) (= (aref (dec->bin (aref board i 0)) j) (aref (dec->bin (aref board i 1)) j)))
					(if (and (not (= (aref board i 0) 16)) (not (= (aref board i 2) 16))) (= (aref (dec->bin (aref board i 0)) j) (aref (dec->bin (aref board i 2)) j)))
					(if (and (not (= (aref board i 0) 16)) (not (= (aref board i 3) 16))) (= (aref (dec->bin (aref board i 0)) j) (aref (dec->bin (aref board i 3)) j)))
					)
				(return-from game-over-p 1))
		
				;columns
				((and
					(if (and (not (= (aref board 0 i) 16)) (not (= (aref board 1 i) 16))) (= (aref (dec->bin (aref board 0 i)) j) (aref (dec->bin (aref board 1 i)) j)))
					(if (and (not (= (aref board 0 i) 16)) (not (= (aref board 2 i) 16))) (= (aref (dec->bin (aref board 0 i)) j) (aref (dec->bin (aref board 2 i)) j)))
					(if (and (not (= (aref board 0 i) 16)) (not (= (aref board 3 i) 16))) (= (aref (dec->bin (aref board 0 i)) j) (aref (dec->bin (aref board 3 i)) j)))
					) 
				(return-from game-over-p 1))
		
				;diagonals
				((and
					(if (and (not (= (aref board 0 0) 16)) (not (= (aref board 1 1) 16))) (= (aref (dec->bin (aref board 0 0)) j) (aref (dec->bin (aref board 1 1)) j)))
					(if (and (not (= (aref board 0 0) 16)) (not (= (aref board 2 2) 16))) (= (aref (dec->bin (aref board 0 0)) j) (aref (dec->bin (aref board 2 2)) j)))
					(if (and (not (= (aref board 0 0) 16)) (not (= (aref board 3 3) 16))) (= (aref (dec->bin (aref board 0 0)) j) (aref (dec->bin (aref board 3 3)) j)))
					)
				(return-from game-over-p 1))
				((and
					(if (and (not (= (aref board 0 3) 16)) (not (= (aref board 1 2) 16))) (= (aref (dec->bin (aref board 0 3)) j) (aref (dec->bin (aref board 1 2)) j)))
					(if (and (not (= (aref board 0 3) 16)) (not (= (aref board 2 1) 16))) (= (aref (dec->bin (aref board 0 3)) j) (aref (dec->bin (aref board 2 1)) j)))
					(if (and (not (= (aref board 0 3) 16)) (not (= (aref board 3 0) 16))) (= (aref (dec->bin (aref board 0 3)) j) (aref (dec->bin (aref board 3 0)) j)))
					)
				(return-from game-over-p 1))
				
				;draw-p
				((draw-p board) (return-from game-over-p 2))
				
				;othervise nill
				(t nil))))))

(defun make-bin ()
	(setf bin (make-array 16))
	(setf (aref bin 0) (make-array 4 :initial-contents '(0 0 0 0)))
	(setf (aref bin 1) (make-array 4 :initial-contents '(0 0 0 1)))
	(setf (aref bin 2) (make-array 4 :initial-contents '(0 0 1 0)))
	(setf (aref bin 3) (make-array 4 :initial-contents '(0 0 1 1)))
	(setf (aref bin 4) (make-array 4 :initial-contents '(0 1 0 0)))
	(setf (aref bin 5) (make-array 4 :initial-contents '(0 1 0 1)))
	(setf (aref bin 6) (make-array 4 :initial-contents '(0 1 1 0)))
	(setf (aref bin 7) (make-array 4 :initial-contents '(0 1 1 1)))
	(setf (aref bin 8) (make-array 4 :initial-contents '(1 0 0 0)))
	(setf (aref bin 9) (make-array 4 :initial-contents '(1 0 0 1)))
	(setf (aref bin 10) (make-array 4 :initial-contents '(1 0 1 0)))
	(setf (aref bin 11) (make-array 4 :initial-contents '(1 0 1 1)))
	(setf (aref bin 12) (make-array 4 :initial-contents '(1 1 0 0)))
	(setf (aref bin 13) (make-array 4 :initial-contents '(1 1 0 1)))
	(setf (aref bin 14) (make-array 4 :initial-contents '(1 1 1 0)))
	(setf (aref bin 15) (make-array 4 :initial-contents '(1 1 1 1)))
	(return-from make-bin bin))
	
(defun game () 
	(setf board (make-array '(4 4) :initial-element 16))
	(setf figures (make-array 16))
	(dotimes (i 16) (setf (aref figures i) i))
	(setf bin (make-bin))
	
	(let ((turn-counter (1+ (random 2 (make-random-state t)))))
		(loop 
			(if (game-over-p board) (let ((result `(:x, turn-counter :y, (game-over-p board)))) (return-from game result)))
			(display-board board)
			
			(if(evenp turn-counter)
				(one-turn board figures 'p)
				(one-turn board figures 'c))
			
			(incf turn-counter))
		))
	

(setf result (game))	
(if (evenp (getf result :x)) 
	(if (= (getf result :y) 1) 
		(format t "You lost!~%") 
		(format t "It was a draw!~%"))
	(if (= (getf result :y) 1) 
		(format t "You won!~%") 
		(format t "It was a draw!~%")))