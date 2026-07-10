# LeetCode #49: Group Anagrams (Medium)

[Problem Link](https://leetcode.com/problems/group-anagrams/)

## Analysis

The problem asks us to group an array of strings `strs` such that all anagrams (words formed by rearranging the letters of another word) are clustered together in lists.

---

## Brute Force Approach

Iterate through the list of words. For each word that has not been grouped yet, compare it against all subsequent ungrouped words. Check if they are anagrams of each other. If they are, add them to the same group.

### Algorithm

```python
def isAnagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    n = len(strs)
    visited = [False] * n
    result = []
    
    for i in range(n):
        if visited[i]:
            continue
        current_group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and isAnagram(strs[i], strs[j]):
                current_group.append(strs[j])
                visited[j] = True
        result.append(current_group)
        
    return result
```

### Complexity

- **Time Complexity:** **O(N^2 * K log K)** where **N** is the number of strings, and **K** is the max length of a string, due to the nested comparison loops and sorting.
- **Space Complexity:** **O(N)** auxiliary space for the `visited` array (excluding output space).

---

## Optimized Approach (Using Hash Map with Sorted Keys)

Instead of comparing every pair of strings, we can sort the characters of each string to produce a unique signature (key). All anagrams will share the same sorted string signature. We store them in a hash map where the sorted string is the key, and the value is a list of original strings.

### Algorithm

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = defaultdict(list)
        
        for word in strs:
            sorted_key = "".join(sorted(word))
            anagrams_map[sorted_key].append(word)
            
        return list(anagrams_map.values())
```

### Complexity

- **Time Complexity:** **O(N * K log K)** where **N** is the number of strings, and **K** is the max length of a string, since we sort each string of length **K**.
- **Space Complexity:** **O(N * K)** to store the hash map containing all elements.
