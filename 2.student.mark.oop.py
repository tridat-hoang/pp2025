class SchoolEntity:
    def __init__(self):
        self._id = ""
        self._name = ""

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def input_data(self):
        self._id = input(f"Enter {self.__class__.__name__} ID: ")
        self._name = input(f"Enter {self.__class__.__name__} Name: ")

    def __str__(self):
        return f"{self._id} | {self._name}"


class Student(SchoolEntity):
    def __init__(self):
        super().__init__()
        self._dob = ""

    def input_data(self):
        super().input_data()
        self._dob = input("Enter Student DoB: ")

    def __str__(self):
        return f"{super().__str__()} | {self._dob}"


class Course(SchoolEntity):
    pass


class SchoolSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self):
        try:
            count = int(input("Number of students: "))
            for _ in range(count):
                s = Student()
                s.input_data()
                self.__students.append(s)
        except ValueError:
            print("Invalid number input.")

    def input_courses(self):
        try:
            count = int(input("Number of courses: "))
            for _ in range(count):
                c = Course()
                c.input_data()
                self.__courses.append(c)
        except ValueError:
            print("Invalid number input.")

    def list_students(self):
        print("\n--- Student List ---")
        if not self.__students:
            print("No students yet.")
        for s in self.__students:
            print(s)

    def list_courses(self):
        print("\n--- Course List ---")
        if not self.__courses:
            print("No courses yet.")
        for c in self.__courses:
            print(c)

    def input_marks(self):
        if not self.__students or not self.__courses:
            print("Need students and courses first!")
            return
        
        self.list_courses()
        cid = input("Enter Course ID to input marks: ")
        
        if cid not in [c.get_id() for c in self.__courses]:
            print("Course not found!")
            return

        for s in self.__students:
            try:
                m = float(input(f"Mark for {s.get_id()} - {s.get_name()}: "))
                self.__marks[(cid, s.get_id())] = m
            except ValueError:
                print("Invalid mark format. Skipping.")

    def show_marks(self):
        if not self.__students or not self.__courses:
            print("Need students and courses first!")
            return
        
        self.list_courses()
        cid = input("Enter Course ID to view marks: ")
        
        if cid not in [c.get_id() for c in self.__courses]:
            print("Course not found!")
            return

        print(f"\n--- Marks for Course: {cid} ---")
        for s in self.__students:
            m = self.__marks.get((cid, s.get_id()))
            print(f"{s.get_id()} | {s.get_name()} : {m if m is not None else 'No mark'}")

    def main_menu(self):
        while True:
            print("\n==============================")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks")
            print("6. Show marks")
            print("0. Exit")
            print("==============================")
            c = input("Choice: ")
            
            if c == "1": self.input_students()
            elif c == "2": self.input_courses()
            elif c == "3": self.list_students()
            elif c == "4": self.list_courses()
            elif c == "5": self.input_marks()
            elif c == "6": self.show_marks()
            elif c == "0": break
            else: print("Invalid choice!")

if __name__ == "__main__":
    system = SchoolSystem()
    system.main_menu()