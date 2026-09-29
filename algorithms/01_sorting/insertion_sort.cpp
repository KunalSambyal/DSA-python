// insertion_sort.cpp
/**
 * Insertion Sort implementation in C++.
 * Time Complexity: O(N) best case, O(N^2) average and worst case
 * Space Complexity: O(1) auxiliary space
 */

#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};

    std::cout << "Array before sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    insertionSort(arr);

    std::cout << "Array after sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    return 0;
}
