# student record management system

# الداله الرئيسيه مع القاىمه
def main():
    while True:
        print("Student Record Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Display Average Grade")
        print("4. Display Top Student")
        print("5. Search Student by ID")
        print("6. Count Failed Students")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            addstudent()
        elif choice == "2":
            displaystudent()
        elif choice == "3":
            displayAvg()
        elif choice == "4":
            displayTop()
        elif choice == "5":
            search()
        elif choice == "6":
            countFailed()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
# داله لاضافه طالب جديد
def addstudent():
    file = open("student.txt","a")
    student = input("Enter student id: ")
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    file.write(f"{str(id)}\n")
    file.write(f"{name}\n")
    file.write(f"{str(grade)}\n")
    file.close()
    print("Student added successfully.")

# داله لعرض جميع الطلاب
def displaystudent():
    try:
        file = open("student.txt","r")
        print("Student Records:")
        while True:
            student_id = file.readline().strip()
            if not student_id:
                break
        name = file.readline().strip()
        grade = file.readline().strip()
        print("-------------------------")
        print(f"id: {student_id}")
        print(f"name: {name}")
        print(f"grade: {grade}")
        file.close()
    except FileNotFoundError:
        print("No student records found.")



# داله لحساب متوسط الدرجات 
def displayAvg():
    try:
        file = open("student.txt","r")
        total_grade = 0
        count = 0
        while True:
            student_id = file.readline().strip()
            if not student_id:
                break
            name = file.readline().strip()
            grade = file.readline().strip()
            total_grade += float(grade)
            count += 1
        file.close()
        if count > 0:
            avg_grade = total_grade / count
            print(f"Average grade: {avg_grade:.2f}")
        
    except  Exception as var: 
        print(var)

# داله لايجاد الطالب صاحب اعلي درجه
def displayTop():
    try:
        file = open("student.txt","r")
        top_student = None
        top_grade = -1
        while True:
            student_id = file.readline().strip()
            if not student_id:
                break
            name = file.readline().strip()
            grade = float(file.readline().strip())
            if grade > top_grade:
                top_grade = grade
                top_student = (student_id, name, grade)
        file.close()
        if top_student:
            print("Top Student:")
            print("-------------------------")
            print(f"id: {top_student[0]}")
            print(f"name: {top_student[1]}")
            print(f"grade: {top_student[2]}")
        else:
            print("No student records found.")
    except Exception as x:
        print(x)
# داله للبحث عن  طالب باسخدام رقم معرف
def search():
    try:
        id_search = int(input("Enter student id to search: "))
        file = open("student.txt","r")
        while True:
            student_id = file.readline().strip()
            if not student_id:
                break
            name = file.readline().strip()
            grade = file.readline().strip()
            if int(student_id) == id_search:
                print("Student Found:")
                print("-------------------------")
                print(f"id: {student_id}")
                print(f"name: {name}")
                print(f"grade: {grade}")
                file.close()
                return
            file.close()
            print("Student not found.")
    except Exception as error:
        print(error)

# داله لحساب عدد الطلاب الراسبين
def countFailed():
    try:
        file = open("student.txt","r")
        failed_count = 0
        while True:
            student_id = file.readline().strip()
            if not student_id:
                break
            name = file.readline().strip()
            grade = float(file.readline().strip())
            if grade < 50:
                failed_count += 1
        file.close()
        print(f"Number of failed students: {failed_count}")
    except Exception as var:
        print(var)
# تشغيل البرنامج
main()
