### Observations
+ groups
	+ 9 horizontal rows
	+ 9 vertical rows
	+ 9 blocks
+ each cell is part of 3 groups
+ ![[../../../z_images/Pasted image 20231105151114.png]]
+ ![[../../../z_images/Pasted image 20231106113437.png]]
	+ a cell has only one possible number =>
		+ remove this number from other cells
+ ![[../../../z_images/Pasted image 20231106113244.png]]
	+ a number is in only one cell possible =>
		+ remove all other possible entries for this cell
		+ decrement counters for these entries

### Pseudocode
+ ![[../../../z_images/Pasted image 20231106114100.png]]
+ ![[../../../z_images/Pasted image 20231106114438.png]]
+ more sophisticated backtracking version
	+ able to solve level 2 sudokus
	+ guesses a number for a square
		+ ![[../../../z_images/Pasted image 20231106120120.png]]
	+ level 3 sudokus would need 2 backtracking steps
	+ ![[../../../z_images/Pasted image 20231106120311.png]]
		+ 8 would lead to a contradiction => try 6
		+ 6 solves the sudoku
+ constant time and space complexity
	+ assuming a regular 9x9 sudoku
	+ otherwise NP complete?
