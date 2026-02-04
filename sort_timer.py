# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 02/04/2026
# Description: Timing comparison of bubble sort vs insertion sort performance

import time
import random
from matplotlib import pyplot


def bubble_time(data_list):
    """
    Times how long bubble sort takes to sort the list.
    """
    begin = time.perf_counter()
    
    # Standard bubble sort implementation
    for outer in range(len(data_list) - 1):
        for inner in range(len(data_list) - outer - 1):
            if data_list[inner] > data_list[inner + 1]:
                # Swap elements
                temp = data_list[inner]
                data_list[inner] = data_list[inner + 1]
                data_list[inner + 1] = temp
    
    finish = time.perf_counter()
    return finish - begin


def insertion_time(data_list):
    """
    Times how long insertion sort takes to sort the list.
    """
    begin = time.perf_counter()
    
    # Standard insertion sort
    for slot in range(1, len(data_list)):
        key = data_list[slot]
        position = slot - 1
        
        while position >= 0 and data_list[position] > key:
            data_list[position + 1] = data_list[position]
            position -= 1
        
        data_list[position + 1] = key
    
    finish = time.perf_counter()
    return finish - begin


def sort_times_for_random_list(n):
    """
    Generates a random list of n integers (1 to n) and times both sorts.
    Returns tuple of (bubble_time, insertion_time).
    """
    # Build random list
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(1, n))
    
    # Make a copy for the second sort
    duplicate_list = list(original_list)
    
    # Time both algorithms
    bubble_elapsed = bubble_time(original_list)
    insertion_elapsed = insertion_time(duplicate_list)
    
    return (bubble_elapsed, insertion_elapsed)


def compare_sorts():
    """
    Generates performance graph comparing bubble sort and insertion sort
    across different list sizes.
    """
    # Test these list sizes
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    
    bubble_results = []
    insertion_results = []
    
    # Run timing tests
    print("Running performance tests...")
    for size in sizes:
        b_time, i_time = sort_times_for_random_list(size)
        bubble_results.append(b_time)
        insertion_results.append(i_time)
        print(f"  Completed {size} elements - Bubble: {b_time:.4f}s, Insertion: {i_time:.4f}s")
    
    # Build the graph
    pyplot.figure(figsize=(12, 7))
    pyplot.style.use('seaborn-v0_8-darkgrid')
    
    pyplot.plot(sizes, bubble_results, 'bs-', linewidth=2.5, 
                markersize=8, label='Bubble Sort', alpha=0.8)
    pyplot.plot(sizes, insertion_results, 'md-', linewidth=2.5, 
                markersize=8, label='Insertion Sort', alpha=0.8)
    
    pyplot.xlabel('List Size (Number of Elements)', fontsize=13, fontweight='bold')
    pyplot.ylabel('Execution Time (seconds)', fontsize=13, fontweight='bold')
    pyplot.title('Sorting Algorithm Performance Comparison\nBubble Sort vs Insertion Sort', 
                 fontsize=15, fontweight='bold', pad=20)
    pyplot.legend(loc='upper left', fontsize=11, framealpha=0.9, shadow=True)
    pyplot.grid(True, alpha=0.3)
    pyplot.tight_layout()
    
    print("\nDisplaying graph...")
    pyplot.show()


def main():
    """Runs the sort comparison."""
    compare_sorts()


if __name__ == "__main__":
    main()
