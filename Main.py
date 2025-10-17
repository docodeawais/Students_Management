import json

class Student:

    def view_all_student():
        pass
        print("Viewing all students...")
        with open("record.json", "r") as f:
            record = json.load(f)
            print("Serial no\t Name\t\t Roll_no\t City")
            for student in record:
                
                print(f"{student['id']}\t\t {student['name']}\t\t {student['roll_no']}\t\t {student['city']}")

    def add_student():

        student = {}
        print("Adding a new student...")
        print("Please provide student details.")
        input_name = input("Enter student name: ")
        input_rollno = input("Enter student Roll no: ")
        input_city = input("Enter student city: ")

        student["name"] = input_name
        student["roll_no"] = input_rollno
        student["city"] = input_city

        print(student, type(student))

        with open("record.json", "r") as f:
            data = json.load(f)
            if data:
                last_id = data[-1]["id"]  
            else:
                last_id = 0
            student["id"] = last_id + 1
            data.append(student)
                
        with open("record.json", "w") as f:
            json.dump(data, f, indent=4)


    def search_student():
        print("Searching for a student...")
        roll_number = input("Enter Roll Number to search: ")

        with open("record.json", "r") as f:
            record = json.load(f)
            for student in record:
                if roll_number == student['roll_no']:
                    print("Serial no\t Name\t\t Roll_no\t City")
                    print(f"{student['id']}\t\t {student['name']}\t\t {student['roll_no']}\t\t {student['city']}")
            # Code to search for a student

    def delete_student():
        print("Deleting a student...")
        
        roll_number = input("Enter Roll Number to Delete Student Record: ")
        with open("record.json", "r") as f: 
            record = json.load(f)
        for student in record:
            if roll_number == student['roll_no']:
                record.remove(student)
                print("Record Deleted Succesfully....")
            else:
                print("Student not Found...")

            with open("record.json", "w") as f:
                json.dump(record, f, indent=4)
            # Code to Delete a student

    def update_student():
        print("Updating student information...")
        roll_no = input("Enter Roll Number to Update: ")
        with open("record.json", "r") as f:
            record = json.load(f)

            for student in record:
                if(roll_no == student['roll_no']):
                    print("Student Found\n")

                    choice = input("What you want to update:\n1. Name\n2. Roll Number\n 3. City\n")

                    if(choice == '1'):
                        updated_name = input("Enter Updated Name: ")
                        student['name'] = updated_name

                        with open("record.json", "w") as f:
                            json.dump(record, f, indent=4)
                        Student.view_all_student()

                    elif(choice == '2'):
                        updated_roll = input("Enter Updated Roll Number: ")
                        student['roll_no'] = updated_roll

                        with open("record.json", "w") as f:
                            json.dump(record, f, indent=4)
                        Student.view_all_student()

                    elif(choice == '3'):
                        updated_city = input("Enter Updated City: ")
                        student['city'] = updated_city
                            

                    with open("record.json", "w") as f:
                        json.dump(record, f, indent=4)
                    Student.view_all_student()
            # Code to update a student

    def student_management(self):
        pass
        print("\n\n\t\t\tDashboard Student Management System\n\n")

        print("Select an operation to perform:\n")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit\n")

        choice = int(input("Enter your choice (1-6): "))

        try:
            if choice == 1:
                Student.add_student()
            # Code to add a student
            elif choice == 2:
                Student.view_all_student()
            # Code to view students
            elif choice == 3:
                Student.search_student()
            elif choice == 4:
                Student.delete_student()
            # Code to delete a student
            elif choice == 5:
                Student.update_student()
            elif choice == 6:
                print("Exiting the system. Goodbye!")
                return
        except:
            print("Invalid Choice")


std = Student()
i=2
while(i>0):
    std.student_management()
