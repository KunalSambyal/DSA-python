// bubble_sort.cpp
/**
 * Bubble Sort implementation in C++.
 * Time Complexity: O(N) best case, O(N^2) average and worst case
 * Space Complexity: O(1) auxiliary space
 */

#include <iostream>
#include <vector>

void bubbleSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = n - 1; i >= 0; --i) {
        bool didSwap = false;
        for (int j = 0; j < i; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                didSwap = true;
            }
        }
        if (!didSwap) {
            break;
        }
    }
}

int main() {
    std::vector<int> arr = {64, -34, 25, 12, 22, 11, 90};

    std::cout << "Array before sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    bubbleSort(arr);

    std::cout << "Array after sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    return 0;
}
