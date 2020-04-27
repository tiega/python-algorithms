from sort_test_helper import sort_test_helper

def merge(arr: list, l: int, m: int, r: int) -> None:
    temp = []
    left_arr = arr[l:m+1]
    right_arr = arr[m+1:r+1]
    l_ = 0
    r_ = 0
    
    # Merge two arrays
    while l_ < len(left_arr) and r_ < len(right_arr):
        if left_arr[l_] < right_arr[r_]:
            temp.append(left_arr[l_])
            l_ += 1
        else:
            temp.append(right_arr[r_])
            r_ += 1

    # Copy remaining over
    while l_ < len(left_arr):
        temp.append(left_arr[l_])
        l_ += 1

    while r_ < len(right_arr):
        temp.append(right_arr[r_])
        r_ += 1

    for i, v in enumerate(temp):
        arr[l+i] = v


def merge_sort_helper(arr: list, l: int, r: int) -> None:
    if l < r:
        m = int(l + (r-l)//2)
        merge_sort_helper(arr, l, m)
        merge_sort_helper(arr, m+1, r)
        merge(arr, l, m, r)


def merge_sort(arr: list) -> list:
    merge_sort_helper(arr, 0, len(arr)-1)
    return arr


if __name__ == "__main__":
    sort_test_helper(merge_sort)

