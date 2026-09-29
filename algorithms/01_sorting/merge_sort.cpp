// merge_sort.cpp
/**
 * Merge Sort implementation in C++.
 * Time Complexity: O(N log N) best, average, and worst case
 * Space Complexity: O(N) auxiliary space
 */

#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int low, int mid, int high) {
    std::vector<int> temp;
    int left = low;
    int right = mid + 1;

    while (left <= mid && right <= high) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left++]);
        } else {
            temp.push_back(arr[right++]);
        }
    }

    while (left <= mid) {
        temp.push_back(arr[left++]);
    }

    while (right <= high) {
        temp.push_back(arr[right++]);
    }

    for (int i = low; i <= high; ++i) {
        arr[i] = temp[i - low];
    }
}

void mergeSortHelper(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;
        mergeSortHelper(arr, low, mid);
        mergeSortHelper(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

void mergeSort(std::vector<int>& arr) {
    if (!arr.empty()) {
        mergeSortHelper(arr, 0, static_cast<int>(arr.size()) - 1);
    }
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};

    std::cout << "Array before sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    mergeSort(arr);

    std::cout << "Array after sort: ";
    for (int num : arr) std::cout << num << " ";
    std::cout << "\n";

    return 0;
}
