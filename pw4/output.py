def print_students(students, stdscr=None):
    if stdscr:
        stdscr.addstr("\n=== Student List ===\n")
        for s in students:
            stdscr.addstr(f"{s}\n")
    else:
        print("\n=== Student List ===")
        for s in students:
            print(s)

def print_courses(courses, stdscr=None):
    if stdscr:
        stdscr.addstr("\n=== Course List ===\n")
        for c in courses:
            stdscr.addstr(f"{c}\n")
    else:
        print("\n=== Course List ===")
        for c in courses:
            print(c)

def print_marks(courses, students, marks, stdscr=None):
    if not courses:
        if stdscr:
            stdscr.addstr("No courses available.\n")
        else:
            print("No courses available.")
        return
        
    if stdscr:
        stdscr.addstr("\n=== Show Marks ===\n")
        for c in courses:
            stdscr.addstr(f"{c}\n")
        stdscr.addstr("Enter Course ID: ")
        cid = stdscr.getstr().decode()
    else:
        print("\n=== Show Marks ===")
        for c in courses:
            print(c)
        cid = input("Enter Course ID: ")
    
    if stdscr:
        stdscr.addstr(f"Marks for course {cid}:\n")
        for s in students:
            m = marks.get((cid, s.get_id()), "No mark")
            stdscr.addstr(f"{s.get_name()} ({s.get_id()}): {m}\n")
    else:
        print(f"Marks for course {cid}:")
        for s in students:
            m = marks.get((cid, s.get_id()), "No mark")
            print(f"{s.get_name()} ({s.get_id()}): {m}")

def print_menu(stdscr=None):
    menu_items = [
        "1. Add students",
        "2. Add courses",
        "3. List students",
        "4. List courses",
        "5. Input marks",
        "6. Show marks",
        "0. Exit"
    ]
    if stdscr:
        stdscr.addstr("\n----------------------\n")
        for item in menu_items:
            stdscr.addstr(f"{item}\n")
        stdscr.addstr("Your choice: ")
    else:
        print("\n----------------------")
        for item in menu_items:
            print(item)
        return input("Your choice: ")
