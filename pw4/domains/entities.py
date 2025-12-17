class Entity:
    def __init__(self):
        self._id = ""
        self._name = ""

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def input_info(self, stdscr=None):
        if stdscr:
            stdscr.addstr("Enter ID: ")
            self._id = stdscr.getstr().decode()
            stdscr.addstr("Enter Name: ")
            self._name = stdscr.getstr().decode()
        else:
            self._id = input("Enter ID: ")
            self._name = input("Enter Name: ")

    def __str__(self):
        return f"{self._id} | {self._name}"


class Student(Entity):
    def __init__(self):
        super().__init__()
        self._dob = ""
        self.gpa = 0

    def input_info(self, stdscr=None):
        if stdscr:
            stdscr.addstr("--- Input Student Info ---\n")
            super().input_info(stdscr)
            stdscr.addstr("Enter DoB: ")
            self._dob = stdscr.getstr().decode()
        else:
            print("--- Input Student Info ---")
            super().input_info()
            self._dob = input("Enter DoB: ")

    def __str__(self):
        return f"{super().__str__()} | {self._dob}"


class Course(Entity):
    def __init__(self):
        super().__init__()
        self._credit = 0

    def input_info(self, stdscr=None):
        if stdscr:
            stdscr.addstr("--- Input Course Info ---\n")
            super().input_info(stdscr)
            stdscr.addstr("Enter credit: ")
            self._credit = int(stdscr.getstr().decode())
        else:
            print("--- Input Course Info ---")
            super().input_info()
            self._credit = int(input("Enter credit: "))

    def __str__(self):
        return f"{super().__str__()} | {self._credit}"
