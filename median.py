"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def med():
    while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
        except ValueError:
            print("Some input could not be converted to a number!")
        else:
            break

    numbers = sorted(numbers)

    med_val = (numbers[len(numbers) // 2]) if (len(numbers) & 1) else ((numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2)

    return med_val if len(numbers) > 0 else 0

print(med())
