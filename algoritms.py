import random
import time
import matplotlib.pyplot as plt

# Генерация случайного списка чисел
def generate_random_list(size, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

# 1. Быстрая сортировка (O(n log n))
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 2. Сортировка слиянием (O(n log n))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. Пузырьковая сортировка (O(n^2))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 4. Сортировка вставками (O(n^2))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 5. Сортировка выбором (O(n^2))
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 6. Сортировка подсчётом (O(n + k))
def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)
    return sorted_arr

# 7. Пирамидальная сортировка (O(n log n))
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# 8. Сортировка Шелла (O(n log n) в среднем)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Линейный поиск (O(n))
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Бинарный поиск (O(log n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Измерение времени выполнения
def measure_time(func, arr, *args):
    start = time.time()
    result = func(arr, *args) if args else func(arr)
    return result, time.time() - start

# Визуализация времени работы алгоритмов
def plot_sorting_times(times):
    algorithms = list(times.keys())
    exec_times = list(times.values())

    plt.figure(figsize=(12, 6))
    plt.bar(algorithms, exec_times, color=['blue', 'green', 'red', 'purple', 'orange', 'brown', 'cyan', 'magenta'])
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.xticks(rotation=30)
    plt.grid(axis='y')
    plt.show()

# Главная функция
def main():
    size = 500  # Размер списка
    max_value = 1000
    random_list = generate_random_list(size, 0, max_value)

    # Измерение времени сортировки
    times = {}

    sorted_list, times["Quick Sort"] = measure_time(quick_sort, random_list)
    _, times["Merge Sort"] = measure_time(merge_sort, random_list)
    _, times["Bubble Sort"] = measure_time(bubble_sort, random_list.copy())
    _, times["Insertion Sort"] = measure_time(insertion_sort, random_list.copy())
    _, times["Selection Sort"] = measure_time(selection_sort, random_list.copy())
    _, times["Counting Sort"] = measure_time(counting_sort, random_list.copy(), max_value)
    _, times["Heap Sort"] = measure_time(heap_sort, random_list.copy())
    _, times["Shell Sort"] = measure_time(shell_sort, random_list.copy())

    for name, t in times.items():
        print(f"{name}: {t:.6f} sec")

    # Поиск элемента
    target = random.choice(sorted_list)
    lin_index, lin_time = measure_time(linear_search, sorted_list, target)
    bin_index, bin_time = measure_time(binary_search, sorted_list, target)

    print(f"Linear Search Time: {lin_time:.6f} sec, Found at index: {lin_index}")
    print(f"Binary Search Time: {bin_time:.6f} sec, Found at index: {bin_index}")

    # График времени сортировки
    plot_sorting_times(times)

if __name__ == "__main__":
    main()