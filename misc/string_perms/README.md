# String Permutations

Problem Statement: Given a string s. Return a list of all permutations of s
Example: Input "abc" outputs: ["abc", "acb", "bac", "bca", "cab", "cba"]

### Approach
- recursive 
  1. break into substring by systematically removing a char
  2. get all perms of substring - return if substring has length 1
  3. concat removed char with returned perms of substring

### Complexity
```
T(n) = n*T(n-1)
     = n*[n-1*T(n-2)]
     = n*[n-1*[n-2*T(n-3)]]
     .
     .
     .
     = n*n-1*n-2*...*1
=> O(n!)
```
