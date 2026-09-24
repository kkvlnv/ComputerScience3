class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# INHERITANCE
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# AGGREGATION
class Classroom:
    def __init__(self, section):
        self.section = section
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"Students in {self.section}:")
        for student in self.students:
            print(student.name)


# COMPOSITION
class School:
    def __init__(self, name):
        self.name = name

        # Classroom objects belong to the School
        self.classrooms = [
            Classroom("9-A"),
            Classroom("9-B")
        ]

    def show_classrooms(self):
        print(f"Classrooms in {self.name}:")
        for classroom in self.classrooms:
            print(classroom.section)


# CREATE STUDENTS
student1 = Student("Ana", 15, "S001")
student2 = Student("Mark", 15, "S002")
student3 = Student("Lia", 14, "S003")

# CREATE TEACHER
teacher = Teacher("Ms. Cruz", 30, "Science")

# CREATE SCHOOL
school = School("Example High School")

# AGGREGATION:
# Students exist independently of the classroom.
school.classrooms[0].add_student(student1)
school.classrooms[0].add_student(student2)

school.classrooms[1].add_student(student3)

# METHODS
student1.introduce()
student1.study()

teacher.introduce()
teacher.teach()

school.show_classrooms()

school.classrooms[0].show_students()
school.classrooms[1].show_students()
