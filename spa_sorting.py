# Name: Abhay Kumar
# Roll No.: 2501730185
# Section: A

import random
import time


# INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# QUICK SORT 
def partition(arr, low, high):
    # Random pivot to avoid worst case
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)

        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1


# TIME MEASUREMENT
def measure_time(sort_func, arr, is_quick=False):
    temp_arr = arr.copy()

    start = time.perf_counter()

    if is_quick:
        sort_func(temp_arr, 0, len(temp_arr) - 1)
    else:
        sort_func(temp_arr)

    end = time.perf_counter()

    return end - start


# DATASET GENERATOR
def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = []

    for size in sizes:
        random_data = [random.randint(1, 10000) for _ in range(size)]
        datasets.append(("Random", size, random_data))

        sorted_data = sorted(random_data)
        datasets.append(("Sorted", size, sorted_data))

        reverse_data = sorted_data[::-1]
        datasets.append(("Reverse", size, reverse_data))

    return datasets


# MAIN
def main():
    datasets = generate_datasets()
    results = []

    print("\nRunning Sorting Performance Analyzer...\n")

    for dtype, size, data in datasets:
        print(f"Processing: {dtype} | Size: {size}")

        insertion_time = measure_time(insertion_sort, data)
        merge_time = measure_time(merge_sort, data)
        quick_time = measure_time(quick_sort, data, is_quick=True)

        results.append((size, dtype, insertion_time, merge_time, quick_time))

    # Display
    print("\nRESULTS:\n")
    print(f"{'Size':<8}{'Type':<10}{'Insertion':<15}{'Merge':<15}{'Quick':<15}")

    for r in results:
        print(f"{r[0]:<8}{r[1]:<10}{r[2]:<15.6f}{r[3]:<15.6f}{r[4]:<15.6f}")

    # Save to file
    with open("output.txt", "w") as f:
        f.write("Sorting Performance Results\n\n")
        f.write(f"{'Size':<8}{'Type':<10}{'Insertion':<15}{'Merge':<15}{'Quick':<15}\n")

        for r in results:
            f.write(f"{r[0]:<8}{r[1]:<10}{r[2]:<15.6f}{r[3]:<15.6f}{r[4]:<15.6f}\n")

    print("\nResults saved to output.txt")


# RUN
if __name__ == "__main__":
    main()