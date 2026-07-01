# basic_hashing.py
"""
Introduction to Hashing for DSA in Python.
Covers:
1. Counting frequencies of array elements using dictionaries (Hash Maps)
2. Finding the highest and lowest frequency elements
3. Concept of query lookups in O(1) time
"""

def count_frequencies(arr):
    """Counts the occurrences of each element in an array using a hash map."""
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    return freq_map

def find_highest_lowest_frequency(freq_map):
    """Finds elements with the highest and lowest frequency from a frequency map."""
    if not freq_map:
        return None, None
        
    highest_freq = -1
    lowest_freq = float('inf')
    
    highest_element = None
    lowest_element = None
    
    for element, count in freq_map.items():
        if count > highest_freq:
            highest_freq = count
            highest_element = element
        if count < lowest_freq:
            lowest_freq = count
            lowest_element = element
            
    return (highest_element, highest_freq), (lowest_element, lowest_freq)

def demo_hashing():
    print("=" * 60)
    print(" BASIC HASHING FOR DSA ")
    print("=" * 60)
    
    data = [10, 5, 10, 15, 10, 5, 20, 10, 15]
    print(f"Input Array: {data}")
    
    # 1. Frequency mapping
    freq_map = count_frequencies(data)
    print(f"Frequency Map: {freq_map}")
    
    # 2. Query lookup demonstration
    query = 15
    print(f"Query '{query}' count: {freq_map.get(query, 0)}")
    
    # 3. Min/Max frequency elements
    highest, lowest = find_highest_lowest_frequency(freq_map)
    print(f"\nHighest Frequency Element: {highest[0]} (frequency: {highest[1]})")
    print(f"Lowest Frequency Element: {lowest[0]} (frequency: {lowest[1]})")

if __name__ == "__main__":
    demo_hashing()
