class Entity:
    def __init__(self):
        self._id = ""
        self._name = ""

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def input_info(self):
        self._id = input("Enter ID: ")
        self._name = input("Enter Name: ")

    def __str__(self):
        return f"{self._id} | {self._name}"


class Student(Entity):
    def __init__(self):
        super().__init__()
        self._dob = ""

    def input_info(self):
        print("--- Input Student Info ---")
        super().input_info()
        self._dob = input("Enter DoB: ")

    def __str__(self):
        return f"{super().__str__()} | {self._dob}"


class Course(Entity):
    def input_info(self):
        print("--- Input Course Info ---")
        super().input_info()


class Management:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def add_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input_info()
            self.__students.append(s)

    def add_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input_info()
            self.__courses.append(c)

    def list_students(self):
        print("\n=== Student List ===")
        for s in self.__students:
            print(s)

    def list_courses(self):
        print("\n=== Course List ===")
        for c in self.__courses:
            print(c)

    def input_marks(self):
        print("\n=== Input Marks ===")
        self.list_courses()
        cid = input("Enter Course ID: ")
        
        found = False
        for c in self.__courses:
            if c.get_id() == cid:
                found = True
                break
        
        if not found:
            print("Course not found!")
            return

        for s in self.__students:
            m = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
            self.__marks[(cid, s.get_id())] = m

    def show_marks(self):
        print("\n=== Show Marks ===")
        self.list_courses()
        cid = input("Enter Course ID: ")
        
        print(f"Marks for course {cid}:")
        for s in self.__students:
            m = self.__marks.get((cid, s.get_id()), "No mark")
            print(f"{s.get_name()} ({s.get_id()}): {m}")

    def menu(self):
        while True:
            print("\n----------------------")
            print("1. Add students")
            print("2. Add courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks")
            print("6. Show marks")
            print("0. Exit")
            choice = input("Your choice: ")
            
            if choice == "1": self.add_students()
            elif choice == "2": self.add_courses()
            elif choice == "3": self.list_students()
            elif choice == "4": self.list_courses()
            elif choice == "5": self.input_marks()
            elif choice == "6": self.show_marks()
            elif choice == "0": break
            else: print("Invalid choice.")

if __name__ == "__main__":
    app = Management()
    app.menu()