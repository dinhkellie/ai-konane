# ai-konane
Game playing program that uses the minimax algorithm with alpha-beta pruning to play the game Konane



Where the players are X and O and the periods represent empty spaces.
A user inputs a move in form of integers: r1, c1, r2, c2 where r1, c1 refer to the start position and r2, c2 are the desired end position of that piece.

The program structure has a Konane class to describe game behavior (legal moves, make move, update board) and a Player class to describe player behavior (initialize, input move). Some issues I ran into was that the way I was generating a board, the coordinates were not x, y but rather row, column. So 4, 5 would map to 4 down, 5 across. I switched around the coordinates to match the example coordinate system. Another small issue was that the user inputs a move within the range of 1-8 while the board spaces go from 0-7. I had to add/subtract one in these cases.

The human player prompts the user to input a move, while the random player chooses a move at random from the generated list of moves. 
