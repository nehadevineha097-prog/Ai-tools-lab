def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, otherwise False.
    """
    return s == s[::-1]


def count_words(text):
    """Count the number of words in a text.

    Args:
        text: The text whose words should be counted.

    Returns:
        The number of words in the text.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        c: Temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.
    """
    return (c * 9 / 5) + 32