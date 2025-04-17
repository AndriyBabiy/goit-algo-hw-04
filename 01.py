import timeit
import random

class Sorting:
    """Class for collectively interacting with sorting functions"""
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return self.merge(self.merge_sort(left_half), self.merge_sort(right_half))

    def merge(self, left, right):
        """Merges sub-elements of merge_sort"""
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    def insertion_sort(self, arr):
        arr = arr[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

def timed(func, func_name = ""):
    """Timing the function and returning the amount of time taken"""
    print(f'{func_name}: \
          {timeit.timeit(f"{func}", setup="from __main__ import arr, Sorting")} seconds, \
            {func if len(func)<30 else ""}')

if __name__ == "__main__":
    random.seed(42)
    arr = random.choices(range(100), k=10000)
    # print(arr)
    timed(Sorting().merge_sort(arr), "merge_sort")
    timed(Sorting().insertion_sort(arr), "insertion_sort")
    timed(sorted(arr), "timsort")
