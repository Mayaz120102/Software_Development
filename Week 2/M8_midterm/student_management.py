class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    def view_all_students(self):
        for student in self.student_list:
            print(
                f"ID: {student.student_id}, Name: {student.name}, Department: {student.department}, Enrolled: {student.status}"
            )
        # print("\n")

    # for self_purpose (not for the mid)
    # def enroll_student(self):
    #     student_id = int(input("enter id: "))
    #     name = input("enter name: ")
    #     department = input("enter department")
    #     is_enrolled = True

    #     Student(student_id, name, department, is_enrolled)
    #     print("Student Enrolled Succesfully")


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def status(self):
        return self.__is_enrolled

    def view_student_info(self):
        print(self.__student_id, self.__name, self.__department, self.__is_enrolled)

    def enroll_student(self):
        if self.__is_enrolled == False:
            self.__is_enrolled = True
            print(
                f"\nThis ID:{self.__student_id},Name:{self.__name} is enrolled successfully"
            )
            print("\n")
        else:
            print(f"\nId:{self.__student_id} Already enrolled")

    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False

            print(
                f"\nStudent ID:{self.__student_id} Name:{self.__name} has been dropped\n"
            )
        else:
            print(f"\nID:{self.__student_id} is already Dropped\n")


s1 = Student(101, "Abrar Mayaz", "CSE", True)
s2 = Student(102, "Arman Talukder", "CSE", True)
s3 = Student(103, "Ashraf Jisan", "CSE", False)
s4 = Student(104, "Abdullah Showqi", "CSE", True)

sdb = StudentDatabase()


while True:
    print(
        "\n\n\t-----------------------Student Management System-----------------------\t\n"
    )
    print("1. View All Student: ")
    print("2. Enroll Student: ")
    print("3. Drop Student: ")
    print("4. Exit")

    option = int(input("Enter your Choice: "))

    if option == 1:
        print("\nShowing the Student List:\n")
        sdb.view_all_students()
    elif option == 2:
        student_id = int(input("Enter the id: "))
        found = False
        for student in StudentDatabase.student_list:
            if student.student_id == student_id:
                student.enroll_student()
                found = True
                break
        if found == False:
            print("\nInvalid Student ID,Please Enter the valid one")
    elif option == 3:
        student_id = int(input("Enter the Student id: "))
        found = False
        for student in StudentDatabase.student_list:
            if student.student_id == student_id:
                student.drop_student()
                found = True
                break
        if found == False:
            print("\nInvalid Student Id\n")

    elif option == 4:
        print("Extiting From the Menu")
        print("\n\t=============================0=============================\n")
        break
    else:
        print("\nPlease Choose the valid options\n")
