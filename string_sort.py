# Author: Samuel Baird
# Assignment 5b
# GitHub username: OSU_S13BAIRD
# Date: 10/27/2025
# Description: Function that sorts a list of strings in place using insertion sort (case-insensitive)

def string_sort(string_list):
    """
    Sort a list of strings in place using insertion sort.
    Sorting ignores case (case-insensitive).
    
    Args:
        string_list: A list of strings to be sorted
    """
    for i in range(1, len(string_list)):
        current_string = string_list[i]
        current_lower = current_string.lower()
        j = i - 1
        
        # Move strings that are greater (ignoring case) to the right
        while j >= 0 and string_list[j].lower() > current_lower:
            string_list[j + 1] = string_list[j]
            j -= 1
        
        string_list[j + 1] = current_string
