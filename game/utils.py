"""
Utility functions
"""
import time


def formatted_time(timer: float) -> str:
    """
    Formats the elapsed time in seconds into a string in the format "MM:SS".

    Args:
        timer (float): The elapsed time in seconds.

    Returns:
        str: The formatted time string in the format "MM:SS".
    """
    elapsed_time = time.gmtime(time.perf_counter() - timer)
    return time.strftime("%M:%S", elapsed_time)
