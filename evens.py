def even_number_of_evens(numbers):
    """
    Suggested tests for test case
    1. should raise a TypeError if a list is not passed into the function
    2. if numbers is empty, return False
    3. if the number of even numbers is 0, return False
    4. if the number of even numbers is odd, return False
    5. if the number of even numbers is even, return True
    """

    if isinstance(numbers, list):
        # list comprehension used here instead of for loop
        evens = sum([1 for n in numbers if n % 2 == 0])

        # replaces if else statement into one line of code
        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens(5))
