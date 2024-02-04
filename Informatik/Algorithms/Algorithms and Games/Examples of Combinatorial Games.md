### Chocolate Game - Chomp
+ First-Player Win
+ quadratic board
	+ ![](../../z_images/Pasted%20image%2020231004122109.png)
	+ ![](../../z_images/Pasted%20image%2020231004122004.png)
	+ optimal strategy
		+ take piece top right of the toxic piece
		+ creates two independent fields
		+ Tweedledum-Tweedledee-Principle
			+ first player copies moves of second player
+ rectangle board (of arbitrary size)
	+ draws are not possible
		+ must be a first or second player win
	+ assuming A does not have a winning strategy
		+ A can just take the top right piece
		+ B makes a winning move
		+ A could have just started with the move B just made
			+ strategy stealing
		+ contradiction
			+ A must have a winning strategy for every possible game board size
			+ First-Player Win
			+ A’s winning strategy exists but is unknown
				+ for general board sizes
				
### Tic Tak Toe
+ [[2 Player Combinatorial Game]]
+ no winner if played optimally
+ [[Min-Max Decision Tree]]
	+ ![](../../z_images/Pasted%20image%2020231004154541.png)
	+ ![](../../z_images/Pasted%20image%2020231004155224.png)
		+ only 765 states when stopping after winning

### Nine Men’s Morris - Mühle
+ http://ninemensmorris.ist.tugraz.at:8080/
+ 3 phases
	+ placing stones
	+ moving stones 
		+ allowed along the lines
	+ moving stones 
		+ jumping allowed
+ 3 stones along a line
	+ choose opponent’s stone to remove
+ draw if played optimally
+ operations to combine equivalent game states
	+ ![](../../z_images/Pasted%20image%2020231004161837.png)

### Connect 4
+ http://connect4.ist.tugraz.at:8080/
+ First-Player Win
+ states (7x6 board)
	+ 0 to 42 fields which have a
		+ yellow token
		+ red token
		+ no token
	+ ![](../../z_images/Pasted%20image%2020231005145505.png)
	+ 7 bit per column
		+ $7*7=49$ bit require 6 byte + 1 bit  
		+ first 1 acts as separator 
			+ marks the first token
			+ afterwards only the color is stored
		+ last separator is not needed
			+ number of half moves = total number of tokens
			+ count tokens in first 6 columns
			+ tokens in last column = total number of tokens - tokens in first 6 columns
		+ only store empty fields and colors without separator
			+ saves 1 bit $\Rightarrow$ exactly 6 byte required
		+ ![](../../z_images/Pasted%20image%2020231005150058.png)
+ move generator
	+ up to 7 successors
	+ add a token to a non-full column
+ identify final states
	+ draw
		+ 42 tokens placed and no win
	+ lose
		+ check if previous player has won
	+ win
		+ check 11 4-tuples which include just placed token
		+ fields above just placed token not considered
+ hybrid approach
	+ store first 23 half moves in DB
	+ compute remaining decision tree online
	+ maximum remaining search depth $42 - 23 = 19$
		+ with ~$5$ possible moves on average
	+ ![](../../z_images/Pasted%20image%2020231005154159.png)

