# Day 07: HashMap Counting and multiset


## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Intersection_of_Two_Arrays_II.py](./Intersection_of_Two_Arrays_II.py) | Build freq of each element  from first array and iterate the second array if the current element is present append it to result and reduce the freq key value and remove the key if its 0   | o(n+m) | o(m) |
| Variant 1 | [Intersection_of_Two_Arrays.py](./Intersection_of_Two_Arrays.py) | Do the same approach as above ,but this time remove the key not decrement since no duplicate is allowed | o(n+m) | o(n)|
| Variant 2 | [union_of_Two_array.py](./union_of_Two_array.py) | insert element from both array to set and convert set to list | o(n+m) | o(n+m) |
| Variant 3 | [Find_Common_characters.py](./Find_Common_characters.py) | build freq for each char in each word and compare the current freq with the previous and take the min value across the keys in both freq  | o(n*m) | o(l) |
| Variant 4 | [Intersection_of_Three_sorted_array.py](./Intersection_of_Three_sorted_array.py) | three pointer and increment others with respect to one pointer and check everything is equal or not and increment the base pointer | o(len1+len2+len3) | o(min(len1,len2,len3)) |

---