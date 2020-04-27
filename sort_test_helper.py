import numpy as np

def sort_test_helper(fn):
    for _ in range(5):
        l = np.random.randint(5, 10)
        A = np.random.randint(0, 10, l)
        print(f"Before sort: {A}")
        A_sorted = fn(A)
        print(f"After sort : {A_sorted}")

        assert np.allclose(A_sorted, np.sort(A))
