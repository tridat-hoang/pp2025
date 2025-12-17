from domains.entities import Student, Course

def input_student_info(stdscr=None):
    s = Student()
    s.input_info(stdscr)
    return s

def input_course_info(stdscr=None):
    c = Course()
    c.input_info(stdscr)
    return c

def input_students(stdscr=None):
    if stdscr:
        stdscr.addstr("Number of students: ")
        n = int(stdscr.getstr().decode())
    else:
        n = int(input("Number of students: "))
    
    students = []
    for _ in range(n):
        s = input_student_info(stdscr)
        students.append(s)
    return students

def input_courses(stdscr=None):
    if stdscr:
        stdscr.addstr("Number of courses: ")
        n = int(stdscr.getstr().decode())
    else:
        n = int(input("Number of courses: "))
        
    courses = []
    for _ in range(n):
        c = input_course_info(stdscr)
        courses.append(c)
    return courses

def input_marks(courses, students, stdscr=None):
    if not courses:
        if stdscr:
            stdscr.addstr("No courses available. Please add courses first.\n")
        else:
            print("No courses available. Please add courses first.")
        return {}

    if stdscr:
        stdscr.addstr("\n=== Input Marks ===\n")
        for c in courses:
            stdscr.addstr(f"{c}\n")
        stdscr.addstr("Enter Course ID: ")
        cid = stdscr.getstr().decode()
    else:
        print("\n=== Input Marks ===")
        for c in courses:
            print(c)
        cid = input("Enter Course ID: ")
        
    found = any(c.get_id() == cid for c in courses)
    
    if not found:
        if stdscr:
            stdscr.addstr("Course not found!\n")
        else:
            print("Course not found!")
        return {}

    marks = {}
    for s in students:
        if stdscr:
            stdscr.addstr(f"Mark for {s.get_name()} ({s.get_id()}): ")
            mark = float(stdscr.getstr().decode())
        else:
            mark = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
        marks[(cid, s.get_id())] = mark
    return marks
