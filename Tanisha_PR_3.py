print("     Welcome to Student Data Organizer")

students = []

subjects_offered = set()

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n    Add Student ")

        stu_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth: ")

        print("\nEnter 3 subjects:")

        subject1 = input("Subject 1: ")
        subject2 = input("Subject 2: ")
        subject3 = input("Subject 3: ")

        subjects = [subject1, subject2, subject3]

        subjects_offered.update(subjects)

        student = {
            "student_id": stu_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == "2":

        print("\n    Display All Students")

        if len(students) == 0:

            print("No student records found.")

        else:

            for student in students:

                print("\nStudent ID: {}".format(student["stu_id"]))
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grade: {student['grade']}")
                print(f"Date of Birth: {student['dob']}")
                print(f"Subjects: {student['subjects']}")

    elif choice == "3":

        print("\n    Update Student Information")

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["student_id"] == student_id:

                print("\n1. Update Age")
                print("2. Update Grade")
                print("3. Update Subjects")

                update_choice = input("Enter your choice: ")

                if update_choice == "1":

                    student["age"] = int(input("Enter new age: "))

                    print("Age updated successfully!")

                elif update_choice == "2":

                    student["grade"] = input("Enter new grade: ")

                    print("Grade updated successfully!")

                elif update_choice == "3":

                    print("\nEnter new subjects:")

                    subject1 = input("Subject 1: ")
                    subject2 = input("Subject 2: ")
                    subject3 = input("Subject 3: ")

                    new_subjects = [subject1, subject2, subject3]

                    student["subjects"] = new_subjects

                    subjects_offered.update(new_subjects)

                    print("Subjects updated successfully!")

                else:

                    print("Invalid choice!")

                found = True
                break

        if found == False:

            print("Student ID not found!")

    elif choice == "4":

        print("\n     Delete Student ")

        student_id = input("Enter Student ID: ")

        found = False

        for i in range(len(students)):

            if students[i]["student_id"] == stu_id:

                del students[i]

                print("Student deleted successfully!")

                found = True
                break

        if found == False:

            print("Student ID not found!")

    elif choice == "5":

        print("\n    Subjects Offered")

        if len(subjects_offered) == 0:

            print("No subjects available.")

        else:

            for subject in subjects_offered:

                print(subject)

    elif choice == "6":

        print("\nThank you for using Student Data Organizer!")
        print("Program exited successfully.")

        break

    else:

        print("Invalid choice! Please enter 1 to 6.")