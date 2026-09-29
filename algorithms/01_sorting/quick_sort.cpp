// quick_sort.cpp
/**
 * Quick Sort implementation in C++.
 * Time Complexity: O(N log N) best and average case, O(N^2) worst case
 * Space Complexity: O(log N) auxiliary space for call stack
 */

#include <iostream>
#include <vector>

int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortHelper(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortHelper(arr, low, pi - 1);
        quickSortHelper(arr, pi + 1, high);
    }
}

void quickSort(std::vector<int>& arr) {
    if (!arr.empty()) {
        quickSortHelper(arr, 0, static_cast<int>(arr.size()) - 1);
    }
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};

    std::cout << "Array before sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    quickSort(arr);

    std::cout << "Array after sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    return 0;
}
