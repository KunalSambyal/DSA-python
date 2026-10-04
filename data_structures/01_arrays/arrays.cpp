// arrays.cpp
/**
 * Core guide to Vectors (Dynamic Arrays) in C++ for CP and DSA.
 * Covers:
 * 1. C++ std::vector Basics (Creation, Sizing, and Core Methods)
 * 2. Elementary Array Operations (Insertions, Deletions, Traversal)
 * 3. Essential Array Algorithms (Min/Max, Search, and Reverse)
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <string>

// =====================================================================
// 1. C++ std::vector Basics (Dynamic Arrays)
// =====================================================================
void demoVectorBasics()
{
    std::cout << std::string(60, '=') << "\n";
    std::cout << " 1. C++ VECTOR CREATION & METHODS \n";
    std::cout << std::string(60, '=') << "\n";

    // Creation Methods
    std::vector<int> vecLit = {1, 2, 3, 4, 5};
    std::vector<int> vecRep(5, 0); // 5 elements initialized to 0

    std::cout << "Literal vector: ";
    for (int x : vecLit)
        std::cout << x << " ";
    std::cout << "\nRepeated values: ";
    for (int x : vecRep)
        std::cout << x << " ";
    std::cout << "\n";

    // Core vector methods
    std::vector<int> vec = {10, 20, 30};
    vec.push_back(40); // Append to end
    std::cout << "\nAfter push_back(40): ";
    for (int x : vec)
        std::cout << x << " ";

    vec.pop_back(); // Pop from end
    std::cout << "\nAfter pop_back(): ";
    for (int x : vec)
        std::cout << x << " ";

    vec.insert(vec.begin() + 1, 15); // Insert 15 at index 1
    std::cout << "\nAfter insert(begin() + 1, 15): ";
    for (int x : vec)
        std::cout << x << " ";

    vec.erase(vec.begin() + 1); // Erase element at index 1
    std::cout << "\nAfter erase(begin() + 1): ";
    for (int x : vec)
        std::cout << x << " ";

    std::reverse(vec.begin(), vec.end()); // Reverse in-place
    std::cout << "\nAfter reverse(): ";
    for (int x : vec)
        std::cout << x << " ";

    std::sort(vec.begin(), vec.end()); // Sort in-place
    std::cout << "\nAfter sort(): ";
    for (int x : vec)
        std::cout << x << " ";
    std::cout << "\n";
}

// =====================================================================
// 2. Elementary Array Operations
// =====================================================================
void insertAtStart(std::vector<int> &arr, int element)
{
    arr.insert(arr.begin(), element);
}

void insertAtEnd(std::vector<int> &arr, int element)
{
    arr.push_back(element);
}

void insertAtIndex(std::vector<int> &arr, int index, int element)
{
    if (index < 0 || index > static_cast<int>(arr.size()))
    {
        throw std::out_of_range("Index out of bounds");
    }
    arr.insert(arr.begin() + index, element);
}

int deleteFromStart(std::vector<int> &arr)
{
    if (arr.empty())
    {
        throw std::out_of_range("Cannot delete from an empty array");
    }
    int firstVal = arr.front();
    arr.erase(arr.begin());
    return firstVal;
}

int deleteFromEnd(std::vector<int> &arr)
{
    if (arr.empty())
    {
        throw std::out_of_range("Cannot delete from an empty array");
    }
    int lastVal = arr.back();
    arr.pop_back();
    return lastVal;
}

int deleteByIndex(std::vector<int> &arr, int index)
{
    if (index < 0 || index >= static_cast<int>(arr.size()))
    {
        throw std::out_of_range("Index out of bounds");
    }
    int val = arr[index];
    arr.erase(arr.begin() + index);
    return val;
}

void traverseArray(const std::vector<int> &arr)
{
    for (int i = 0; i < static_cast<int>(arr.size()); ++i)
    {
        std::cout << "  Index " << i << " -> " << arr[i] << "\n";
    }
}

void demoElementaryOperations()
{
    std::cout << "\n"
              << std::string(60, '=') << "\n";
    std::cout << " 2. ELEMENTARY ARRAY OPERATIONS \n";
    std::cout << std::string(60, '=') << "\n";

    std::vector<int> arr = {10, 20, 30, 40};
    std::cout << "Initial Array: ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    insertAtStart(arr, 5);
    std::cout << "After insertAtStart(5): ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    insertAtEnd(arr, 50);
    std::cout << "After insertAtEnd(50): ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    insertAtIndex(arr, 2, 15);
    std::cout << "After insertAtIndex(2, 15): ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    int poppedFirst = deleteFromStart(arr);
    std::cout << "After deleteFromStart() [removed " << poppedFirst << "]: ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    int poppedLast = deleteFromEnd(arr);
    std::cout << "After deleteFromEnd() [removed " << poppedLast << "]: ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    int poppedMid = deleteByIndex(arr, 1);
    std::cout << "After deleteByIndex(1) [removed " << poppedMid << "]: ";
    for (int x : arr)
        std::cout << x << " ";
    std::cout << "\n";

    std::cout << "Traversal:\n";
    traverseArray(arr);
}

// =====================================================================
// 3. Essential Array Algorithms
// =====================================================================
int findMinimum(const std::vector<int> &arr)
{
    if (arr.empty())
    {
        throw std::invalid_argument("Array is empty");
    }
    int minVal = arr[0];
    for (int num : arr)
    {
        if (num < minVal)
        {
            minVal = num;
        }
    }
    return minVal;
}

int linearSearch(const std::vector<int> &arr, int target)
{
    for (int i = 0; i < static_cast<int>(arr.size()); ++i)
    {
        if (arr[i] == target)
        {
            return i;
        }
    }
    return -1;
}

int binarySearch(const std::vector<int> &arr, int target)
{
    int low = 0;
    int high = static_cast<int>(arr.size()) - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return -1;
}

void reverseArrayInPlace(std::vector<int> &arr)
{
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;

    while (left < right)
    {
        std::swap(arr[left], arr[right]);
        ++left;
        --right;
    }
}

void demoArrayAlgorithms()
{
    std::cout << "\n"
              << std::string(60, '=') << "\n";
    std::cout << " 3. ESSENTIAL ARRAY ALGORITHMS \n";
    std::cout << std::string(60, '=') << "\n";

    std::vector<int> data = {42, 7, 19, 88, 3, 55};
    std::cout << "Original Data: ";
    for (int x : data)
        std::cout << x << " ";
    std::cout << "\n";

    // Min Value
    std::cout << "Minimum Value: " << findMinimum(data) << "\n";

    // Linear Search
    std::cout << "Linear Search (Find 88): Index " << linearSearch(data, 88) << "\n";

    // Binary Search
    std::vector<int> sortedData = data;
    std::sort(sortedData.begin(), sortedData.end());
    std::cout << "Sorted Data for Binary Search: ";
    for (int x : sortedData)
        std::cout << x << " ";
    std::cout << "\n";
    std::cout << "Binary Search (Find 88): Index " << binarySearch(sortedData, 88) << "\n";

    // In-place Reversal
    reverseArrayInPlace(data);
    std::cout << "Data after in-place reversal: ";
    for (int x : data)
        std::cout << x << " ";
    std::cout << "\n";
}

int main()
{
    demoVectorBasics();
    demoElementaryOperations();
    demoArrayAlgorithms();
    return 0;
}
