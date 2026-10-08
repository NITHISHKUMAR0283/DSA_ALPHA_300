# Week2 Day1 -oct8 Two pointers 

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
|Primary|[valid_Palindrome](./Valid_palindrome.py)|convert the string to list while removing char which are not alpha numeric and from start and end shrink the pointer at same time and compare | o(n)|o(n)|
|Variant 1|[Valid_palindrome_II](./valid_palindrome_II.py)|same as the above problem , just check whethere remaining string is palindrome , by skipping left or right |o(n)|o(1)|
|Variant 2|[Reverse only letters](./Reverse_only_letters.py)|take the letters from starting and start to replace letters from last|o(n^2)|o(n)|
|Variant 3|[palindromic substring](./palindromic_substring.py)|at each index check palindrom by two pointers | o(n^2)|o(n)|
|Variant 4|[palindromic Linked list](./palindrom_linkedlist.py)|find middle by slow and fast pointer then reverse the next half and tranverse and check it is palindrom or not from the both end |o(n)|o(1)|
|variant 5|[palindromic number](./palindromic_number.py)|% will give the last digit and / will remove the last digit , so we can get last digit with these two operators , we store in list and do it again and compare with list |o(n)|o(n)|