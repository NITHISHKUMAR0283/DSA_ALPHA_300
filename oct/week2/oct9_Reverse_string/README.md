# OCT 9 - Reverse string 

|type |Problem | approach|time|space|
| :--- | :--- | :--- | :--- | :--- |
|primary|[Reverse string](./Reverse%20String.py)|use two pointer from both end to swap both side | o(n)|o(1)|
|variant 1|[Reverse string II](./Reverse_string_2.py)|take window of k and reverse using the above method | o(n)|o(n)|
|variant 2|[Reverse vowels](./reverse_vowels.py)|record the vowels of string from starting and start replacing from end in another for loop | o(n)|o(n)|
|variant 3|[Reverse Prefix](./reverse_prefix.py)|run a pointer to detect the starting char and once found reverse from start  | o(n)|o(n)|
|variant 4|[reverse word](./Reverse_word.py)|start to search for space once detected reverse the word and move start and do search for space again | o(n^2)|o(n)|
|variant 5|[reverse word in string ](./Reverse_word.py)|use the variant 4 to select the words and reverse and append to a result string with a space and reverse and retrun at the end| o(n^2)|o(1)|