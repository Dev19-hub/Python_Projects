import os
FILE_NAME = "Students.txt"
student = {}
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                name,marks = line.rsplit(",", 1)
                student[name] = int(marks)


while True: 
    print("\n-----STUDENT MANAGER APP----")
    print("1. Add student")
    print("2. View Students")
    print("3. Check Results")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        name = input("Enter Student Name: ").strip()

        try:
            marks = int(input("Enter your marks: "))
            if not 0<= marks <= 100:
                print("Marks between 0 to 100.")
                continue

            student[name] = marks

            with open(FILE_NAME, "w") as file:
                for student_name, student_marks in student.items():
                    file.write(f"{student_name}, {student_marks}\n")

            print(f"{name} successfully added!!")
        except ValueError:
            print("Please enter marks as a whole number")
            
    elif choice == "2":
        if not student:
            print("No student found")
        else:
            print("\n Student Records: ")
            for name, marks in student.items():
                print(name, ":", marks)
                
    elif choice == "3":
        name = input("Enter the student name: ").strip()

        if name in student:
            marks = student[name]
            print("Marks: ", marks)

            if marks >= 40:
                print("Student Pass")
            else:
                print("Failed")
        else:
            print("Student Not Found")

    elif choice == "4":
        print("Exitingggg...")
        break

    else:
        print("Invalid Input")