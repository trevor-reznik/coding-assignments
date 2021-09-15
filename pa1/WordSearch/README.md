# WordSearch Program

Wordsearch Program
PA1 | CSC210 | Fall 21
<p>
Parse text and dictionary files from stdin path params.
Search for matches going up/dowm back/forward. Print all
matches in sorted order to stdout.
<p>
Usage:
 <code>java WordSearch.java dictionary puzzle</code>
<p>
Example:
 <code>java WordSearch.java myDict.txt myPuzzle.txt</code>
<p>
<b>Dictionary File</b> should be a text file of words delimited by newline
characters.
<b>Puzzle File</b> should be a text file containing rows
delimited by newline characters.


### Runtime Improvement History

###### Version 1

real	0m1.182s
user	0m3.098s
sys	0m0.137s


###### Version 2

```
real	0m1.238s
user	0m3.353s
sys	    0m0.084s
```

Changed `rotatePuzzle()` implementation to convert/use arrays for objects that are only being looked up and linked lists for objects that are only being appended to.

Reduce linked list of chars to a string for final output instead of concatting (copying and appending) a string on each iteration.

###### Version 3

Changed text files (puzzles and dictionary) to be immediately converted to arrays after parsing, because only doing lookups after originally deleting first two lines of puzzle file. Time is not improved because I also removed the feature that would break the search loop after one result -- so it now going through entire iteration (searching for duplicates) everytime. 


```
real	0m1.188s
user	0m3.230s
sys	    0m0.094s
```