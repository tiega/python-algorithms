from sort_test_helper import sort_test_helper

def bubble_sort(arr: list):
    # Bubble sort in-place
    # Time complexity: O(n)
    n = len(arr)
    for i in range(n):
        did_swap = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = True
        if not did_swap:
            break
    return arr
    

if __name__ == "__main__":
    sort_test_helper(bubble_sort)
