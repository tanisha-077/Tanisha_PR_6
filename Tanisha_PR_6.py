
import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open(self.filename, "x") as file:
                    file.write("[" + time + "]\n" + entry + "\n\n")

            except FileExistsError:
                with open(self.filename, "a") as file:
                    file.write("[" + time + "]\n" + entry + "\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Journal Entries:")
                print(file.read())

        except FileNotFoundError:
            print("Journal file does not exist. Add an entry first.")

        except PermissionError:
            print("Permission denied!")

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                data = file.read()

            found = False

            for entry in data.split("\n\n"):
                if keyword.lower() in entry.lower():
                    print(entry)
                    found = True

            if not found:
                print("No matching entries found.")

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print("Permission denied!")

    def delete_entries(self):
        try:
            choice = input("Are you sure? (yes/no): ")

            if choice.lower() == "yes":
                with open(self.filename, "w") as file:
                    file.write("")

                os.remove(self.filename)
                print("All entries deleted successfully!")

            else:
                print("Delete cancelled.")

        except FileNotFoundError:
            print("No journal entries to delete.")

        except PermissionError:
            print("Permission denied!")

    def menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager.")
                print("Goodbye!")
                break

            else:
                print("Invalid option. Try again.")

journal = JournalManager()

journal.menu()