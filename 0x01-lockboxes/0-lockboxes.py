#!/usr/bin/python3

"""
This module provides a function canUnlockAll that determines if all boxes
can be opened using the provided keys in a given configuration.
"""


# Using Depth-First Search (DFS) algorithm.
def canUnlockAll(boxes):
    """
    This function checks if all boxes can be opened using the provided keys

    Args:
        boxes: A list of lists, where each inner list represents
        the keys found in a box.

    Returns: True if all boxes can be opened, False otherwise.
    """
    # Track visited boxes
    visited_boxes = [0]

    # Track keys to explore (LIFO - stack behavior)
    keys_to_explore = [0]

    boxes_num = len(boxes)

    while keys_to_explore:
        # Get the next key to explore
        current_key = keys_to_explore.pop()

        # Check keys available in the box associated with the current key
        for key in boxes[current_key]:
            if key not in visited_boxes and key < boxes_num:
                visited_boxes.append(key)
                keys_to_explore.append(key)

    return len(visited_boxes) == boxes_num


# Using Breadth-First Search (BFS) algorithm.

# from collections import deque

# def canUnlockAll(boxes):
#     """
#     This function checks if all boxes can be opened using the provided keys
#     using Breadth-First Search (BFS) algorithm.

#     Args:
#         boxes: A list of lists, where each inner list represents
#         the keys found in a box.

#     Returns: True if all boxes can be opened, False otherwise.
#     """
#     # Track visited boxes
#     visited_boxes = [0]

#     # Track keys to explore (FIFO - stack behavior)
#     keys_to_explore = deque()
#     keys_to_explore.append(0)

#     boxes_num = len(boxes)

#     while keys_to_explore:
#         # Get the next key to explore
#         current_key = keys_to_explore.popleft()
#         print(f'Exploring key for box number: {current_key}')

#         # Check keys available in the box associated with the current key
#         for key in boxes[current_key]:
#             if key not in visited_boxes and key < boxes_num:
#                 visited_boxes.append(key)
#                 keys_to_explore.append(key)

#     return len(visited_boxes) == boxes_num
