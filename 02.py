
class MergeSort:
    """Class for merge functions"""
    def merge_k_lists(self, arr):
        """Merging a list of lists"""
        if len(arr) <= 1:
            return self.merge_sort(arr[0])

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return self.merge(self.merge_k_lists(left_half), self.merge_k_lists(right_half))

    def merge_sort(self, arr):
        """Merging a list"""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return self.merge(self.merge_sort(left_half), self.merge_sort(right_half))

    def merge(self, left, right):
        """Merging a left list and a right list into one"""
        merged = []

        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index+=1
            else:
                merged.append(right[right_index])
                right_index+=1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6], [9, 12, 4]]
    print(MergeSort().merge_k_lists(lists))
