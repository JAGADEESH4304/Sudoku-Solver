This sudoku solver helps to give efficent solutions to the given puzzle using Backtracking.


Here it checks for every possible case if the number is suitable for the entire row,col and 3*3 board, than it goes for next one and so on..



Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.



Space Complexity: O(1), since I am refilling the given board itself, there is no extra space required, so constant space complexity.
