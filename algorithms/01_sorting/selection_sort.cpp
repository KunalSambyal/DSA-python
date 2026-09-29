// selection_sort.cpp
/**
 * Selection Sort implementation in C++.
 * Time Complexity: O(N^2) best, average, and worst case
 * Space Complexity: O(1) auxiliary space
 */

#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            std::swap(arr[i], arr[minIdx]);
        }
    }
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};

    std::cout << "Array before sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    selectionSort(arr);

    std::cout << "Array after sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    return 0;
}
