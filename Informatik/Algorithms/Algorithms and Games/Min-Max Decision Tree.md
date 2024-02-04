### Classical Approach
+ starting position as root
	+ during game the current position
+ states as nodes
+ possible moves as edges to child nodes
	+ states may be reached by multiple move sequences
	+ performance improvement possible
		+ no longer a tree
+ tree depth is bounded
	+ exponential overhead
	+ combinatorial explosion 
+ half move
	+ own move + opponents move = full move
	+ must also consider the opponents answer move
	+ k half moves
		+ $\lfloor \frac{k}{2}\rfloor$ $(+1)$ moves per player
+ ![](../../z_images/Pasted%20image%2020231004125826.png)
	+ not shown possible moves are symmetrical
+ leaves nodes are evaluated using heuristics
	+ heuristic scores the game state
	+ terminal states (win, lose) have extreme values
	+ non-leave nodes evaluated by traversing the tree downwards
		+ chooses maximum/minimum score of available moves
+ maximizer and minimizer
	+ one player wants to maximize the value of all child nodes
	+ other player wants to minimize the value of all child nodes
	+ ![](../../z_images/Pasted%20image%2020231004130753.png)

### α-β Pruning
+ prevents combinatorial explosion
+ reduces states to consider
	+ combines states with identical outcome
+ more efficient and equal results as the classical approach
+ stops traversing tree downwards upon reaching
	+ a minimum value smaller than current maximum
	+ a maximum value larger than current minimum
	+ ![](../../z_images/Pasted%20image%2020231004132231.png)
	+ ![](../../z_images/Pasted%20image%2020231004132615.png)
+ pseudo code
	+ ![](../../z_images/Pasted%20image%2020231004132655.png)
+ examples
	+ ![](../../z_images/Pasted%20image%2020231004133517.png)
	+ ![](../../z_images/Pasted%20image%2020231004134124.png)
+ pre-sorted $\alpha-\beta$ pruning
	+ efficiency depends on order of states
	+ ![](../../z_images/Pasted%20image%2020231004134247.png)
