# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 02/04/2026
# Description: Implementation of Box class and insertion sort algorithm to organize
#              Box objects by descending volume order


class Box:
    """Represents a three-dimensional box with measurable dimensions."""
    
    def __init__(self, length, width, height):
        """
        Create a new Box instance.
        
        Parameters:
            length: The length dimension of the box
            width: The width dimension of the box
            height: The height dimension of the box
        """
        self._length = length
        self._width = width
        self._height = height
    
    def volume(self):
        """Calculate and return the box's volume (length × width × height)."""
        return self._length * self._width * self._height
    
    def get_length(self):
        """Retrieve the box's length."""
        return self._length
    
    def get_width(self):
        """Retrieve the box's width."""
        return self._width
    
    def get_height(self):
        """Retrieve the box's height."""
        return self._height


def box_sort(box_list):
    """
    Apply insertion sort to arrange Box objects in descending volume order.
    The original list is modified in place rather than creating a new list.
    
    Parameters:
        box_list: List containing Box objects to be sorted
    """
    for index in range(1, len(box_list)):
        key_box = box_list[index]
        position = index
        
        # Shift elements with lesser volumes rightward
        while position > 0 and box_list[position - 1].volume() < key_box.volume():
            box_list[position] = box_list[position - 1]
            position -= 1
        
        # Insert the key box at its correct position
        box_list[position] = key_box
