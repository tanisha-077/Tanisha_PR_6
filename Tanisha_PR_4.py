dataset = []
summary = {}


def input_data():
    """Take 1D list data from the user."""
    global dataset

    print("\n    Input Data")

    n = int(input("Enter number of elements: "))
    dataset = []

    for i in range(n):
        value = int(input("Enter value " + str(i + 1) + ": "))
        dataset.append(value)

    print("Data has been stored successfully!")


def display_summary():
    """Display basic statistics using built-in functions."""
    global summary

    total = len(dataset)
    minimum = min(dataset)
    maximum = max(dataset)
    total_sum = sum(dataset)
    average = total_sum / total

    summary = {
        "Total": total,
        "Minimum": minimum,
        "Maximum": maximum,
        "Sum": total_sum,
        "Average": average
    }

    print("\nData Summary:")
    print("- Total elements:", total)
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total_sum)
    print("- Average value:", round(average, 2))


def factorial(n):
    """Calculate factorial using recursion."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def filter_data():
    """Filter data using lambda function."""

    threshold = int(input("Enter a threshold value: "))

    result = list(filter(lambda x: x >= threshold, dataset))

    print("Filtered Data (values >= " + str(threshold) + "):", end=" ")

    for i in range(len(result)):
        print(result[i], end="")

        if i < len(result) - 1:
            print(", ", end="")

    print()


def sort_data():
    """Sort data in ascending or descending order."""

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    new_data = dataset.copy()

    if choice == 1:
        new_data.sort()
        print("Sorted Data in Ascending Order:", end=" ")

    elif choice == 2:
        new_data.sort(reverse=True)
        print("Sorted Data in Descending Order:", end=" ")

    else:
        print("Invalid choice!")
        return

    for i in range(len(new_data)):
        print(new_data[i], end="")

        if i < len(new_data) - 1:
            print(", ", end="")

    print()


def statistics(*args, **kwargs):
    """Return multiple statistics using args and kwargs."""

    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    if "name" in kwargs:
        print("Dataset Name:", kwargs["name"])

    return minimum, maximum, total, average


def display_statistics():
    """Display dataset statistics using multiple return values."""

    minimum, maximum, total, average = statistics(
        *dataset,
        name="My Dataset"
    )

    print("\nDataset Statistics:")
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total)
    print("- Average value:", round(average, 2))


def show_comment():
    """Display documentation of all user-defined functions."""

    print("\n--- Function Documentation ---")

    print("input_data:", input_data.__doc__)
    print("display_summary:", display_summary.__doc__)
    print("factorial:", factorial.__doc__)
    print("filter_data:", filter_data.__doc__)
    print("sort_data:", sort_data.__doc__)
    print("statistics:", statistics.__doc__)
    print("display_statistics:", display_statistics.__doc__)

print("Welcome to the Data Analyzer and Transformer Program")

show_comment()

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:

        input_data()

    elif choice == 2:

        if len(dataset) == 0:
            print("Please input data first.")
        else:
            display_summary()

    elif choice == 3:

        number = int(input("Enter a number to calculate its factorial: "))

        if number < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            print("Factorial of", number, "is:", factorial(number))

    elif choice == 4:

        if len(dataset) == 0:
            print("Please input data first.")
        else:
            filter_data()

    elif choice == 5:

        if len(dataset) == 0:
            print("Please input data first.")
        else:
            sort_data()

    elif choice == 6:

        if len(dataset) == 0:
            print("Please input data first.")
        else:
            display_statistics()

    elif choice == 7:

        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:

        print("Invalid choice! Please try again.")