print("        Welcome to LOGIC BOX")

while True:

    print("\n1. Pattern Generation")
    print("2. Number Analysis")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid number of rows!")
            break

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 2:

        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end <= start:
            print("End number must be greater than start number!")
            continue

        total = 0

        for i in range(start, end + 1):

            if i == 0:
                pass
            elif i % 2 == 0:
                print(i, "is Even")
            else:
                print(i, "is Odd")

            total = total + i

        print("The Sum is =", total)

    elif choice == 3:

        print("Thank you for using Logic Box!")
        break

    else:
        print("Invalid choice!")