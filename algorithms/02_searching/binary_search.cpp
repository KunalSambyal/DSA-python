// binary_search.cpp
/**
 * Binary Search implementations in C++.
 * Covers:
 * 1. Iterative Binary Search
 * 2. Recursive Binary Search
 *
 * Time Complexity: O(1) best case, O(log N) average and worst case
 * Space Complexity: O(1) for iterative, O(log N) for recursive call stack
 */

#include <iostream>
#include <vector>

// =====================================================================
// 1. Iterative Binary Search
// =====================================================================
int binarySearchIterative(const std::vector<int> &arr, int target)
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

// =====================================================================
// 2. Recursive Binary Search
// =====================================================================
int binarySearchRecursiveHelper(const std::vector<int> &arr, int target, int low, int high)
{
    if (low > high)
    {
        return -1;
    }

    int mid = low + (high - low) / 2;
    if (arr[mid] == target)
    {
        return mid;
    }
    else if (arr[mid] < target)
    {
        return binarySearchRecursiveHelper(arr, target, mid + 1, high);
    }
    else
    {
        return binarySearchRecursiveHelper(arr, target, low, mid - 1);
    }
}

int binarySearchRecursive(const std::vector<int> &arr, int target)
{
    return binarySearchRecursiveHelper(arr, target, 0, static_cast<int>(arr.size()) - 1);
}

void demoIterativeSearch()
{
    std::cout << std::string(60, '=') << "\n";
    std::cout << " 1. ITERATIVE BINARY SEARCH \n";
    std::cout << std::string(60, '=') << "\n";

    std::vector<int> data = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int target = 23;

    std::cout << "Array: ";
    for (int num : data)
        std::cout << num << " ";
    std::cout << "\nTarget: " << target << "\n";

    int result = binarySearchIterative(data, target);
    std::cout << "Target found at index: " << result << "\n\n";

    int targetMissing = 50;
    std::cout << "Target: " << targetMissing << "\n";
    int resultMissing = binarySearchIterative(data, targetMissing);
    std::cout << "Target found at index: " << resultMissing << "\n";
}

void demoRecursiveSearch()
{
    std::cout << "\n"
              << std::string(60, '=') << "\n";
    std::cout << " 2. RECURSIVE BINARY SEARCH \n";
    std::cout << std::string(60, '=') << "\n";

    std::vector<int> data = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int target = 23;

    std::cout << "Array: ";
    for (int num : data)
        std::cout << num << " ";
    std::cout << "\nTarget: " << target << "\n";

    int result = binarySearchRecursive(data, target);
    std::cout << "Target found at index: " << result << "\n\n";

    int targetMissing = 50;
    std::cout << "Target: " << targetMissing << "\n";
    int resultMissing = binarySearchRecursive(data, targetMissing);
    std::cout << "Target found at index: " << resultMissing << "\n";
}

int main()
{
    demoIterativeSearch();
    demoRecursiveSearch();
    return 0;
}
