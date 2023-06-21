minimax algorithm 
1. terminal function: returns true if the game is terminated else false
2. value: if game in terminal state this function return 1 if we won the game and -1 for losing 0 for a draw
3. player: used to determine whose turn to play the max or  min
4. actions: gives all the possible actions we take in that state
5. result: takes a state and on action and tells us what the new state of game will be after that action

```
	  | X | O        |   |              | X | O   
       -----------    -----------        -----------  
result( X | X | O  ,     |   |     ) =    X | X | O
       -----------    -----------        -----------
          | O |          |   | X            | O | X 

```
