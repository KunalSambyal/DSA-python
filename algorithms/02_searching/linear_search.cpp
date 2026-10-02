// linear_search.cpp
/**
 * Linear Search implementation in C++.
 * Covers:
 * 1. Linear Search Algorithm
 *
 * Time Complexity: O(1) best case, O(N) average and worst case
 * Space Complexity: O(1) auxiliary space
 */

#include <iostream>
#include <vector>

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

void demoLinearSearch()
{
    std::cout << std::string(60, '=') << "\n";
    std::cout << " 1. LINEAR SEARCH \n";
    std::cout << std::string(60, '=') << "\n";

    std::vector<int> data = {2, 12, 5, 8, -16, 23, -38, 56, 72, 91};
    int target = 23;

    std::cout << "Array: ";
    for (int num : data)
        std::cout << num << " ";
    std::cout << "\nTarget: " << target << "\n";

    int result = linearSearch(data, target);
    std::cout << "Target found at index: " << result << "\n\n";

    int targetMissing = 50;
    std::cout << "Target: " << targetMissing << "\n";
    int resultMissing = linearSearch(data, targetMissing);
    std::cout << "Target found at index: " << resultMissing << "\n";
}

int main()
{
    demoLinearSearch();
    return 0;
}
