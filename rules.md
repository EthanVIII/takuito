## Graphical Notation for Players

"O" - Player 1 normal piece
"X" - Player 2 normal piece
"o" - Player 1 wall
"x" - Player 2 wall
"1" - Player 1 capstone
"2" - Player 2 capstone

"OOX" - Player 1 on the top.

## Notation for pieces

Each move is dictated as a series of characters in a string.

1st char - "n" or "m".

n - indicates placing a new piece. New pieces can only be placed on blank spaces.
m - indicates moving a piece/pieces on the board.


If 1st char was "n"

	2nd char -
	
		w - indicates a wall piece
		c - indicates a capstone
		p - indicates a normal piece

	3rd and 4th char - 
	
		Indicates the coordinate of placement. a4 would be x = 0, y = 4. e0 would be x = 4, y = 0.

If 1st chat was "m"
	
	2nd char -

		# - integer 0-4 that indicates the number of additional pieces you are moving.
	
	3rd and 4th char - 
		
		Indicates the starting coordinate of move. (e.g. a0,b3)

	5th char - 
		
		u/d/l/r - up (y+1), down (y-1), left (x-1), right (x+1).

	LOOP vv
	
	6th char (Opt.) -

		# - integer 0-4 that indicates the number of additional piece you are moving.
		    Cannot move if you currently have only one piece.
	
	7th char (Opt.)
			 
		u/d/l/r - up, down, left, right


