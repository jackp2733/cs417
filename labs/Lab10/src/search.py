"""
Lab 10: Searching — From Linear Scan to Divide and Conquer

In this lab you will implement two search algorithms and then
create versions that count comparisons so you can measure
their performance.

Complete the four functions marked with TODO.
Do NOT change the function signatures.

Run tests:
    pytest -v
"""


# ── TODO 1: Sequential Search ────────────────────────────────────


def sequential_search(a_list, target):
    for item in a_list:
        if item == target:
            return True
    return False
   
    pass  # TODO: implement this


# ── TODO 2: Binary Search ────────────────────────────────────────


def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2
        mid_value = a_list[mid]

        if mid_value == target:
            return True
        elif target < mid_value:
            # target is in the left half
            last = mid - 1
        else:
            # target is in the right half
            first = mid + 1

    return False
    pass  # TODO: implement this


# ── TODO 3: Counted Versions ─────────────────────────────────────


def sequential_search_counted(a_list, target):
    comparisons = 0

    for item in a_list:
        comparisons += 1  # compare item to target
        if item == target:
            return True, comparisons

    # not found
    return False, comparisons
   
    pass  # TODO: implement this


def binary_search_counted(a_list, target):
    first = 0
    last = len(a_list) - 1
    comparisons = 0

    while first <= last:
        mid = (first + last) // 2
        mid_value = a_list[mid]

        # We are comparing this mid element to the target
        comparisons += 1

        if mid_value == target:
            return True, comparisons
        elif target < mid_value:
            last = mid - 1
        else:
            first = mid + 1

    return False, comparisons
    
    pass  # TODO: implement this
