class Student:
    def _init_(self, name, reg_number, marks):
        self.name = name
        self.reg_number = reg_number
        self.marks = marks
        self.average = sum(self.marks) / len(self.marks)
    
    def _str_(self):
        return f"Name: {self.name}, Registration Number: {self.reg_number}, Marks: {self.marks}, Average Marks: {self.average}"

def main():
    num_students = int(input("Enter the number of students: "))
    students_dict = {}

    for i in range(1, num_students + 1):
        print(f"\nEnter details for student {i}:")
        name = input("Name: ")
        reg_number = input("Registration Number: ")
        marks = []
        for j in range(3):
            mark = float(input(f"Enter mark for Subject {j + 1}: "))
            marks.append(mark)
        
        student = Student(name, reg_number, marks)
        students_dict[name] = {
            'Registration Number': reg_number,
            'Marks': marks,
            'Average Marks': student.average
        }
    
    print("\nStudent Details:")
    for name, details in students_dict.items():
        print(f"\nStudent Name: {name}")
        for key, value in details.items():
            print(f"{key}: {value}")

if _name_ == "_main_":
    main()
    
    main()
