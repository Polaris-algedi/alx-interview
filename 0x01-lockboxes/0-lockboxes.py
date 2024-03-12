#!/usr/bin/python3

"""
This module provides a function canUnlockAll that determines if all boxes
can be opened using the provided keys in a given configuration.
"""

def canUnlockAll(boxes):
  """
  This function checks if all boxes can be opened using the provided keys
  using Depth-First Search (DFS) algorithm.

  Args:
      boxes: A list of lists, where each inner list represents the keys found in a box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """
  # Track visited boxes
  visited_boxes = [0]

  # Track keys to explore (LIFO - stack behavior)
  keys_to_explore = [0]

  while keys_to_explore:
    # Get the next key to explore
    current_key = keys_to_explore.pop()

    # Check keys available in the box associated with the current key
    for key in boxes[current_key]:
      if key not in visited_boxes:
        visited_boxes.append(key)
        keys_to_explore.append(key)

  # All boxes unlocked if the number of visited boxes matches the total number of boxes
  return len(visited_boxes) == len(boxes)
