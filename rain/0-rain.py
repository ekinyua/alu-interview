#!/usr/bin/python3
"""Rain. """
"""
    Calculates the amount of water retained between walls after it rains.

    Args:
    walls: A list of non-negative integers representing the heights of walls
    with unit width 1, as if viewing the cross-section of a relief map.

    Returns:
    An integer indicating the total amount of rainwater
    retained between the walls.
"""


def rain(walls):
    """calculate how much water will be retained after it rains"""
    if not walls or len(walls) < 3:
        return 0
    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water += min(left, right) - walls[i]
    return water
